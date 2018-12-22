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

import com.google.fhir.stu3.proto.Uri;

/** A wrapper around the Uri FHIR primitive type. */
public class UriWrapper extends PrimitiveWrapper<Uri> {

  private static final Uri NULL_URI = Uri.newBuilder().addExtension(getNoValueExtension()).build();

  /** Create an UriWrapper from a Uri. */
  public UriWrapper(Uri uri) {
    super(uri);
  }

  /** Create an UriWrapper from a java String. */
  public UriWrapper(String input) {
    super(input == null ? NULL_URI : parseAndValidate(input));
  }

  @Override
  protected String printValue() {
    return getWrapped().getValue();
  }

  private static Uri parseAndValidate(String input) {
    return Uri.newBuilder().setValue(input).build();
  }
}
