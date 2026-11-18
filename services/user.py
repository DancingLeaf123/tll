from models import AsyncSessionFactory, User
import grpc
import user_pb2
import user_pb2_grpc
import sqlalchemy.exc

class UserService(user_pb2_grpc.UserServicer):
    async def GetUser(self, request: user_pb2.CreateUserRequest, context):
        mobile = request.mobile
        async with AsyncSessionFactory() as session:
            try:
                async with session.begin():
                    user = User(mobile=mobile)
                    session.add(user)
                    # sqlalchemy_serializer
                    response = user_pb2.UserResponse(user=user.to_dict())
                    return response
            except sqlalchemy.exc.IntegrityError:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details(f"该手机号已经存在！")
