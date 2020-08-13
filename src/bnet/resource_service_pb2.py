# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/resource_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/resource_service.proto',
  package='bnet.protocol.resources',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x1b\x62net/resource_service.proto\x12\x17\x62net.protocol.resources\"Y\n\x14\x43ontentHandleRequest\x12\x12\n\nprogram_id\x18\x01 \x02(\x07\x12\x11\n\tstream_id\x18\x02 \x02(\x07\x12\x1a\n\x06locale\x18\x03 \x01(\x07:\n1701729619'
)




_CONTENTHANDLEREQUEST = _descriptor.Descriptor(
  name='ContentHandleRequest',
  full_name='bnet.protocol.resources.ContentHandleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='program_id', full_name='bnet.protocol.resources.ContentHandleRequest.program_id', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='bnet.protocol.resources.ContentHandleRequest.stream_id', index=1,
      number=2, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locale', full_name='bnet.protocol.resources.ContentHandleRequest.locale', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=1701729619,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['ContentHandleRequest'] = _CONTENTHANDLEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContentHandleRequest = _reflection.GeneratedProtocolMessageType('ContentHandleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTENTHANDLEREQUEST,
  '__module__' : 'bnet.resource_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.resources.ContentHandleRequest)
  })
_sym_db.RegisterMessage(ContentHandleRequest)


# @@protoc_insertion_point(module_scope)
