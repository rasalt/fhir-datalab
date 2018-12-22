//    Copyright 2018 Google Inc.
//
//    Licensed under the Apache License, Version 2.0 (the "License");
//    you may not use this file except in compliance with the License.
//    You may obtain a copy of the License at
//
//        https://www.apache.org/licenses/LICENSE-2.0
//
//    Unless required by applicable law or agreed to in writing, software
//    distributed under the License is distributed on an "AS IS" BASIS,
//    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//    See the License for the specific language governing permissions and
//    limitations under the License.

package com.google.fhir.stu3;

import com.google.fhir.stu3.proto.Integer;
import java.util.regex.Pattern;

/** A wrapper around the Integer FHIR primitive type. */
public class IntegerWrapper extends NumericTypeWrapper<Integer> {

  private static final Pattern INTEGER_PATTERN =
      Pattern.compile(AnnotationUtils.getValueRegexForPrimitiveType(Integer.getDefaultInstance()));
  private static final Integer NULL_INTEGER =
      Integer.newBuilder().addExtension(getNoValueExtension()).build();

  /** Create an IntegerWrapper from an Integer. */
  public IntegerWrapper(Integer integer) {
    super(integer);
  }

  /** Create an IntegerWrapper from a java String. */
  public IntegerWrapper(String input) {
    super(input == null ? NULL_INTEGER : parseAndValidate(input));
  }

  private static Integer parseAndValidate(String input) {
    validateUsingPattern(INTEGER_PATTERN, input);
    return Integer.newBuilder().setValue(java.lang.Integer.parseInt(input)).build();
  }

  @Override
  protected String printValue() {
    return java.lang.Integer.toString(getWrapped().getValue());
  }
}
