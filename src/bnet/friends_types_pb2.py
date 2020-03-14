# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/friends_types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bnet import attribute_pb2 as bnet_dot_attribute__pb2
from bnet import entity_pb2 as bnet_dot_entity__pb2
from bnet import invitation_types_pb2 as bnet_dot_invitation__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/friends_types.proto',
  package='bnet.protocol.friends',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x18\x62net/friends_types.proto\x12\x15\x62net.protocol.friends\x1a\x14\x62net/attribute.proto\x1a\x11\x62net/entity.proto\x1a\x1b\x62net/invitation_types.proto\"\xce\x01\n\x06\x46riend\x12#\n\x02id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x02 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x10\n\x04role\x18\x03 \x03(\rB\x02\x10\x01\x12\x15\n\nprivileges\x18\x04 \x01(\x04:\x01\x30\x12\x18\n\x10\x61ttributes_epoch\x18\x05 \x01(\x04\x12\x11\n\tfull_name\x18\x06 \x01(\t\x12\x12\n\nbattle_tag\x18\x07 \x01(\t\"\xa9\x01\n\x10\x46riendInvitation\x12\x1d\n\x0e\x66irst_received\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x04role\x18\x02 \x03(\rB\x02\x10\x01\x32\x64\n\rfriend_invite\x12$.bnet.protocol.invitation.Invitation\x18g \x01(\x0b\x32\'.bnet.protocol.friends.FriendInvitation\"\xa2\x02\n\x16\x46riendInvitationParams\x12\x14\n\x0ctarget_email\x18\x01 \x01(\t\x12\x19\n\x11target_battle_tag\x18\x02 \x01(\t\x12\x1a\n\x12inviter_battle_tag\x18\x03 \x01(\t\x12\x19\n\x11inviter_full_name\x18\x04 \x01(\t\x12\x1c\n\x14invitee_display_name\x18\x05 \x01(\t\x12\x10\n\x04role\x18\x06 \x03(\rB\x02\x10\x01\x32p\n\rfriend_params\x12*.bnet.protocol.invitation.InvitationParams\x18g \x01(\x0b\x32-.bnet.protocol.friends.FriendInvitationParams'
  ,
  dependencies=[bnet_dot_attribute__pb2.DESCRIPTOR,bnet_dot_entity__pb2.DESCRIPTOR,bnet_dot_invitation__types__pb2.DESCRIPTOR,])




_FRIEND = _descriptor.Descriptor(
  name='Friend',
  full_name='bnet.protocol.friends.Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.friends.Friend.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.friends.Friend.attribute', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.Friend.role', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='privileges', full_name='bnet.protocol.friends.Friend.privileges', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes_epoch', full_name='bnet.protocol.friends.Friend.attributes_epoch', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='bnet.protocol.friends.Friend.full_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battle_tag', full_name='bnet.protocol.friends.Friend.battle_tag', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=122,
  serialized_end=328,
)


_FRIENDINVITATION = _descriptor.Descriptor(
  name='FriendInvitation',
  full_name='bnet.protocol.friends.FriendInvitation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_received', full_name='bnet.protocol.friends.FriendInvitation.first_received', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.FriendInvitation.role', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='friend_invite', full_name='bnet.protocol.friends.FriendInvitation.friend_invite', index=0,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=331,
  serialized_end=500,
)


_FRIENDINVITATIONPARAMS = _descriptor.Descriptor(
  name='FriendInvitationParams',
  full_name='bnet.protocol.friends.FriendInvitationParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_email', full_name='bnet.protocol.friends.FriendInvitationParams.target_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_battle_tag', full_name='bnet.protocol.friends.FriendInvitationParams.target_battle_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inviter_battle_tag', full_name='bnet.protocol.friends.FriendInvitationParams.inviter_battle_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inviter_full_name', full_name='bnet.protocol.friends.FriendInvitationParams.inviter_full_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invitee_display_name', full_name='bnet.protocol.friends.FriendInvitationParams.invitee_display_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.FriendInvitationParams.role', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='friend_params', full_name='bnet.protocol.friends.FriendInvitationParams.friend_params', index=0,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=503,
  serialized_end=793,
)

_FRIEND.fields_by_name['id'].message_type = bnet_dot_entity__pb2._ENTITYID
_FRIEND.fields_by_name['attribute'].message_type = bnet_dot_attribute__pb2._ATTRIBUTE
DESCRIPTOR.message_types_by_name['Friend'] = _FRIEND
DESCRIPTOR.message_types_by_name['FriendInvitation'] = _FRIENDINVITATION
DESCRIPTOR.message_types_by_name['FriendInvitationParams'] = _FRIENDINVITATIONPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Friend = _reflection.GeneratedProtocolMessageType('Friend', (_message.Message,), {
  'DESCRIPTOR' : _FRIEND,
  '__module__' : 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.Friend)
  })
_sym_db.RegisterMessage(Friend)

FriendInvitation = _reflection.GeneratedProtocolMessageType('FriendInvitation', (_message.Message,), {
  'DESCRIPTOR' : _FRIENDINVITATION,
  '__module__' : 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendInvitation)
  })
_sym_db.RegisterMessage(FriendInvitation)

FriendInvitationParams = _reflection.GeneratedProtocolMessageType('FriendInvitationParams', (_message.Message,), {
  'DESCRIPTOR' : _FRIENDINVITATIONPARAMS,
  '__module__' : 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendInvitationParams)
  })
_sym_db.RegisterMessage(FriendInvitationParams)

_FRIENDINVITATION.extensions_by_name['friend_invite'].message_type = _FRIENDINVITATION
bnet_dot_invitation__types__pb2.Invitation.RegisterExtension(_FRIENDINVITATION.extensions_by_name['friend_invite'])
_FRIENDINVITATIONPARAMS.extensions_by_name['friend_params'].message_type = _FRIENDINVITATIONPARAMS
bnet_dot_invitation__types__pb2.InvitationParams.RegisterExtension(_FRIENDINVITATIONPARAMS.extensions_by_name['friend_params'])

_FRIEND.fields_by_name['role']._options = None
_FRIENDINVITATION.fields_by_name['role']._options = None
_FRIENDINVITATIONPARAMS.fields_by_name['role']._options = None
# @@protoc_insertion_point(module_scope)
