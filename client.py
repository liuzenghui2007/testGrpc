import grpc
import array_pb2
import array_pb2_grpc

def run_single_array():
    # 连接到 gRPC 服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = array_pb2_grpc.ArrayServiceStub(channel)
        response = stub.GetArray(array_pb2.Empty())
        # 打印获取的数组大小
        array = list(response.row)
        print(f"Received array of size: {len(array)}")
        print("First 10 elements:", array[:10])

def run_array_stream():
    # 连接到 gRPC 服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = array_pb2_grpc.ArrayServiceStub(channel)
        responses = stub.GetArrayStream(array_pb2.Empty())
        # 逐个接收流中的数组
        for idx, response in enumerate(responses):
            array = list(response.row)
            print(f"Received stream array {idx + 1}, size: {len(array)}")
            print("First 10 elements:", array[:10])

if __name__ == '__main__':
    print("Fetching a single array:")
    run_single_array()
    
    print("\nFetching array stream:")
    run_array_stream()
