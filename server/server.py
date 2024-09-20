import grpc
from proto import randomizer_pb2
from proto import randomizer_pb2_grpc
import time
import uuid
from concurrent import futures
import random

class DataGenerator:
    def __init__(self):
        self.start_time = time.time()

    def seconds_since_start(self):
        return time.time() - self.start_time

    @staticmethod
    def generate_random_string():
        return "RandomString_" + str(uuid.uuid4())

    @staticmethod
    def generate_random_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def generate_random_array(size):
        return [random.random() for _ in range(size)]

    @staticmethod
    def generate_random_2d_array(rows, cols):
        return [randomizer_pb2.NumberArray(values=[random.random() for _ in range(cols)]) for _ in range(rows)]

class RandomizerService(randomizer_pb2_grpc.RandomizerServiceServicer):
    def __init__(self):
        self.data_generator = DataGenerator()

    def GetRandomString(self, request, context):
        # 返回一个随机字符串
        return randomizer_pb2.RandomStringResponse(value=self.data_generator.generate_random_string())

    def GetRandomUUIDStream(self, request, context):
        # 持续返回随机UUID
        while True:
            yield randomizer_pb2.RandomUUIDResponse(uuid=self.data_generator.generate_random_uuid())
            time.sleep(1)  # 暂停1秒，避免过快发送

    def GetArray(self, request, context):
        # 创建一个640x1的随机浮点数数组
        array = self.data_generator.generate_random_array(640)
        return randomizer_pb2.ArrayResponse(row=array)

    def GetArrayStream(self, request, context):
        # 持续发送640的随机浮点数数组
        while True:
            array = self.data_generator.generate_random_array(640)
            yield randomizer_pb2.ArrayResponse(row=array)
            time.sleep(1)  # 暂停1秒，避免过快发送

    def Get2DArray(self, request, context):
        # 创建一个640x512的随机浮点数数组
        array = self.data_generator.generate_random_2d_array(640, 512)
        return randomizer_pb2.NumberArray2D(matrix=array, seconds_since_start=self.data_generator.seconds_since_start())

    def Get2DArrayStream(self, request, context):
        # 持续发送640x512的随机浮点数数组
        while True:
            array = self.data_generator.generate_random_2d_array(640, 512)
            yield randomizer_pb2.NumberArray2D(matrix=array, seconds_since_start=self.data_generator.seconds_since_start())
            time.sleep(1)  # 暂停1秒，避免过快发送

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    randomizer_pb2_grpc.add_RandomizerServiceServicer_to_server(
        RandomizerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
