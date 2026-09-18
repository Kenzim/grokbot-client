from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomModeSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOM_MODE_SOURCE_UNSPECIFIED: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_AGENT_SKILL: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_PLUGIN_SKILL: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_REPO_SKILL: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_MANAGED_SKILL: _ClassVar[CustomModeSource]

class TodoStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TODO_STATUS_UNSPECIFIED: _ClassVar[TodoStatus]
    TODO_STATUS_PENDING: _ClassVar[TodoStatus]
    TODO_STATUS_IN_PROGRESS: _ClassVar[TodoStatus]
    TODO_STATUS_COMPLETED: _ClassVar[TodoStatus]
    TODO_STATUS_CANCELLED: _ClassVar[TodoStatus]
CUSTOM_MODE_SOURCE_UNSPECIFIED: CustomModeSource
CUSTOM_MODE_SOURCE_AGENT_SKILL: CustomModeSource
CUSTOM_MODE_SOURCE_PLUGIN_SKILL: CustomModeSource
CUSTOM_MODE_SOURCE_REPO_SKILL: CustomModeSource
CUSTOM_MODE_SOURCE_MANAGED_SKILL: CustomModeSource
TODO_STATUS_UNSPECIFIED: TodoStatus
TODO_STATUS_PENDING: TodoStatus
TODO_STATUS_IN_PROGRESS: TodoStatus
TODO_STATUS_COMPLETED: TodoStatus
TODO_STATUS_CANCELLED: TodoStatus

class CustomModeDescriptor(_message.Message):
    __slots__ = ("id", "label", "description", "icon", "color", "source", "source_path", "source_hash", "managed_skill_id", "plugin_id", "plugin_snapshot_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    MANAGED_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_SNAPSHOT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    description: str
    icon: str
    color: str
    source: CustomModeSource
    source_path: str
    source_hash: str
    managed_skill_id: str
    plugin_id: str
    plugin_snapshot_token: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., color: _Optional[str] = ..., source: _Optional[_Union[CustomModeSource, str]] = ..., source_path: _Optional[str] = ..., source_hash: _Optional[str] = ..., managed_skill_id: _Optional[str] = ..., plugin_id: _Optional[str] = ..., plugin_snapshot_token: _Optional[str] = ...) -> None: ...

class McpApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class McpError(_message.Message):
    __slots__ = ("error", "needs_auth")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NEEDS_AUTH_FIELD_NUMBER: _ClassVar[int]
    error: str
    needs_auth: bool
    def __init__(self, error: _Optional[str] = ..., needs_auth: bool = ...) -> None: ...

class McpImageContent(_message.Message):
    __slots__ = ("data", "mime_type")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    mime_type: str
    def __init__(self, data: _Optional[bytes] = ..., mime_type: _Optional[str] = ...) -> None: ...

class McpPermissionDenied(_message.Message):
    __slots__ = ("error", "is_readonly")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    error: str
    is_readonly: bool
    def __init__(self, error: _Optional[str] = ..., is_readonly: bool = ...) -> None: ...

class McpRejected(_message.Message):
    __slots__ = ("reason", "is_readonly")
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    reason: str
    is_readonly: bool
    def __init__(self, reason: _Optional[str] = ..., is_readonly: bool = ...) -> None: ...

class McpResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "permission_denied", "tool_not_found", "server_not_found", "approved")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    TOOL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    SERVER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    success: McpSuccess
    error: McpError
    rejected: McpRejected
    permission_denied: McpPermissionDenied
    tool_not_found: McpToolNotFound
    server_not_found: McpServerNotFound
    approved: McpApproved
    def __init__(self, success: _Optional[_Union[McpSuccess, _Mapping]] = ..., error: _Optional[_Union[McpError, _Mapping]] = ..., rejected: _Optional[_Union[McpRejected, _Mapping]] = ..., permission_denied: _Optional[_Union[McpPermissionDenied, _Mapping]] = ..., tool_not_found: _Optional[_Union[McpToolNotFound, _Mapping]] = ..., server_not_found: _Optional[_Union[McpServerNotFound, _Mapping]] = ..., approved: _Optional[_Union[McpApproved, _Mapping]] = ...) -> None: ...

class McpServerNotFound(_message.Message):
    __slots__ = ("name", "available_servers")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SERVERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    available_servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., available_servers: _Optional[_Iterable[str]] = ...) -> None: ...

class McpSuccess(_message.Message):
    __slots__ = ("content", "is_error", "structured_content")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[McpToolResultContentItem]
    is_error: bool
    structured_content: _struct_pb2.Struct
    def __init__(self, content: _Optional[_Iterable[_Union[McpToolResultContentItem, _Mapping]]] = ..., is_error: bool = ..., structured_content: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class McpTextContent(_message.Message):
    __slots__ = ("text", "output_location")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    text: str
    output_location: OutputLocation
    def __init__(self, text: _Optional[str] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ...) -> None: ...

class McpToolDefinition(_message.Message):
    __slots__ = ("name", "description", "input_schema", "provider_identifier", "tool_name", "input_schema_json", "output_schema_json", "annotations_json")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_JSON_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    input_schema: _struct_pb2.Value
    provider_identifier: str
    tool_name: str
    input_schema_json: str
    output_schema_json: str
    annotations_json: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., provider_identifier: _Optional[str] = ..., tool_name: _Optional[str] = ..., input_schema_json: _Optional[str] = ..., output_schema_json: _Optional[str] = ..., annotations_json: _Optional[str] = ...) -> None: ...

class McpToolNotFound(_message.Message):
    __slots__ = ("name", "available_tools")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TOOLS_FIELD_NUMBER: _ClassVar[int]
    name: str
    available_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., available_tools: _Optional[_Iterable[str]] = ...) -> None: ...

class McpToolResultContentItem(_message.Message):
    __slots__ = ("text", "image")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    text: McpTextContent
    image: McpImageContent
    def __init__(self, text: _Optional[_Union[McpTextContent, _Mapping]] = ..., image: _Optional[_Union[McpImageContent, _Mapping]] = ...) -> None: ...

class OutputLocation(_message.Message):
    __slots__ = ("file_path", "size_bytes", "line_count")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    size_bytes: int
    line_count: int
    def __init__(self, file_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., line_count: _Optional[int] = ...) -> None: ...

class RequestedModel(_message.Message):
    __slots__ = ()
    class ModelParameterValue(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: str
        value: str
        def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class TodoItem(_message.Message):
    __slots__ = ("id", "content", "status", "created_at", "updated_at", "dependencies")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    status: TodoStatus
    created_at: int
    updated_at: int
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[TodoStatus, str]] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., dependencies: _Optional[_Iterable[str]] = ...) -> None: ...
