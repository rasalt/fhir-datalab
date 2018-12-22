/*
 * Copyright 2018 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef GOOGLE_FHIR_STU3_JSON_FORMAT_H_
#define GOOGLE_FHIR_STU3_JSON_FORMAT_H_

#include <string>

#include "google/protobuf/message.h"
#include "absl/time/time.h"
#include "google/fhir/status/status.h"
#include "google/fhir/status/statusor.h"
#include "tensorflow/core/lib/core/errors.h"

namespace google {
namespace fhir {
namespace stu3 {

using std::string;

// Merges a string of raw FHIR json into an existing message.
// Takes a default timezone for timelike data that does not specify timezone.
::google::fhir::Status MergeJsonFhirStringIntoProto(
    const string& raw_json, google::protobuf::Message* target,
    absl::TimeZone default_timezone);

// Given a template for a FHIR resource type, creates a resource proto of that
// type and merges a string of raw FHIR json into it.
// Takes a default timezone for timelike data that does not specify timezone.
template <typename R>
::google::fhir::StatusOr<R> JsonFhirStringToProto(
    const string& raw_json, const absl::TimeZone default_timezone) {
  R resource;
  FHIR_RETURN_IF_ERROR(
      MergeJsonFhirStringIntoProto(raw_json, &resource, default_timezone));
  return resource;
}

::google::fhir::StatusOr<string> PrettyPrintFhirToJsonString(
    const google::protobuf::Message& fhir_proto, const absl::TimeZone default_timezone);

::google::fhir::StatusOr<string> PrintFhirToJsonString(
    const google::protobuf::Message& fhir_proto, const absl::TimeZone default_timezone);

::google::fhir::StatusOr<string> PrintFhirToJsonStringForAnalytics(
    const google::protobuf::Message& fhir_proto, const absl::TimeZone default_timezone);

::google::fhir::StatusOr<string> PrettyPrintFhirToJsonStringForAnalytics(
    const google::protobuf::Message& fhir_proto, const absl::TimeZone default_timezone);

}  // namespace stu3
}  // namespace fhir
}  // namespace google

#endif  // GOOGLE_FHIR_STU3_JSON_FORMAT_H_
