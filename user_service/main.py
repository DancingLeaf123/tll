import grpc
from services.user import UserServicer
from services.interceptors import UserInterceptor
from protos import user_pb2_grpc
import asyncio


async def main():
    server = grpc.aio.server(interceptors=[UserInterceptor()])
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:5001')
    await server.start()
    print("gRPC server is running on port 5001...")
    await server.wait_for_termination()
    
if __name__ == '__main__':
    asyncio.run(main())