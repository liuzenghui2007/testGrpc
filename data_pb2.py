# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndata.proto\x12\nrandomizer\"\x07\n\x05\x45mpty\"`\n\rArrayResponse\x12\x32\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32$.randomizer.ArrayResponse.FloatArray\x1a\x1b\n\nFloatArray\x12\r\n\x05items\x18\x01 \x03(\x02\x32\x9b\x01\n\x11RandomizerService\x12>\n\x0eGetRandomArray\x12\x11.randomizer.Empty\x1a\x19.randomizer.ArrayResponse\x12\x46\n\x14GetRandomArrayStream\x12\x11.randomizer.Empty\x1a\x19.randomizer.ArrayResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=26
  _globals['_EMPTY']._serialized_end=33
  _globals['_ARRAYRESPONSE']._serialized_start=35
  _globals['_ARRAYRESPONSE']._serialized_end=131
  _globals['_ARRAYRESPONSE_FLOATARRAY']._serialized_start=104
  _globals['_ARRAYRESPONSE_FLOATARRAY']._serialized_end=131
  _globals['_RANDOMIZERSERVICE']._serialized_start=134
  _globals['_RANDOMIZERSERVICE']._serialized_end=289
# @@protoc_insertion_point(module_scope)
