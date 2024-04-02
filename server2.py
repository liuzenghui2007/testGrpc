import grpc
import randomizer_pb2
import randomizer_pb2_grpc
import time
import uuid
from concurrent import futures

crt = "/Users/liu/out/localhost.crt"
key = "/Users/liu/out/localhost.key"

class RandomizerService(randomizer_pb2_grpc.RandomizerServiceServicer):

    def GetRandomString(self, request, context):
        # 返回一个随机字符串
        return randomizer_pb2.RandomStringResponse(value="RandomString_" + str(uuid.uuid4()))

    def GetRandomUUIDStream(self, request, context):
        # 持续返回随机UUID
        while True:
            yield randomizer_pb2.RandomUUIDResponse(uuid=str(uuid.uuid4()))
            time.sleep(100/1000)  # 暂停1秒，避免过快发送


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    randomizer_pb2_grpc.add_RandomizerServiceServicer_to_server(
        RandomizerService(), server)
   # 配置服务器以使用 TLS
    # 配置服务器以使用 TLS
   # Load SSL credentials
    server_credentials = grpc.ssl_server_credentials(
        [(open(crt, "rb").read(), open(key, "rb").read())]
    )    
    server.add_secure_port('localhost:50051', server_credentials)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
