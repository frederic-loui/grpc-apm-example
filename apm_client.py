#!/usr/bin/python3

import grpc
import time

import apm_pb2
import apm_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = apm_pb2_grpc.APMStub(channel)

NREN='RENATER'
organization = apm_pb2.Text(str_text=NREN)
response = stub.GetAPMFromNRENName(organization)
print("Request from GRPC client ---> [%s]"
        % (NREN))
print("Answer from GRPC server ---> [%s]"
        % (response.str_text))

time.sleep(2)

NREN='KIFU'
organization = apm_pb2.Text(str_text=NREN)
response = stub.GetAPMFromNRENName(organization)
print("Request from GRPC client ---> [%s]"
        % (NREN))
print("Answer from GRPC server ---> [%s]"
        % (response.str_text))

time.sleep(2)

NREN='DFN'
organization = apm_pb2.Text(str_text=NREN)
response = stub.GetAPMFromNRENName(organization)
print("Request from GRPC client ---> [%s]"
        % (NREN))
print("Answer from GRPC server ---> [%s]"
        % (response.str_text))

