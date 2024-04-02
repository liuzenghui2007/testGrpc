import grpc
import randomizer_pb2
import randomizer_pb2_grpc
import asyncio
import uuid
from concurrent import futures


class RandomizerService(randomizer_pb2_grpc.RandomizerServiceServicer):

    async def GetRandomString(self, request, context):
        return randomizer_pb2.RandomStringResponse(value="RandomString_" + str(uuid.uuid4()))

    async def GetRandomUUIDStream(self, request, context):
        while True:
            yield randomizer_pb2.RandomUUIDResponse(uuid=str(uuid.uuid4()))
            await asyncio.sleep(0.1)  # 使用异步sleep


async def serve():
    server = grpc.aio.server()
    randomizer_pb2_grpc.add_RandomizerServiceServicer_to_server(
        RandomizerService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())
