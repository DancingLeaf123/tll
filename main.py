import grpc
from services.user import UserService
from protos import user_pb2_grpc
import asyncio


async def main():
    server = grpc.aio.server()
    user_pb2_grpc.add_UserServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:5001')
    await server.start()
    print("gRPC server is running on port 5001...")
    await server.wait_for_termination()
    
if __name__ == '__main__':
    asyncio.run(main())