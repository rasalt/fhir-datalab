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

import com.google.fhir.stu3.proto.Element;
import com.google.fhir.stu3.proto.Xhtml;

/** A wrapper around the Xhtml FHIR primitive type. */
public class XhtmlWrapper extends PrimitiveWrapper<Xhtml> {

  /** Create an XhtmlWrapper from an Xhtml. */
  public XhtmlWrapper(Xhtml xhtml) {
    super(xhtml);
  }

  /** Create an XhtmlWrapper from a java String, disallowing null inputs */
  public XhtmlWrapper(String input) {
    super(input == null ? null : Xhtml.newBuilder().setValue(input).build());
    if (input == null) {
      throw new IllegalArgumentException("Invalid input: null");
    }
  }

  @Override
  protected String printValue() {
    return getWrapped().getValue();
  }

  /** All valid Xhtml objects contain a value. */
  @Override
  public boolean hasValue() {
    return true;
  }

  /** Get the Element part of this primitive. Xhtml objects can never have any extensions. */
  @Override
  public Element getElement() {
    if (!getWrapped().hasId()) {
      return null;
    }
    return Element.newBuilder().setId(getWrapped().getId()).build();
  }
}
