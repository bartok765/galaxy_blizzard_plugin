# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/challenge_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bnet import attribute_pb2 as bnet_dot_attribute__pb2
from bnet import entity_pb2 as bnet_dot_entity__pb2
from bnet import rpc_pb2 as bnet_dot_rpc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/challenge_service.proto',
  package='bnet.protocol.challenge',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x1c\x62net/challenge_service.proto\x12\x17\x62net.protocol.challenge\x1a\x14\x62net/attribute.proto\x1a\x11\x62net/entity.proto\x1a\x0e\x62net/rpc.proto\"H\n\tChallenge\x12\x0c\n\x04type\x18\x01 \x02(\x07\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x03 \x01(\t\x12\x0f\n\x07retries\x18\x04 \x01(\r\"^\n\x16\x43hallengePickedRequest\x12\x11\n\tchallenge\x18\x01 \x02(\x07\x12\n\n\x02id\x18\x02 \x01(\r\x12%\n\x16new_challenge_protocol\x18\x03 \x01(\x08:\x05\x66\x61lse\"\'\n\x17\x43hallengePickedResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"D\n\x18\x43hallengeAnsweredRequest\x12\x0e\n\x06\x61nswer\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\n\n\x02id\x18\x03 \x01(\r\"U\n\x19\x43hallengeAnsweredResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x10\n\x08\x64o_retry\x18\x02 \x01(\x08\x12\x18\n\x10record_not_found\x18\x03 \x01(\x08\"\'\n\x19\x43hallengeCancelledRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x8b\x02\n\x1aSendChallengeToUserRequest\x12)\n\x07peer_id\x18\x01 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x36\n\nchallenges\x18\x03 \x03(\x0b\x32\".bnet.protocol.challenge.Challenge\x12\x0f\n\x07\x63ontext\x18\x04 \x02(\x07\x12\x0f\n\x07timeout\x18\x05 \x01(\x04\x12\x36\n\nattributes\x18\x06 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\")\n\x1bSendChallengeToUserResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\xe7\x01\n\x14\x43hallengeUserRequest\x12\x36\n\nchallenges\x18\x01 \x03(\x0b\x32\".bnet.protocol.challenge.Challenge\x12\x0f\n\x07\x63ontext\x18\x02 \x02(\x07\x12\n\n\x02id\x18\x03 \x01(\r\x12\x10\n\x08\x64\x65\x61\x64line\x18\x04 \x01(\x04\x12\x36\n\nattributes\x18\x05 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x30\n\x0fgame_account_id\x18\x06 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"T\n\x16\x43hallengeResultRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\x07\x12\x10\n\x08\x65rror_id\x18\x03 \x01(\r\x12\x0e\n\x06\x61nswer\x18\x04 \x01(\x0c\"X\n\x18\x43hallengeExternalRequest\x12\x15\n\rrequest_token\x18\x01 \x01(\t\x12\x14\n\x0cpayload_type\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"F\n\x17\x43hallengeExternalResult\x12\x15\n\rrequest_token\x18\x01 \x01(\t\x12\x14\n\x06passed\x18\x02 \x01(\x08:\x04true'
  ,
  dependencies=[bnet_dot_attribute__pb2.DESCRIPTOR,bnet_dot_entity__pb2.DESCRIPTOR,bnet_dot_rpc__pb2.DESCRIPTOR,])




_CHALLENGE = _descriptor.Descriptor(
  name='Challenge',
  full_name='bnet.protocol.challenge.Challenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bnet.protocol.challenge.Challenge.type', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='bnet.protocol.challenge.Challenge.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='bnet.protocol.challenge.Challenge.answer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retries', full_name='bnet.protocol.challenge.Challenge.retries', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=114,
  serialized_end=186,
)


_CHALLENGEPICKEDREQUEST = _descriptor.Descriptor(
  name='ChallengePickedRequest',
  full_name='bnet.protocol.challenge.ChallengePickedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='bnet.protocol.challenge.ChallengePickedRequest.challenge', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.challenge.ChallengePickedRequest.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_challenge_protocol', full_name='bnet.protocol.challenge.ChallengePickedRequest.new_challenge_protocol', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=188,
  serialized_end=282,
)


_CHALLENGEPICKEDRESPONSE = _descriptor.Descriptor(
  name='ChallengePickedResponse',
  full_name='bnet.protocol.challenge.ChallengePickedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='bnet.protocol.challenge.ChallengePickedResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=284,
  serialized_end=323,
)


_CHALLENGEANSWEREDREQUEST = _descriptor.Descriptor(
  name='ChallengeAnsweredRequest',
  full_name='bnet.protocol.challenge.ChallengeAnsweredRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='bnet.protocol.challenge.ChallengeAnsweredRequest.answer', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='bnet.protocol.challenge.ChallengeAnsweredRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.challenge.ChallengeAnsweredRequest.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=325,
  serialized_end=393,
)


_CHALLENGEANSWEREDRESPONSE = _descriptor.Descriptor(
  name='ChallengeAnsweredResponse',
  full_name='bnet.protocol.challenge.ChallengeAnsweredResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='bnet.protocol.challenge.ChallengeAnsweredResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_retry', full_name='bnet.protocol.challenge.ChallengeAnsweredResponse.do_retry', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record_not_found', full_name='bnet.protocol.challenge.ChallengeAnsweredResponse.record_not_found', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=395,
  serialized_end=480,
)


_CHALLENGECANCELLEDREQUEST = _descriptor.Descriptor(
  name='ChallengeCancelledRequest',
  full_name='bnet.protocol.challenge.ChallengeCancelledRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.challenge.ChallengeCancelledRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=482,
  serialized_end=521,
)


_SENDCHALLENGETOUSERREQUEST = _descriptor.Descriptor(
  name='SendChallengeToUserRequest',
  full_name='bnet.protocol.challenge.SendChallengeToUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer_id', full_name='bnet.protocol.challenge.SendChallengeToUserRequest.peer_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.challenge.SendChallengeToUserRequest.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenges', full_name='bnet.protocol.challenge.SendChallengeToUserRequest.challenges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='bnet.protocol.challenge.SendChallengeToUserRequest.context', index=3,
      number=4, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='bnet.protocol.challenge.SendChallengeToUserRequest.timeout', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='bnet.protocol.challenge.SendChallengeToUserRequest.attributes', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=524,
  serialized_end=791,
)


_SENDCHALLENGETOUSERRESPONSE = _descriptor.Descriptor(
  name='SendChallengeToUserResponse',
  full_name='bnet.protocol.challenge.SendChallengeToUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.challenge.SendChallengeToUserResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=793,
  serialized_end=834,
)


_CHALLENGEUSERREQUEST = _descriptor.Descriptor(
  name='ChallengeUserRequest',
  full_name='bnet.protocol.challenge.ChallengeUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenges', full_name='bnet.protocol.challenge.ChallengeUserRequest.challenges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='bnet.protocol.challenge.ChallengeUserRequest.context', index=1,
      number=2, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.challenge.ChallengeUserRequest.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='bnet.protocol.challenge.ChallengeUserRequest.deadline', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='bnet.protocol.challenge.ChallengeUserRequest.attributes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.challenge.ChallengeUserRequest.game_account_id', index=5,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=837,
  serialized_end=1068,
)


_CHALLENGERESULTREQUEST = _descriptor.Descriptor(
  name='ChallengeResultRequest',
  full_name='bnet.protocol.challenge.ChallengeResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.challenge.ChallengeResultRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='bnet.protocol.challenge.ChallengeResultRequest.type', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_id', full_name='bnet.protocol.challenge.ChallengeResultRequest.error_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='bnet.protocol.challenge.ChallengeResultRequest.answer', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1070,
  serialized_end=1154,
)


_CHALLENGEEXTERNALREQUEST = _descriptor.Descriptor(
  name='ChallengeExternalRequest',
  full_name='bnet.protocol.challenge.ChallengeExternalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_token', full_name='bnet.protocol.challenge.ChallengeExternalRequest.request_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='bnet.protocol.challenge.ChallengeExternalRequest.payload_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='bnet.protocol.challenge.ChallengeExternalRequest.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1156,
  serialized_end=1244,
)


_CHALLENGEEXTERNALRESULT = _descriptor.Descriptor(
  name='ChallengeExternalResult',
  full_name='bnet.protocol.challenge.ChallengeExternalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_token', full_name='bnet.protocol.challenge.ChallengeExternalResult.request_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passed', full_name='bnet.protocol.challenge.ChallengeExternalResult.passed', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1246,
  serialized_end=1316,
)

_SENDCHALLENGETOUSERREQUEST.fields_by_name['peer_id'].message_type = bnet_dot_rpc__pb2._PROCESSID
_SENDCHALLENGETOUSERREQUEST.fields_by_name['game_account_id'].message_type = bnet_dot_entity__pb2._ENTITYID
_SENDCHALLENGETOUSERREQUEST.fields_by_name['challenges'].message_type = _CHALLENGE
_SENDCHALLENGETOUSERREQUEST.fields_by_name['attributes'].message_type = bnet_dot_attribute__pb2._ATTRIBUTE
_CHALLENGEUSERREQUEST.fields_by_name['challenges'].message_type = _CHALLENGE
_CHALLENGEUSERREQUEST.fields_by_name['attributes'].message_type = bnet_dot_attribute__pb2._ATTRIBUTE
_CHALLENGEUSERREQUEST.fields_by_name['game_account_id'].message_type = bnet_dot_entity__pb2._ENTITYID
DESCRIPTOR.message_types_by_name['Challenge'] = _CHALLENGE
DESCRIPTOR.message_types_by_name['ChallengePickedRequest'] = _CHALLENGEPICKEDREQUEST
DESCRIPTOR.message_types_by_name['ChallengePickedResponse'] = _CHALLENGEPICKEDRESPONSE
DESCRIPTOR.message_types_by_name['ChallengeAnsweredRequest'] = _CHALLENGEANSWEREDREQUEST
DESCRIPTOR.message_types_by_name['ChallengeAnsweredResponse'] = _CHALLENGEANSWEREDRESPONSE
DESCRIPTOR.message_types_by_name['ChallengeCancelledRequest'] = _CHALLENGECANCELLEDREQUEST
DESCRIPTOR.message_types_by_name['SendChallengeToUserRequest'] = _SENDCHALLENGETOUSERREQUEST
DESCRIPTOR.message_types_by_name['SendChallengeToUserResponse'] = _SENDCHALLENGETOUSERRESPONSE
DESCRIPTOR.message_types_by_name['ChallengeUserRequest'] = _CHALLENGEUSERREQUEST
DESCRIPTOR.message_types_by_name['ChallengeResultRequest'] = _CHALLENGERESULTREQUEST
DESCRIPTOR.message_types_by_name['ChallengeExternalRequest'] = _CHALLENGEEXTERNALREQUEST
DESCRIPTOR.message_types_by_name['ChallengeExternalResult'] = _CHALLENGEEXTERNALRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Challenge = _reflection.GeneratedProtocolMessageType('Challenge', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGE,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.Challenge)
  })
_sym_db.RegisterMessage(Challenge)

ChallengePickedRequest = _reflection.GeneratedProtocolMessageType('ChallengePickedRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEPICKEDREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengePickedRequest)
  })
_sym_db.RegisterMessage(ChallengePickedRequest)

ChallengePickedResponse = _reflection.GeneratedProtocolMessageType('ChallengePickedResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEPICKEDRESPONSE,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengePickedResponse)
  })
_sym_db.RegisterMessage(ChallengePickedResponse)

ChallengeAnsweredRequest = _reflection.GeneratedProtocolMessageType('ChallengeAnsweredRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEANSWEREDREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeAnsweredRequest)
  })
_sym_db.RegisterMessage(ChallengeAnsweredRequest)

ChallengeAnsweredResponse = _reflection.GeneratedProtocolMessageType('ChallengeAnsweredResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEANSWEREDRESPONSE,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeAnsweredResponse)
  })
_sym_db.RegisterMessage(ChallengeAnsweredResponse)

ChallengeCancelledRequest = _reflection.GeneratedProtocolMessageType('ChallengeCancelledRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGECANCELLEDREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeCancelledRequest)
  })
_sym_db.RegisterMessage(ChallengeCancelledRequest)

SendChallengeToUserRequest = _reflection.GeneratedProtocolMessageType('SendChallengeToUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDCHALLENGETOUSERREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.SendChallengeToUserRequest)
  })
_sym_db.RegisterMessage(SendChallengeToUserRequest)

SendChallengeToUserResponse = _reflection.GeneratedProtocolMessageType('SendChallengeToUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDCHALLENGETOUSERRESPONSE,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.SendChallengeToUserResponse)
  })
_sym_db.RegisterMessage(SendChallengeToUserResponse)

ChallengeUserRequest = _reflection.GeneratedProtocolMessageType('ChallengeUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEUSERREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeUserRequest)
  })
_sym_db.RegisterMessage(ChallengeUserRequest)

ChallengeResultRequest = _reflection.GeneratedProtocolMessageType('ChallengeResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGERESULTREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeResultRequest)
  })
_sym_db.RegisterMessage(ChallengeResultRequest)

ChallengeExternalRequest = _reflection.GeneratedProtocolMessageType('ChallengeExternalRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEEXTERNALREQUEST,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeExternalRequest)
  })
_sym_db.RegisterMessage(ChallengeExternalRequest)

ChallengeExternalResult = _reflection.GeneratedProtocolMessageType('ChallengeExternalResult', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEEXTERNALRESULT,
  '__module__' : 'bnet.challenge_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.challenge.ChallengeExternalResult)
  })
_sym_db.RegisterMessage(ChallengeExternalResult)


# @@protoc_insertion_point(module_scope)
