# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/evidence/v1beta1/tx.proto\x12\x17\x63osmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\x8e\x01\n\x11MsgSubmitEvidence\x12+\n\tsubmitter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x34\n\x08\x65vidence\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08\x45vidence:\x16\x82\xe7\xb0*\tsubmitter\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\")\n\x19MsgSubmitEvidenceResponse\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x32w\n\x03Msg\x12p\n\x0eSubmitEvidence\x12*.cosmos.evidence.v1beta1.MsgSubmitEvidence\x1a\x32.cosmos.evidence.v1beta1.MsgSubmitEvidenceResponseB3Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa8\xe2\x1e\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.evidence.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types\250\342\036\001'
  _MSGSUBMITEVIDENCE.fields_by_name['submitter']._options = None
  _MSGSUBMITEVIDENCE.fields_by_name['submitter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSUBMITEVIDENCE.fields_by_name['evidence']._options = None
  _MSGSUBMITEVIDENCE.fields_by_name['evidence']._serialized_options = b'\312\264-\010Evidence'
  _MSGSUBMITEVIDENCE._options = None
  _MSGSUBMITEVIDENCE._serialized_options = b'\202\347\260*\tsubmitter\350\240\037\000\210\240\037\000'
  _MSGSUBMITEVIDENCE._serialized_start=163
  _MSGSUBMITEVIDENCE._serialized_end=305
  _MSGSUBMITEVIDENCERESPONSE._serialized_start=307
  _MSGSUBMITEVIDENCERESPONSE._serialized_end=348
  _MSG._serialized_start=350
  _MSG._serialized_end=469
# @@protoc_insertion_point(module_scope)
