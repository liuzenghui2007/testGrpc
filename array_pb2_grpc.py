# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import array_pb2 as array__pb2


class ArrayServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetArray = channel.unary_unary(
                '/array.ArrayService/GetArray',
                request_serializer=array__pb2.Empty.SerializeToString,
                response_deserializer=array__pb2.ArrayResponse.FromString,
                )
        self.GetArrayStream = channel.unary_stream(
                '/array.ArrayService/GetArrayStream',
                request_serializer=array__pb2.Empty.SerializeToString,
                response_deserializer=array__pb2.ArrayResponse.FromString,
                )


class ArrayServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetArray(self, request, context):
        """获取单个640x512的数组
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetArrayStream(self, request, context):
        """获取640x512的数组流
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ArrayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArray,
                    request_deserializer=array__pb2.Empty.FromString,
                    response_serializer=array__pb2.ArrayResponse.SerializeToString,
            ),
            'GetArrayStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetArrayStream,
                    request_deserializer=array__pb2.Empty.FromString,
                    response_serializer=array__pb2.ArrayResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'array.ArrayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ArrayService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/array.ArrayService/GetArray',
            array__pb2.Empty.SerializeToString,
            array__pb2.ArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetArrayStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/array.ArrayService/GetArrayStream',
            array__pb2.Empty.SerializeToString,
            array__pb2.ArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
