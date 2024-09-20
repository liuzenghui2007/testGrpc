# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto import randomizer_pb2 as proto_dot_randomizer__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/randomizer_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RandomizerServiceStub(object):
    """定义服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRandomString = channel.unary_unary(
                '/randomizer.RandomizerService/GetRandomString',
                request_serializer=proto_dot_randomizer__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_randomizer__pb2.RandomStringResponse.FromString,
                _registered_method=True)
        self.GetRandomUUIDStream = channel.unary_stream(
                '/randomizer.RandomizerService/GetRandomUUIDStream',
                request_serializer=proto_dot_randomizer__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_randomizer__pb2.RandomUUIDResponse.FromString,
                _registered_method=True)
        self.GetArray = channel.unary_unary(
                '/randomizer.RandomizerService/GetArray',
                request_serializer=proto_dot_randomizer__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_randomizer__pb2.ArrayResponse.FromString,
                _registered_method=True)
        self.GetArrayStream = channel.unary_stream(
                '/randomizer.RandomizerService/GetArrayStream',
                request_serializer=proto_dot_randomizer__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_randomizer__pb2.ArrayResponse.FromString,
                _registered_method=True)
        self.Get2DArray = channel.unary_unary(
                '/randomizer.RandomizerService/Get2DArray',
                request_serializer=proto_dot_randomizer__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_randomizer__pb2.NumberArray2D.FromString,
                _registered_method=True)
        self.Get2DArrayStream = channel.unary_stream(
                '/randomizer.RandomizerService/Get2DArrayStream',
                request_serializer=proto_dot_randomizer__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_randomizer__pb2.NumberArray2D.FromString,
                _registered_method=True)


class RandomizerServiceServicer(object):
    """定义服务
    """

    def GetRandomString(self, request, context):
        """一元接口，返回一个随机字符串
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRandomUUIDStream(self, request, context):
        """流接口，持续返回随机UUID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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

    def Get2DArray(self, request, context):
        """获取二维数组
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get2DArrayStream(self, request, context):
        """获取二维数组流
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RandomizerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRandomString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRandomString,
                    request_deserializer=proto_dot_randomizer__pb2.Empty.FromString,
                    response_serializer=proto_dot_randomizer__pb2.RandomStringResponse.SerializeToString,
            ),
            'GetRandomUUIDStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetRandomUUIDStream,
                    request_deserializer=proto_dot_randomizer__pb2.Empty.FromString,
                    response_serializer=proto_dot_randomizer__pb2.RandomUUIDResponse.SerializeToString,
            ),
            'GetArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArray,
                    request_deserializer=proto_dot_randomizer__pb2.Empty.FromString,
                    response_serializer=proto_dot_randomizer__pb2.ArrayResponse.SerializeToString,
            ),
            'GetArrayStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetArrayStream,
                    request_deserializer=proto_dot_randomizer__pb2.Empty.FromString,
                    response_serializer=proto_dot_randomizer__pb2.ArrayResponse.SerializeToString,
            ),
            'Get2DArray': grpc.unary_unary_rpc_method_handler(
                    servicer.Get2DArray,
                    request_deserializer=proto_dot_randomizer__pb2.Empty.FromString,
                    response_serializer=proto_dot_randomizer__pb2.NumberArray2D.SerializeToString,
            ),
            'Get2DArrayStream': grpc.unary_stream_rpc_method_handler(
                    servicer.Get2DArrayStream,
                    request_deserializer=proto_dot_randomizer__pb2.Empty.FromString,
                    response_serializer=proto_dot_randomizer__pb2.NumberArray2D.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'randomizer.RandomizerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('randomizer.RandomizerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RandomizerService(object):
    """定义服务
    """

    @staticmethod
    def GetRandomString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/randomizer.RandomizerService/GetRandomString',
            proto_dot_randomizer__pb2.Empty.SerializeToString,
            proto_dot_randomizer__pb2.RandomStringResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRandomUUIDStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/randomizer.RandomizerService/GetRandomUUIDStream',
            proto_dot_randomizer__pb2.Empty.SerializeToString,
            proto_dot_randomizer__pb2.RandomUUIDResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/randomizer.RandomizerService/GetArray',
            proto_dot_randomizer__pb2.Empty.SerializeToString,
            proto_dot_randomizer__pb2.ArrayResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_stream(
            request,
            target,
            '/randomizer.RandomizerService/GetArrayStream',
            proto_dot_randomizer__pb2.Empty.SerializeToString,
            proto_dot_randomizer__pb2.ArrayResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get2DArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/randomizer.RandomizerService/Get2DArray',
            proto_dot_randomizer__pb2.Empty.SerializeToString,
            proto_dot_randomizer__pb2.NumberArray2D.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get2DArrayStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/randomizer.RandomizerService/Get2DArrayStream',
            proto_dot_randomizer__pb2.Empty.SerializeToString,
            proto_dot_randomizer__pb2.NumberArray2D.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
