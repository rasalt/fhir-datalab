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

import com.google.fhir.stu3.proto.Annotations;
import com.google.fhir.stu3.proto.Code;
import com.google.fhir.stu3.proto.Extension;
import com.google.protobuf.Descriptors.Descriptor;
import com.google.protobuf.Descriptors.EnumValueDescriptor;
import com.google.protobuf.Descriptors.FieldDescriptor;
import com.google.protobuf.Message;
import com.google.protobuf.MessageOrBuilder;
import java.util.regex.Pattern;

/**
 * A wrapper around the Code FHIR primitive type. This wrapper also supports reading from and
 * writing to specialized Code types.
 */
public class CodeWrapper extends PrimitiveWrapper<Code> {

  private static final Pattern CODE_PATTERN =
      Pattern.compile(AnnotationUtils.getValueRegexForPrimitiveType(Code.getDefaultInstance()));
  private static final Code NULL_CODE =
      Code.newBuilder().addExtension(getNoValueExtension()).build();

  /** Create a CodeWrapper from a Code. */
  public CodeWrapper(Code code) {
    super(code);
  }

  /** Create a CodeWrapper from a java String. */
  public CodeWrapper(String input) {
    super(input == null ? NULL_CODE : parseAndValidate(input));
  }

  /** Create a CodeWrapper from a specialized code. */
  public static CodeWrapper of(MessageOrBuilder code) {
    Descriptor descriptor = code.getDescriptorForType();
    // Handle specialized codes.
    if (!descriptor.getOptions().hasExtension(Annotations.fhirValuesetUrl)) {
      throw new IllegalArgumentException(
          "Type " + descriptor.getFullName() + " is not a FHIR code type");
    }
    Code.Builder builder = Code.newBuilder();
    // Copy the Element parts.
    FieldDescriptor idField = descriptor.findFieldByName("id");
    if (code.hasField(idField)) {
      builder.setId((com.google.fhir.stu3.proto.String) code.getField(idField));
    }
    builder.addAllExtension(ExtensionWrapper.fromExtensionsIn(code).build());

    FieldDescriptor valueField = descriptor.findFieldByName("value");
    if (!code.hasField(valueField)) {
      // We're done.
      return new CodeWrapper(builder.build());
    }
    if (valueField.getType() == FieldDescriptor.Type.STRING) {
      return new CodeWrapper(builder.setValue((String) code.getField(valueField)).build());
    }
    if (valueField.getType() != FieldDescriptor.Type.ENUM) {
      throw new IllegalArgumentException("Invalid source message: " + descriptor.getFullName());
    }
    EnumValueDescriptor enumValue = (EnumValueDescriptor) code.getField(valueField);
    if (enumValue.getOptions().hasExtension(Annotations.fhirOriginalCode)) {
      return new CodeWrapper(
          builder
              .setValue(enumValue.getOptions().getExtension(Annotations.fhirOriginalCode))
              .build());
    } else {
      return new CodeWrapper(
          builder.setValue(enumValue.getName().toLowerCase().replace('_', '-')).build());
    }
  }

  @Override
  @SuppressWarnings("unchecked")
  public <B extends Message.Builder> B copyInto(B builder) {
    Descriptor descriptor = builder.getDescriptorForType();
    // Handle standard codes.
    if (!descriptor.getOptions().hasExtension(Annotations.fhirValuesetUrl)) {
      if (!builder.getDescriptorForType().equals(Code.getDescriptor())) {
        throw new IllegalArgumentException(
            "Type " + descriptor.getFullName() + " is not a FHIR code type");
      }
      return super.copyInto(builder);
    }
    // Handle specialized codes.
    if (getWrapped().hasId()) {
      builder.setField(descriptor.findFieldByName("id"), getWrapped().getId());
    }
    for (Extension e : getWrapped().getExtensionList()) {
      builder.addRepeatedField(descriptor.findFieldByName("extension"), e);
    }
    if (!hasValue()) {
      // We're done if there is no value to parse.
      return builder;
    }
    FieldDescriptor valueField = descriptor.findFieldByName("value");
    if (valueField.getType() == FieldDescriptor.Type.STRING) {
      return (B) builder.setField(valueField, getWrapped().getValue());
    }
    if (valueField.getType() != FieldDescriptor.Type.ENUM) {
      throw new IllegalArgumentException("Invalid target message: " + descriptor.getFullName());
    }

    // TODO: improve strictness of this parsing step.
    EnumValueDescriptor enumValue =
        valueField
            .getEnumType()
            .findValueByName(getWrapped().getValue().toUpperCase().replace('-', '_'));
    if (enumValue != null
        && enumValue.getNumber() != 0
        && !enumValue.getOptions().hasExtension(Annotations.fhirOriginalCode)) {
      return (B) builder.setField(valueField, enumValue);
    }

    // Try again, explicitly looking for original codes.
    for (EnumValueDescriptor value : valueField.getEnumType().getValues()) {
      if (value.getOptions().hasExtension(Annotations.fhirOriginalCode)
          && value
              .getOptions()
              .getExtension(Annotations.fhirOriginalCode)
              .equals(getWrapped().getValue())) {
        return (B) builder.setField(valueField, value);
      }
    }
    throw new IllegalArgumentException(
        "Failed to convert to "
            + descriptor.getFullName()
            + ": \""
            + this
            + "\" is not a valid enum entry");
  }

  private static Code parseAndValidate(String input) {
    validateUsingPattern(CODE_PATTERN, input);
    return Code.newBuilder().setValue(input).build();
  }

  @Override
  protected String printValue() {
    return getWrapped().getValue();
  }
}
