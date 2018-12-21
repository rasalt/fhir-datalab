# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/stu3/google_extensions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.stu3 import annotations_pb2 as proto_dot_stu3_dot_annotations__pb2
from proto.stu3 import datatypes_pb2 as proto_dot_stu3_dot_datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/stu3/google_extensions.proto',
  package='google.fhir.stu3.google',
  syntax='proto3',
  serialized_options=_b('\n\033com.google.fhir.stu3.googleP\001'),
  serialized_pb=_b('\n\"proto/stu3/google_extensions.proto\x12\x17google.fhir.stu3.google\x1a\x1cproto/stu3/annotations.proto\x1a\x1aproto/stu3/datatypes.proto\"\xff\x02\n\x1b\x42\x61se64BinarySeparatorStride\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12\x34\n\textension\x18\x02 \x03(\x0b\x32!.google.fhir.stu3.proto.Extension\x12\x39\n\tseparator\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.StringB\x06\xf0\xd0\x87\xeb\x04\x01\x12;\n\x06stride\x18\x05 \x01(\x0b\x32#.google.fhir.stu3.proto.PositiveIntB\x06\xf0\xd0\x87\xeb\x04\x01:\x85\x01\xc0\x9f\xe3\xb6\x05\x02\x9a\xb5\x8e\x93\x06\x31http://hl7.org/fhir/StructureDefinition/Extension\xb2\xfe\xe4\x97\x06\x42https://g.co/fhir/StructureDefinition/base64Binary-separatorStride\"\xbd\x07\n\nEventLabel\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12\x34\n\textension\x18\x02 \x03(\x0b\x32!.google.fhir.stu3.proto.Extension\x12:\n\x07patient\x18\x04 \x01(\x0b\x32!.google.fhir.stu3.proto.ReferenceB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x34\n\x04type\x18\x05 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.CodingB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x34\n\nevent_time\x18\x06 \x01(\x0b\x32 .google.fhir.stu3.proto.DateTime\x12\x31\n\x06source\x18\x07 \x01(\x0b\x32!.google.fhir.stu3.proto.Reference\x12\x38\n\x05label\x18\x08 \x03(\x0b\x32).google.fhir.stu3.google.EventLabel.Label\x1a\xc2\x03\n\x05Label\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12:\n\nclass_name\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.CodingB\x06\xf0\xd0\x87\xeb\x04\x01\x12W\n\x0b\x63lass_value\x18\x05 \x01(\x0b\x32\x34.google.fhir.stu3.google.EventLabel.Label.ClassValueB\x0c\xf8\xe1\xe3\xc9\x05\x01\xf0\xd0\x87\xeb\x04\x01\x1a\xf7\x01\n\nClassValue\x12\x32\n\x07\x62oolean\x18\x01 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.BooleanH\x00\x12\x32\n\x07\x64\x65\x63imal\x18\x02 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.DecimalH\x00\x12\x32\n\x07integer\x18\x03 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.IntegerH\x00\x12>\n\x0cstring_value\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.StringH\x00R\x06stringB\r\n\x0b\x63lass_value:s\xc0\x9f\xe3\xb6\x05\x02\x9a\xb5\x8e\x93\x06\x31http://hl7.org/fhir/StructureDefinition/Extension\xb2\xfe\xe4\x97\x06\x30https://g.co/fhir/StructureDefinition/eventLabel\"\x8e\x03\n\x0c\x45ventTrigger\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12\x34\n\textension\x18\x02 \x03(\x0b\x32!.google.fhir.stu3.proto.Extension\x12\x34\n\x04type\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.CodingB\x06\xf0\xd0\x87\xeb\x04\x01\x12<\n\nevent_time\x18\x05 \x01(\x0b\x32 .google.fhir.stu3.proto.DateTimeB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x31\n\x06source\x18\x06 \x01(\x0b\x32!.google.fhir.stu3.proto.Reference:u\xc0\x9f\xe3\xb6\x05\x02\x9a\xb5\x8e\x93\x06\x31http://hl7.org/fhir/StructureDefinition/Extension\xb2\xfe\xe4\x97\x06\x32https://g.co/fhir/StructureDefinition/eventTrigger\"\xf7\x01\n\x13PrimitiveHasNoValue\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12\x36\n\rvalue_boolean\x18\x03 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.Boolean:|\xc0\x9f\xe3\xb6\x05\x02\x9a\xb5\x8e\x93\x06\x31http://hl7.org/fhir/StructureDefinition/Extension\xb2\xfe\xe4\x97\x06\x39https://g.co/fhir/StructureDefinition/primitiveHasNoValueB\x1f\n\x1b\x63om.google.fhir.stu3.googleP\x01\x62\x06proto3')
  ,
  dependencies=[proto_dot_stu3_dot_annotations__pb2.DESCRIPTOR,proto_dot_stu3_dot_datatypes__pb2.DESCRIPTOR,])




_BASE64BINARYSEPARATORSTRIDE = _descriptor.Descriptor(
  name='Base64BinarySeparatorStride',
  full_name='google.fhir.stu3.google.Base64BinarySeparatorStride',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.google.Base64BinarySeparatorStride.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.stu3.google.Base64BinarySeparatorStride.extension', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='separator', full_name='google.fhir.stu3.google.Base64BinarySeparatorStride.separator', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stride', full_name='google.fhir.stu3.google.Base64BinarySeparatorStride.stride', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\300\237\343\266\005\002\232\265\216\223\0061http://hl7.org/fhir/StructureDefinition/Extension\262\376\344\227\006Bhttps://g.co/fhir/StructureDefinition/base64Binary-separatorStride'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=505,
)


_EVENTLABEL_LABEL_CLASSVALUE = _descriptor.Descriptor(
  name='ClassValue',
  full_name='google.fhir.stu3.google.EventLabel.Label.ClassValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boolean', full_name='google.fhir.stu3.google.EventLabel.Label.ClassValue.boolean', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decimal', full_name='google.fhir.stu3.google.EventLabel.Label.ClassValue.decimal', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integer', full_name='google.fhir.stu3.google.EventLabel.Label.ClassValue.integer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.fhir.stu3.google.EventLabel.Label.ClassValue.string_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='string', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='class_value', full_name='google.fhir.stu3.google.EventLabel.Label.ClassValue.class_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1101,
  serialized_end=1348,
)

_EVENTLABEL_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='google.fhir.stu3.google.EventLabel.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.google.EventLabel.Label.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='google.fhir.stu3.google.EventLabel.Label.class_name', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_value', full_name='google.fhir.stu3.google.EventLabel.Label.class_value', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\370\341\343\311\005\001\360\320\207\353\004\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENTLABEL_LABEL_CLASSVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=898,
  serialized_end=1348,
)

_EVENTLABEL = _descriptor.Descriptor(
  name='EventLabel',
  full_name='google.fhir.stu3.google.EventLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.google.EventLabel.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.stu3.google.EventLabel.extension', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patient', full_name='google.fhir.stu3.google.EventLabel.patient', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.fhir.stu3.google.EventLabel.type', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.fhir.stu3.google.EventLabel.event_time', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.fhir.stu3.google.EventLabel.source', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.fhir.stu3.google.EventLabel.label', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENTLABEL_LABEL, ],
  enum_types=[
  ],
  serialized_options=_b('\300\237\343\266\005\002\232\265\216\223\0061http://hl7.org/fhir/StructureDefinition/Extension\262\376\344\227\0060https://g.co/fhir/StructureDefinition/eventLabel'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=1465,
)


_EVENTTRIGGER = _descriptor.Descriptor(
  name='EventTrigger',
  full_name='google.fhir.stu3.google.EventTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.google.EventTrigger.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.stu3.google.EventTrigger.extension', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.fhir.stu3.google.EventTrigger.type', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.fhir.stu3.google.EventTrigger.event_time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\360\320\207\353\004\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.fhir.stu3.google.EventTrigger.source', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\300\237\343\266\005\002\232\265\216\223\0061http://hl7.org/fhir/StructureDefinition/Extension\262\376\344\227\0062https://g.co/fhir/StructureDefinition/eventTrigger'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1468,
  serialized_end=1866,
)


_PRIMITIVEHASNOVALUE = _descriptor.Descriptor(
  name='PrimitiveHasNoValue',
  full_name='google.fhir.stu3.google.PrimitiveHasNoValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.google.PrimitiveHasNoValue.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_boolean', full_name='google.fhir.stu3.google.PrimitiveHasNoValue.value_boolean', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\300\237\343\266\005\002\232\265\216\223\0061http://hl7.org/fhir/StructureDefinition/Extension\262\376\344\227\0069https://g.co/fhir/StructureDefinition/primitiveHasNoValue'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1869,
  serialized_end=2116,
)

_BASE64BINARYSEPARATORSTRIDE.fields_by_name['id'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_BASE64BINARYSEPARATORSTRIDE.fields_by_name['extension'].message_type = proto_dot_stu3_dot_datatypes__pb2._EXTENSION
_BASE64BINARYSEPARATORSTRIDE.fields_by_name['separator'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_BASE64BINARYSEPARATORSTRIDE.fields_by_name['stride'].message_type = proto_dot_stu3_dot_datatypes__pb2._POSITIVEINT
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['boolean'].message_type = proto_dot_stu3_dot_datatypes__pb2._BOOLEAN
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['decimal'].message_type = proto_dot_stu3_dot_datatypes__pb2._DECIMAL
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['integer'].message_type = proto_dot_stu3_dot_datatypes__pb2._INTEGER
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['string_value'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTLABEL_LABEL_CLASSVALUE.containing_type = _EVENTLABEL_LABEL
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['boolean'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['boolean'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['decimal'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['decimal'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['integer'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['integer'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['string_value'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['string_value'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL.fields_by_name['id'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTLABEL_LABEL.fields_by_name['class_name'].message_type = proto_dot_stu3_dot_datatypes__pb2._CODING
_EVENTLABEL_LABEL.fields_by_name['class_value'].message_type = _EVENTLABEL_LABEL_CLASSVALUE
_EVENTLABEL_LABEL.containing_type = _EVENTLABEL
_EVENTLABEL.fields_by_name['id'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTLABEL.fields_by_name['extension'].message_type = proto_dot_stu3_dot_datatypes__pb2._EXTENSION
_EVENTLABEL.fields_by_name['patient'].message_type = proto_dot_stu3_dot_datatypes__pb2._REFERENCE
_EVENTLABEL.fields_by_name['type'].message_type = proto_dot_stu3_dot_datatypes__pb2._CODING
_EVENTLABEL.fields_by_name['event_time'].message_type = proto_dot_stu3_dot_datatypes__pb2._DATETIME
_EVENTLABEL.fields_by_name['source'].message_type = proto_dot_stu3_dot_datatypes__pb2._REFERENCE
_EVENTLABEL.fields_by_name['label'].message_type = _EVENTLABEL_LABEL
_EVENTTRIGGER.fields_by_name['id'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTTRIGGER.fields_by_name['extension'].message_type = proto_dot_stu3_dot_datatypes__pb2._EXTENSION
_EVENTTRIGGER.fields_by_name['type'].message_type = proto_dot_stu3_dot_datatypes__pb2._CODING
_EVENTTRIGGER.fields_by_name['event_time'].message_type = proto_dot_stu3_dot_datatypes__pb2._DATETIME
_EVENTTRIGGER.fields_by_name['source'].message_type = proto_dot_stu3_dot_datatypes__pb2._REFERENCE
_PRIMITIVEHASNOVALUE.fields_by_name['id'].message_type = proto_dot_stu3_dot_datatypes__pb2._STRING
_PRIMITIVEHASNOVALUE.fields_by_name['value_boolean'].message_type = proto_dot_stu3_dot_datatypes__pb2._BOOLEAN
DESCRIPTOR.message_types_by_name['Base64BinarySeparatorStride'] = _BASE64BINARYSEPARATORSTRIDE
DESCRIPTOR.message_types_by_name['EventLabel'] = _EVENTLABEL
DESCRIPTOR.message_types_by_name['EventTrigger'] = _EVENTTRIGGER
DESCRIPTOR.message_types_by_name['PrimitiveHasNoValue'] = _PRIMITIVEHASNOVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Base64BinarySeparatorStride = _reflection.GeneratedProtocolMessageType('Base64BinarySeparatorStride', (_message.Message,), dict(
  DESCRIPTOR = _BASE64BINARYSEPARATORSTRIDE,
  __module__ = 'proto.stu3.google_extensions_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.stu3.google.Base64BinarySeparatorStride)
  ))
_sym_db.RegisterMessage(Base64BinarySeparatorStride)

EventLabel = _reflection.GeneratedProtocolMessageType('EventLabel', (_message.Message,), dict(

  Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(

    ClassValue = _reflection.GeneratedProtocolMessageType('ClassValue', (_message.Message,), dict(
      DESCRIPTOR = _EVENTLABEL_LABEL_CLASSVALUE,
      __module__ = 'proto.stu3.google_extensions_pb2'
      # @@protoc_insertion_point(class_scope:google.fhir.stu3.google.EventLabel.Label.ClassValue)
      ))
    ,
    DESCRIPTOR = _EVENTLABEL_LABEL,
    __module__ = 'proto.stu3.google_extensions_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.stu3.google.EventLabel.Label)
    ))
  ,
  DESCRIPTOR = _EVENTLABEL,
  __module__ = 'proto.stu3.google_extensions_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.stu3.google.EventLabel)
  ))
_sym_db.RegisterMessage(EventLabel)
_sym_db.RegisterMessage(EventLabel.Label)
_sym_db.RegisterMessage(EventLabel.Label.ClassValue)

EventTrigger = _reflection.GeneratedProtocolMessageType('EventTrigger', (_message.Message,), dict(
  DESCRIPTOR = _EVENTTRIGGER,
  __module__ = 'proto.stu3.google_extensions_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.stu3.google.EventTrigger)
  ))
_sym_db.RegisterMessage(EventTrigger)

PrimitiveHasNoValue = _reflection.GeneratedProtocolMessageType('PrimitiveHasNoValue', (_message.Message,), dict(
  DESCRIPTOR = _PRIMITIVEHASNOVALUE,
  __module__ = 'proto.stu3.google_extensions_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.stu3.google.PrimitiveHasNoValue)
  ))
_sym_db.RegisterMessage(PrimitiveHasNoValue)


DESCRIPTOR._options = None
_BASE64BINARYSEPARATORSTRIDE.fields_by_name['separator']._options = None
_BASE64BINARYSEPARATORSTRIDE.fields_by_name['stride']._options = None
_BASE64BINARYSEPARATORSTRIDE._options = None
_EVENTLABEL_LABEL.fields_by_name['class_name']._options = None
_EVENTLABEL_LABEL.fields_by_name['class_value']._options = None
_EVENTLABEL.fields_by_name['patient']._options = None
_EVENTLABEL.fields_by_name['type']._options = None
_EVENTLABEL._options = None
_EVENTTRIGGER.fields_by_name['type']._options = None
_EVENTTRIGGER.fields_by_name['event_time']._options = None
_EVENTTRIGGER._options = None
_PRIMITIVEHASNOVALUE._options = None
# @@protoc_insertion_point(module_scope)