"""Protobuf service descriptors + types import used by the high-level APIs."""

from grokbot._proto.aiserver.v1 import DashboardService_pb2 as dash_pb2
from grokbot._proto.aiserver.v1 import GrokBotService_pb2 as gb_pb2
from grokbot._proto.aiserver.v1 import types_pb2 as t

GB = gb_pb2.DESCRIPTOR.services_by_name["GrokBotService"]
DASH = dash_pb2.DESCRIPTOR.services_by_name["DashboardService"]

__all__ = ["GB", "DASH", "t"]
