import grpc
from concurrent import futures
import numpy as np
import time

import array_pb2
import array_pb2_grpc

# 实现ArrayService服务
class ArrayService(array_pb2_grpc.ArrayServiceServicer):
    def GetArray(self, request, context):
        array = np.random.rand(512, 640).astype(np.float32)  # 生成随机数组
        response = array_pb2.ArrayResponse()
        for row in array:
            response.row.extend(row)  # 每一行添加到response中
        return response

    def GetArrayStream(self, request, context):
        for _ in range(5):  # 示例：生成5个随机数组流
            array = np.random.rand(512, 640).astype(np.float32)
            response = array_pb2.ArrayResponse()
            for row in array:
                response.row.extend(row)
            yield response
            time.sleep(1)  # 模拟延迟

# 启动 gRPC 服务器
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    array_pb2_grpc.add_ArrayServiceServicer_to_server(ArrayService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
