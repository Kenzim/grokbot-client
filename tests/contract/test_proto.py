"""Contract: generated pb2 imports and proto sources exist."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_generated_modules_import():
    from grokbot._proto.aiserver.v1 import DashboardService_pb2, GrokBotService_pb2, types_pb2

    svc = DashboardService_pb2.DESCRIPTOR.services_by_name["DashboardService"]
    assert "GetMe" in svc.methods_by_name
    assert (
        "WatchGrokBotTranscripts"
        in GrokBotService_pb2.DESCRIPTOR.services_by_name["GrokBotService"].methods_by_name
    )
    assert types_pb2.GetMeRequest.DESCRIPTOR.full_name == "aiserver.v1.GetMeRequest"


def test_proto_sources_present():
    assert (ROOT / "proto/aiserver/v1/types.proto").is_file()
    assert (ROOT / "proto/aiserver/v1/GrokBotService.proto").is_file()
    assert (ROOT / "proto/agent/v1/types.proto").is_file()
