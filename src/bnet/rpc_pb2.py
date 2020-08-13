# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/rpc.proto',
  package='bnet.protocol',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x62net/rpc.proto\x12\rbnet.protocol\"\x0c\n\nNORESPONSE\"(\n\x07\x41\x64\x64ress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\")\n\tProcessId\x12\r\n\x05label\x18\x01 \x02(\r\x12\r\n\x05\x65poch\x18\x02 \x02(\r\"M\n\rObjectAddress\x12&\n\x04host\x18\x01 \x02(\x0b\x32\x18.bnet.protocol.ProcessId\x12\x14\n\tobject_id\x18\x02 \x01(\x04:\x01\x30\"\x08\n\x06NoData\"z\n\tErrorInfo\x12\x34\n\x0eobject_address\x18\x01 \x02(\x0b\x32\x1c.bnet.protocol.ObjectAddress\x12\x0e\n\x06status\x18\x02 \x02(\r\x12\x14\n\x0cservice_hash\x18\x03 \x02(\r\x12\x11\n\tmethod_id\x18\x04 \x02(\r\"\xb2\x01\n\x06Header\x12\x12\n\nservice_id\x18\x01 \x02(\r\x12\x11\n\tmethod_id\x18\x02 \x01(\r\x12\r\n\x05token\x18\x03 \x02(\r\x12\x14\n\tobject_id\x18\x04 \x01(\x04:\x01\x30\x12\x0f\n\x04size\x18\x05 \x01(\r:\x01\x30\x12\x11\n\x06status\x18\x06 \x01(\r:\x01\x30\x12\'\n\x05\x65rror\x18\x07 \x03(\x0b\x32\x18.bnet.protocol.ErrorInfo\x12\x0f\n\x07timeout\x18\x08 \x01(\x04'
)




_NORESPONSE = _descriptor.Descriptor(
  name='NORESPONSE',
  full_name='bnet.protocol.NORESPONSE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=33,
  serialized_end=45,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='bnet.protocol.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='bnet.protocol.Address.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='bnet.protocol.Address.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=47,
  serialized_end=87,
)


_PROCESSID = _descriptor.Descriptor(
  name='ProcessId',
  full_name='bnet.protocol.ProcessId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='bnet.protocol.ProcessId.label', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='bnet.protocol.ProcessId.epoch', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=89,
  serialized_end=130,
)


_OBJECTADDRESS = _descriptor.Descriptor(
  name='ObjectAddress',
  full_name='bnet.protocol.ObjectAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.ObjectAddress.host', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.ObjectAddress.object_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=132,
  serialized_end=209,
)


_NODATA = _descriptor.Descriptor(
  name='NoData',
  full_name='bnet.protocol.NoData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=211,
  serialized_end=219,
)


_ERRORINFO = _descriptor.Descriptor(
  name='ErrorInfo',
  full_name='bnet.protocol.ErrorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_address', full_name='bnet.protocol.ErrorInfo.object_address', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='bnet.protocol.ErrorInfo.status', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_hash', full_name='bnet.protocol.ErrorInfo.service_hash', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_id', full_name='bnet.protocol.ErrorInfo.method_id', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=221,
  serialized_end=343,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='bnet.protocol.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_id', full_name='bnet.protocol.Header.service_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_id', full_name='bnet.protocol.Header.method_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='bnet.protocol.Header.token', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.Header.object_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='bnet.protocol.Header.size', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='bnet.protocol.Header.status', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='bnet.protocol.Header.error', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='bnet.protocol.Header.timeout', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=346,
  serialized_end=524,
)

_OBJECTADDRESS.fields_by_name['host'].message_type = _PROCESSID
_ERRORINFO.fields_by_name['object_address'].message_type = _OBJECTADDRESS
_HEADER.fields_by_name['error'].message_type = _ERRORINFO
DESCRIPTOR.message_types_by_name['NORESPONSE'] = _NORESPONSE
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['ProcessId'] = _PROCESSID
DESCRIPTOR.message_types_by_name['ObjectAddress'] = _OBJECTADDRESS
DESCRIPTOR.message_types_by_name['NoData'] = _NODATA
DESCRIPTOR.message_types_by_name['ErrorInfo'] = _ERRORINFO
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NORESPONSE = _reflection.GeneratedProtocolMessageType('NORESPONSE', (_message.Message,), {
  'DESCRIPTOR' : _NORESPONSE,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.NORESPONSE)
  })
_sym_db.RegisterMessage(NORESPONSE)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.Address)
  })
_sym_db.RegisterMessage(Address)

ProcessId = _reflection.GeneratedProtocolMessageType('ProcessId', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSID,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.ProcessId)
  })
_sym_db.RegisterMessage(ProcessId)

ObjectAddress = _reflection.GeneratedProtocolMessageType('ObjectAddress', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTADDRESS,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.ObjectAddress)
  })
_sym_db.RegisterMessage(ObjectAddress)

NoData = _reflection.GeneratedProtocolMessageType('NoData', (_message.Message,), {
  'DESCRIPTOR' : _NODATA,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.NoData)
  })
_sym_db.RegisterMessage(NoData)

ErrorInfo = _reflection.GeneratedProtocolMessageType('ErrorInfo', (_message.Message,), {
  'DESCRIPTOR' : _ERRORINFO,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.ErrorInfo)
  })
_sym_db.RegisterMessage(ErrorInfo)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'bnet.rpc_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.Header)
  })
_sym_db.RegisterMessage(Header)


# @@protoc_insertion_point(module_scope)
