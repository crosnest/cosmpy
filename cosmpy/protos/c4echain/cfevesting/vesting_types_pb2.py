# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfevesting/vesting_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'c4echain/cfevesting/vesting_types.proto\x12 chain4energy.c4echain.cfevesting\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\"T\n\x0cVestingTypes\x12\x44\n\rvesting_types\x18\x01 \x03(\x0b\x32-.chain4energy.c4echain.cfevesting.VestingType\"\xd2\x01\n\x0bVestingType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\rlockup_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12;\n\x0evesting_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12<\n\x04\x66ree\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x36Z4github.com/chain4energy/c4e-chain/x/cfevesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfevesting.vesting_types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/chain4energy/c4e-chain/x/cfevesting/types'
  _VESTINGTYPE.fields_by_name['lockup_period']._options = None
  _VESTINGTYPE.fields_by_name['lockup_period']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _VESTINGTYPE.fields_by_name['vesting_period']._options = None
  _VESTINGTYPE.fields_by_name['vesting_period']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _VESTINGTYPE.fields_by_name['free']._options = None
  _VESTINGTYPE.fields_by_name['free']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _VESTINGTYPES._serialized_start=131
  _VESTINGTYPES._serialized_end=215
  _VESTINGTYPE._serialized_start=218
  _VESTINGTYPE._serialized_end=428
# @@protoc_insertion_point(module_scope)
