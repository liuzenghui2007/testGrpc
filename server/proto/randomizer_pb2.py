# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/randomizer.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'proto/randomizer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16proto/randomizer.proto\x12\nrandomizer\"\x07\n\x05\x45mpty\"%\n\x14RandomStringResponse\x12\r\n\x05value\x18\x01 \x01(\t\"\"\n\x12RandomUUIDResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x1c\n\rArrayResponse\x12\x0b\n\x03row\x18\x01 \x03(\x02\x32\xa3\x02\n\x11RandomizerService\x12\x46\n\x0fGetRandomString\x12\x11.randomizer.Empty\x1a .randomizer.RandomStringResponse\x12J\n\x13GetRandomUUIDStream\x12\x11.randomizer.Empty\x1a\x1e.randomizer.RandomUUIDResponse0\x01\x12\x38\n\x08GetArray\x12\x11.randomizer.Empty\x1a\x19.randomizer.ArrayResponse\x12@\n\x0eGetArrayStream\x12\x11.randomizer.Empty\x1a\x19.randomizer.ArrayResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.randomizer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=38
  _globals['_EMPTY']._serialized_end=45
  _globals['_RANDOMSTRINGRESPONSE']._serialized_start=47
  _globals['_RANDOMSTRINGRESPONSE']._serialized_end=84
  _globals['_RANDOMUUIDRESPONSE']._serialized_start=86
  _globals['_RANDOMUUIDRESPONSE']._serialized_end=120
  _globals['_ARRAYRESPONSE']._serialized_start=122
  _globals['_ARRAYRESPONSE']._serialized_end=150
  _globals['_RANDOMIZERSERVICE']._serialized_start=153
  _globals['_RANDOMIZERSERVICE']._serialized_end=444
# @@protoc_insertion_point(module_scope)
