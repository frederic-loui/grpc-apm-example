# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import apm_pb2 as apm__pb2


class APMStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPMFromNRENName = channel.unary_unary(
                '/APM/GetAPMFromNRENName',
                request_serializer=apm__pb2.Text.SerializeToString,
                response_deserializer=apm__pb2.Text.FromString,
                )


class APMServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAPMFromNRENName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APMServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPMFromNRENName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPMFromNRENName,
                    request_deserializer=apm__pb2.Text.FromString,
                    response_serializer=apm__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'APM', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class APM(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAPMFromNRENName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/APM/GetAPMFromNRENName',
            apm__pb2.Text.SerializeToString,
            apm__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
