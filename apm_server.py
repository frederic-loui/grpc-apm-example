#!/usr/bin/python3 

import grpc
from concurrent import futures
import time

import apm_pb2
import apm_pb2_grpc

import apm

class APMServicer(apm_pb2_grpc.APMServicer):

    def GetAPMFromNRENName(self, request, context):
        print('Receiving from GRPC client %s for NREN: %s'
                % (context.peer(),request.str_text))
        response = apm_pb2.Text()
        response.str_text = apm.get_apm_name(request.str_text)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

apm_pb2_grpc.add_APMServicer_to_server(
        APMServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
