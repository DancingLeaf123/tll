import grpc
from protos import user_pb2, user_pb2_grpc

def test_create_user(stub):
    try:
        request = user_pb2.CreateUserRequest()
        request.mobile = '12345678902'
        response = stub.CreateUser(request)
        print(response)
    except grpc.RpcError as e:
        print(e.code())
        print(e.details())    
        
def test_get_user_by_id(stub):
    request = user_pb2.IdRequest()
    request.id = 2123582071203954688
    response = stub.GetUserById(request)
    print(response)
    
def test_get_user_by_mobile(stub):
    request = user_pb2.MobileRequest()
    request.mobile = '13510565919'
    response = stub.GetUserByMobile(request)
    print(response)

def main():
    with grpc.insecure_channel('127.0.0.1:5001') as channel:
        stub = user_pb2_grpc.UserStub(channel)
        # test_create_user(stub)
        test_get_user_by_mobile(stub)
        

if __name__ == '__main__':
    main()