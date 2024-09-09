import grpc
import data_pb2
import data_pb2_grpc

def run():
    # 连接到服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.RandomizerServiceStub(channel)
        
        # 调用 GetRandomArray 方法
        print("Requesting a single random array...")
        response = stub.GetRandomArray(data_pb2.Empty())
        print("Received array with dimensions:", len(response.data), "x", len(response.data[0].items))

        # 调用 GetRandomArrayStream 方法
        print("\nStreaming random arrays...")
        try:
            for response in stub.GetRandomArrayStream(data_pb2.Empty()):
                print("Streamed array with dimensions:", len(response.data), "x", len(response.data[0].items))
                break  # 只打印第一个数组，然后退出循环
        except grpc.RpcError as e:
            print(f"An error occurred: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()