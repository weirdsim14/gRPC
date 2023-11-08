from concurrent import futures
import grpc
import example_pb2
import example_pb2_grpc

# The service definition.
class GreeterServicer(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return example_pb2.HelloReply(message='Hello, %s!' % request.name)

# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
example_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

# Listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
