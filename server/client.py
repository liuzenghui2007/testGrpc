import grpc

# 这里从server和proto导入都可以？
from proto import randomizer_pb2
from proto import randomizer_pb2_grpc

def run():
    # 连接到服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = randomizer_pb2_grpc.RandomizerServiceStub(channel)
        
        # 调用一元接口
        response = stub.GetRandomString(randomizer_pb2.Empty())
        print("GetRandomString response:", response.value)
        
        # 调用流接口
        try:
            for response in stub.GetRandomUUIDStream(randomizer_pb2.Empty()):
                print("GetRandomUUIDStream response:", response.uuid)
        except grpc._channel._Rendezvous as err:
            print(err)

if __name__ == '__main__':
    run()