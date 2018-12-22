#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for bundle_to_label."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import datetime
import os

from absl.testing import absltest
import apache_beam as beam
from apache_beam.testing import test_pipeline
from apache_beam.testing import util
from google.protobuf import text_format
from proto.stu3 import resources_pb2
from py.google.fhir.labels import bundle_to_label
from py.google.fhir.labels import label


# TODO(kunzhang, cykoo): Move this to a proper location.
_TESTDATA_PATH = 'com_google_fhir/testdata/stu3/labels'


class BundleToLabelTest(absltest.TestCase):

  def setUp(self):
    self._test_data_dir = os.path.join(absltest.get_default_test_srcdir(),
                                       _TESTDATA_PATH)
    self._bundle = resources_pb2.Bundle()
    with open(os.path.join(self._test_data_dir, 'bundle_1.pbtxt')) as f:
      text_format.Parse(f.read(), self._bundle)
    enc = self._bundle.entry[0].resource.encounter
    patient = self._bundle.entry[1].resource.patient

    self._expected_label = label.ComposeLabel(
        patient, enc,
        label.LOS_RANGE_LABEL,
        'above_14',
        # 24 hours after admission
        datetime.datetime(2009, 2, 14, 23, 31, 30))

  def testPipeline(self):
    with test_pipeline.TestPipeline() as pipeline:
      result = (
          pipeline
          | 'input' >> beam.Create([self._bundle])
          | 'process' >> beam.ParDo(
              bundle_to_label.LengthOfStayRangeLabelAt24HoursFn()))
      util.assert_that(result, util.equal_to([self._expected_label]))


if __name__ == '__main__':
  absltest.main()
