import grpc
from concurrent import futures
import numpy as np
import data_pb2
import data_pb2_grpc

# Import the generate_signal function from gen_dna.py
from gen_dna import generate_signal, SAMPLE_RATE, DURATION

class RandomizerService(data_pb2_grpc.RandomizerServiceServicer):
    def GetRandomArray(self, request, context):
        # Generate a 640x512 array using generate_signal
        array_response = data_pb2.ArrayResponse()
        for _ in range(640):
            float_array = array_response.data.add()
            signal = generate_signal(SAMPLE_RATE * DURATION)
            float_array.items.extend(signal[:512])  # Assuming you want the first 512 samples
        return array_response

    def GetRandomArrayStream(self, request, context):
        while True:
            array_response = data_pb2.ArrayResponse()
            for _ in range(640):
                float_array = array_response.data.add()
                signal = generate_signal(SAMPLE_RATE * DURATION)
                float_array.items.extend(signal[:512])  # Assuming you want the first 512 samples
            yield array_response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_RandomizerServiceServicer_to_server(RandomizerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
