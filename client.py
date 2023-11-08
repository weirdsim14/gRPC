import grpc
import example_pb2
import example_pb2_grpc

# Open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# Create a stub (client)
stub = example_pb2_grpc.GreeterStub(channel)

# Create a valid request message
hello_request = example_pb2.HelloRequest(name='World')

# Make the call
response = stub.SayHello(hello_request)

print(response.message)
