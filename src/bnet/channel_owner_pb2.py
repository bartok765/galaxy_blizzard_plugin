# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/channel_owner.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bnet import channel_types_pb2 as bnet_dot_channel__types__pb2
from bnet import entity_pb2 as bnet_dot_entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/channel_owner.proto',
  package='bnet.protocol.channel',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x18\x62net/channel_owner.proto\x12\x15\x62net.protocol.channel\x1a\x18\x62net/channel_types.proto\x1a\x11\x62net/entity.proto\"\x15\n\x13GetChannelIdRequest\"C\n\x14GetChannelIdResponse\x12+\n\nchannel_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\xeb\x02\n\x14\x43reateChannelRequest\x12/\n\x0e\x61gent_identity\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.Identity\x12\x38\n\x0cmember_state\x18\x02 \x01(\x0b\x32\".bnet.protocol.channel.MemberState\x12:\n\rchannel_state\x18\x03 \x01(\x0b\x32#.bnet.protocol.channel.ChannelState\x12+\n\nchannel_id\x18\x04 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x05 \x01(\x04\x12,\n\x0blocal_agent\x18\x06 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12>\n\x12local_member_state\x18\x07 \x01(\x0b\x32\".bnet.protocol.channel.MemberState\"W\n\x15\x43reateChannelResponse\x12\x11\n\tobject_id\x18\x01 \x02(\x04\x12+\n\nchannel_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\x93\x02\n\x12JoinChannelRequest\x12/\n\x0e\x61gent_identity\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.Identity\x12\x38\n\x0cmember_state\x18\x02 \x01(\x0b\x32\".bnet.protocol.channel.MemberState\x12+\n\nchannel_id\x18\x03 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x04 \x02(\x04\x12\x32\n\x11\x66riend_account_id\x18\x05 \x03(\x0b\x32\x17.bnet.protocol.EntityId\x12\x1e\n\x10local_subscriber\x18\x06 \x01(\x08:\x04true\"\x87\x01\n\x13JoinChannelResponse\x12\x11\n\tobject_id\x18\x01 \x01(\x04\x12(\n\x19require_friend_validation\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x33\n\x12privileged_account\x18\x03 \x03(\x0b\x32\x17.bnet.protocol.EntityId\"\x84\x01\n\x17SubscribeChannelRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12+\n\nchannel_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x03 \x02(\x04\"-\n\x18SubscribeChannelResponse\x12\x11\n\tobject_id\x18\x01 \x01(\x04\"\x81\x01\n\x12\x46indChannelRequest\x12/\n\x0e\x61gent_identity\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.Identity\x12:\n\x07options\x18\x02 \x02(\x0b\x32).bnet.protocol.channel.FindChannelOptions\"Q\n\x13\x46indChannelResponse\x12:\n\x07\x63hannel\x18\x01 \x03(\x0b\x32).bnet.protocol.channel.ChannelDescription\"\xa9\x01\n\x15GetChannelInfoRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12+\n\nchannel_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x1a\n\x0b\x66\x65tch_state\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rfetch_members\x18\x04 \x01(\x08:\x05\x66\x61lse\"R\n\x16GetChannelInfoResponse\x12\x38\n\x0c\x63hannel_info\x18\x01 \x01(\x0b\x32\".bnet.protocol.channel.ChannelInfo'
  ,
  dependencies=[bnet_dot_channel__types__pb2.DESCRIPTOR,bnet_dot_entity__pb2.DESCRIPTOR,])




_GETCHANNELIDREQUEST = _descriptor.Descriptor(
  name='GetChannelIdRequest',
  full_name='bnet.protocol.channel.GetChannelIdRequest',
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
  serialized_start=96,
  serialized_end=117,
)


_GETCHANNELIDRESPONSE = _descriptor.Descriptor(
  name='GetChannelIdResponse',
  full_name='bnet.protocol.channel.GetChannelIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.GetChannelIdResponse.channel_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=186,
)


_CREATECHANNELREQUEST = _descriptor.Descriptor(
  name='CreateChannelRequest',
  full_name='bnet.protocol.channel.CreateChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_identity', full_name='bnet.protocol.channel.CreateChannelRequest.agent_identity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_state', full_name='bnet.protocol.channel.CreateChannelRequest.member_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_state', full_name='bnet.protocol.channel.CreateChannelRequest.channel_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.CreateChannelRequest.channel_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel.CreateChannelRequest.object_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_agent', full_name='bnet.protocol.channel.CreateChannelRequest.local_agent', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_member_state', full_name='bnet.protocol.channel.CreateChannelRequest.local_member_state', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=552,
)


_CREATECHANNELRESPONSE = _descriptor.Descriptor(
  name='CreateChannelResponse',
  full_name='bnet.protocol.channel.CreateChannelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel.CreateChannelResponse.object_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.CreateChannelResponse.channel_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=641,
)


_JOINCHANNELREQUEST = _descriptor.Descriptor(
  name='JoinChannelRequest',
  full_name='bnet.protocol.channel.JoinChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_identity', full_name='bnet.protocol.channel.JoinChannelRequest.agent_identity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_state', full_name='bnet.protocol.channel.JoinChannelRequest.member_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.JoinChannelRequest.channel_id', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel.JoinChannelRequest.object_id', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_account_id', full_name='bnet.protocol.channel.JoinChannelRequest.friend_account_id', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_subscriber', full_name='bnet.protocol.channel.JoinChannelRequest.local_subscriber', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=644,
  serialized_end=919,
)


_JOINCHANNELRESPONSE = _descriptor.Descriptor(
  name='JoinChannelResponse',
  full_name='bnet.protocol.channel.JoinChannelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel.JoinChannelResponse.object_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='require_friend_validation', full_name='bnet.protocol.channel.JoinChannelResponse.require_friend_validation', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='privileged_account', full_name='bnet.protocol.channel.JoinChannelResponse.privileged_account', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=922,
  serialized_end=1057,
)


_SUBSCRIBECHANNELREQUEST = _descriptor.Descriptor(
  name='SubscribeChannelRequest',
  full_name='bnet.protocol.channel.SubscribeChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel.SubscribeChannelRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.SubscribeChannelRequest.channel_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel.SubscribeChannelRequest.object_id', index=2,
      number=3, type=4, cpp_type=4, label=2,
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
  serialized_start=1060,
  serialized_end=1192,
)


_SUBSCRIBECHANNELRESPONSE = _descriptor.Descriptor(
  name='SubscribeChannelResponse',
  full_name='bnet.protocol.channel.SubscribeChannelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel.SubscribeChannelResponse.object_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=1194,
  serialized_end=1239,
)


_FINDCHANNELREQUEST = _descriptor.Descriptor(
  name='FindChannelRequest',
  full_name='bnet.protocol.channel.FindChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_identity', full_name='bnet.protocol.channel.FindChannelRequest.agent_identity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='bnet.protocol.channel.FindChannelRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1242,
  serialized_end=1371,
)


_FINDCHANNELRESPONSE = _descriptor.Descriptor(
  name='FindChannelResponse',
  full_name='bnet.protocol.channel.FindChannelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='bnet.protocol.channel.FindChannelResponse.channel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1373,
  serialized_end=1454,
)


_GETCHANNELINFOREQUEST = _descriptor.Descriptor(
  name='GetChannelInfoRequest',
  full_name='bnet.protocol.channel.GetChannelInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel.GetChannelInfoRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.GetChannelInfoRequest.channel_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch_state', full_name='bnet.protocol.channel.GetChannelInfoRequest.fetch_state', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch_members', full_name='bnet.protocol.channel.GetChannelInfoRequest.fetch_members', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=1457,
  serialized_end=1626,
)


_GETCHANNELINFORESPONSE = _descriptor.Descriptor(
  name='GetChannelInfoResponse',
  full_name='bnet.protocol.channel.GetChannelInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_info', full_name='bnet.protocol.channel.GetChannelInfoResponse.channel_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1628,
  serialized_end=1710,
)

_GETCHANNELIDRESPONSE.fields_by_name['channel_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_CREATECHANNELREQUEST.fields_by_name['agent_identity'].message_type = bnet_dot_entity__pb2._IDENTITY
_CREATECHANNELREQUEST.fields_by_name['member_state'].message_type = bnet_dot_channel__types__pb2._MEMBERSTATE
_CREATECHANNELREQUEST.fields_by_name['channel_state'].message_type = bnet_dot_channel__types__pb2._CHANNELSTATE
_CREATECHANNELREQUEST.fields_by_name['channel_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_CREATECHANNELREQUEST.fields_by_name['local_agent'].message_type = bnet_dot_entity__pb2._ENTITYID
_CREATECHANNELREQUEST.fields_by_name['local_member_state'].message_type = bnet_dot_channel__types__pb2._MEMBERSTATE
_CREATECHANNELRESPONSE.fields_by_name['channel_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_JOINCHANNELREQUEST.fields_by_name['agent_identity'].message_type = bnet_dot_entity__pb2._IDENTITY
_JOINCHANNELREQUEST.fields_by_name['member_state'].message_type = bnet_dot_channel__types__pb2._MEMBERSTATE
_JOINCHANNELREQUEST.fields_by_name['channel_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_JOINCHANNELREQUEST.fields_by_name['friend_account_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_JOINCHANNELRESPONSE.fields_by_name['privileged_account'].message_type = bnet_dot_entity__pb2._ENTITYID
_SUBSCRIBECHANNELREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_SUBSCRIBECHANNELREQUEST.fields_by_name['channel_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_FINDCHANNELREQUEST.fields_by_name['agent_identity'].message_type = bnet_dot_entity__pb2._IDENTITY
_FINDCHANNELREQUEST.fields_by_name['options'].message_type = bnet_dot_channel__types__pb2._FINDCHANNELOPTIONS
_FINDCHANNELRESPONSE.fields_by_name['channel'].message_type = bnet_dot_channel__types__pb2._CHANNELDESCRIPTION
_GETCHANNELINFOREQUEST.fields_by_name['agent_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_GETCHANNELINFOREQUEST.fields_by_name['channel_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_GETCHANNELINFORESPONSE.fields_by_name['channel_info'].message_type = bnet_dot_channel__types__pb2._CHANNELINFO
DESCRIPTOR.message_types_by_name['GetChannelIdRequest'] = _GETCHANNELIDREQUEST
DESCRIPTOR.message_types_by_name['GetChannelIdResponse'] = _GETCHANNELIDRESPONSE
DESCRIPTOR.message_types_by_name['CreateChannelRequest'] = _CREATECHANNELREQUEST
DESCRIPTOR.message_types_by_name['CreateChannelResponse'] = _CREATECHANNELRESPONSE
DESCRIPTOR.message_types_by_name['JoinChannelRequest'] = _JOINCHANNELREQUEST
DESCRIPTOR.message_types_by_name['JoinChannelResponse'] = _JOINCHANNELRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeChannelRequest'] = _SUBSCRIBECHANNELREQUEST
DESCRIPTOR.message_types_by_name['SubscribeChannelResponse'] = _SUBSCRIBECHANNELRESPONSE
DESCRIPTOR.message_types_by_name['FindChannelRequest'] = _FINDCHANNELREQUEST
DESCRIPTOR.message_types_by_name['FindChannelResponse'] = _FINDCHANNELRESPONSE
DESCRIPTOR.message_types_by_name['GetChannelInfoRequest'] = _GETCHANNELINFOREQUEST
DESCRIPTOR.message_types_by_name['GetChannelInfoResponse'] = _GETCHANNELINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetChannelIdRequest = _reflection.GeneratedProtocolMessageType('GetChannelIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHANNELIDREQUEST,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.GetChannelIdRequest)
  })
_sym_db.RegisterMessage(GetChannelIdRequest)

GetChannelIdResponse = _reflection.GeneratedProtocolMessageType('GetChannelIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCHANNELIDRESPONSE,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.GetChannelIdResponse)
  })
_sym_db.RegisterMessage(GetChannelIdResponse)

CreateChannelRequest = _reflection.GeneratedProtocolMessageType('CreateChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECHANNELREQUEST,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.CreateChannelRequest)
  })
_sym_db.RegisterMessage(CreateChannelRequest)

CreateChannelResponse = _reflection.GeneratedProtocolMessageType('CreateChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECHANNELRESPONSE,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.CreateChannelResponse)
  })
_sym_db.RegisterMessage(CreateChannelResponse)

JoinChannelRequest = _reflection.GeneratedProtocolMessageType('JoinChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINCHANNELREQUEST,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.JoinChannelRequest)
  })
_sym_db.RegisterMessage(JoinChannelRequest)

JoinChannelResponse = _reflection.GeneratedProtocolMessageType('JoinChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOINCHANNELRESPONSE,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.JoinChannelResponse)
  })
_sym_db.RegisterMessage(JoinChannelResponse)

SubscribeChannelRequest = _reflection.GeneratedProtocolMessageType('SubscribeChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANNELREQUEST,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.SubscribeChannelRequest)
  })
_sym_db.RegisterMessage(SubscribeChannelRequest)

SubscribeChannelResponse = _reflection.GeneratedProtocolMessageType('SubscribeChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANNELRESPONSE,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.SubscribeChannelResponse)
  })
_sym_db.RegisterMessage(SubscribeChannelResponse)

FindChannelRequest = _reflection.GeneratedProtocolMessageType('FindChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDCHANNELREQUEST,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.FindChannelRequest)
  })
_sym_db.RegisterMessage(FindChannelRequest)

FindChannelResponse = _reflection.GeneratedProtocolMessageType('FindChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDCHANNELRESPONSE,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.FindChannelResponse)
  })
_sym_db.RegisterMessage(FindChannelResponse)

GetChannelInfoRequest = _reflection.GeneratedProtocolMessageType('GetChannelInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHANNELINFOREQUEST,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.GetChannelInfoRequest)
  })
_sym_db.RegisterMessage(GetChannelInfoRequest)

GetChannelInfoResponse = _reflection.GeneratedProtocolMessageType('GetChannelInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCHANNELINFORESPONSE,
  '__module__' : 'bnet.channel_owner_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.GetChannelInfoResponse)
  })
_sym_db.RegisterMessage(GetChannelInfoResponse)


# @@protoc_insertion_point(module_scope)
