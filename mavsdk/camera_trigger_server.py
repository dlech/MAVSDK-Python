# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import camera_trigger_server_pb2, camera_trigger_server_pb2_grpc
from enum import Enum




class CameraTriggerServer(AsyncBase):
    """
     Provides handling of camera trigger commands.

     Generated by dcsdkgen - MAVSDK CameraTriggerServer API
    """

    # Plugin name
    name = "CameraTriggerServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = camera_trigger_server_pb2_grpc.CameraTriggerServerServiceStub(channel)

    

    async def capture(self):
        """
         Subscribe to single-capture MAV_CMD_IMAGE_START_CAPTURE commands

         Yields
         -------
         sequence_number : uint32_t
             
         
        """

        request = camera_trigger_server_pb2.SubscribeCaptureRequest()
        capture_stream = self._stub.SubscribeCapture(request)

        try:
            async for response in capture_stream:
                

            
                yield response.sequence_number
        finally:
            capture_stream.cancel()