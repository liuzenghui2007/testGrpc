import grpc
import randomizer_pb2
import randomizer_pb2_grpc
import time
import uuid
from concurrent import futures
import random


class RandomizerService(randomizer_pb2_grpc.RandomizerServiceServicer):

    def GetRandomString(self, request, context):
        # 返回一个随机字符串
        print('dd')
        return randomizer_pb2.RandomStringResponse(value="RandomString_" + str(uuid.uuid4()))

    def GetRandomUUIDStream(self, request, context):
        # 持续返回随机UUID
        while True:
            yield randomizer_pb2.RandomUUIDResponse(uuid=str(uuid.uuid4()))
            time.sleep(100/1000)  # 暂停1秒，避免过快发送

    def GetArray(self, request, context):
        # 创建一个640x512的随机浮点数数组
        array = [random.random() for _ in range(640)]
        print(array)
        return randomizer_pb2.ArrayResponse(row=array)

    def GetArrayStream(self, request, context):
        # 持续发送640x512的随机浮点数数组
        while True:
            array = [random.random() for _ in range(640)]
            yield  randomizer_pb2.ArrayResponse(row=array)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    randomizer_pb2_grpc.add_RandomizerServiceServicer_to_server(
        RandomizerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
