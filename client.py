import grpc
import data_pb2
import data_pb2_grpc

def run():
    # Connect to the server
    channel = grpc.insecure_channel('localhost:50051')
    stub = data_pb2_grpc.RandomizerServiceStub(channel)

    # Test GetRandomArray
    print("Testing GetRandomArray...")
    try:
        response = stub.GetRandomArray(data_pb2.Empty())
        for i, float_array in enumerate(response.data):
            print(f"Row {i}:", float_array.items)
    except grpc.RpcError as e:
        print(f"GetRandomArray RPC failed: {e}")

    # Test GetRandomArrayStream
    print("Testing GetRandomArrayStream...")
    try:
        for response in stub.GetRandomArrayStream(data_pb2.Empty()):
            for i, float_array in enumerate(response.data):
                print(f"Stream Row {i}:", float_array.items)
    except grpc.RpcError as e:
        print(f"GetRandomArrayStream RPC failed: {e}")

if __name__ == '__main__':
    run()
