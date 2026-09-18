from grokbot._proto.agent.v1 import types_pb2 as _types_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllowlistConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALLOWLIST_CONFIG_UNSPECIFIED: _ClassVar[AllowlistConfig]
    ALLOWLIST_CONFIG_ALLOWLIST: _ClassVar[AllowlistConfig]
    ALLOWLIST_CONFIG_BLOCKLIST: _ClassVar[AllowlistConfig]

class AutoCreatePrMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTO_CREATE_PR_MODE_UNSPECIFIED: _ClassVar[AutoCreatePrMode]
    AUTO_CREATE_PR_MODE_ALWAYS: _ClassVar[AutoCreatePrMode]
    AUTO_CREATE_PR_MODE_SINGLE: _ClassVar[AutoCreatePrMode]
    AUTO_CREATE_PR_MODE_NEVER: _ClassVar[AutoCreatePrMode]

class AutoCreatePrSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTO_CREATE_PR_SETTING_UNSPECIFIED: _ClassVar[AutoCreatePrSetting]
    AUTO_CREATE_PR_SETTING_ALWAYS: _ClassVar[AutoCreatePrSetting]
    AUTO_CREATE_PR_SETTING_SINGLE: _ClassVar[AutoCreatePrSetting]
    AUTO_CREATE_PR_SETTING_NEVER: _ClassVar[AutoCreatePrSetting]

class AutomationDefaultVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTOMATION_DEFAULT_VISIBILITY_UNSPECIFIED: _ClassVar[AutomationDefaultVisibility]
    AUTOMATION_DEFAULT_VISIBILITY_VISIBLE: _ClassVar[AutomationDefaultVisibility]
    AUTOMATION_DEFAULT_VISIBILITY_EDITABLE: _ClassVar[AutomationDefaultVisibility]
    AUTOMATION_DEFAULT_VISIBILITY_PRIVATE: _ClassVar[AutomationDefaultVisibility]

class AvailableModelsScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABLE_MODELS_SCOPE_UNSPECIFIED: _ClassVar[AvailableModelsScope]
    AVAILABLE_MODELS_SCOPE_USER_AVAILABLE: _ClassVar[AvailableModelsScope]
    AVAILABLE_MODELS_SCOPE_AUTOMATIONS: _ClassVar[AvailableModelsScope]
    AVAILABLE_MODELS_SCOPE_ADMIN_SETTINGS_ALL_APPLICATION_MODELS: _ClassVar[AvailableModelsScope]

class BackgroundComposerQuickActionExecutionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_COMPOSER_QUICK_ACTION_EXECUTION_MODE_UNSPECIFIED: _ClassVar[BackgroundComposerQuickActionExecutionMode]
    BACKGROUND_COMPOSER_QUICK_ACTION_EXECUTION_MODE_SUBAGENT: _ClassVar[BackgroundComposerQuickActionExecutionMode]
    BACKGROUND_COMPOSER_QUICK_ACTION_EXECUTION_MODE_PARENT_AGENT: _ClassVar[BackgroundComposerQuickActionExecutionMode]

class BackgroundComposerQuickActionSubagentTemplateOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_UNSPECIFIED: _ClassVar[BackgroundComposerQuickActionSubagentTemplateOperation]
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_CREATE: _ClassVar[BackgroundComposerQuickActionSubagentTemplateOperation]
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_UPDATE: _ClassVar[BackgroundComposerQuickActionSubagentTemplateOperation]
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_DELETE: _ClassVar[BackgroundComposerQuickActionSubagentTemplateOperation]

class BackgroundComposerQuickActionSubagentTemplateScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_UNSPECIFIED: _ClassVar[BackgroundComposerQuickActionSubagentTemplateScope]
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_BUILTIN: _ClassVar[BackgroundComposerQuickActionSubagentTemplateScope]
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_USER: _ClassVar[BackgroundComposerQuickActionSubagentTemplateScope]
    BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_TEAM: _ClassVar[BackgroundComposerQuickActionSubagentTemplateScope]

class BulkTeamMemberSandBoxAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BULK_TEAM_MEMBER_SAND_BOX_ACTION_UNSPECIFIED: _ClassVar[BulkTeamMemberSandBoxAction]
    BULK_TEAM_MEMBER_SAND_BOX_ACTION_KILL: _ClassVar[BulkTeamMemberSandBoxAction]
    BULK_TEAM_MEMBER_SAND_BOX_ACTION_RECREATE: _ClassVar[BulkTeamMemberSandBoxAction]

class BulkTeamMemberSandBoxItemState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_UNSPECIFIED: _ClassVar[BulkTeamMemberSandBoxItemState]
    BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_QUEUED: _ClassVar[BulkTeamMemberSandBoxItemState]
    BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_RUNNING: _ClassVar[BulkTeamMemberSandBoxItemState]
    BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_SUCCEEDED: _ClassVar[BulkTeamMemberSandBoxItemState]
    BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_SKIPPED: _ClassVar[BulkTeamMemberSandBoxItemState]
    BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_FAILED: _ClassVar[BulkTeamMemberSandBoxItemState]

class BulkTeamMemberSandBoxOperationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_UNSPECIFIED: _ClassVar[BulkTeamMemberSandBoxOperationState]
    BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_RUNNING: _ClassVar[BulkTeamMemberSandBoxOperationState]
    BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_SUCCEEDED: _ClassVar[BulkTeamMemberSandBoxOperationState]
    BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_PARTIALLY_SUCCEEDED: _ClassVar[BulkTeamMemberSandBoxOperationState]
    BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_FAILED: _ClassVar[BulkTeamMemberSandBoxOperationState]

class CanvasVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANVAS_VISIBILITY_UNSPECIFIED: _ClassVar[CanvasVisibility]
    CANVAS_VISIBILITY_PRIVATE: _ClassVar[CanvasVisibility]
    CANVAS_VISIBILITY_TEAM_VIEW: _ClassVar[CanvasVisibility]

class ClientLogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_LOG_LEVEL_UNSPECIFIED: _ClassVar[ClientLogLevel]
    CLIENT_LOG_LEVEL_INFO: _ClassVar[ClientLogLevel]
    CLIENT_LOG_LEVEL_DEBUG: _ClassVar[ClientLogLevel]
    CLIENT_LOG_LEVEL_WARN: _ClassVar[ClientLogLevel]
    CLIENT_LOG_LEVEL_ERROR: _ClassVar[ClientLogLevel]

class ClientOS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_OS_UNSPECIFIED: _ClassVar[ClientOS]
    CLIENT_OS_WINDOWS: _ClassVar[ClientOS]
    CLIENT_OS_MACOS: _ClassVar[ClientOS]
    CLIENT_OS_LINUX: _ClassVar[ClientOS]
    CLIENT_OS_IOS: _ClassVar[ClientOS]
    CLIENT_OS_ANDROID: _ClassVar[ClientOS]

class CloudAgentEffortMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_AGENT_EFFORT_MODE_UNSPECIFIED: _ClassVar[CloudAgentEffortMode]
    CLOUD_AGENT_EFFORT_MODE_STANDARD: _ClassVar[CloudAgentEffortMode]
    CLOUD_AGENT_EFFORT_MODE_GRIND: _ClassVar[CloudAgentEffortMode]

class CloudAgentEgressProtectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_AGENT_EGRESS_PROTECTION_MODE_UNSPECIFIED: _ClassVar[CloudAgentEgressProtectionMode]
    CLOUD_AGENT_EGRESS_PROTECTION_MODE_ALLOW_ALL: _ClassVar[CloudAgentEgressProtectionMode]
    CLOUD_AGENT_EGRESS_PROTECTION_MODE_DEFAULT_WITH_NETWORK_SETTINGS: _ClassVar[CloudAgentEgressProtectionMode]
    CLOUD_AGENT_EGRESS_PROTECTION_MODE_NETWORK_SETTINGS_ONLY: _ClassVar[CloudAgentEgressProtectionMode]
    CLOUD_AGENT_EGRESS_PROTECTION_MODE_PARENT_PLUS_NETWORK_SETTINGS: _ClassVar[CloudAgentEgressProtectionMode]

class CredentialExpirationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_EXPIRATION_MODE_UNSPECIFIED: _ClassVar[CredentialExpirationMode]
    CREDENTIAL_EXPIRATION_MODE_DISABLED: _ClassVar[CredentialExpirationMode]
    CREDENTIAL_EXPIRATION_MODE_WARN: _ClassVar[CredentialExpirationMode]
    CREDENTIAL_EXPIRATION_MODE_ENFORCE: _ClassVar[CredentialExpirationMode]

class CredentialLifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[CredentialLifecycleState]
    CREDENTIAL_LIFECYCLE_STATE_ACTIVE: _ClassVar[CredentialLifecycleState]
    CREDENTIAL_LIFECYCLE_STATE_EXPIRING: _ClassVar[CredentialLifecycleState]
    CREDENTIAL_LIFECYCLE_STATE_GRACE: _ClassVar[CredentialLifecycleState]
    CREDENTIAL_LIFECYCLE_STATE_EXPIRED: _ClassVar[CredentialLifecycleState]
    CREDENTIAL_LIFECYCLE_STATE_PROVIDER_REJECTED: _ClassVar[CredentialLifecycleState]

class CredentialTargetRuleKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_TARGET_RULE_KIND_UNSPECIFIED: _ClassVar[CredentialTargetRuleKind]
    CREDENTIAL_TARGET_RULE_KIND_EXACT_HOST_PORT: _ClassVar[CredentialTargetRuleKind]
    CREDENTIAL_TARGET_RULE_KIND_REGISTRABLE_DOMAIN: _ClassVar[CredentialTargetRuleKind]

class EffectivePluginInstallMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFFECTIVE_PLUGIN_INSTALL_MODE_UNSPECIFIED: _ClassVar[EffectivePluginInstallMode]
    EFFECTIVE_PLUGIN_INSTALL_MODE_USER: _ClassVar[EffectivePluginInstallMode]
    EFFECTIVE_PLUGIN_INSTALL_MODE_TEAM_DEFAULT: _ClassVar[EffectivePluginInstallMode]
    EFFECTIVE_PLUGIN_INSTALL_MODE_TEAM_REQUIRED: _ClassVar[EffectivePluginInstallMode]

class FirstPartyPluginMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_PARTY_PLUGIN_MODE_UNSPECIFIED: _ClassVar[FirstPartyPluginMode]
    FIRST_PARTY_PLUGIN_MODE_ENABLE_ALL: _ClassVar[FirstPartyPluginMode]
    FIRST_PARTY_PLUGIN_MODE_ALLOWLIST: _ClassVar[FirstPartyPluginMode]

class GithubArtifactPostingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GITHUB_ARTIFACT_POSTING_MODE_UNSPECIFIED: _ClassVar[GithubArtifactPostingMode]
    GITHUB_ARTIFACT_POSTING_MODE_POST_ARTIFACT: _ClassVar[GithubArtifactPostingMode]
    GITHUB_ARTIFACT_POSTING_MODE_LINK_ONLY: _ClassVar[GithubArtifactPostingMode]

class GitMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GIT_MODE_UNSPECIFIED: _ClassVar[GitMode]
    GIT_MODE_USER_CONTROLLED: _ClassVar[GitMode]
    GIT_MODE_ALWAYS_DISABLED: _ClassVar[GitMode]

class GrokBotAgentHarnessKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_AGENT_HARNESS_KIND_UNSPECIFIED: _ClassVar[GrokBotAgentHarnessKind]
    GROK_BOT_AGENT_HARNESS_KIND_BOX: _ClassVar[GrokBotAgentHarnessKind]
    GROK_BOT_AGENT_HARNESS_KIND_TEMPORAL: _ClassVar[GrokBotAgentHarnessKind]

class GrokBotAgentKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_AGENT_KIND_UNSPECIFIED: _ClassVar[GrokBotAgentKind]
    GROK_BOT_AGENT_KIND_AGENT: _ClassVar[GrokBotAgentKind]
    GROK_BOT_AGENT_KIND_ROOM: _ClassVar[GrokBotAgentKind]

class GrokBotAgentMessageDelivery(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_AGENT_MESSAGE_DELIVERY_UNSPECIFIED: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_DELIVERED_TEMPORAL: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_DELIVERED_BOX: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_DUPLICATE: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_TARGET_NOT_FOUND: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_FORBIDDEN: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_BOX_UNREACHABLE: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_TEMPORAL_UNAVAILABLE: _ClassVar[GrokBotAgentMessageDelivery]
    GROK_BOT_AGENT_MESSAGE_DELIVERY_INVALID_TARGET: _ClassVar[GrokBotAgentMessageDelivery]

class GrokBotAgentSessionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_AGENT_SESSION_KIND_UNSPECIFIED: _ClassVar[GrokBotAgentSessionKind]
    GROK_BOT_AGENT_SESSION_KIND_MAIN: _ClassVar[GrokBotAgentSessionKind]
    GROK_BOT_AGENT_SESSION_KIND_SLACK_DM: _ClassVar[GrokBotAgentSessionKind]
    GROK_BOT_AGENT_SESSION_KIND_SLACK_THREAD: _ClassVar[GrokBotAgentSessionKind]
    GROK_BOT_AGENT_SESSION_KIND_DM: _ClassVar[GrokBotAgentSessionKind]
    GROK_BOT_AGENT_SESSION_KIND_GROUP: _ClassVar[GrokBotAgentSessionKind]

class GrokBotAgentVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_AGENT_VISIBILITY_UNSPECIFIED: _ClassVar[GrokBotAgentVisibility]
    GROK_BOT_AGENT_VISIBILITY_OWNER: _ClassVar[GrokBotAgentVisibility]
    GROK_BOT_AGENT_VISIBILITY_TEAM: _ClassVar[GrokBotAgentVisibility]

class GrokBotAutoReviewApprovalResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_UNSPECIFIED: _ClassVar[GrokBotAutoReviewApprovalResolution]
    GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_APPROVED: _ClassVar[GrokBotAutoReviewApprovalResolution]
    GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_DENIED: _ClassVar[GrokBotAutoReviewApprovalResolution]
    GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_ALWAYS: _ClassVar[GrokBotAutoReviewApprovalResolution]

class GrokBotBoxDiskPressureLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_BOX_DISK_PRESSURE_LEVEL_UNSPECIFIED: _ClassVar[GrokBotBoxDiskPressureLevel]
    GROK_BOT_BOX_DISK_PRESSURE_LEVEL_NONE: _ClassVar[GrokBotBoxDiskPressureLevel]
    GROK_BOT_BOX_DISK_PRESSURE_LEVEL_SOFT: _ClassVar[GrokBotBoxDiskPressureLevel]
    GROK_BOT_BOX_DISK_PRESSURE_LEVEL_HARD: _ClassVar[GrokBotBoxDiskPressureLevel]

class GrokBotBoxHandBackTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_BOX_HAND_BACK_TRIGGER_UNSPECIFIED: _ClassVar[GrokBotBoxHandBackTrigger]
    GROK_BOT_BOX_HAND_BACK_TRIGGER_BUTTON: _ClassVar[GrokBotBoxHandBackTrigger]
    GROK_BOT_BOX_HAND_BACK_TRIGGER_VIEWER_CLOSED: _ClassVar[GrokBotBoxHandBackTrigger]
    GROK_BOT_BOX_HAND_BACK_TRIGGER_DISMISSED: _ClassVar[GrokBotBoxHandBackTrigger]

class GrokBotBoxHarnessMigrationPassState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_UNSPECIFIED: _ClassVar[GrokBotBoxHarnessMigrationPassState]
    GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_DISABLED: _ClassVar[GrokBotBoxHarnessMigrationPassState]
    GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_DONE: _ClassVar[GrokBotBoxHarnessMigrationPassState]
    GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_PENDING: _ClassVar[GrokBotBoxHarnessMigrationPassState]

class GrokBotClientSurface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_CLIENT_SURFACE_UNSPECIFIED: _ClassVar[GrokBotClientSurface]
    GROK_BOT_CLIENT_SURFACE_DESKTOP: _ClassVar[GrokBotClientSurface]
    GROK_BOT_CLIENT_SURFACE_MOBILE: _ClassVar[GrokBotClientSurface]

class GrokBotConnectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_CONNECTOR_TYPE_UNSPECIFIED: _ClassVar[GrokBotConnectorType]
    GROK_BOT_CONNECTOR_TYPE_USER: _ClassVar[GrokBotConnectorType]
    GROK_BOT_CONNECTOR_TYPE_TEAM: _ClassVar[GrokBotConnectorType]

class GrokBotCredentialRequestResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_CREDENTIAL_REQUEST_RESOLUTION_UNSPECIFIED: _ClassVar[GrokBotCredentialRequestResolution]
    GROK_BOT_CREDENTIAL_REQUEST_RESOLUTION_APPROVED: _ClassVar[GrokBotCredentialRequestResolution]
    GROK_BOT_CREDENTIAL_REQUEST_RESOLUTION_DENIED: _ClassVar[GrokBotCredentialRequestResolution]

class GrokBotFeedbackAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_FEEDBACK_ACTION_UNSPECIFIED: _ClassVar[GrokBotFeedbackAction]
    GROK_BOT_FEEDBACK_ACTION_UP: _ClassVar[GrokBotFeedbackAction]
    GROK_BOT_FEEDBACK_ACTION_DOWN: _ClassVar[GrokBotFeedbackAction]
    GROK_BOT_FEEDBACK_ACTION_SUBMIT: _ClassVar[GrokBotFeedbackAction]
    GROK_BOT_FEEDBACK_ACTION_REVERT: _ClassVar[GrokBotFeedbackAction]

class GrokBotFirstPartyTemplate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_FIRST_PARTY_TEMPLATE_UNSPECIFIED: _ClassVar[GrokBotFirstPartyTemplate]
    GROK_BOT_FIRST_PARTY_TEMPLATE_SWE: _ClassVar[GrokBotFirstPartyTemplate]

class GrokBotLocalToolPermissionCardResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_UNSPECIFIED: _ClassVar[GrokBotLocalToolPermissionCardResolution]
    GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_ALLOW_ONCE: _ClassVar[GrokBotLocalToolPermissionCardResolution]
    GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_DENY: _ClassVar[GrokBotLocalToolPermissionCardResolution]
    GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_ALWAYS: _ClassVar[GrokBotLocalToolPermissionCardResolution]
    GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_NEVER: _ClassVar[GrokBotLocalToolPermissionCardResolution]

class GrokBotMarketplaceImageKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_MARKETPLACE_IMAGE_KIND_UNSPECIFIED: _ClassVar[GrokBotMarketplaceImageKind]
    GROK_BOT_MARKETPLACE_IMAGE_KIND_BOT: _ClassVar[GrokBotMarketplaceImageKind]
    GROK_BOT_MARKETPLACE_IMAGE_KIND_CREATOR: _ClassVar[GrokBotMarketplaceImageKind]

class GrokBotMarketplaceListingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_MARKETPLACE_LISTING_STATUS_UNSPECIFIED: _ClassVar[GrokBotMarketplaceListingStatus]
    GROK_BOT_MARKETPLACE_LISTING_STATUS_PENDING_REVIEW: _ClassVar[GrokBotMarketplaceListingStatus]
    GROK_BOT_MARKETPLACE_LISTING_STATUS_LISTED: _ClassVar[GrokBotMarketplaceListingStatus]
    GROK_BOT_MARKETPLACE_LISTING_STATUS_DELISTED: _ClassVar[GrokBotMarketplaceListingStatus]

class GrokBotRoomMemberTurnDispatch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_UNSPECIFIED: _ClassVar[GrokBotRoomMemberTurnDispatch]
    GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_ACCEPTED: _ClassVar[GrokBotRoomMemberTurnDispatch]
    GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_DUPLICATE: _ClassVar[GrokBotRoomMemberTurnDispatch]
    GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_NOT_TEMPORAL: _ClassVar[GrokBotRoomMemberTurnDispatch]
    GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_TARGET_NOT_FOUND: _ClassVar[GrokBotRoomMemberTurnDispatch]
    GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_TEMPORAL_UNAVAILABLE: _ClassVar[GrokBotRoomMemberTurnDispatch]

class GrokBotRoomMemberTurnOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotRoomMemberTurnOutcome]
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_SENT: _ClassVar[GrokBotRoomMemberTurnOutcome]
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_PASS: _ClassVar[GrokBotRoomMemberTurnOutcome]
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_SKIPPED: _ClassVar[GrokBotRoomMemberTurnOutcome]
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_TIMEOUT: _ClassVar[GrokBotRoomMemberTurnOutcome]
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_CANCELLED: _ClassVar[GrokBotRoomMemberTurnOutcome]
    GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_ERROR: _ClassVar[GrokBotRoomMemberTurnOutcome]

class GrokBotRoomMemberTurnResultIntake(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_UNSPECIFIED: _ClassVar[GrokBotRoomMemberTurnResultIntake]
    GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_ACCEPTED: _ClassVar[GrokBotRoomMemberTurnResultIntake]
    GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_UNKNOWN_NONCE: _ClassVar[GrokBotRoomMemberTurnResultIntake]
    GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_HOST_UNAVAILABLE: _ClassVar[GrokBotRoomMemberTurnResultIntake]

class GrokBotRosterChangeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_ROSTER_CHANGE_KIND_UNSPECIFIED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_AGENT_CREATED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_AGENT_UPDATED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_AGENT_DELETED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_AGENT_VISIBILITY_CHANGED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_ROOM_MEMBERS_CHANGED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_SIDEBAR_VISIBILITY_CHANGED: _ClassVar[GrokBotRosterChangeKind]
    GROK_BOT_ROSTER_CHANGE_KIND_USER_SETTINGS_CHANGED: _ClassVar[GrokBotRosterChangeKind]

class GrokBotSendStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SEND_STATUS_UNSPECIFIED: _ClassVar[GrokBotSendStatus]
    GROK_BOT_SEND_STATUS_NOT_FOUND: _ClassVar[GrokBotSendStatus]
    GROK_BOT_SEND_STATUS_ACCEPTED: _ClassVar[GrokBotSendStatus]
    GROK_BOT_SEND_STATUS_REJECTED: _ClassVar[GrokBotSendStatus]
    GROK_BOT_SEND_STATUS_PENDING: _ClassVar[GrokBotSendStatus]
    GROK_BOT_SEND_STATUS_UNKNOWN_DURABILITY: _ClassVar[GrokBotSendStatus]

class GrokBotSessionBoxCredentialState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_UNSPECIFIED: _ClassVar[GrokBotSessionBoxCredentialState]
    GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_ABSENT: _ClassVar[GrokBotSessionBoxCredentialState]
    GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_PRESENT: _ClassVar[GrokBotSessionBoxCredentialState]
    GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_REVOKED: _ClassVar[GrokBotSessionBoxCredentialState]

class GrokBotSessionBoxPodState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SESSION_BOX_POD_STATE_UNSPECIFIED: _ClassVar[GrokBotSessionBoxPodState]
    GROK_BOT_SESSION_BOX_POD_STATE_ABSENT: _ClassVar[GrokBotSessionBoxPodState]
    GROK_BOT_SESSION_BOX_POD_STATE_REACHABLE: _ClassVar[GrokBotSessionBoxPodState]
    GROK_BOT_SESSION_BOX_POD_STATE_HIBERNATED: _ClassVar[GrokBotSessionBoxPodState]
    GROK_BOT_SESSION_BOX_POD_STATE_STARTING: _ClassVar[GrokBotSessionBoxPodState]
    GROK_BOT_SESSION_BOX_POD_STATE_UNKNOWN: _ClassVar[GrokBotSessionBoxPodState]

class GrokBotSlackConnectOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SLACK_CONNECT_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotSlackConnectOutcome]
    GROK_BOT_SLACK_CONNECT_OUTCOME_STARTED: _ClassVar[GrokBotSlackConnectOutcome]
    GROK_BOT_SLACK_CONNECT_OUTCOME_UNSUPPORTED_HARNESS: _ClassVar[GrokBotSlackConnectOutcome]

class GrokBotSlackInstallOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SLACK_INSTALL_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_INSTALLED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_PENDING_ADMIN_APPROVAL: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_NOT_CONNECTED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_WORKSPACE_REQUIRED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_MANAGER_REAUTH_REQUIRED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_INSUFFICIENT_SCOPES: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_INSTALL_CONFLICT: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_RATELIMITED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_SLACK_REJECTED: _ClassVar[GrokBotSlackInstallOutcome]
    GROK_BOT_SLACK_INSTALL_OUTCOME_UNSUPPORTED_HARNESS: _ClassVar[GrokBotSlackInstallOutcome]

class GrokBotSlackInstallStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SLACK_INSTALL_STATUS_UNSPECIFIED: _ClassVar[GrokBotSlackInstallStatus]
    GROK_BOT_SLACK_INSTALL_STATUS_NOT_CONNECTED: _ClassVar[GrokBotSlackInstallStatus]
    GROK_BOT_SLACK_INSTALL_STATUS_APP_CREATED: _ClassVar[GrokBotSlackInstallStatus]
    GROK_BOT_SLACK_INSTALL_STATUS_CONNECTED: _ClassVar[GrokBotSlackInstallStatus]
    GROK_BOT_SLACK_INSTALL_STATUS_UNSUPPORTED_HARNESS: _ClassVar[GrokBotSlackInstallStatus]

class GrokBotSlackReinstallOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SLACK_REINSTALL_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_UPDATED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_UP_TO_DATE: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_RECREATE_REQUIRED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_PENDING_ADMIN_APPROVAL: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_NOT_CONNECTED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_MANAGER_REAUTH_REQUIRED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_INSUFFICIENT_SCOPES: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_RATELIMITED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_SLACK_REJECTED: _ClassVar[GrokBotSlackReinstallOutcome]
    GROK_BOT_SLACK_REINSTALL_OUTCOME_UNSUPPORTED_HARNESS: _ClassVar[GrokBotSlackReinstallOutcome]

class GrokBotSlackUninstallOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotSlackUninstallOutcome]
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_REMOVED: _ClassVar[GrokBotSlackUninstallOutcome]
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_NOT_CONNECTED: _ClassVar[GrokBotSlackUninstallOutcome]
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_MANAGER_REAUTH_REQUIRED: _ClassVar[GrokBotSlackUninstallOutcome]
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_RATELIMITED: _ClassVar[GrokBotSlackUninstallOutcome]
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_SLACK_REJECTED: _ClassVar[GrokBotSlackUninstallOutcome]
    GROK_BOT_SLACK_UNINSTALL_OUTCOME_UNSUPPORTED_HARNESS: _ClassVar[GrokBotSlackUninstallOutcome]

class GrokBotStripeLinkPaymentMethodKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_STRIPE_LINK_PAYMENT_METHOD_KIND_UNSPECIFIED: _ClassVar[GrokBotStripeLinkPaymentMethodKind]
    GROK_BOT_STRIPE_LINK_PAYMENT_METHOD_KIND_CARD: _ClassVar[GrokBotStripeLinkPaymentMethodKind]
    GROK_BOT_STRIPE_LINK_PAYMENT_METHOD_KIND_BANK_ACCOUNT: _ClassVar[GrokBotStripeLinkPaymentMethodKind]

class GrokBotStripeLinkPaymentMethodsOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotStripeLinkPaymentMethodsOutcome]
    GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_OK: _ClassVar[GrokBotStripeLinkPaymentMethodsOutcome]
    GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_NEEDS_AUTH: _ClassVar[GrokBotStripeLinkPaymentMethodsOutcome]
    GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_UNAVAILABLE: _ClassVar[GrokBotStripeLinkPaymentMethodsOutcome]

class GrokBotTemplateOwnerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_TEMPLATE_OWNER_TYPE_UNSPECIFIED: _ClassVar[GrokBotTemplateOwnerType]
    GROK_BOT_TEMPLATE_OWNER_TYPE_USER: _ClassVar[GrokBotTemplateOwnerType]
    GROK_BOT_TEMPLATE_OWNER_TYPE_TEAM: _ClassVar[GrokBotTemplateOwnerType]

class GrokBotTemplateVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_TEMPLATE_VISIBILITY_UNSPECIFIED: _ClassVar[GrokBotTemplateVisibility]
    GROK_BOT_TEMPLATE_VISIBILITY_PUBLIC: _ClassVar[GrokBotTemplateVisibility]
    GROK_BOT_TEMPLATE_VISIBILITY_TEAM: _ClassVar[GrokBotTemplateVisibility]

class GrokBotTemporalHarnessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_TEMPORAL_HARNESS_MODE_UNSPECIFIED: _ClassVar[GrokBotTemporalHarnessMode]
    GROK_BOT_TEMPORAL_HARNESS_MODE_OFF: _ClassVar[GrokBotTemporalHarnessMode]
    GROK_BOT_TEMPORAL_HARNESS_MODE_SHADOW: _ClassVar[GrokBotTemporalHarnessMode]
    GROK_BOT_TEMPORAL_HARNESS_MODE_LIVE: _ClassVar[GrokBotTemporalHarnessMode]
    GROK_BOT_TEMPORAL_HARNESS_MODE_BOX: _ClassVar[GrokBotTemporalHarnessMode]

class GrokBotTurnFailureCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_TURN_FAILURE_CODE_UNSPECIFIED: _ClassVar[GrokBotTurnFailureCode]
    GROK_BOT_TURN_FAILURE_CODE_INTERNAL: _ClassVar[GrokBotTurnFailureCode]
    GROK_BOT_TURN_FAILURE_CODE_TIMEOUT: _ClassVar[GrokBotTurnFailureCode]
    GROK_BOT_TURN_FAILURE_CODE_USAGE_LIMIT: _ClassVar[GrokBotTurnFailureCode]
    GROK_BOT_TURN_FAILURE_CODE_RATE_LIMIT: _ClassVar[GrokBotTurnFailureCode]

class GrokBotUserComputerMessagesConsentVerdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_UNSPECIFIED: _ClassVar[GrokBotUserComputerMessagesConsentVerdict]
    GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_STANDING: _ClassVar[GrokBotUserComputerMessagesConsentVerdict]
    GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_ASK: _ClassVar[GrokBotUserComputerMessagesConsentVerdict]
    GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_REFUSED: _ClassVar[GrokBotUserComputerMessagesConsentVerdict]

class GrokBotUserFormClientPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_USER_FORM_CLIENT_PLATFORM_UNSPECIFIED: _ClassVar[GrokBotUserFormClientPlatform]
    GROK_BOT_USER_FORM_CLIENT_PLATFORM_DESKTOP: _ClassVar[GrokBotUserFormClientPlatform]
    GROK_BOT_USER_FORM_CLIENT_PLATFORM_IOS: _ClassVar[GrokBotUserFormClientPlatform]
    GROK_BOT_USER_FORM_CLIENT_PLATFORM_ANDROID: _ClassVar[GrokBotUserFormClientPlatform]

class GrokBotUserFormDismissMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_USER_FORM_DISMISS_MODE_UNSPECIFIED: _ClassVar[GrokBotUserFormDismissMode]
    GROK_BOT_USER_FORM_DISMISS_MODE_DISMISSED: _ClassVar[GrokBotUserFormDismissMode]
    GROK_BOT_USER_FORM_DISMISS_MODE_ESCALATED: _ClassVar[GrokBotUserFormDismissMode]

class GrokBotUserMessageDelivery(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_USER_MESSAGE_DELIVERY_UNSPECIFIED: _ClassVar[GrokBotUserMessageDelivery]
    GROK_BOT_USER_MESSAGE_DELIVERY_ACCEPTED_BOX: _ClassVar[GrokBotUserMessageDelivery]
    GROK_BOT_USER_MESSAGE_DELIVERY_ACCEPTED_TEMPORAL: _ClassVar[GrokBotUserMessageDelivery]
    GROK_BOT_USER_MESSAGE_DELIVERY_DUPLICATE: _ClassVar[GrokBotUserMessageDelivery]
    GROK_BOT_USER_MESSAGE_DELIVERY_REFUSED: _ClassVar[GrokBotUserMessageDelivery]

class GrokBotUserSettingsField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_USER_SETTINGS_FIELD_UNSPECIFIED: _ClassVar[GrokBotUserSettingsField]
    GROK_BOT_USER_SETTINGS_FIELD_MCP_SERVERS: _ClassVar[GrokBotUserSettingsField]
    GROK_BOT_USER_SETTINGS_FIELD_TIME_ZONE: _ClassVar[GrokBotUserSettingsField]
    GROK_BOT_USER_SETTINGS_FIELD_AUTO_REVIEW: _ClassVar[GrokBotUserSettingsField]
    GROK_BOT_USER_SETTINGS_FIELD_PINNED_AGENTS: _ClassVar[GrokBotUserSettingsField]
    GROK_BOT_USER_SETTINGS_FIELD_SIDEBAR_SECTIONS: _ClassVar[GrokBotUserSettingsField]
    GROK_BOT_USER_SETTINGS_FIELD_HAS_SEEN_ONBOARDING: _ClassVar[GrokBotUserSettingsField]

class GrokBotVirtualCardOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_VIRTUAL_CARD_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotVirtualCardOutcome]
    GROK_BOT_VIRTUAL_CARD_OUTCOME_APPROVED: _ClassVar[GrokBotVirtualCardOutcome]
    GROK_BOT_VIRTUAL_CARD_OUTCOME_DENIED: _ClassVar[GrokBotVirtualCardOutcome]
    GROK_BOT_VIRTUAL_CARD_OUTCOME_NEEDS_AUTH: _ClassVar[GrokBotVirtualCardOutcome]
    GROK_BOT_VIRTUAL_CARD_OUTCOME_FAILED: _ClassVar[GrokBotVirtualCardOutcome]

class GrokBotVirtualCardRaiseOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_VIRTUAL_CARD_RAISE_OUTCOME_UNSPECIFIED: _ClassVar[GrokBotVirtualCardRaiseOutcome]
    GROK_BOT_VIRTUAL_CARD_RAISE_OUTCOME_RAISED: _ClassVar[GrokBotVirtualCardRaiseOutcome]
    GROK_BOT_VIRTUAL_CARD_RAISE_OUTCOME_ALREADY_PENDING: _ClassVar[GrokBotVirtualCardRaiseOutcome]

class GrokBotVirtualCardResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROK_BOT_VIRTUAL_CARD_RESOLUTION_UNSPECIFIED: _ClassVar[GrokBotVirtualCardResolution]
    GROK_BOT_VIRTUAL_CARD_RESOLUTION_APPROVED: _ClassVar[GrokBotVirtualCardResolution]
    GROK_BOT_VIRTUAL_CARD_RESOLUTION_DENIED: _ClassVar[GrokBotVirtualCardResolution]

class LlmGatewayAuthMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LLM_GATEWAY_AUTH_MODE_UNSPECIFIED: _ClassVar[LlmGatewayAuthMode]
    LLM_GATEWAY_AUTH_MODE_JWT_ACCESS: _ClassVar[LlmGatewayAuthMode]
    LLM_GATEWAY_AUTH_MODE_CUSTOMER_MANAGED: _ClassVar[LlmGatewayAuthMode]

class LlmGatewayCredentialSourceStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LLM_GATEWAY_CREDENTIAL_SOURCE_STRATEGY_UNSPECIFIED: _ClassVar[LlmGatewayCredentialSourceStrategy]
    LLM_GATEWAY_CREDENTIAL_SOURCE_STRATEGY_TEAM_CREDENTIAL_ALL_SURFACES: _ClassVar[LlmGatewayCredentialSourceStrategy]
    LLM_GATEWAY_CREDENTIAL_SOURCE_STRATEGY_CLIENT_LOCAL_TEAM_CLOUD: _ClassVar[LlmGatewayCredentialSourceStrategy]

class LocalToolPermissionCeiling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCAL_TOOL_PERMISSION_CEILING_UNSPECIFIED: _ClassVar[LocalToolPermissionCeiling]
    LOCAL_TOOL_PERMISSION_CEILING_NEVER: _ClassVar[LocalToolPermissionCeiling]
    LOCAL_TOOL_PERMISSION_CEILING_ASK: _ClassVar[LocalToolPermissionCeiling]
    LOCAL_TOOL_PERMISSION_CEILING_ALWAYS: _ClassVar[LocalToolPermissionCeiling]

class MarketplaceAccessPrincipalKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MARKETPLACE_ACCESS_PRINCIPAL_KIND_UNSPECIFIED: _ClassVar[MarketplaceAccessPrincipalKind]
    MARKETPLACE_ACCESS_PRINCIPAL_KIND_USER: _ClassVar[MarketplaceAccessPrincipalKind]
    MARKETPLACE_ACCESS_PRINCIPAL_KIND_TEAM_MEMBER_GROUP: _ClassVar[MarketplaceAccessPrincipalKind]
    MARKETPLACE_ACCESS_PRINCIPAL_KIND_TEAM_ADMIN_GROUP: _ClassVar[MarketplaceAccessPrincipalKind]
    MARKETPLACE_ACCESS_PRINCIPAL_KIND_GROUP: _ClassVar[MarketplaceAccessPrincipalKind]

class McpServedBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MCP_SERVED_BY_UNSPECIFIED: _ClassVar[McpServedBy]
    MCP_SERVED_BY_CURSOR: _ClassVar[McpServedBy]
    MCP_SERVED_BY_GROK: _ClassVar[McpServedBy]

class NetworkingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORKING_MODE_UNSPECIFIED: _ClassVar[NetworkingMode]
    NETWORKING_MODE_USER_CONTROLLED: _ClassVar[NetworkingMode]
    NETWORKING_MODE_ALWAYS_DISABLED: _ClassVar[NetworkingMode]

class PluginLifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLUGIN_LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_LISTED: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_UNLISTED: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_DRAFT: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_PENDING: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_REJECTED: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLISHER_SUBMISSION: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PRIVATE_ACTIVE: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_DEPRECATED: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PRIVATE_DEPRECATED: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PUBLIC_INVALID: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PRIVATE_INVALID: _ClassVar[PluginLifecycleState]
    PLUGIN_LIFECYCLE_STATE_PRIVATE_PUBLISHED: _ClassVar[PluginLifecycleState]

class PluginStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLUGIN_STATUS_UNSPECIFIED: _ClassVar[PluginStatus]
    PLUGIN_STATUS_DRAFT: _ClassVar[PluginStatus]
    PLUGIN_STATUS_PENDING_APPROVAL: _ClassVar[PluginStatus]
    PLUGIN_STATUS_APPROVED: _ClassVar[PluginStatus]
    PLUGIN_STATUS_REJECTED: _ClassVar[PluginStatus]
    PLUGIN_STATUS_UNLISTED: _ClassVar[PluginStatus]

class PrivacyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVACY_MODE_UNSPECIFIED: _ClassVar[PrivacyMode]
    PRIVACY_MODE_NO_STORAGE: _ClassVar[PrivacyMode]
    PRIVACY_MODE_NO_TRAINING: _ClassVar[PrivacyMode]
    PRIVACY_MODE_USAGE_DATA_TRAINING_ALLOWED: _ClassVar[PrivacyMode]
    PRIVACY_MODE_USAGE_CODEBASE_TRAINING_ALLOWED: _ClassVar[PrivacyMode]

class PrivateInferenceEnablement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVATE_INFERENCE_ENABLEMENT_UNSPECIFIED: _ClassVar[PrivateInferenceEnablement]
    PRIVATE_INFERENCE_ENABLEMENT_ENABLED: _ClassVar[PrivateInferenceEnablement]
    PRIVATE_INFERENCE_ENABLEMENT_DISABLED: _ClassVar[PrivateInferenceEnablement]

class PrReviewOpenDestinationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PR_REVIEW_OPEN_DESTINATION_MODE_UNSPECIFIED: _ClassVar[PrReviewOpenDestinationMode]
    PR_REVIEW_OPEN_DESTINATION_MODE_GITHUB: _ClassVar[PrReviewOpenDestinationMode]
    PR_REVIEW_OPEN_DESTINATION_MODE_GRAPHITE: _ClassVar[PrReviewOpenDestinationMode]
    PR_REVIEW_OPEN_DESTINATION_MODE_REVIEW_CURSOR: _ClassVar[PrReviewOpenDestinationMode]

class PrReviewOpenSurfaceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PR_REVIEW_OPEN_SURFACE_MODE_UNSPECIFIED: _ClassVar[PrReviewOpenSurfaceMode]
    PR_REVIEW_OPEN_SURFACE_MODE_IN_APP: _ClassVar[PrReviewOpenSurfaceMode]
    PR_REVIEW_OPEN_SURFACE_MODE_EXTERNAL_BROWSER: _ClassVar[PrReviewOpenSurfaceMode]

class PublicArtifactSharingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLIC_ARTIFACT_SHARING_MODE_UNSPECIFIED: _ClassVar[PublicArtifactSharingMode]
    PUBLIC_ARTIFACT_SHARING_MODE_ALLOWED: _ClassVar[PublicArtifactSharingMode]
    PUBLIC_ARTIFACT_SHARING_MODE_DISABLED: _ClassVar[PublicArtifactSharingMode]

class SandboxingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SANDBOXING_MODE_UNSPECIFIED: _ClassVar[SandboxingMode]
    SANDBOXING_MODE_ENABLED: _ClassVar[SandboxingMode]
    SANDBOXING_MODE_DISABLED: _ClassVar[SandboxingMode]

class SandBoxMigrationPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_BOX_MIGRATION_PHASE_UNSPECIFIED: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_BACKING_UP: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_CREATING: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_MOVING: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_CLEANING_UP: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_WIPING: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_DONE: _ClassVar[SandBoxMigrationPhase]
    SAND_BOX_MIGRATION_PHASE_FAILED: _ClassVar[SandBoxMigrationPhase]

class SandboxReadBoundaryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SANDBOX_READ_BOUNDARY_MODE_UNSPECIFIED: _ClassVar[SandboxReadBoundaryMode]
    SANDBOX_READ_BOUNDARY_MODE_SYSTEM: _ClassVar[SandboxReadBoundaryMode]
    SANDBOX_READ_BOUNDARY_MODE_WORKSPACE: _ClassVar[SandboxReadBoundaryMode]

class SandBoxRunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_BOX_RUN_STATE_UNSPECIFIED: _ClassVar[SandBoxRunState]
    SAND_BOX_RUN_STATE_ABSENT: _ClassVar[SandBoxRunState]
    SAND_BOX_RUN_STATE_HIBERNATED: _ClassVar[SandBoxRunState]
    SAND_BOX_RUN_STATE_RUNNING: _ClassVar[SandBoxRunState]
    SAND_BOX_RUN_STATE_STARTING: _ClassVar[SandBoxRunState]

class SandBoxStoreMultipartOperationFailureCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_UNSPECIFIED: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_PRECONDITION_FAILED: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_UPLOAD_NOT_FOUND: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_INVALID_PARTS: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_CHECKSUM_MISMATCH: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_TRANSIENT: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_INTERNAL: _ClassVar[SandBoxStoreMultipartOperationFailureCode]
    SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_RESTART_REQUIRED: _ClassVar[SandBoxStoreMultipartOperationFailureCode]

class SandBoxUpgradeScheduleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_BOX_UPGRADE_SCHEDULE_STATE_UNSPECIFIED: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_SCHEDULED: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_CLAIMED: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_RUNNING: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_WAITING_FOR_IMAGE: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_COMPLETED: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_MISSED: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_FAILED: _ClassVar[SandBoxUpgradeScheduleState]
    SAND_BOX_UPGRADE_SCHEDULE_STATE_CANCELLED: _ClassVar[SandBoxUpgradeScheduleState]

class SandCredentialDecisionHarness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_CREDENTIAL_DECISION_HARNESS_UNSPECIFIED: _ClassVar[SandCredentialDecisionHarness]
    SAND_CREDENTIAL_DECISION_HARNESS_BOX: _ClassVar[SandCredentialDecisionHarness]
    SAND_CREDENTIAL_DECISION_HARNESS_TEMPORAL: _ClassVar[SandCredentialDecisionHarness]

class SandEgressMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_EGRESS_MODE_UNSPECIFIED: _ClassVar[SandEgressMode]
    SAND_EGRESS_MODE_ALLOW_ALL: _ClassVar[SandEgressMode]
    SAND_EGRESS_MODE_DEFAULT_WITH_NETWORK_SETTINGS: _ClassVar[SandEgressMode]
    SAND_EGRESS_MODE_NETWORK_SETTINGS_ONLY: _ClassVar[SandEgressMode]

class SandGroupAccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_GROUP_ACCESS_MODE_UNSPECIFIED: _ClassVar[SandGroupAccessMode]
    SAND_GROUP_ACCESS_MODE_ALL: _ClassVar[SandGroupAccessMode]
    SAND_GROUP_ACCESS_MODE_LIMITED: _ClassVar[SandGroupAccessMode]

class SandSetupManifestScopeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND_SETUP_MANIFEST_SCOPE_KIND_UNSPECIFIED: _ClassVar[SandSetupManifestScopeKind]
    SAND_SETUP_MANIFEST_SCOPE_KIND_USER: _ClassVar[SandSetupManifestScopeKind]
    SAND_SETUP_MANIFEST_SCOPE_KIND_TEAM: _ClassVar[SandSetupManifestScopeKind]
    SAND_SETUP_MANIFEST_SCOPE_KIND_ORGANIZATION: _ClassVar[SandSetupManifestScopeKind]

class SetGrokBotAgentVisibilityOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_UNSPECIFIED: _ClassVar[SetGrokBotAgentVisibilityOutcome]
    SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_UPDATED: _ClassVar[SetGrokBotAgentVisibilityOutcome]
    SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_UNSUPPORTED_HARNESS: _ClassVar[SetGrokBotAgentVisibilityOutcome]
    SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_NO_TEAM: _ClassVar[SetGrokBotAgentVisibilityOutcome]

class SharedConversationVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARED_CONVERSATION_VISIBILITY_UNSPECIFIED: _ClassVar[SharedConversationVisibility]
    SHARED_CONVERSATION_VISIBILITY_PRIVATE: _ClassVar[SharedConversationVisibility]
    SHARED_CONVERSATION_VISIBILITY_TEAM: _ClassVar[SharedConversationVisibility]
    SHARED_CONVERSATION_VISIBILITY_PUBLIC: _ClassVar[SharedConversationVisibility]

class SpendGroupByCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEND_GROUP_BY_CATEGORY_UNSPECIFIED: _ClassVar[SpendGroupByCategory]
    SPEND_GROUP_BY_CATEGORY_MODEL: _ClassVar[SpendGroupByCategory]
    SPEND_GROUP_BY_CATEGORY_USAGE_TYPE: _ClassVar[SpendGroupByCategory]

class SpendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEND_TYPE_UNSPECIFIED: _ClassVar[SpendType]
    SPEND_TYPE_ON_DEMAND: _ClassVar[SpendType]
    SPEND_TYPE_INCLUDED: _ClassVar[SpendType]
    SPEND_TYPE_ALL: _ClassVar[SpendType]

class TeamFollowupEnabledMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEAM_FOLLOWUP_ENABLED_MODE_UNSPECIFIED: _ClassVar[TeamFollowupEnabledMode]
    TEAM_FOLLOWUP_ENABLED_MODE_DISABLED: _ClassVar[TeamFollowupEnabledMode]
    TEAM_FOLLOWUP_ENABLED_MODE_SERVICE_ACCOUNTS_ONLY: _ClassVar[TeamFollowupEnabledMode]
    TEAM_FOLLOWUP_ENABLED_MODE_ALL: _ClassVar[TeamFollowupEnabledMode]

class TeamMarketplacePluginInstallMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEAM_MARKETPLACE_PLUGIN_INSTALL_MODE_OPTIONAL: _ClassVar[TeamMarketplacePluginInstallMode]
    TEAM_MARKETPLACE_PLUGIN_INSTALL_MODE_DEFAULT: _ClassVar[TeamMarketplacePluginInstallMode]
    TEAM_MARKETPLACE_PLUGIN_INSTALL_MODE_REQUIRED: _ClassVar[TeamMarketplacePluginInstallMode]

class TeamMemberBillingTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEAM_MEMBER_BILLING_TIER_UNSPECIFIED: _ClassVar[TeamMemberBillingTier]
    TEAM_MEMBER_BILLING_TIER_TIER_1000: _ClassVar[TeamMemberBillingTier]
    TEAM_MEMBER_BILLING_TIER_TIER_2000: _ClassVar[TeamMemberBillingTier]

class TeamRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEAM_ROLE_UNSPECIFIED: _ClassVar[TeamRole]
    TEAM_ROLE_OWNER: _ClassVar[TeamRole]
    TEAM_ROLE_MEMBER: _ClassVar[TeamRole]
    TEAM_ROLE_FREE_OWNER: _ClassVar[TeamRole]
    TEAM_ROLE_REMOVED: _ClassVar[TeamRole]
ALLOWLIST_CONFIG_UNSPECIFIED: AllowlistConfig
ALLOWLIST_CONFIG_ALLOWLIST: AllowlistConfig
ALLOWLIST_CONFIG_BLOCKLIST: AllowlistConfig
AUTO_CREATE_PR_MODE_UNSPECIFIED: AutoCreatePrMode
AUTO_CREATE_PR_MODE_ALWAYS: AutoCreatePrMode
AUTO_CREATE_PR_MODE_SINGLE: AutoCreatePrMode
AUTO_CREATE_PR_MODE_NEVER: AutoCreatePrMode
AUTO_CREATE_PR_SETTING_UNSPECIFIED: AutoCreatePrSetting
AUTO_CREATE_PR_SETTING_ALWAYS: AutoCreatePrSetting
AUTO_CREATE_PR_SETTING_SINGLE: AutoCreatePrSetting
AUTO_CREATE_PR_SETTING_NEVER: AutoCreatePrSetting
AUTOMATION_DEFAULT_VISIBILITY_UNSPECIFIED: AutomationDefaultVisibility
AUTOMATION_DEFAULT_VISIBILITY_VISIBLE: AutomationDefaultVisibility
AUTOMATION_DEFAULT_VISIBILITY_EDITABLE: AutomationDefaultVisibility
AUTOMATION_DEFAULT_VISIBILITY_PRIVATE: AutomationDefaultVisibility
AVAILABLE_MODELS_SCOPE_UNSPECIFIED: AvailableModelsScope
AVAILABLE_MODELS_SCOPE_USER_AVAILABLE: AvailableModelsScope
AVAILABLE_MODELS_SCOPE_AUTOMATIONS: AvailableModelsScope
AVAILABLE_MODELS_SCOPE_ADMIN_SETTINGS_ALL_APPLICATION_MODELS: AvailableModelsScope
BACKGROUND_COMPOSER_QUICK_ACTION_EXECUTION_MODE_UNSPECIFIED: BackgroundComposerQuickActionExecutionMode
BACKGROUND_COMPOSER_QUICK_ACTION_EXECUTION_MODE_SUBAGENT: BackgroundComposerQuickActionExecutionMode
BACKGROUND_COMPOSER_QUICK_ACTION_EXECUTION_MODE_PARENT_AGENT: BackgroundComposerQuickActionExecutionMode
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_UNSPECIFIED: BackgroundComposerQuickActionSubagentTemplateOperation
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_CREATE: BackgroundComposerQuickActionSubagentTemplateOperation
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_UPDATE: BackgroundComposerQuickActionSubagentTemplateOperation
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_OPERATION_DELETE: BackgroundComposerQuickActionSubagentTemplateOperation
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_UNSPECIFIED: BackgroundComposerQuickActionSubagentTemplateScope
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_BUILTIN: BackgroundComposerQuickActionSubagentTemplateScope
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_USER: BackgroundComposerQuickActionSubagentTemplateScope
BACKGROUND_COMPOSER_QUICK_ACTION_SUBAGENT_TEMPLATE_SCOPE_TEAM: BackgroundComposerQuickActionSubagentTemplateScope
BULK_TEAM_MEMBER_SAND_BOX_ACTION_UNSPECIFIED: BulkTeamMemberSandBoxAction
BULK_TEAM_MEMBER_SAND_BOX_ACTION_KILL: BulkTeamMemberSandBoxAction
BULK_TEAM_MEMBER_SAND_BOX_ACTION_RECREATE: BulkTeamMemberSandBoxAction
BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_UNSPECIFIED: BulkTeamMemberSandBoxItemState
BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_QUEUED: BulkTeamMemberSandBoxItemState
BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_RUNNING: BulkTeamMemberSandBoxItemState
BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_SUCCEEDED: BulkTeamMemberSandBoxItemState
BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_SKIPPED: BulkTeamMemberSandBoxItemState
BULK_TEAM_MEMBER_SAND_BOX_ITEM_STATE_FAILED: BulkTeamMemberSandBoxItemState
BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_UNSPECIFIED: BulkTeamMemberSandBoxOperationState
BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_RUNNING: BulkTeamMemberSandBoxOperationState
BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_SUCCEEDED: BulkTeamMemberSandBoxOperationState
BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_PARTIALLY_SUCCEEDED: BulkTeamMemberSandBoxOperationState
BULK_TEAM_MEMBER_SAND_BOX_OPERATION_STATE_FAILED: BulkTeamMemberSandBoxOperationState
CANVAS_VISIBILITY_UNSPECIFIED: CanvasVisibility
CANVAS_VISIBILITY_PRIVATE: CanvasVisibility
CANVAS_VISIBILITY_TEAM_VIEW: CanvasVisibility
CLIENT_LOG_LEVEL_UNSPECIFIED: ClientLogLevel
CLIENT_LOG_LEVEL_INFO: ClientLogLevel
CLIENT_LOG_LEVEL_DEBUG: ClientLogLevel
CLIENT_LOG_LEVEL_WARN: ClientLogLevel
CLIENT_LOG_LEVEL_ERROR: ClientLogLevel
CLIENT_OS_UNSPECIFIED: ClientOS
CLIENT_OS_WINDOWS: ClientOS
CLIENT_OS_MACOS: ClientOS
CLIENT_OS_LINUX: ClientOS
CLIENT_OS_IOS: ClientOS
CLIENT_OS_ANDROID: ClientOS
CLOUD_AGENT_EFFORT_MODE_UNSPECIFIED: CloudAgentEffortMode
CLOUD_AGENT_EFFORT_MODE_STANDARD: CloudAgentEffortMode
CLOUD_AGENT_EFFORT_MODE_GRIND: CloudAgentEffortMode
CLOUD_AGENT_EGRESS_PROTECTION_MODE_UNSPECIFIED: CloudAgentEgressProtectionMode
CLOUD_AGENT_EGRESS_PROTECTION_MODE_ALLOW_ALL: CloudAgentEgressProtectionMode
CLOUD_AGENT_EGRESS_PROTECTION_MODE_DEFAULT_WITH_NETWORK_SETTINGS: CloudAgentEgressProtectionMode
CLOUD_AGENT_EGRESS_PROTECTION_MODE_NETWORK_SETTINGS_ONLY: CloudAgentEgressProtectionMode
CLOUD_AGENT_EGRESS_PROTECTION_MODE_PARENT_PLUS_NETWORK_SETTINGS: CloudAgentEgressProtectionMode
CREDENTIAL_EXPIRATION_MODE_UNSPECIFIED: CredentialExpirationMode
CREDENTIAL_EXPIRATION_MODE_DISABLED: CredentialExpirationMode
CREDENTIAL_EXPIRATION_MODE_WARN: CredentialExpirationMode
CREDENTIAL_EXPIRATION_MODE_ENFORCE: CredentialExpirationMode
CREDENTIAL_LIFECYCLE_STATE_UNSPECIFIED: CredentialLifecycleState
CREDENTIAL_LIFECYCLE_STATE_ACTIVE: CredentialLifecycleState
CREDENTIAL_LIFECYCLE_STATE_EXPIRING: CredentialLifecycleState
CREDENTIAL_LIFECYCLE_STATE_GRACE: CredentialLifecycleState
CREDENTIAL_LIFECYCLE_STATE_EXPIRED: CredentialLifecycleState
CREDENTIAL_LIFECYCLE_STATE_PROVIDER_REJECTED: CredentialLifecycleState
CREDENTIAL_TARGET_RULE_KIND_UNSPECIFIED: CredentialTargetRuleKind
CREDENTIAL_TARGET_RULE_KIND_EXACT_HOST_PORT: CredentialTargetRuleKind
CREDENTIAL_TARGET_RULE_KIND_REGISTRABLE_DOMAIN: CredentialTargetRuleKind
EFFECTIVE_PLUGIN_INSTALL_MODE_UNSPECIFIED: EffectivePluginInstallMode
EFFECTIVE_PLUGIN_INSTALL_MODE_USER: EffectivePluginInstallMode
EFFECTIVE_PLUGIN_INSTALL_MODE_TEAM_DEFAULT: EffectivePluginInstallMode
EFFECTIVE_PLUGIN_INSTALL_MODE_TEAM_REQUIRED: EffectivePluginInstallMode
FIRST_PARTY_PLUGIN_MODE_UNSPECIFIED: FirstPartyPluginMode
FIRST_PARTY_PLUGIN_MODE_ENABLE_ALL: FirstPartyPluginMode
FIRST_PARTY_PLUGIN_MODE_ALLOWLIST: FirstPartyPluginMode
GITHUB_ARTIFACT_POSTING_MODE_UNSPECIFIED: GithubArtifactPostingMode
GITHUB_ARTIFACT_POSTING_MODE_POST_ARTIFACT: GithubArtifactPostingMode
GITHUB_ARTIFACT_POSTING_MODE_LINK_ONLY: GithubArtifactPostingMode
GIT_MODE_UNSPECIFIED: GitMode
GIT_MODE_USER_CONTROLLED: GitMode
GIT_MODE_ALWAYS_DISABLED: GitMode
GROK_BOT_AGENT_HARNESS_KIND_UNSPECIFIED: GrokBotAgentHarnessKind
GROK_BOT_AGENT_HARNESS_KIND_BOX: GrokBotAgentHarnessKind
GROK_BOT_AGENT_HARNESS_KIND_TEMPORAL: GrokBotAgentHarnessKind
GROK_BOT_AGENT_KIND_UNSPECIFIED: GrokBotAgentKind
GROK_BOT_AGENT_KIND_AGENT: GrokBotAgentKind
GROK_BOT_AGENT_KIND_ROOM: GrokBotAgentKind
GROK_BOT_AGENT_MESSAGE_DELIVERY_UNSPECIFIED: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_DELIVERED_TEMPORAL: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_DELIVERED_BOX: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_DUPLICATE: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_TARGET_NOT_FOUND: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_FORBIDDEN: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_BOX_UNREACHABLE: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_TEMPORAL_UNAVAILABLE: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_MESSAGE_DELIVERY_INVALID_TARGET: GrokBotAgentMessageDelivery
GROK_BOT_AGENT_SESSION_KIND_UNSPECIFIED: GrokBotAgentSessionKind
GROK_BOT_AGENT_SESSION_KIND_MAIN: GrokBotAgentSessionKind
GROK_BOT_AGENT_SESSION_KIND_SLACK_DM: GrokBotAgentSessionKind
GROK_BOT_AGENT_SESSION_KIND_SLACK_THREAD: GrokBotAgentSessionKind
GROK_BOT_AGENT_SESSION_KIND_DM: GrokBotAgentSessionKind
GROK_BOT_AGENT_SESSION_KIND_GROUP: GrokBotAgentSessionKind
GROK_BOT_AGENT_VISIBILITY_UNSPECIFIED: GrokBotAgentVisibility
GROK_BOT_AGENT_VISIBILITY_OWNER: GrokBotAgentVisibility
GROK_BOT_AGENT_VISIBILITY_TEAM: GrokBotAgentVisibility
GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_UNSPECIFIED: GrokBotAutoReviewApprovalResolution
GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_APPROVED: GrokBotAutoReviewApprovalResolution
GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_DENIED: GrokBotAutoReviewApprovalResolution
GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_ALWAYS: GrokBotAutoReviewApprovalResolution
GROK_BOT_BOX_DISK_PRESSURE_LEVEL_UNSPECIFIED: GrokBotBoxDiskPressureLevel
GROK_BOT_BOX_DISK_PRESSURE_LEVEL_NONE: GrokBotBoxDiskPressureLevel
GROK_BOT_BOX_DISK_PRESSURE_LEVEL_SOFT: GrokBotBoxDiskPressureLevel
GROK_BOT_BOX_DISK_PRESSURE_LEVEL_HARD: GrokBotBoxDiskPressureLevel
GROK_BOT_BOX_HAND_BACK_TRIGGER_UNSPECIFIED: GrokBotBoxHandBackTrigger
GROK_BOT_BOX_HAND_BACK_TRIGGER_BUTTON: GrokBotBoxHandBackTrigger
GROK_BOT_BOX_HAND_BACK_TRIGGER_VIEWER_CLOSED: GrokBotBoxHandBackTrigger
GROK_BOT_BOX_HAND_BACK_TRIGGER_DISMISSED: GrokBotBoxHandBackTrigger
GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_UNSPECIFIED: GrokBotBoxHarnessMigrationPassState
GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_DISABLED: GrokBotBoxHarnessMigrationPassState
GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_DONE: GrokBotBoxHarnessMigrationPassState
GROK_BOT_BOX_HARNESS_MIGRATION_PASS_STATE_PENDING: GrokBotBoxHarnessMigrationPassState
GROK_BOT_CLIENT_SURFACE_UNSPECIFIED: GrokBotClientSurface
GROK_BOT_CLIENT_SURFACE_DESKTOP: GrokBotClientSurface
GROK_BOT_CLIENT_SURFACE_MOBILE: GrokBotClientSurface
GROK_BOT_CONNECTOR_TYPE_UNSPECIFIED: GrokBotConnectorType
GROK_BOT_CONNECTOR_TYPE_USER: GrokBotConnectorType
GROK_BOT_CONNECTOR_TYPE_TEAM: GrokBotConnectorType
GROK_BOT_CREDENTIAL_REQUEST_RESOLUTION_UNSPECIFIED: GrokBotCredentialRequestResolution
GROK_BOT_CREDENTIAL_REQUEST_RESOLUTION_APPROVED: GrokBotCredentialRequestResolution
GROK_BOT_CREDENTIAL_REQUEST_RESOLUTION_DENIED: GrokBotCredentialRequestResolution
GROK_BOT_FEEDBACK_ACTION_UNSPECIFIED: GrokBotFeedbackAction
GROK_BOT_FEEDBACK_ACTION_UP: GrokBotFeedbackAction
GROK_BOT_FEEDBACK_ACTION_DOWN: GrokBotFeedbackAction
GROK_BOT_FEEDBACK_ACTION_SUBMIT: GrokBotFeedbackAction
GROK_BOT_FEEDBACK_ACTION_REVERT: GrokBotFeedbackAction
GROK_BOT_FIRST_PARTY_TEMPLATE_UNSPECIFIED: GrokBotFirstPartyTemplate
GROK_BOT_FIRST_PARTY_TEMPLATE_SWE: GrokBotFirstPartyTemplate
GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_UNSPECIFIED: GrokBotLocalToolPermissionCardResolution
GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_ALLOW_ONCE: GrokBotLocalToolPermissionCardResolution
GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_DENY: GrokBotLocalToolPermissionCardResolution
GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_ALWAYS: GrokBotLocalToolPermissionCardResolution
GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_NEVER: GrokBotLocalToolPermissionCardResolution
GROK_BOT_MARKETPLACE_IMAGE_KIND_UNSPECIFIED: GrokBotMarketplaceImageKind
GROK_BOT_MARKETPLACE_IMAGE_KIND_BOT: GrokBotMarketplaceImageKind
GROK_BOT_MARKETPLACE_IMAGE_KIND_CREATOR: GrokBotMarketplaceImageKind
GROK_BOT_MARKETPLACE_LISTING_STATUS_UNSPECIFIED: GrokBotMarketplaceListingStatus
GROK_BOT_MARKETPLACE_LISTING_STATUS_PENDING_REVIEW: GrokBotMarketplaceListingStatus
GROK_BOT_MARKETPLACE_LISTING_STATUS_LISTED: GrokBotMarketplaceListingStatus
GROK_BOT_MARKETPLACE_LISTING_STATUS_DELISTED: GrokBotMarketplaceListingStatus
GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_UNSPECIFIED: GrokBotRoomMemberTurnDispatch
GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_ACCEPTED: GrokBotRoomMemberTurnDispatch
GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_DUPLICATE: GrokBotRoomMemberTurnDispatch
GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_NOT_TEMPORAL: GrokBotRoomMemberTurnDispatch
GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_TARGET_NOT_FOUND: GrokBotRoomMemberTurnDispatch
GROK_BOT_ROOM_MEMBER_TURN_DISPATCH_TEMPORAL_UNAVAILABLE: GrokBotRoomMemberTurnDispatch
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_UNSPECIFIED: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_SENT: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_PASS: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_SKIPPED: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_TIMEOUT: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_CANCELLED: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_OUTCOME_ERROR: GrokBotRoomMemberTurnOutcome
GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_UNSPECIFIED: GrokBotRoomMemberTurnResultIntake
GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_ACCEPTED: GrokBotRoomMemberTurnResultIntake
GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_UNKNOWN_NONCE: GrokBotRoomMemberTurnResultIntake
GROK_BOT_ROOM_MEMBER_TURN_RESULT_INTAKE_HOST_UNAVAILABLE: GrokBotRoomMemberTurnResultIntake
GROK_BOT_ROSTER_CHANGE_KIND_UNSPECIFIED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_AGENT_CREATED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_AGENT_UPDATED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_AGENT_DELETED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_AGENT_VISIBILITY_CHANGED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_ROOM_MEMBERS_CHANGED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_SIDEBAR_VISIBILITY_CHANGED: GrokBotRosterChangeKind
GROK_BOT_ROSTER_CHANGE_KIND_USER_SETTINGS_CHANGED: GrokBotRosterChangeKind
GROK_BOT_SEND_STATUS_UNSPECIFIED: GrokBotSendStatus
GROK_BOT_SEND_STATUS_NOT_FOUND: GrokBotSendStatus
GROK_BOT_SEND_STATUS_ACCEPTED: GrokBotSendStatus
GROK_BOT_SEND_STATUS_REJECTED: GrokBotSendStatus
GROK_BOT_SEND_STATUS_PENDING: GrokBotSendStatus
GROK_BOT_SEND_STATUS_UNKNOWN_DURABILITY: GrokBotSendStatus
GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_UNSPECIFIED: GrokBotSessionBoxCredentialState
GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_ABSENT: GrokBotSessionBoxCredentialState
GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_PRESENT: GrokBotSessionBoxCredentialState
GROK_BOT_SESSION_BOX_CREDENTIAL_STATE_REVOKED: GrokBotSessionBoxCredentialState
GROK_BOT_SESSION_BOX_POD_STATE_UNSPECIFIED: GrokBotSessionBoxPodState
GROK_BOT_SESSION_BOX_POD_STATE_ABSENT: GrokBotSessionBoxPodState
GROK_BOT_SESSION_BOX_POD_STATE_REACHABLE: GrokBotSessionBoxPodState
GROK_BOT_SESSION_BOX_POD_STATE_HIBERNATED: GrokBotSessionBoxPodState
GROK_BOT_SESSION_BOX_POD_STATE_STARTING: GrokBotSessionBoxPodState
GROK_BOT_SESSION_BOX_POD_STATE_UNKNOWN: GrokBotSessionBoxPodState
GROK_BOT_SLACK_CONNECT_OUTCOME_UNSPECIFIED: GrokBotSlackConnectOutcome
GROK_BOT_SLACK_CONNECT_OUTCOME_STARTED: GrokBotSlackConnectOutcome
GROK_BOT_SLACK_CONNECT_OUTCOME_UNSUPPORTED_HARNESS: GrokBotSlackConnectOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_UNSPECIFIED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_INSTALLED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_PENDING_ADMIN_APPROVAL: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_NOT_CONNECTED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_WORKSPACE_REQUIRED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_MANAGER_REAUTH_REQUIRED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_INSUFFICIENT_SCOPES: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_INSTALL_CONFLICT: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_RATELIMITED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_SLACK_REJECTED: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_OUTCOME_UNSUPPORTED_HARNESS: GrokBotSlackInstallOutcome
GROK_BOT_SLACK_INSTALL_STATUS_UNSPECIFIED: GrokBotSlackInstallStatus
GROK_BOT_SLACK_INSTALL_STATUS_NOT_CONNECTED: GrokBotSlackInstallStatus
GROK_BOT_SLACK_INSTALL_STATUS_APP_CREATED: GrokBotSlackInstallStatus
GROK_BOT_SLACK_INSTALL_STATUS_CONNECTED: GrokBotSlackInstallStatus
GROK_BOT_SLACK_INSTALL_STATUS_UNSUPPORTED_HARNESS: GrokBotSlackInstallStatus
GROK_BOT_SLACK_REINSTALL_OUTCOME_UNSPECIFIED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_UPDATED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_UP_TO_DATE: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_RECREATE_REQUIRED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_PENDING_ADMIN_APPROVAL: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_NOT_CONNECTED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_MANAGER_REAUTH_REQUIRED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_INSUFFICIENT_SCOPES: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_RATELIMITED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_SLACK_REJECTED: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_REINSTALL_OUTCOME_UNSUPPORTED_HARNESS: GrokBotSlackReinstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_UNSPECIFIED: GrokBotSlackUninstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_REMOVED: GrokBotSlackUninstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_NOT_CONNECTED: GrokBotSlackUninstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_MANAGER_REAUTH_REQUIRED: GrokBotSlackUninstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_RATELIMITED: GrokBotSlackUninstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_SLACK_REJECTED: GrokBotSlackUninstallOutcome
GROK_BOT_SLACK_UNINSTALL_OUTCOME_UNSUPPORTED_HARNESS: GrokBotSlackUninstallOutcome
GROK_BOT_STRIPE_LINK_PAYMENT_METHOD_KIND_UNSPECIFIED: GrokBotStripeLinkPaymentMethodKind
GROK_BOT_STRIPE_LINK_PAYMENT_METHOD_KIND_CARD: GrokBotStripeLinkPaymentMethodKind
GROK_BOT_STRIPE_LINK_PAYMENT_METHOD_KIND_BANK_ACCOUNT: GrokBotStripeLinkPaymentMethodKind
GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_UNSPECIFIED: GrokBotStripeLinkPaymentMethodsOutcome
GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_OK: GrokBotStripeLinkPaymentMethodsOutcome
GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_NEEDS_AUTH: GrokBotStripeLinkPaymentMethodsOutcome
GROK_BOT_STRIPE_LINK_PAYMENT_METHODS_OUTCOME_UNAVAILABLE: GrokBotStripeLinkPaymentMethodsOutcome
GROK_BOT_TEMPLATE_OWNER_TYPE_UNSPECIFIED: GrokBotTemplateOwnerType
GROK_BOT_TEMPLATE_OWNER_TYPE_USER: GrokBotTemplateOwnerType
GROK_BOT_TEMPLATE_OWNER_TYPE_TEAM: GrokBotTemplateOwnerType
GROK_BOT_TEMPLATE_VISIBILITY_UNSPECIFIED: GrokBotTemplateVisibility
GROK_BOT_TEMPLATE_VISIBILITY_PUBLIC: GrokBotTemplateVisibility
GROK_BOT_TEMPLATE_VISIBILITY_TEAM: GrokBotTemplateVisibility
GROK_BOT_TEMPORAL_HARNESS_MODE_UNSPECIFIED: GrokBotTemporalHarnessMode
GROK_BOT_TEMPORAL_HARNESS_MODE_OFF: GrokBotTemporalHarnessMode
GROK_BOT_TEMPORAL_HARNESS_MODE_SHADOW: GrokBotTemporalHarnessMode
GROK_BOT_TEMPORAL_HARNESS_MODE_LIVE: GrokBotTemporalHarnessMode
GROK_BOT_TEMPORAL_HARNESS_MODE_BOX: GrokBotTemporalHarnessMode
GROK_BOT_TURN_FAILURE_CODE_UNSPECIFIED: GrokBotTurnFailureCode
GROK_BOT_TURN_FAILURE_CODE_INTERNAL: GrokBotTurnFailureCode
GROK_BOT_TURN_FAILURE_CODE_TIMEOUT: GrokBotTurnFailureCode
GROK_BOT_TURN_FAILURE_CODE_USAGE_LIMIT: GrokBotTurnFailureCode
GROK_BOT_TURN_FAILURE_CODE_RATE_LIMIT: GrokBotTurnFailureCode
GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_UNSPECIFIED: GrokBotUserComputerMessagesConsentVerdict
GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_STANDING: GrokBotUserComputerMessagesConsentVerdict
GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_ASK: GrokBotUserComputerMessagesConsentVerdict
GROK_BOT_USER_COMPUTER_MESSAGES_CONSENT_VERDICT_REFUSED: GrokBotUserComputerMessagesConsentVerdict
GROK_BOT_USER_FORM_CLIENT_PLATFORM_UNSPECIFIED: GrokBotUserFormClientPlatform
GROK_BOT_USER_FORM_CLIENT_PLATFORM_DESKTOP: GrokBotUserFormClientPlatform
GROK_BOT_USER_FORM_CLIENT_PLATFORM_IOS: GrokBotUserFormClientPlatform
GROK_BOT_USER_FORM_CLIENT_PLATFORM_ANDROID: GrokBotUserFormClientPlatform
GROK_BOT_USER_FORM_DISMISS_MODE_UNSPECIFIED: GrokBotUserFormDismissMode
GROK_BOT_USER_FORM_DISMISS_MODE_DISMISSED: GrokBotUserFormDismissMode
GROK_BOT_USER_FORM_DISMISS_MODE_ESCALATED: GrokBotUserFormDismissMode
GROK_BOT_USER_MESSAGE_DELIVERY_UNSPECIFIED: GrokBotUserMessageDelivery
GROK_BOT_USER_MESSAGE_DELIVERY_ACCEPTED_BOX: GrokBotUserMessageDelivery
GROK_BOT_USER_MESSAGE_DELIVERY_ACCEPTED_TEMPORAL: GrokBotUserMessageDelivery
GROK_BOT_USER_MESSAGE_DELIVERY_DUPLICATE: GrokBotUserMessageDelivery
GROK_BOT_USER_MESSAGE_DELIVERY_REFUSED: GrokBotUserMessageDelivery
GROK_BOT_USER_SETTINGS_FIELD_UNSPECIFIED: GrokBotUserSettingsField
GROK_BOT_USER_SETTINGS_FIELD_MCP_SERVERS: GrokBotUserSettingsField
GROK_BOT_USER_SETTINGS_FIELD_TIME_ZONE: GrokBotUserSettingsField
GROK_BOT_USER_SETTINGS_FIELD_AUTO_REVIEW: GrokBotUserSettingsField
GROK_BOT_USER_SETTINGS_FIELD_PINNED_AGENTS: GrokBotUserSettingsField
GROK_BOT_USER_SETTINGS_FIELD_SIDEBAR_SECTIONS: GrokBotUserSettingsField
GROK_BOT_USER_SETTINGS_FIELD_HAS_SEEN_ONBOARDING: GrokBotUserSettingsField
GROK_BOT_VIRTUAL_CARD_OUTCOME_UNSPECIFIED: GrokBotVirtualCardOutcome
GROK_BOT_VIRTUAL_CARD_OUTCOME_APPROVED: GrokBotVirtualCardOutcome
GROK_BOT_VIRTUAL_CARD_OUTCOME_DENIED: GrokBotVirtualCardOutcome
GROK_BOT_VIRTUAL_CARD_OUTCOME_NEEDS_AUTH: GrokBotVirtualCardOutcome
GROK_BOT_VIRTUAL_CARD_OUTCOME_FAILED: GrokBotVirtualCardOutcome
GROK_BOT_VIRTUAL_CARD_RAISE_OUTCOME_UNSPECIFIED: GrokBotVirtualCardRaiseOutcome
GROK_BOT_VIRTUAL_CARD_RAISE_OUTCOME_RAISED: GrokBotVirtualCardRaiseOutcome
GROK_BOT_VIRTUAL_CARD_RAISE_OUTCOME_ALREADY_PENDING: GrokBotVirtualCardRaiseOutcome
GROK_BOT_VIRTUAL_CARD_RESOLUTION_UNSPECIFIED: GrokBotVirtualCardResolution
GROK_BOT_VIRTUAL_CARD_RESOLUTION_APPROVED: GrokBotVirtualCardResolution
GROK_BOT_VIRTUAL_CARD_RESOLUTION_DENIED: GrokBotVirtualCardResolution
LLM_GATEWAY_AUTH_MODE_UNSPECIFIED: LlmGatewayAuthMode
LLM_GATEWAY_AUTH_MODE_JWT_ACCESS: LlmGatewayAuthMode
LLM_GATEWAY_AUTH_MODE_CUSTOMER_MANAGED: LlmGatewayAuthMode
LLM_GATEWAY_CREDENTIAL_SOURCE_STRATEGY_UNSPECIFIED: LlmGatewayCredentialSourceStrategy
LLM_GATEWAY_CREDENTIAL_SOURCE_STRATEGY_TEAM_CREDENTIAL_ALL_SURFACES: LlmGatewayCredentialSourceStrategy
LLM_GATEWAY_CREDENTIAL_SOURCE_STRATEGY_CLIENT_LOCAL_TEAM_CLOUD: LlmGatewayCredentialSourceStrategy
LOCAL_TOOL_PERMISSION_CEILING_UNSPECIFIED: LocalToolPermissionCeiling
LOCAL_TOOL_PERMISSION_CEILING_NEVER: LocalToolPermissionCeiling
LOCAL_TOOL_PERMISSION_CEILING_ASK: LocalToolPermissionCeiling
LOCAL_TOOL_PERMISSION_CEILING_ALWAYS: LocalToolPermissionCeiling
MARKETPLACE_ACCESS_PRINCIPAL_KIND_UNSPECIFIED: MarketplaceAccessPrincipalKind
MARKETPLACE_ACCESS_PRINCIPAL_KIND_USER: MarketplaceAccessPrincipalKind
MARKETPLACE_ACCESS_PRINCIPAL_KIND_TEAM_MEMBER_GROUP: MarketplaceAccessPrincipalKind
MARKETPLACE_ACCESS_PRINCIPAL_KIND_TEAM_ADMIN_GROUP: MarketplaceAccessPrincipalKind
MARKETPLACE_ACCESS_PRINCIPAL_KIND_GROUP: MarketplaceAccessPrincipalKind
MCP_SERVED_BY_UNSPECIFIED: McpServedBy
MCP_SERVED_BY_CURSOR: McpServedBy
MCP_SERVED_BY_GROK: McpServedBy
NETWORKING_MODE_UNSPECIFIED: NetworkingMode
NETWORKING_MODE_USER_CONTROLLED: NetworkingMode
NETWORKING_MODE_ALWAYS_DISABLED: NetworkingMode
PLUGIN_LIFECYCLE_STATE_UNSPECIFIED: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_LISTED: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_UNLISTED: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_DRAFT: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_PENDING: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_REJECTED: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLISHER_SUBMISSION: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PRIVATE_ACTIVE: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_DEPRECATED: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PRIVATE_DEPRECATED: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PUBLIC_INVALID: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PRIVATE_INVALID: PluginLifecycleState
PLUGIN_LIFECYCLE_STATE_PRIVATE_PUBLISHED: PluginLifecycleState
PLUGIN_STATUS_UNSPECIFIED: PluginStatus
PLUGIN_STATUS_DRAFT: PluginStatus
PLUGIN_STATUS_PENDING_APPROVAL: PluginStatus
PLUGIN_STATUS_APPROVED: PluginStatus
PLUGIN_STATUS_REJECTED: PluginStatus
PLUGIN_STATUS_UNLISTED: PluginStatus
PRIVACY_MODE_UNSPECIFIED: PrivacyMode
PRIVACY_MODE_NO_STORAGE: PrivacyMode
PRIVACY_MODE_NO_TRAINING: PrivacyMode
PRIVACY_MODE_USAGE_DATA_TRAINING_ALLOWED: PrivacyMode
PRIVACY_MODE_USAGE_CODEBASE_TRAINING_ALLOWED: PrivacyMode
PRIVATE_INFERENCE_ENABLEMENT_UNSPECIFIED: PrivateInferenceEnablement
PRIVATE_INFERENCE_ENABLEMENT_ENABLED: PrivateInferenceEnablement
PRIVATE_INFERENCE_ENABLEMENT_DISABLED: PrivateInferenceEnablement
PR_REVIEW_OPEN_DESTINATION_MODE_UNSPECIFIED: PrReviewOpenDestinationMode
PR_REVIEW_OPEN_DESTINATION_MODE_GITHUB: PrReviewOpenDestinationMode
PR_REVIEW_OPEN_DESTINATION_MODE_GRAPHITE: PrReviewOpenDestinationMode
PR_REVIEW_OPEN_DESTINATION_MODE_REVIEW_CURSOR: PrReviewOpenDestinationMode
PR_REVIEW_OPEN_SURFACE_MODE_UNSPECIFIED: PrReviewOpenSurfaceMode
PR_REVIEW_OPEN_SURFACE_MODE_IN_APP: PrReviewOpenSurfaceMode
PR_REVIEW_OPEN_SURFACE_MODE_EXTERNAL_BROWSER: PrReviewOpenSurfaceMode
PUBLIC_ARTIFACT_SHARING_MODE_UNSPECIFIED: PublicArtifactSharingMode
PUBLIC_ARTIFACT_SHARING_MODE_ALLOWED: PublicArtifactSharingMode
PUBLIC_ARTIFACT_SHARING_MODE_DISABLED: PublicArtifactSharingMode
SANDBOXING_MODE_UNSPECIFIED: SandboxingMode
SANDBOXING_MODE_ENABLED: SandboxingMode
SANDBOXING_MODE_DISABLED: SandboxingMode
SAND_BOX_MIGRATION_PHASE_UNSPECIFIED: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_BACKING_UP: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_CREATING: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_MOVING: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_CLEANING_UP: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_WIPING: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_DONE: SandBoxMigrationPhase
SAND_BOX_MIGRATION_PHASE_FAILED: SandBoxMigrationPhase
SANDBOX_READ_BOUNDARY_MODE_UNSPECIFIED: SandboxReadBoundaryMode
SANDBOX_READ_BOUNDARY_MODE_SYSTEM: SandboxReadBoundaryMode
SANDBOX_READ_BOUNDARY_MODE_WORKSPACE: SandboxReadBoundaryMode
SAND_BOX_RUN_STATE_UNSPECIFIED: SandBoxRunState
SAND_BOX_RUN_STATE_ABSENT: SandBoxRunState
SAND_BOX_RUN_STATE_HIBERNATED: SandBoxRunState
SAND_BOX_RUN_STATE_RUNNING: SandBoxRunState
SAND_BOX_RUN_STATE_STARTING: SandBoxRunState
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_UNSPECIFIED: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_PRECONDITION_FAILED: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_UPLOAD_NOT_FOUND: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_INVALID_PARTS: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_CHECKSUM_MISMATCH: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_TRANSIENT: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_INTERNAL: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_STORE_MULTIPART_OPERATION_FAILURE_CODE_RESTART_REQUIRED: SandBoxStoreMultipartOperationFailureCode
SAND_BOX_UPGRADE_SCHEDULE_STATE_UNSPECIFIED: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_SCHEDULED: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_CLAIMED: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_RUNNING: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_WAITING_FOR_IMAGE: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_COMPLETED: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_MISSED: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_FAILED: SandBoxUpgradeScheduleState
SAND_BOX_UPGRADE_SCHEDULE_STATE_CANCELLED: SandBoxUpgradeScheduleState
SAND_CREDENTIAL_DECISION_HARNESS_UNSPECIFIED: SandCredentialDecisionHarness
SAND_CREDENTIAL_DECISION_HARNESS_BOX: SandCredentialDecisionHarness
SAND_CREDENTIAL_DECISION_HARNESS_TEMPORAL: SandCredentialDecisionHarness
SAND_EGRESS_MODE_UNSPECIFIED: SandEgressMode
SAND_EGRESS_MODE_ALLOW_ALL: SandEgressMode
SAND_EGRESS_MODE_DEFAULT_WITH_NETWORK_SETTINGS: SandEgressMode
SAND_EGRESS_MODE_NETWORK_SETTINGS_ONLY: SandEgressMode
SAND_GROUP_ACCESS_MODE_UNSPECIFIED: SandGroupAccessMode
SAND_GROUP_ACCESS_MODE_ALL: SandGroupAccessMode
SAND_GROUP_ACCESS_MODE_LIMITED: SandGroupAccessMode
SAND_SETUP_MANIFEST_SCOPE_KIND_UNSPECIFIED: SandSetupManifestScopeKind
SAND_SETUP_MANIFEST_SCOPE_KIND_USER: SandSetupManifestScopeKind
SAND_SETUP_MANIFEST_SCOPE_KIND_TEAM: SandSetupManifestScopeKind
SAND_SETUP_MANIFEST_SCOPE_KIND_ORGANIZATION: SandSetupManifestScopeKind
SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_UNSPECIFIED: SetGrokBotAgentVisibilityOutcome
SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_UPDATED: SetGrokBotAgentVisibilityOutcome
SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_UNSUPPORTED_HARNESS: SetGrokBotAgentVisibilityOutcome
SET_GROK_BOT_AGENT_VISIBILITY_OUTCOME_NO_TEAM: SetGrokBotAgentVisibilityOutcome
SHARED_CONVERSATION_VISIBILITY_UNSPECIFIED: SharedConversationVisibility
SHARED_CONVERSATION_VISIBILITY_PRIVATE: SharedConversationVisibility
SHARED_CONVERSATION_VISIBILITY_TEAM: SharedConversationVisibility
SHARED_CONVERSATION_VISIBILITY_PUBLIC: SharedConversationVisibility
SPEND_GROUP_BY_CATEGORY_UNSPECIFIED: SpendGroupByCategory
SPEND_GROUP_BY_CATEGORY_MODEL: SpendGroupByCategory
SPEND_GROUP_BY_CATEGORY_USAGE_TYPE: SpendGroupByCategory
SPEND_TYPE_UNSPECIFIED: SpendType
SPEND_TYPE_ON_DEMAND: SpendType
SPEND_TYPE_INCLUDED: SpendType
SPEND_TYPE_ALL: SpendType
TEAM_FOLLOWUP_ENABLED_MODE_UNSPECIFIED: TeamFollowupEnabledMode
TEAM_FOLLOWUP_ENABLED_MODE_DISABLED: TeamFollowupEnabledMode
TEAM_FOLLOWUP_ENABLED_MODE_SERVICE_ACCOUNTS_ONLY: TeamFollowupEnabledMode
TEAM_FOLLOWUP_ENABLED_MODE_ALL: TeamFollowupEnabledMode
TEAM_MARKETPLACE_PLUGIN_INSTALL_MODE_OPTIONAL: TeamMarketplacePluginInstallMode
TEAM_MARKETPLACE_PLUGIN_INSTALL_MODE_DEFAULT: TeamMarketplacePluginInstallMode
TEAM_MARKETPLACE_PLUGIN_INSTALL_MODE_REQUIRED: TeamMarketplacePluginInstallMode
TEAM_MEMBER_BILLING_TIER_UNSPECIFIED: TeamMemberBillingTier
TEAM_MEMBER_BILLING_TIER_TIER_1000: TeamMemberBillingTier
TEAM_MEMBER_BILLING_TIER_TIER_2000: TeamMemberBillingTier
TEAM_ROLE_UNSPECIFIED: TeamRole
TEAM_ROLE_OWNER: TeamRole
TEAM_ROLE_MEMBER: TeamRole
TEAM_ROLE_FREE_OWNER: TeamRole
TEAM_ROLE_REMOVED: TeamRole

class AbortSandBoxStoreMultipartWritesRequest(_message.Message):
    __slots__ = ("uploads",)
    UPLOADS_FIELD_NUMBER: _ClassVar[int]
    uploads: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartWriteAbort]
    def __init__(self, uploads: _Optional[_Iterable[_Union[SandBoxStoreMultipartWriteAbort, _Mapping]]] = ...) -> None: ...

class AbortSandBoxStoreMultipartWritesResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartAbortResult]
    def __init__(self, results: _Optional[_Iterable[_Union[SandBoxStoreMultipartAbortResult, _Mapping]]] = ...) -> None: ...

class ActivateGrokBotTemplateVersionRequest(_message.Message):
    __slots__ = ("share_id", "version")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    version: int
    def __init__(self, share_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ActivateGrokBotTemplateVersionResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: GrokBotTemplate
    def __init__(self, template: _Optional[_Union[GrokBotTemplate, _Mapping]] = ...) -> None: ...

class AddGrokBotAgentSkillRequest(_message.Message):
    __slots__ = ("agent_id", "name", "description", "content")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    description: str
    content: str
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class AddGrokBotAgentSkillResponse(_message.Message):
    __slots__ = ("marketplace", "plugins", "skill")
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    skill: GrokBotAgentPluginSkill
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ..., skill: _Optional[_Union[GrokBotAgentPluginSkill, _Mapping]] = ...) -> None: ...

class AdminCommandDenylist(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rules: _Optional[_Iterable[str]] = ...) -> None: ...

class AdminDeleteGrokBotAgentRequest(_message.Message):
    __slots__ = ("agent_id", "team_id", "operator_email")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    team_id: int
    operator_email: str
    def __init__(self, agent_id: _Optional[str] = ..., team_id: _Optional[int] = ..., operator_email: _Optional[str] = ...) -> None: ...

class AdminDeleteGrokBotAgentResponse(_message.Message):
    __slots__ = ("id", "slack_app_removal")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_APP_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    slack_app_removal: GrokBotSlackAppRemoval
    def __init__(self, id: _Optional[str] = ..., slack_app_removal: _Optional[_Union[GrokBotSlackAppRemoval, _Mapping]] = ...) -> None: ...

class AdminForceDeleteGrokBotSessionBoxRequest(_message.Message):
    __slots__ = ("agent_id", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class AdminForceDeleteGrokBotSessionBoxResponse(_message.Message):
    __slots__ = ("deleted", "reason", "tenant_id", "deleted_pod_count", "revoked_credential_count", "stamp_cleared", "box_key")
    DELETED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_CREDENTIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    STAMP_CLEARED_FIELD_NUMBER: _ClassVar[int]
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    reason: str
    tenant_id: str
    deleted_pod_count: int
    revoked_credential_count: int
    stamp_cleared: bool
    box_key: str
    def __init__(self, deleted: bool = ..., reason: _Optional[str] = ..., tenant_id: _Optional[str] = ..., deleted_pod_count: _Optional[int] = ..., revoked_credential_count: _Optional[int] = ..., stamp_cleared: bool = ..., box_key: _Optional[str] = ...) -> None: ...

class AdminForceRecreateSandBoxRequest(_message.Message):
    __slots__ = ("auth_id", "flavor")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ...) -> None: ...

class AdminGetGrokBotAgentDefinitionRequest(_message.Message):
    __slots__ = ("agent_ref", "identity_only")
    AGENT_REF_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_ONLY_FIELD_NUMBER: _ClassVar[int]
    agent_ref: str
    identity_only: bool
    def __init__(self, agent_ref: _Optional[str] = ..., identity_only: bool = ...) -> None: ...

class AdminGetGrokBotAgentDefinitionResponse(_message.Message):
    __slots__ = ("identity", "definition", "refusal")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    identity: GrokBotAgentDefinitionIdentity
    definition: GrokBotAgentDefinition
    refusal: str
    def __init__(self, identity: _Optional[_Union[GrokBotAgentDefinitionIdentity, _Mapping]] = ..., definition: _Optional[_Union[GrokBotAgentDefinition, _Mapping]] = ..., refusal: _Optional[str] = ...) -> None: ...

class AdminGetGrokBotSessionBoxRequest(_message.Message):
    __slots__ = ("agent_id", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class AdminGetGrokBotSessionBoxResponse(_message.Message):
    __slots__ = ("box", "host", "store")
    BOX_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    box: GrokBotSessionBox
    host: AdminSandBoxHostStatusResponse
    store: AdminSandBoxStoreStatusResponse
    def __init__(self, box: _Optional[_Union[GrokBotSessionBox, _Mapping]] = ..., host: _Optional[_Union[AdminSandBoxHostStatusResponse, _Mapping]] = ..., store: _Optional[_Union[AdminSandBoxStoreStatusResponse, _Mapping]] = ...) -> None: ...

class AdminGetGrokBotTeamAgentSharedStateRequest(_message.Message):
    __slots__ = ("team_id", "agent_id", "identity_only")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_ONLY_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    agent_id: str
    identity_only: bool
    def __init__(self, team_id: _Optional[int] = ..., agent_id: _Optional[str] = ..., identity_only: bool = ...) -> None: ...

class AdminGetGrokBotTeamAgentSharedStateResponse(_message.Message):
    __slots__ = ("identity", "owner_email", "owner_multiplayer_gate", "shared_state", "refusal")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    OWNER_MULTIPLAYER_GATE_FIELD_NUMBER: _ClassVar[int]
    SHARED_STATE_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    identity: GrokBotAgentDefinitionIdentity
    owner_email: str
    owner_multiplayer_gate: bool
    shared_state: GrokBotTeamAgentSharedState
    refusal: str
    def __init__(self, identity: _Optional[_Union[GrokBotAgentDefinitionIdentity, _Mapping]] = ..., owner_email: _Optional[str] = ..., owner_multiplayer_gate: bool = ..., shared_state: _Optional[_Union[GrokBotTeamAgentSharedState, _Mapping]] = ..., refusal: _Optional[str] = ...) -> None: ...

class AdminGetSandAgentTranscriptPageRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "agent_id", "before_seq", "limit", "since_ms", "until_ms")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SINCE_MS_FIELD_NUMBER: _ClassVar[int]
    UNTIL_MS_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    agent_id: str
    before_seq: int
    limit: int
    since_ms: int
    until_ms: int
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., agent_id: _Optional[str] = ..., before_seq: _Optional[int] = ..., limit: _Optional[int] = ..., since_ms: _Optional[int] = ..., until_ms: _Optional[int] = ...) -> None: ...

class AdminGetSandAgentTranscriptPageResponse(_message.Message):
    __slots__ = ("reachable", "entries_json", "reason", "next_before_seq")
    REACHABLE_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_JSON_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    NEXT_BEFORE_SEQ_FIELD_NUMBER: _ClassVar[int]
    reachable: bool
    entries_json: str
    reason: str
    next_before_seq: int
    def __init__(self, reachable: bool = ..., entries_json: _Optional[str] = ..., reason: _Optional[str] = ..., next_before_seq: _Optional[int] = ...) -> None: ...

class AdminHibernateGrokBotSessionBoxRequest(_message.Message):
    __slots__ = ("agent_id", "session_id", "force")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    force: bool
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class AdminHibernateGrokBotSessionBoxResponse(_message.Message):
    __slots__ = ("started", "reason", "tenant_id", "box_key")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    started: bool
    reason: str
    tenant_id: str
    box_key: str
    def __init__(self, started: bool = ..., reason: _Optional[str] = ..., tenant_id: _Optional[str] = ..., box_key: _Optional[str] = ...) -> None: ...

class AdminHibernateSandBoxRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "force")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    force: bool
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., force: bool = ...) -> None: ...

class AdminHibernateSandBoxResponse(_message.Message):
    __slots__ = ("started", "reason")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    started: bool
    reason: str
    def __init__(self, started: bool = ..., reason: _Optional[str] = ...) -> None: ...

class AdminListGrokBotSessionBoxesRequest(_message.Message):
    __slots__ = ("auth_id", "agent_id", "page_cursor")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    agent_id: str
    page_cursor: str
    def __init__(self, auth_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., page_cursor: _Optional[str] = ...) -> None: ...

class AdminListGrokBotSessionBoxesResponse(_message.Message):
    __slots__ = ("boxes", "next_page_cursor")
    BOXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    boxes: _containers.RepeatedCompositeFieldContainer[GrokBotSessionBox]
    next_page_cursor: str
    def __init__(self, boxes: _Optional[_Iterable[_Union[GrokBotSessionBox, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...

class AdminListGrokBotTeamAgentsRequest(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    def __init__(self, team_id: _Optional[int] = ...) -> None: ...

class AdminListGrokBotTeamAgentsResponse(_message.Message):
    __slots__ = ("agents", "team_name", "truncated", "orphaned_slack_apps", "orphaned_slack_apps_truncated")
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    ORPHANED_SLACK_APPS_FIELD_NUMBER: _ClassVar[int]
    ORPHANED_SLACK_APPS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[GrokBotTeamAgent]
    team_name: str
    truncated: bool
    orphaned_slack_apps: _containers.RepeatedCompositeFieldContainer[GrokBotOrphanedSlackApp]
    orphaned_slack_apps_truncated: bool
    def __init__(self, agents: _Optional[_Iterable[_Union[GrokBotTeamAgent, _Mapping]]] = ..., team_name: _Optional[str] = ..., truncated: bool = ..., orphaned_slack_apps: _Optional[_Iterable[_Union[GrokBotOrphanedSlackApp, _Mapping]]] = ..., orphaned_slack_apps_truncated: bool = ...) -> None: ...

class AdminListSandAgentsRequest(_message.Message):
    __slots__ = ("auth_id", "flavor")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ...) -> None: ...

class AdminListSandAgentsResponse(_message.Message):
    __slots__ = ("reachable", "agents_json", "reason")
    REACHABLE_FIELD_NUMBER: _ClassVar[int]
    AGENTS_JSON_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    reachable: bool
    agents_json: str
    reason: str
    def __init__(self, reachable: bool = ..., agents_json: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class AdminListSandBoxStoreManifestVersionsRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "cursor", "max_versions", "parse_limit", "before_timestamp_ms")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    MAX_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PARSE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    cursor: str
    max_versions: int
    parse_limit: int
    before_timestamp_ms: int
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., cursor: _Optional[str] = ..., max_versions: _Optional[int] = ..., parse_limit: _Optional[int] = ..., before_timestamp_ms: _Optional[int] = ...) -> None: ...

class AdminListSandBoxStoreManifestVersionsResponse(_message.Message):
    __slots__ = ("store_id", "versions", "next_cursor", "truncated", "time_scan_capped")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    TIME_SCAN_CAPPED_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    versions: _containers.RepeatedCompositeFieldContainer[SandBoxStoreManifestVersion]
    next_cursor: str
    truncated: bool
    time_scan_capped: bool
    def __init__(self, store_id: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[SandBoxStoreManifestVersion, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., truncated: bool = ..., time_scan_capped: bool = ...) -> None: ...

class AdminReapGrokBotSessionBoxNowRequest(_message.Message):
    __slots__ = ("agent_id", "session_id", "dry_run")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    dry_run: bool
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ..., dry_run: bool = ...) -> None: ...

class AdminReapGrokBotSessionBoxNowResponse(_message.Message):
    __slots__ = ("result", "reason", "tenant_id", "dry_run", "pod_count", "deleted_pod_count", "revoked_credential_count", "deleted_object_count", "stamp_cleared", "box_key")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_CREDENTIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    STAMP_CLEARED_FIELD_NUMBER: _ClassVar[int]
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    result: str
    reason: str
    tenant_id: str
    dry_run: bool
    pod_count: int
    deleted_pod_count: int
    revoked_credential_count: int
    deleted_object_count: int
    stamp_cleared: bool
    box_key: str
    def __init__(self, result: _Optional[str] = ..., reason: _Optional[str] = ..., tenant_id: _Optional[str] = ..., dry_run: bool = ..., pod_count: _Optional[int] = ..., deleted_pod_count: _Optional[int] = ..., revoked_credential_count: _Optional[int] = ..., deleted_object_count: _Optional[int] = ..., stamp_cleared: bool = ..., box_key: _Optional[str] = ...) -> None: ...

class AdminRecreateSandBoxRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "preserve_data", "force")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_DATA_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    preserve_data: bool
    force: bool
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., preserve_data: bool = ..., force: bool = ...) -> None: ...

class AdminRestoreSandBoxStoreSnapshotRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "manifest_version_id", "expected_entry_count")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    manifest_version_id: str
    expected_entry_count: int
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., manifest_version_id: _Optional[str] = ..., expected_entry_count: _Optional[int] = ...) -> None: ...

class AdminRestoreSandBoxStoreSnapshotResponse(_message.Message):
    __slots__ = ("started", "reason", "operation_id", "current_entry_count", "target_entry_count")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    started: bool
    reason: str
    operation_id: str
    current_entry_count: int
    target_entry_count: int
    def __init__(self, started: bool = ..., reason: _Optional[str] = ..., operation_id: _Optional[str] = ..., current_entry_count: _Optional[int] = ..., target_entry_count: _Optional[int] = ...) -> None: ...

class AdminRetryGrokBotSlackAppRemovalRequest(_message.Message):
    __slots__ = ("agent_id", "team_id", "operator_email")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    team_id: int
    operator_email: str
    def __init__(self, agent_id: _Optional[str] = ..., team_id: _Optional[int] = ..., operator_email: _Optional[str] = ...) -> None: ...

class AdminRetryGrokBotSlackAppRemovalResponse(_message.Message):
    __slots__ = ("slack_app_removal",)
    SLACK_APP_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    slack_app_removal: GrokBotSlackAppRemoval
    def __init__(self, slack_app_removal: _Optional[_Union[GrokBotSlackAppRemoval, _Mapping]] = ...) -> None: ...

class AdminSandBoxHostStatusRequest(_message.Message):
    __slots__ = ("auth_id", "flavor")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ...) -> None: ...

class AdminSandBoxHostStatusResponse(_message.Message):
    __slots__ = ("gateway_reachable", "host_version", "host_update_available", "latest_host_version", "is_busy", "last_busy_at_ms")
    GATEWAY_REACHABLE_FIELD_NUMBER: _ClassVar[int]
    HOST_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOST_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    LATEST_HOST_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_BUSY_FIELD_NUMBER: _ClassVar[int]
    LAST_BUSY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    gateway_reachable: bool
    host_version: str
    host_update_available: bool
    latest_host_version: str
    is_busy: bool
    last_busy_at_ms: int
    def __init__(self, gateway_reachable: bool = ..., host_version: _Optional[str] = ..., host_update_available: bool = ..., latest_host_version: _Optional[str] = ..., is_busy: bool = ..., last_busy_at_ms: _Optional[int] = ...) -> None: ...

class AdminSandBoxStoreStatusRequest(_message.Message):
    __slots__ = ("auth_id", "flavor")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ...) -> None: ...

class AdminSandBoxStoreStatusResponse(_message.Message):
    __slots__ = ("durable", "entry_count", "total_bytes", "last_snapshot_at_ms", "reachable")
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_SNAPSHOT_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REACHABLE_FIELD_NUMBER: _ClassVar[int]
    durable: bool
    entry_count: int
    total_bytes: int
    last_snapshot_at_ms: int
    reachable: bool
    def __init__(self, durable: bool = ..., entry_count: _Optional[int] = ..., total_bytes: _Optional[int] = ..., last_snapshot_at_ms: _Optional[int] = ..., reachable: bool = ...) -> None: ...

class AdminSnapshotSandBoxStoreRequest(_message.Message):
    __slots__ = ("auth_id", "flavor")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ...) -> None: ...

class AdminSnapshotSandBoxStoreResponse(_message.Message):
    __slots__ = ("ok", "manifest_entries", "files_uploaded", "reason")
    OK_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    FILES_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    manifest_entries: int
    files_uploaded: int
    reason: str
    def __init__(self, ok: bool = ..., manifest_entries: _Optional[int] = ..., files_uploaded: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class AdminUpdateSandBoxHostRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "force")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    force: bool
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., force: bool = ...) -> None: ...

class AdminUpdateSandBoxHostResponse(_message.Message):
    __slots__ = ("started", "reason", "version")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    started: bool
    reason: str
    version: str
    def __init__(self, started: bool = ..., reason: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class AdminWatchSandBoxMigrationRequest(_message.Message):
    __slots__ = ("auth_id", "flavor", "from_offset_key")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    FROM_OFFSET_KEY_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    flavor: str
    from_offset_key: str
    def __init__(self, auth_id: _Optional[str] = ..., flavor: _Optional[str] = ..., from_offset_key: _Optional[str] = ...) -> None: ...

class AllowedMCPConfiguration(_message.Message):
    __slots__ = ("disable_all", "allowed_mcp_servers", "require_mcp_servers_in_team_network_allowlist", "allow_user_override_mcp_servers", "denied_mcp_servers", "enable_cursor_cloud_mcp")
    DISABLE_ALL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_MCP_SERVERS_IN_TEAM_NETWORK_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    ALLOW_USER_OVERRIDE_MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DENIED_MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CURSOR_CLOUD_MCP_FIELD_NUMBER: _ClassVar[int]
    disable_all: bool
    allowed_mcp_servers: _containers.RepeatedCompositeFieldContainer[AllowedMCPServer]
    require_mcp_servers_in_team_network_allowlist: bool
    allow_user_override_mcp_servers: bool
    denied_mcp_servers: _containers.RepeatedCompositeFieldContainer[AllowedMCPServer]
    enable_cursor_cloud_mcp: bool
    def __init__(self, disable_all: bool = ..., allowed_mcp_servers: _Optional[_Iterable[_Union[AllowedMCPServer, _Mapping]]] = ..., require_mcp_servers_in_team_network_allowlist: bool = ..., allow_user_override_mcp_servers: bool = ..., denied_mcp_servers: _Optional[_Iterable[_Union[AllowedMCPServer, _Mapping]]] = ..., enable_cursor_cloud_mcp: bool = ...) -> None: ...

class AllowedMCPServer(_message.Message):
    __slots__ = ("command", "server_url", "name", "network_allowlist", "tool_allowlist", "network_mode", "tool_allowlist_mode")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SERVER_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    TOOL_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    NETWORK_MODE_FIELD_NUMBER: _ClassVar[int]
    TOOL_ALLOWLIST_MODE_FIELD_NUMBER: _ClassVar[int]
    command: str
    server_url: str
    name: str
    network_allowlist: _containers.RepeatedScalarFieldContainer[str]
    tool_allowlist: _containers.RepeatedScalarFieldContainer[str]
    network_mode: str
    tool_allowlist_mode: str
    def __init__(self, command: _Optional[str] = ..., server_url: _Optional[str] = ..., name: _Optional[str] = ..., network_allowlist: _Optional[_Iterable[str]] = ..., tool_allowlist: _Optional[_Iterable[str]] = ..., network_mode: _Optional[str] = ..., tool_allowlist_mode: _Optional[str] = ...) -> None: ...

class AnalyticsContext(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: ClientInfo
    def __init__(self, client: _Optional[_Union[ClientInfo, _Mapping]] = ...) -> None: ...

class AnalyticsEvent(_message.Message):
    __slots__ = ("event_name", "event_data", "timestamp")
    class EventDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EventData
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EventData, _Mapping]] = ...) -> None: ...
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_data: _containers.MessageMap[str, EventData]
    timestamp: int
    def __init__(self, event_name: _Optional[str] = ..., event_data: _Optional[_Mapping[str, EventData]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ApproveOnePasswordCredentialRequestRequest(_message.Message):
    __slots__ = ("entry_id", "agent_id", "credential_id", "connection_id", "catalog_revision", "target_site", "harness")
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_REVISION_FIELD_NUMBER: _ClassVar[int]
    TARGET_SITE_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    agent_id: str
    credential_id: str
    connection_id: str
    catalog_revision: str
    target_site: str
    harness: SandCredentialDecisionHarness
    def __init__(self, entry_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., credential_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., catalog_revision: _Optional[str] = ..., target_site: _Optional[str] = ..., harness: _Optional[_Union[SandCredentialDecisionHarness, str]] = ...) -> None: ...

class AttributionControls(_message.Message):
    __slots__ = ("disable_attribution",)
    DISABLE_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    disable_attribution: bool
    def __init__(self, disable_attribution: bool = ...) -> None: ...

class AutoReviewInstructions(_message.Message):
    __slots__ = ("allow_instructions", "block_instructions")
    ALLOW_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    allow_instructions: _containers.RepeatedScalarFieldContainer[str]
    block_instructions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allow_instructions: _Optional[_Iterable[str]] = ..., block_instructions: _Optional[_Iterable[str]] = ...) -> None: ...

class AutoReviewRunModeReset(_message.Message):
    __slots__ = ("issued_at_ms",)
    ISSUED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    issued_at_ms: int
    def __init__(self, issued_at_ms: _Optional[int] = ...) -> None: ...

class AutoRunControls(_message.Message):
    __slots__ = ("enabled", "allowed", "blocked", "disable_mcp_auto_run", "delete_file_protection", "enable_run_everything", "mcp_tool_allowlist", "sandboxing_controls", "browser_protection", "enable_smart_auto", "enable_allowlist_mode", "admin_command_denylist")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MCP_AUTO_RUN_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILE_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RUN_EVERYTHING_FIELD_NUMBER: _ClassVar[int]
    MCP_TOOL_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    SANDBOXING_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    BROWSER_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMART_AUTO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ALLOWLIST_MODE_FIELD_NUMBER: _ClassVar[int]
    ADMIN_COMMAND_DENYLIST_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    allowed: _containers.RepeatedScalarFieldContainer[str]
    blocked: _containers.RepeatedScalarFieldContainer[str]
    disable_mcp_auto_run: bool
    delete_file_protection: bool
    enable_run_everything: bool
    mcp_tool_allowlist: _containers.RepeatedScalarFieldContainer[str]
    sandboxing_controls: AutoRunSandboxingControls
    browser_protection: bool
    enable_smart_auto: bool
    enable_allowlist_mode: bool
    admin_command_denylist: AdminCommandDenylist
    def __init__(self, enabled: bool = ..., allowed: _Optional[_Iterable[str]] = ..., blocked: _Optional[_Iterable[str]] = ..., disable_mcp_auto_run: bool = ..., delete_file_protection: bool = ..., enable_run_everything: bool = ..., mcp_tool_allowlist: _Optional[_Iterable[str]] = ..., sandboxing_controls: _Optional[_Union[AutoRunSandboxingControls, _Mapping]] = ..., browser_protection: bool = ..., enable_smart_auto: bool = ..., enable_allowlist_mode: bool = ..., admin_command_denylist: _Optional[_Union[AdminCommandDenylist, _Mapping]] = ...) -> None: ...

class AutoRunSandboxingControls(_message.Message):
    __slots__ = ("sandboxing", "sandbox_networking", "sandbox_git", "sandbox_read_boundary", "sandbox_read_allowlist_paths")
    SANDBOXING_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NETWORKING_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_GIT_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_READ_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_READ_ALLOWLIST_PATHS_FIELD_NUMBER: _ClassVar[int]
    sandboxing: SandboxingMode
    sandbox_networking: NetworkingMode
    sandbox_git: GitMode
    sandbox_read_boundary: SandboxReadBoundaryMode
    sandbox_read_allowlist_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sandboxing: _Optional[_Union[SandboxingMode, str]] = ..., sandbox_networking: _Optional[_Union[NetworkingMode, str]] = ..., sandbox_git: _Optional[_Union[GitMode, str]] = ..., sandbox_read_boundary: _Optional[_Union[SandboxReadBoundaryMode, str]] = ..., sandbox_read_allowlist_paths: _Optional[_Iterable[str]] = ...) -> None: ...

class AvailableModelsRequest(_message.Message):
    __slots__ = ("is_nightly", "include_long_context_models", "exclude_max_named_models", "additional_model_names", "use_model_parameters", "include_hidden_models", "do_not_use_markdown", "variants_will_be_shown_in_exploded_list", "for_automations", "scope", "use_react_model_picker", "use_cloud_agent_effort_modes", "admin_settings_group_public_id", "byok_enabled", "use_parameterized_automations_models", "expected_scope")
    IS_NIGHTLY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LONG_CONTEXT_MODELS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_MAX_NAMED_MODELS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_MODEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    USE_MODEL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HIDDEN_MODELS_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_USE_MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_WILL_BE_SHOWN_IN_EXPLODED_LIST_FIELD_NUMBER: _ClassVar[int]
    FOR_AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    USE_REACT_MODEL_PICKER_FIELD_NUMBER: _ClassVar[int]
    USE_CLOUD_AGENT_EFFORT_MODES_FIELD_NUMBER: _ClassVar[int]
    ADMIN_SETTINGS_GROUP_PUBLIC_ID_FIELD_NUMBER: _ClassVar[int]
    BYOK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_PARAMETERIZED_AUTOMATIONS_MODELS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SCOPE_FIELD_NUMBER: _ClassVar[int]
    is_nightly: bool
    include_long_context_models: bool
    exclude_max_named_models: bool
    additional_model_names: _containers.RepeatedScalarFieldContainer[str]
    use_model_parameters: bool
    include_hidden_models: bool
    do_not_use_markdown: bool
    variants_will_be_shown_in_exploded_list: bool
    for_automations: bool
    scope: AvailableModelsScope
    use_react_model_picker: bool
    use_cloud_agent_effort_modes: bool
    admin_settings_group_public_id: str
    byok_enabled: bool
    use_parameterized_automations_models: bool
    expected_scope: CloudAgentRequestScope
    def __init__(self, is_nightly: bool = ..., include_long_context_models: bool = ..., exclude_max_named_models: bool = ..., additional_model_names: _Optional[_Iterable[str]] = ..., use_model_parameters: bool = ..., include_hidden_models: bool = ..., do_not_use_markdown: bool = ..., variants_will_be_shown_in_exploded_list: bool = ..., for_automations: bool = ..., scope: _Optional[_Union[AvailableModelsScope, str]] = ..., use_react_model_picker: bool = ..., use_cloud_agent_effort_modes: bool = ..., admin_settings_group_public_id: _Optional[str] = ..., byok_enabled: bool = ..., use_parameterized_automations_models: bool = ..., expected_scope: _Optional[_Union[CloudAgentRequestScope, _Mapping]] = ...) -> None: ...

class AvailableModelsResponse(_message.Message):
    __slots__ = ("model_names", "models", "composer_model_config", "cmd_k_model_config", "background_composer_model_config", "plan_execution_model_config", "spec_model_config", "deep_search_model_config", "quick_agent_model_config", "use_model_parameters", "disable_unused_models_after_n_hours", "upgrade_unchanged_models_after_n_hours", "display_configuration", "subagent_model_configs", "experimental_model_id", "experimental_model_display_name", "nudge_new_chats_to_auto_optimize_for")
    class DegradationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEGRADATION_STATUS_UNSPECIFIED: _ClassVar[AvailableModelsResponse.DegradationStatus]
        DEGRADATION_STATUS_DEGRADED: _ClassVar[AvailableModelsResponse.DegradationStatus]
        DEGRADATION_STATUS_DISABLED: _ClassVar[AvailableModelsResponse.DegradationStatus]
    DEGRADATION_STATUS_UNSPECIFIED: AvailableModelsResponse.DegradationStatus
    DEGRADATION_STATUS_DEGRADED: AvailableModelsResponse.DegradationStatus
    DEGRADATION_STATUS_DISABLED: AvailableModelsResponse.DegradationStatus
    class ModelVendorId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_VENDOR_ID_UNSPECIFIED: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_ANTHROPIC: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_OPENAI: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_GOOGLE: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_XAI: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_MOONSHOT: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_CURSOR: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_NVIDIA: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_ZAI: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_META: _ClassVar[AvailableModelsResponse.ModelVendorId]
        MODEL_VENDOR_ID_DEEPSEEK: _ClassVar[AvailableModelsResponse.ModelVendorId]
    MODEL_VENDOR_ID_UNSPECIFIED: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_ANTHROPIC: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_OPENAI: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_GOOGLE: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_XAI: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_MOONSHOT: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_CURSOR: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_NVIDIA: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_ZAI: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_META: AvailableModelsResponse.ModelVendorId
    MODEL_VENDOR_ID_DEEPSEEK: AvailableModelsResponse.ModelVendorId
    class SubagentModelConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AvailableModelsResponse.FeatureModelConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ...) -> None: ...
    class AvailableModel(_message.Message):
        __slots__ = ("name", "default_on", "is_long_context_only", "is_chat_only", "supports_agent", "degradation_status", "price", "tooltip_data", "supports_thinking", "supports_images", "supports_auto_context", "auto_context_max_tokens", "auto_context_extended_max_tokens", "supports_max_mode", "context_token_limit", "context_token_limit_for_max_mode", "client_display_name", "server_model_name", "supports_non_max_mode", "tooltip_data_for_max_mode", "is_recommended_for_background_composer", "supports_plan_mode", "is_user_added", "inputbox_short_model_name", "supports_sandboxing", "supports_cmd_k", "only_supports_cmd_k", "background_composer_sort_order", "parameter_definitions", "variants", "cloud_agent_effort_mode", "cloud_migrate_to_model", "upgrade_model_id", "is_hidden", "legacy_slugs", "id_aliases", "named_model_section_index", "tagline", "visible_in_routed_model_view", "vendor_name", "vendor", "default_disabled_in_admin_allowlist", "cloud_agent_effort_modes", "supports_smart_mode_classifier", "requires_data_retention", "reason_for_zdr_consent_block", "model_picker_badges")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_ON_FIELD_NUMBER: _ClassVar[int]
        IS_LONG_CONTEXT_ONLY_FIELD_NUMBER: _ClassVar[int]
        IS_CHAT_ONLY_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_AGENT_FIELD_NUMBER: _ClassVar[int]
        DEGRADATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        TOOLTIP_DATA_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_THINKING_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_IMAGES_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_AUTO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        AUTO_CONTEXT_MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
        AUTO_CONTEXT_EXTENDED_MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_MAX_MODE_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_TOKEN_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_TOKEN_LIMIT_FOR_MAX_MODE_FIELD_NUMBER: _ClassVar[int]
        CLIENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVER_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_NON_MAX_MODE_FIELD_NUMBER: _ClassVar[int]
        TOOLTIP_DATA_FOR_MAX_MODE_FIELD_NUMBER: _ClassVar[int]
        IS_RECOMMENDED_FOR_BACKGROUND_COMPOSER_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_PLAN_MODE_FIELD_NUMBER: _ClassVar[int]
        IS_USER_ADDED_FIELD_NUMBER: _ClassVar[int]
        INPUTBOX_SHORT_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_SANDBOXING_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_CMD_K_FIELD_NUMBER: _ClassVar[int]
        ONLY_SUPPORTS_CMD_K_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_COMPOSER_SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
        VARIANTS_FIELD_NUMBER: _ClassVar[int]
        CLOUD_AGENT_EFFORT_MODE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_MIGRATE_TO_MODEL_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
        LEGACY_SLUGS_FIELD_NUMBER: _ClassVar[int]
        ID_ALIASES_FIELD_NUMBER: _ClassVar[int]
        NAMED_MODEL_SECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
        TAGLINE_FIELD_NUMBER: _ClassVar[int]
        VISIBLE_IN_ROUTED_MODEL_VIEW_FIELD_NUMBER: _ClassVar[int]
        VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_DISABLED_IN_ADMIN_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
        CLOUD_AGENT_EFFORT_MODES_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_SMART_MODE_CLASSIFIER_FIELD_NUMBER: _ClassVar[int]
        REQUIRES_DATA_RETENTION_FIELD_NUMBER: _ClassVar[int]
        REASON_FOR_ZDR_CONSENT_BLOCK_FIELD_NUMBER: _ClassVar[int]
        MODEL_PICKER_BADGES_FIELD_NUMBER: _ClassVar[int]
        name: str
        default_on: bool
        is_long_context_only: bool
        is_chat_only: bool
        supports_agent: bool
        degradation_status: AvailableModelsResponse.DegradationStatus
        price: float
        tooltip_data: AvailableModelsResponse.TooltipData
        supports_thinking: bool
        supports_images: bool
        supports_auto_context: bool
        auto_context_max_tokens: int
        auto_context_extended_max_tokens: int
        supports_max_mode: bool
        context_token_limit: int
        context_token_limit_for_max_mode: int
        client_display_name: str
        server_model_name: str
        supports_non_max_mode: bool
        tooltip_data_for_max_mode: AvailableModelsResponse.TooltipData
        is_recommended_for_background_composer: bool
        supports_plan_mode: bool
        is_user_added: bool
        inputbox_short_model_name: str
        supports_sandboxing: bool
        supports_cmd_k: bool
        only_supports_cmd_k: bool
        background_composer_sort_order: int
        parameter_definitions: _containers.RepeatedCompositeFieldContainer[ModelParameterDefinition]
        variants: _containers.RepeatedCompositeFieldContainer[AvailableModelsResponse.ModelVariantConfig]
        cloud_agent_effort_mode: CloudAgentEffortMode
        cloud_migrate_to_model: str
        upgrade_model_id: str
        is_hidden: bool
        legacy_slugs: _containers.RepeatedScalarFieldContainer[str]
        id_aliases: _containers.RepeatedScalarFieldContainer[str]
        named_model_section_index: int
        tagline: str
        visible_in_routed_model_view: bool
        vendor_name: str
        vendor: AvailableModelsResponse.ModelVendor
        default_disabled_in_admin_allowlist: bool
        cloud_agent_effort_modes: _containers.RepeatedScalarFieldContainer[CloudAgentEffortMode]
        supports_smart_mode_classifier: bool
        requires_data_retention: bool
        reason_for_zdr_consent_block: str
        model_picker_badges: _containers.RepeatedCompositeFieldContainer[AvailableModelsResponse.ModelPickerBadge]
        def __init__(self, name: _Optional[str] = ..., default_on: bool = ..., is_long_context_only: bool = ..., is_chat_only: bool = ..., supports_agent: bool = ..., degradation_status: _Optional[_Union[AvailableModelsResponse.DegradationStatus, str]] = ..., price: _Optional[float] = ..., tooltip_data: _Optional[_Union[AvailableModelsResponse.TooltipData, _Mapping]] = ..., supports_thinking: bool = ..., supports_images: bool = ..., supports_auto_context: bool = ..., auto_context_max_tokens: _Optional[int] = ..., auto_context_extended_max_tokens: _Optional[int] = ..., supports_max_mode: bool = ..., context_token_limit: _Optional[int] = ..., context_token_limit_for_max_mode: _Optional[int] = ..., client_display_name: _Optional[str] = ..., server_model_name: _Optional[str] = ..., supports_non_max_mode: bool = ..., tooltip_data_for_max_mode: _Optional[_Union[AvailableModelsResponse.TooltipData, _Mapping]] = ..., is_recommended_for_background_composer: bool = ..., supports_plan_mode: bool = ..., is_user_added: bool = ..., inputbox_short_model_name: _Optional[str] = ..., supports_sandboxing: bool = ..., supports_cmd_k: bool = ..., only_supports_cmd_k: bool = ..., background_composer_sort_order: _Optional[int] = ..., parameter_definitions: _Optional[_Iterable[_Union[ModelParameterDefinition, _Mapping]]] = ..., variants: _Optional[_Iterable[_Union[AvailableModelsResponse.ModelVariantConfig, _Mapping]]] = ..., cloud_agent_effort_mode: _Optional[_Union[CloudAgentEffortMode, str]] = ..., cloud_migrate_to_model: _Optional[str] = ..., upgrade_model_id: _Optional[str] = ..., is_hidden: bool = ..., legacy_slugs: _Optional[_Iterable[str]] = ..., id_aliases: _Optional[_Iterable[str]] = ..., named_model_section_index: _Optional[int] = ..., tagline: _Optional[str] = ..., visible_in_routed_model_view: bool = ..., vendor_name: _Optional[str] = ..., vendor: _Optional[_Union[AvailableModelsResponse.ModelVendor, _Mapping]] = ..., default_disabled_in_admin_allowlist: bool = ..., cloud_agent_effort_modes: _Optional[_Iterable[_Union[CloudAgentEffortMode, str]]] = ..., supports_smart_mode_classifier: bool = ..., requires_data_retention: bool = ..., reason_for_zdr_consent_block: _Optional[str] = ..., model_picker_badges: _Optional[_Iterable[_Union[AvailableModelsResponse.ModelPickerBadge, _Mapping]]] = ...) -> None: ...
    class ConfirmationDialogue(_message.Message):
        __slots__ = ("title", "body", "key", "blocks_submission", "presentation")
        class Presentation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRESENTATION_UNSPECIFIED: _ClassVar[AvailableModelsResponse.ConfirmationDialogue.Presentation]
            PRESENTATION_POST_PICKER_WARNING: _ClassVar[AvailableModelsResponse.ConfirmationDialogue.Presentation]
        PRESENTATION_UNSPECIFIED: AvailableModelsResponse.ConfirmationDialogue.Presentation
        PRESENTATION_POST_PICKER_WARNING: AvailableModelsResponse.ConfirmationDialogue.Presentation
        TITLE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        BLOCKS_SUBMISSION_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        title: str
        body: str
        key: str
        blocks_submission: bool
        presentation: AvailableModelsResponse.ConfirmationDialogue.Presentation
        def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., key: _Optional[str] = ..., blocks_submission: bool = ..., presentation: _Optional[_Union[AvailableModelsResponse.ConfirmationDialogue.Presentation, str]] = ...) -> None: ...
    class FeatureModelConfig(_message.Message):
        __slots__ = ("default_model", "fallback_models", "best_of_n_default_models")
        DEFAULT_MODEL_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_MODELS_FIELD_NUMBER: _ClassVar[int]
        BEST_OF_N_DEFAULT_MODELS_FIELD_NUMBER: _ClassVar[int]
        default_model: str
        fallback_models: _containers.RepeatedScalarFieldContainer[str]
        best_of_n_default_models: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, default_model: _Optional[str] = ..., fallback_models: _Optional[_Iterable[str]] = ..., best_of_n_default_models: _Optional[_Iterable[str]] = ...) -> None: ...
    class ModelPickerBadge(_message.Message):
        __slots__ = ("label", "variant", "dismiss_on_selection")
        class Variant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VARIANT_UNSPECIFIED: _ClassVar[AvailableModelsResponse.ModelPickerBadge.Variant]
            VARIANT_ACCENT: _ClassVar[AvailableModelsResponse.ModelPickerBadge.Variant]
            VARIANT_NEUTRAL: _ClassVar[AvailableModelsResponse.ModelPickerBadge.Variant]
            VARIANT_SUCCESS: _ClassVar[AvailableModelsResponse.ModelPickerBadge.Variant]
            VARIANT_WARN: _ClassVar[AvailableModelsResponse.ModelPickerBadge.Variant]
            VARIANT_DANGER: _ClassVar[AvailableModelsResponse.ModelPickerBadge.Variant]
        VARIANT_UNSPECIFIED: AvailableModelsResponse.ModelPickerBadge.Variant
        VARIANT_ACCENT: AvailableModelsResponse.ModelPickerBadge.Variant
        VARIANT_NEUTRAL: AvailableModelsResponse.ModelPickerBadge.Variant
        VARIANT_SUCCESS: AvailableModelsResponse.ModelPickerBadge.Variant
        VARIANT_WARN: AvailableModelsResponse.ModelPickerBadge.Variant
        VARIANT_DANGER: AvailableModelsResponse.ModelPickerBadge.Variant
        LABEL_FIELD_NUMBER: _ClassVar[int]
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        DISMISS_ON_SELECTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        variant: AvailableModelsResponse.ModelPickerBadge.Variant
        dismiss_on_selection: bool
        def __init__(self, label: _Optional[str] = ..., variant: _Optional[_Union[AvailableModelsResponse.ModelPickerBadge.Variant, str]] = ..., dismiss_on_selection: bool = ...) -> None: ...
    class ModelPickerDisplayConfiguration(_message.Message):
        __slots__ = ("routed_model_view_config", "named_models_view_config", "hide_search_bar", "hide_add_models", "model_selection_restriction_message")
        class NamedModelsViewConfig(_message.Message):
            __slots__ = ("named_view_to_routed_model_view_toggle", "named_view_to_routed_model_view_no_button", "named_view_to_routed_model_view_button")
            class NamedViewToRoutedModelViewButton(_message.Message):
                __slots__ = ("markdown",)
                MARKDOWN_FIELD_NUMBER: _ClassVar[int]
                markdown: str
                def __init__(self, markdown: _Optional[str] = ...) -> None: ...
            class NamedViewToRoutedModelViewNoButton(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class NamedViewToRoutedModelViewToggle(_message.Message):
                __slots__ = ("markdown",)
                MARKDOWN_FIELD_NUMBER: _ClassVar[int]
                markdown: str
                def __init__(self, markdown: _Optional[str] = ...) -> None: ...
            NAMED_VIEW_TO_ROUTED_MODEL_VIEW_TOGGLE_FIELD_NUMBER: _ClassVar[int]
            NAMED_VIEW_TO_ROUTED_MODEL_VIEW_NO_BUTTON_FIELD_NUMBER: _ClassVar[int]
            NAMED_VIEW_TO_ROUTED_MODEL_VIEW_BUTTON_FIELD_NUMBER: _ClassVar[int]
            named_view_to_routed_model_view_toggle: AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig.NamedViewToRoutedModelViewToggle
            named_view_to_routed_model_view_no_button: AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig.NamedViewToRoutedModelViewNoButton
            named_view_to_routed_model_view_button: AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig.NamedViewToRoutedModelViewButton
            def __init__(self, named_view_to_routed_model_view_toggle: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig.NamedViewToRoutedModelViewToggle, _Mapping]] = ..., named_view_to_routed_model_view_no_button: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig.NamedViewToRoutedModelViewNoButton, _Mapping]] = ..., named_view_to_routed_model_view_button: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig.NamedViewToRoutedModelViewButton, _Mapping]] = ...) -> None: ...
        class RoutedModelViewConfig(_message.Message):
            __slots__ = ("title", "routed_model_view_to_named_view_toggle", "routed_model_view_to_named_view_button", "hide_search_bar", "hide_routed_model_view")
            class RoutedModelViewToNamedViewButton(_message.Message):
                __slots__ = ("markdown",)
                MARKDOWN_FIELD_NUMBER: _ClassVar[int]
                markdown: str
                def __init__(self, markdown: _Optional[str] = ...) -> None: ...
            class RoutedModelViewToNamedViewToggle(_message.Message):
                __slots__ = ("title_markdown", "subtitle", "set_to_last_named_model")
                TITLE_MARKDOWN_FIELD_NUMBER: _ClassVar[int]
                SUBTITLE_FIELD_NUMBER: _ClassVar[int]
                SET_TO_LAST_NAMED_MODEL_FIELD_NUMBER: _ClassVar[int]
                title_markdown: str
                subtitle: str
                set_to_last_named_model: bool
                def __init__(self, title_markdown: _Optional[str] = ..., subtitle: _Optional[str] = ..., set_to_last_named_model: bool = ...) -> None: ...
            TITLE_FIELD_NUMBER: _ClassVar[int]
            ROUTED_MODEL_VIEW_TO_NAMED_VIEW_TOGGLE_FIELD_NUMBER: _ClassVar[int]
            ROUTED_MODEL_VIEW_TO_NAMED_VIEW_BUTTON_FIELD_NUMBER: _ClassVar[int]
            HIDE_SEARCH_BAR_FIELD_NUMBER: _ClassVar[int]
            HIDE_ROUTED_MODEL_VIEW_FIELD_NUMBER: _ClassVar[int]
            title: str
            routed_model_view_to_named_view_toggle: AvailableModelsResponse.ModelPickerDisplayConfiguration.RoutedModelViewConfig.RoutedModelViewToNamedViewToggle
            routed_model_view_to_named_view_button: AvailableModelsResponse.ModelPickerDisplayConfiguration.RoutedModelViewConfig.RoutedModelViewToNamedViewButton
            hide_search_bar: bool
            hide_routed_model_view: bool
            def __init__(self, title: _Optional[str] = ..., routed_model_view_to_named_view_toggle: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.RoutedModelViewConfig.RoutedModelViewToNamedViewToggle, _Mapping]] = ..., routed_model_view_to_named_view_button: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.RoutedModelViewConfig.RoutedModelViewToNamedViewButton, _Mapping]] = ..., hide_search_bar: bool = ..., hide_routed_model_view: bool = ...) -> None: ...
        ROUTED_MODEL_VIEW_CONFIG_FIELD_NUMBER: _ClassVar[int]
        NAMED_MODELS_VIEW_CONFIG_FIELD_NUMBER: _ClassVar[int]
        HIDE_SEARCH_BAR_FIELD_NUMBER: _ClassVar[int]
        HIDE_ADD_MODELS_FIELD_NUMBER: _ClassVar[int]
        MODEL_SELECTION_RESTRICTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        routed_model_view_config: AvailableModelsResponse.ModelPickerDisplayConfiguration.RoutedModelViewConfig
        named_models_view_config: AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig
        hide_search_bar: bool
        hide_add_models: bool
        model_selection_restriction_message: str
        def __init__(self, routed_model_view_config: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.RoutedModelViewConfig, _Mapping]] = ..., named_models_view_config: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration.NamedModelsViewConfig, _Mapping]] = ..., hide_search_bar: bool = ..., hide_add_models: bool = ..., model_selection_restriction_message: _Optional[str] = ...) -> None: ...
    class ModelVariantConfig(_message.Message):
        __slots__ = ("parameter_values", "display_name", "is_max_mode", "is_default_max_config", "is_default_non_max_config", "tooltip_data", "tagline", "display_name_outside_picker", "variant_string_representation", "confirmation_dialogue", "legacy_slug")
        PARAMETER_VALUES_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_MAX_MODE_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_MAX_CONFIG_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_NON_MAX_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TOOLTIP_DATA_FIELD_NUMBER: _ClassVar[int]
        TAGLINE_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_OUTSIDE_PICKER_FIELD_NUMBER: _ClassVar[int]
        VARIANT_STRING_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
        CONFIRMATION_DIALOGUE_FIELD_NUMBER: _ClassVar[int]
        LEGACY_SLUG_FIELD_NUMBER: _ClassVar[int]
        parameter_values: _containers.RepeatedCompositeFieldContainer[_types_pb2.RequestedModel.ModelParameterValue]
        display_name: str
        is_max_mode: bool
        is_default_max_config: bool
        is_default_non_max_config: bool
        tooltip_data: AvailableModelsResponse.TooltipData
        tagline: str
        display_name_outside_picker: str
        variant_string_representation: str
        confirmation_dialogue: AvailableModelsResponse.ConfirmationDialogue
        legacy_slug: str
        def __init__(self, parameter_values: _Optional[_Iterable[_Union[_types_pb2.RequestedModel.ModelParameterValue, _Mapping]]] = ..., display_name: _Optional[str] = ..., is_max_mode: bool = ..., is_default_max_config: bool = ..., is_default_non_max_config: bool = ..., tooltip_data: _Optional[_Union[AvailableModelsResponse.TooltipData, _Mapping]] = ..., tagline: _Optional[str] = ..., display_name_outside_picker: _Optional[str] = ..., variant_string_representation: _Optional[str] = ..., confirmation_dialogue: _Optional[_Union[AvailableModelsResponse.ConfirmationDialogue, _Mapping]] = ..., legacy_slug: _Optional[str] = ...) -> None: ...
    class ModelVendor(_message.Message):
        __slots__ = ("id", "display_name")
        ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        id: AvailableModelsResponse.ModelVendorId
        display_name: str
        def __init__(self, id: _Optional[_Union[AvailableModelsResponse.ModelVendorId, str]] = ..., display_name: _Optional[str] = ...) -> None: ...
    class TooltipData(_message.Message):
        __slots__ = ("primary_text", "secondary_text", "secondary_warning_text", "icon", "tertiary_text", "tertiary_text_url", "markdown_content")
        PRIMARY_TEXT_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_TEXT_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        TERTIARY_TEXT_FIELD_NUMBER: _ClassVar[int]
        TERTIARY_TEXT_URL_FIELD_NUMBER: _ClassVar[int]
        MARKDOWN_CONTENT_FIELD_NUMBER: _ClassVar[int]
        primary_text: str
        secondary_text: str
        secondary_warning_text: bool
        icon: str
        tertiary_text: str
        tertiary_text_url: str
        markdown_content: str
        def __init__(self, primary_text: _Optional[str] = ..., secondary_text: _Optional[str] = ..., secondary_warning_text: bool = ..., icon: _Optional[str] = ..., tertiary_text: _Optional[str] = ..., tertiary_text_url: _Optional[str] = ..., markdown_content: _Optional[str] = ...) -> None: ...
    MODEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    COMPOSER_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CMD_K_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COMPOSER_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLAN_EXECUTION_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEC_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEEP_SEARCH_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUICK_AGENT_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USE_MODEL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_UNUSED_MODELS_AFTER_N_HOURS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_UNCHANGED_MODELS_AFTER_N_HOURS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_MODEL_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NUDGE_NEW_CHATS_TO_AUTO_OPTIMIZE_FOR_FIELD_NUMBER: _ClassVar[int]
    model_names: _containers.RepeatedScalarFieldContainer[str]
    models: _containers.RepeatedCompositeFieldContainer[AvailableModelsResponse.AvailableModel]
    composer_model_config: AvailableModelsResponse.FeatureModelConfig
    cmd_k_model_config: AvailableModelsResponse.FeatureModelConfig
    background_composer_model_config: AvailableModelsResponse.FeatureModelConfig
    plan_execution_model_config: AvailableModelsResponse.FeatureModelConfig
    spec_model_config: AvailableModelsResponse.FeatureModelConfig
    deep_search_model_config: AvailableModelsResponse.FeatureModelConfig
    quick_agent_model_config: AvailableModelsResponse.FeatureModelConfig
    use_model_parameters: bool
    disable_unused_models_after_n_hours: int
    upgrade_unchanged_models_after_n_hours: int
    display_configuration: AvailableModelsResponse.ModelPickerDisplayConfiguration
    subagent_model_configs: _containers.MessageMap[str, AvailableModelsResponse.FeatureModelConfig]
    experimental_model_id: str
    experimental_model_display_name: str
    nudge_new_chats_to_auto_optimize_for: str
    def __init__(self, model_names: _Optional[_Iterable[str]] = ..., models: _Optional[_Iterable[_Union[AvailableModelsResponse.AvailableModel, _Mapping]]] = ..., composer_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., cmd_k_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., background_composer_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., plan_execution_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., spec_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., deep_search_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., quick_agent_model_config: _Optional[_Union[AvailableModelsResponse.FeatureModelConfig, _Mapping]] = ..., use_model_parameters: bool = ..., disable_unused_models_after_n_hours: _Optional[int] = ..., upgrade_unchanged_models_after_n_hours: _Optional[int] = ..., display_configuration: _Optional[_Union[AvailableModelsResponse.ModelPickerDisplayConfiguration, _Mapping]] = ..., subagent_model_configs: _Optional[_Mapping[str, AvailableModelsResponse.FeatureModelConfig]] = ..., experimental_model_id: _Optional[str] = ..., experimental_model_display_name: _Optional[str] = ..., nudge_new_chats_to_auto_optimize_for: _Optional[str] = ...) -> None: ...

class BackgroundAgentSettings(_message.Message):
    __slots__ = ("allowlist", "allowlist_config", "team_followup_enabled", "auto_create_pr", "pr_review_open_destination", "require_private_workers", "github_artifact_posting", "team_followup_enabled_v2", "enable_long_running_agent_mode", "egress_protection_mode", "lock_egress_protection_mode", "enable_cloud_agent_testing", "restrict_team_secrets_to_admins", "enable_automations", "allow_vm_sharing", "allow_private_workers", "public_artifact_sharing", "ci_failure_followup_enabled", "data_retention", "restrict_team_environment_writes_to_admins", "allow_remote_control", "allow_private_worker_github_token_mint", "allow_private_worker_secret_sync", "disable_cloud_agents_in_sand", "automation_default_visibility")
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    ALLOWLIST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEAM_FOLLOWUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_PR_FIELD_NUMBER: _ClassVar[int]
    PR_REVIEW_OPEN_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PRIVATE_WORKERS_FIELD_NUMBER: _ClassVar[int]
    GITHUB_ARTIFACT_POSTING_FIELD_NUMBER: _ClassVar[int]
    TEAM_FOLLOWUP_ENABLED_V2_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LONG_RUNNING_AGENT_MODE_FIELD_NUMBER: _ClassVar[int]
    EGRESS_PROTECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    LOCK_EGRESS_PROTECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CLOUD_AGENT_TESTING_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_TEAM_SECRETS_TO_ADMINS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_VM_SHARING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PRIVATE_WORKERS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ARTIFACT_SHARING_FIELD_NUMBER: _ClassVar[int]
    CI_FAILURE_FOLLOWUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_RETENTION_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_TEAM_ENVIRONMENT_WRITES_TO_ADMINS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_REMOTE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PRIVATE_WORKER_GITHUB_TOKEN_MINT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PRIVATE_WORKER_SECRET_SYNC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CLOUD_AGENTS_IN_SAND_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_DEFAULT_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    allowlist: _containers.RepeatedScalarFieldContainer[str]
    allowlist_config: AllowlistConfig
    team_followup_enabled: bool
    auto_create_pr: AutoCreatePrMode
    pr_review_open_destination: PrReviewOpenDestinationMode
    require_private_workers: bool
    github_artifact_posting: GithubArtifactPostingMode
    team_followup_enabled_v2: TeamFollowupEnabledMode
    enable_long_running_agent_mode: bool
    egress_protection_mode: CloudAgentEgressProtectionMode
    lock_egress_protection_mode: bool
    enable_cloud_agent_testing: bool
    restrict_team_secrets_to_admins: bool
    enable_automations: bool
    allow_vm_sharing: bool
    allow_private_workers: bool
    public_artifact_sharing: PublicArtifactSharingMode
    ci_failure_followup_enabled: bool
    data_retention: DataRetentionPolicy
    restrict_team_environment_writes_to_admins: bool
    allow_remote_control: bool
    allow_private_worker_github_token_mint: bool
    allow_private_worker_secret_sync: bool
    disable_cloud_agents_in_sand: bool
    automation_default_visibility: AutomationDefaultVisibility
    def __init__(self, allowlist: _Optional[_Iterable[str]] = ..., allowlist_config: _Optional[_Union[AllowlistConfig, str]] = ..., team_followup_enabled: bool = ..., auto_create_pr: _Optional[_Union[AutoCreatePrMode, str]] = ..., pr_review_open_destination: _Optional[_Union[PrReviewOpenDestinationMode, str]] = ..., require_private_workers: bool = ..., github_artifact_posting: _Optional[_Union[GithubArtifactPostingMode, str]] = ..., team_followup_enabled_v2: _Optional[_Union[TeamFollowupEnabledMode, str]] = ..., enable_long_running_agent_mode: bool = ..., egress_protection_mode: _Optional[_Union[CloudAgentEgressProtectionMode, str]] = ..., lock_egress_protection_mode: bool = ..., enable_cloud_agent_testing: bool = ..., restrict_team_secrets_to_admins: bool = ..., enable_automations: bool = ..., allow_vm_sharing: bool = ..., allow_private_workers: bool = ..., public_artifact_sharing: _Optional[_Union[PublicArtifactSharingMode, str]] = ..., ci_failure_followup_enabled: bool = ..., data_retention: _Optional[_Union[DataRetentionPolicy, _Mapping]] = ..., restrict_team_environment_writes_to_admins: bool = ..., allow_remote_control: bool = ..., allow_private_worker_github_token_mint: bool = ..., allow_private_worker_secret_sync: bool = ..., disable_cloud_agents_in_sand: bool = ..., automation_default_visibility: _Optional[_Union[AutomationDefaultVisibility, str]] = ...) -> None: ...

class BackgroundComposerDefaultEnvironmentSetting(_message.Message):
    __slots__ = ("repo_config", "environment_public_id")
    REPO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_PUBLIC_ID_FIELD_NUMBER: _ClassVar[int]
    repo_config: EnvironmentRepoConfig
    environment_public_id: str
    def __init__(self, repo_config: _Optional[_Union[EnvironmentRepoConfig, _Mapping]] = ..., environment_public_id: _Optional[str] = ...) -> None: ...

class BackgroundComposerQuickActionSettings(_message.Message):
    __slots__ = ("quick_action_subagent_slots", "quick_action_subagent_slots_explicitly_set", "quick_action_subagent_catalog_version", "quick_action_subagent_templates", "quick_action_subagent_template_mutations")
    QUICK_ACTION_SUBAGENT_SLOTS_FIELD_NUMBER: _ClassVar[int]
    QUICK_ACTION_SUBAGENT_SLOTS_EXPLICITLY_SET_FIELD_NUMBER: _ClassVar[int]
    QUICK_ACTION_SUBAGENT_CATALOG_VERSION_FIELD_NUMBER: _ClassVar[int]
    QUICK_ACTION_SUBAGENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    QUICK_ACTION_SUBAGENT_TEMPLATE_MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    quick_action_subagent_slots: _containers.RepeatedCompositeFieldContainer[BackgroundComposerQuickActionSubagentSlot]
    quick_action_subagent_slots_explicitly_set: bool
    quick_action_subagent_catalog_version: int
    quick_action_subagent_templates: _containers.RepeatedCompositeFieldContainer[BackgroundComposerQuickActionSubagentTemplate]
    quick_action_subagent_template_mutations: _containers.RepeatedCompositeFieldContainer[BackgroundComposerQuickActionSubagentTemplateMutation]
    def __init__(self, quick_action_subagent_slots: _Optional[_Iterable[_Union[BackgroundComposerQuickActionSubagentSlot, _Mapping]]] = ..., quick_action_subagent_slots_explicitly_set: bool = ..., quick_action_subagent_catalog_version: _Optional[int] = ..., quick_action_subagent_templates: _Optional[_Iterable[_Union[BackgroundComposerQuickActionSubagentTemplate, _Mapping]]] = ..., quick_action_subagent_template_mutations: _Optional[_Iterable[_Union[BackgroundComposerQuickActionSubagentTemplateMutation, _Mapping]]] = ...) -> None: ...

class BackgroundComposerQuickActionSubagentSlot(_message.Message):
    __slots__ = ("id", "label", "template_id", "subagent_type", "enabled", "order", "execution_mode")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    template_id: str
    subagent_type: str
    enabled: bool
    order: int
    execution_mode: BackgroundComposerQuickActionExecutionMode
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., template_id: _Optional[str] = ..., subagent_type: _Optional[str] = ..., enabled: bool = ..., order: _Optional[int] = ..., execution_mode: _Optional[_Union[BackgroundComposerQuickActionExecutionMode, str]] = ...) -> None: ...

class BackgroundComposerQuickActionSubagentTemplate(_message.Message):
    __slots__ = ("template_id", "label", "description", "subagent_type", "prompt", "scope", "can_edit", "can_delete", "icon_name")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CAN_EDIT_FIELD_NUMBER: _ClassVar[int]
    CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
    ICON_NAME_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    label: str
    description: str
    subagent_type: str
    prompt: str
    scope: BackgroundComposerQuickActionSubagentTemplateScope
    can_edit: bool
    can_delete: bool
    icon_name: str
    def __init__(self, template_id: _Optional[str] = ..., label: _Optional[str] = ..., description: _Optional[str] = ..., subagent_type: _Optional[str] = ..., prompt: _Optional[str] = ..., scope: _Optional[_Union[BackgroundComposerQuickActionSubagentTemplateScope, str]] = ..., can_edit: bool = ..., can_delete: bool = ..., icon_name: _Optional[str] = ...) -> None: ...

class BackgroundComposerQuickActionSubagentTemplateMutation(_message.Message):
    __slots__ = ("operation", "template")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    operation: BackgroundComposerQuickActionSubagentTemplateOperation
    template: BackgroundComposerQuickActionSubagentTemplate
    def __init__(self, operation: _Optional[_Union[BackgroundComposerQuickActionSubagentTemplateOperation, str]] = ..., template: _Optional[_Union[BackgroundComposerQuickActionSubagentTemplate, _Mapping]] = ...) -> None: ...

class BackgroundComposerUserEgressPolicy(_message.Message):
    __slots__ = ("allowlist",)
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    allowlist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowlist: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchEvent(_message.Message):
    __slots__ = ("event", "properties", "timestamp", "user_id", "anonymous_id", "message_id", "context")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    event: str
    properties: _struct_pb2.Struct
    timestamp: int
    user_id: str
    anonymous_id: str
    message_id: str
    context: AnalyticsContext
    def __init__(self, event: _Optional[str] = ..., properties: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timestamp: _Optional[int] = ..., user_id: _Optional[str] = ..., anonymous_id: _Optional[str] = ..., message_id: _Optional[str] = ..., context: _Optional[_Union[AnalyticsContext, _Mapping]] = ...) -> None: ...

class BatchRequest(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[BatchEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[BatchEvent, _Mapping]]] = ...) -> None: ...

class BatchResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BeginOnePasswordConnectionRequest(_message.Message):
    __slots__ = ("connection_id", "vault_id")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    vault_id: str
    def __init__(self, connection_id: _Optional[str] = ..., vault_id: _Optional[str] = ...) -> None: ...

class BeginOnePasswordConnectionResponse(_message.Message):
    __slots__ = ("mint_ticket", "connection_id", "expected_generation", "expiration_mode", "provider_expires_in_seconds", "credential_expires_at_ms", "ticket_expires_at_ms", "policy_version")
    MINT_TICKET_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_GENERATION_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXPIRES_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    TICKET_EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    mint_ticket: str
    connection_id: str
    expected_generation: int
    expiration_mode: CredentialExpirationMode
    provider_expires_in_seconds: int
    credential_expires_at_ms: int
    ticket_expires_at_ms: int
    policy_version: int
    def __init__(self, mint_ticket: _Optional[str] = ..., connection_id: _Optional[str] = ..., expected_generation: _Optional[int] = ..., expiration_mode: _Optional[_Union[CredentialExpirationMode, str]] = ..., provider_expires_in_seconds: _Optional[int] = ..., credential_expires_at_ms: _Optional[int] = ..., ticket_expires_at_ms: _Optional[int] = ..., policy_version: _Optional[int] = ...) -> None: ...

class BitbucketIntegrationSettings(_message.Message):
    __slots__ = ("hidden",)
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    def __init__(self, hidden: bool = ...) -> None: ...

class BootstrapStatsigRequest(_message.Message):
    __slots__ = ("ignore_dev_status", "operating_system", "device_model", "os_version", "form_factor", "stable_id", "client_channel", "bundle_id")
    IGNORE_DEV_STATUS_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    STABLE_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    ignore_dev_status: bool
    operating_system: ClientOS
    device_model: str
    os_version: str
    form_factor: str
    stable_id: str
    client_channel: str
    bundle_id: str
    def __init__(self, ignore_dev_status: bool = ..., operating_system: _Optional[_Union[ClientOS, str]] = ..., device_model: _Optional[str] = ..., os_version: _Optional[str] = ..., form_factor: _Optional[str] = ..., stable_id: _Optional[str] = ..., client_channel: _Optional[str] = ..., bundle_id: _Optional[str] = ...) -> None: ...

class BootstrapStatsigResponse(_message.Message):
    __slots__ = ("config", "generated_at_ms")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    config: str
    generated_at_ms: int
    def __init__(self, config: _Optional[str] = ..., generated_at_ms: _Optional[int] = ...) -> None: ...

class BrowserAccessControl(_message.Message):
    __slots__ = ("allowlist", "allowlist_config")
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    ALLOWLIST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    allowlist: _containers.RepeatedScalarFieldContainer[str]
    allowlist_config: AllowlistConfig
    def __init__(self, allowlist: _Optional[_Iterable[str]] = ..., allowlist_config: _Optional[_Union[AllowlistConfig, str]] = ...) -> None: ...

class BrowserSettings(_message.Message):
    __slots__ = ("access_control",)
    ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    access_control: BrowserAccessControl
    def __init__(self, access_control: _Optional[_Union[BrowserAccessControl, _Mapping]] = ...) -> None: ...

class BulkTeamMemberSandBoxOperationItem(_message.Message):
    __slots__ = ("user_id", "state", "reason", "recreate_operation_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RECREATE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    state: BulkTeamMemberSandBoxItemState
    reason: str
    recreate_operation_id: str
    def __init__(self, user_id: _Optional[int] = ..., state: _Optional[_Union[BulkTeamMemberSandBoxItemState, str]] = ..., reason: _Optional[str] = ..., recreate_operation_id: _Optional[str] = ...) -> None: ...

class CancelGrokBotRoomMemberTurnRequest(_message.Message):
    __slots__ = ("nonce", "member_agent_id", "reason")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    nonce: str
    member_agent_id: str
    reason: str
    def __init__(self, nonce: _Optional[str] = ..., member_agent_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelGrokBotRoomMemberTurnResponse(_message.Message):
    __slots__ = ("delivered",)
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    delivered: bool
    def __init__(self, delivered: bool = ...) -> None: ...

class CancelGrokBotUserComputerRequestRequest(_message.Message):
    __slots__ = ("machine_id", "request_id")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    request_id: str
    def __init__(self, machine_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class CancelGrokBotUserComputerRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelSandBoxUpgradeRequest(_message.Message):
    __slots__ = ("dismiss_terminal_outcome",)
    DISMISS_TERMINAL_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    dismiss_terminal_outcome: bool
    def __init__(self, dismiss_terminal_outcome: bool = ...) -> None: ...

class CancelSandBoxUpgradeResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: SandBoxUpgradeSchedule
    def __init__(self, schedule: _Optional[_Union[SandBoxUpgradeSchedule, _Mapping]] = ...) -> None: ...

class CancelSandTrialRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelSandTrialResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckHttpMcpStatusRequest(_message.Message):
    __slots__ = ("server_ids", "oauth_redirect_uri", "team_id", "service_account_id", "force_reauth", "service_account_type", "post_auth_return_url", "account_key", "server_identifiers")
    SERVER_IDS_FIELD_NUMBER: _ClassVar[int]
    OAUTH_REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_REAUTH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_AUTH_RETURN_URL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    server_ids: _containers.RepeatedScalarFieldContainer[int]
    oauth_redirect_uri: str
    team_id: int
    service_account_id: str
    force_reauth: bool
    service_account_type: str
    post_auth_return_url: str
    account_key: str
    server_identifiers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_ids: _Optional[_Iterable[int]] = ..., oauth_redirect_uri: _Optional[str] = ..., team_id: _Optional[int] = ..., service_account_id: _Optional[str] = ..., force_reauth: bool = ..., service_account_type: _Optional[str] = ..., post_auth_return_url: _Optional[str] = ..., account_key: _Optional[str] = ..., server_identifiers: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckHttpMcpStatusResponse(_message.Message):
    __slots__ = ("statuses",)
    class ServerStatus(_message.Message):
        __slots__ = ("id", "is_available", "requires_auth", "auth_url", "error", "has_valid_token", "server_identifier", "served_by")
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        REQUIRES_AUTH_FIELD_NUMBER: _ClassVar[int]
        AUTH_URL_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        HAS_VALID_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        SERVED_BY_FIELD_NUMBER: _ClassVar[int]
        id: int
        is_available: bool
        requires_auth: bool
        auth_url: str
        error: str
        has_valid_token: bool
        server_identifier: str
        served_by: McpServedBy
        def __init__(self, id: _Optional[int] = ..., is_available: bool = ..., requires_auth: bool = ..., auth_url: _Optional[str] = ..., error: _Optional[str] = ..., has_valid_token: bool = ..., server_identifier: _Optional[str] = ..., served_by: _Optional[_Union[McpServedBy, str]] = ...) -> None: ...
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedCompositeFieldContainer[CheckHttpMcpStatusResponse.ServerStatus]
    def __init__(self, statuses: _Optional[_Iterable[_Union[CheckHttpMcpStatusResponse.ServerStatus, _Mapping]]] = ...) -> None: ...

class ClearGrokBotHarnessMigrationHoldInternalRequest(_message.Message):
    __slots__ = ("owner_auth_id",)
    OWNER_AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    owner_auth_id: str
    def __init__(self, owner_auth_id: _Optional[str] = ...) -> None: ...

class ClearGrokBotHarnessMigrationHoldInternalResponse(_message.Message):
    __slots__ = ("cleared",)
    CLEARED_FIELD_NUMBER: _ClassVar[int]
    cleared: bool
    def __init__(self, cleared: bool = ...) -> None: ...

class ClientAction(_message.Message):
    __slots__ = ("command_id", "args")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    args: _containers.ScalarMap[str, str]
    def __init__(self, command_id: _Optional[str] = ..., args: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ClientActionRequest(_message.Message):
    __slots__ = ("action", "args")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    action: str
    args: _containers.ScalarMap[str, str]
    def __init__(self, action: _Optional[str] = ..., args: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ClientActionResponse(_message.Message):
    __slots__ = ("success", "error_message", "info_message", "open_url")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INFO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPEN_URL_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    info_message: str
    open_url: str
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ..., info_message: _Optional[str] = ..., open_url: _Optional[str] = ...) -> None: ...

class ClientInfo(_message.Message):
    __slots__ = ("os", "arch", "os_version", "version", "layout")
    OS_FIELD_NUMBER: _ClassVar[int]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    os: str
    arch: str
    os_version: str
    version: str
    layout: str
    def __init__(self, os: _Optional[str] = ..., arch: _Optional[str] = ..., os_version: _Optional[str] = ..., version: _Optional[str] = ..., layout: _Optional[str] = ...) -> None: ...

class ClientLogEntry(_message.Message):
    __slots__ = ("level", "message", "metadata", "timestamp", "error_message", "error_stack", "key")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STACK_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    level: ClientLogLevel
    message: str
    metadata: _containers.ScalarMap[str, str]
    timestamp: int
    error_message: str
    error_stack: str
    key: str
    def __init__(self, level: _Optional[_Union[ClientLogLevel, str]] = ..., message: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., timestamp: _Optional[int] = ..., error_message: _Optional[str] = ..., error_stack: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class ClientNumericMetric(_message.Message):
    __slots__ = ("metric", "value", "session_id", "ff_hash", "timestamp_ms", "client_version", "os", "enabled_extensions_hash", "ff_resolved", "extensions_resolved", "window_type")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FF_HASH_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_EXTENSIONS_HASH_FIELD_NUMBER: _ClassVar[int]
    FF_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    metric: str
    value: float
    session_id: str
    ff_hash: str
    timestamp_ms: int
    client_version: str
    os: str
    enabled_extensions_hash: str
    ff_resolved: str
    extensions_resolved: str
    window_type: str
    def __init__(self, metric: _Optional[str] = ..., value: _Optional[float] = ..., session_id: _Optional[str] = ..., ff_hash: _Optional[str] = ..., timestamp_ms: _Optional[int] = ..., client_version: _Optional[str] = ..., os: _Optional[str] = ..., enabled_extensions_hash: _Optional[str] = ..., ff_resolved: _Optional[str] = ..., extensions_resolved: _Optional[str] = ..., window_type: _Optional[str] = ...) -> None: ...

class CliSettings(_message.Message):
    __slots__ = ("allowlist", "allowlist_config", "disable_headless")
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    ALLOWLIST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISABLE_HEADLESS_FIELD_NUMBER: _ClassVar[int]
    allowlist: _containers.RepeatedScalarFieldContainer[str]
    allowlist_config: AllowlistConfig
    disable_headless: bool
    def __init__(self, allowlist: _Optional[_Iterable[str]] = ..., allowlist_config: _Optional[_Union[AllowlistConfig, str]] = ..., disable_headless: bool = ...) -> None: ...

class CloudAgentModelSelection(_message.Message):
    __slots__ = ("model_id", "parameters", "max_mode")
    class ParameterValue(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: str
        value: str
        def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MAX_MODE_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    parameters: _containers.RepeatedCompositeFieldContainer[CloudAgentModelSelection.ParameterValue]
    max_mode: bool
    def __init__(self, model_id: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[CloudAgentModelSelection.ParameterValue, _Mapping]]] = ..., max_mode: bool = ...) -> None: ...

class CloudAgentPersonalScope(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloudAgentRequestScope(_message.Message):
    __slots__ = ("personal", "team_id")
    PERSONAL_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    personal: CloudAgentPersonalScope
    team_id: int
    def __init__(self, personal: _Optional[_Union[CloudAgentPersonalScope, _Mapping]] = ..., team_id: _Optional[int] = ...) -> None: ...

class CloudCanvasMetadata(_message.Message):
    __slots__ = ("store_id", "canvas_id", "title", "created_at", "updated_at", "visibility", "can_share_to_team")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    CANVAS_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    CAN_SHARE_TO_TEAM_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    canvas_id: str
    title: str
    created_at: str
    updated_at: str
    visibility: CanvasVisibility
    can_share_to_team: bool
    def __init__(self, store_id: _Optional[str] = ..., canvas_id: _Optional[str] = ..., title: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., visibility: _Optional[_Union[CanvasVisibility, str]] = ..., can_share_to_team: bool = ...) -> None: ...

class CommandDeeplinkControls(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CommandDescriptor(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class CommitGrokBotTranscriptEntriesRequest(_message.Message):
    __slots__ = ("agent_id", "generation", "entries", "deletes", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DELETES_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    generation: int
    entries: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptEntry]
    deletes: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptEntryDelete]
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., generation: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[GrokBotTranscriptEntry, _Mapping]]] = ..., deletes: _Optional[_Iterable[_Union[GrokBotTranscriptEntryDelete, _Mapping]]] = ..., session_id: _Optional[str] = ...) -> None: ...

class CommitGrokBotTranscriptEntriesResponse(_message.Message):
    __slots__ = ("committed_count", "deleted_count", "rejections")
    COMMITTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REJECTIONS_FIELD_NUMBER: _ClassVar[int]
    committed_count: int
    deleted_count: int
    rejections: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptEntryRejection]
    def __init__(self, committed_count: _Optional[int] = ..., deleted_count: _Optional[int] = ..., rejections: _Optional[_Iterable[_Union[GrokBotTranscriptEntryRejection, _Mapping]]] = ...) -> None: ...

class CompleteMcpOAuthRequest(_message.Message):
    __slots__ = ("state_id", "authorization_code")
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    state_id: str
    authorization_code: str
    def __init__(self, state_id: _Optional[str] = ..., authorization_code: _Optional[str] = ...) -> None: ...

class CompleteMcpOAuthResponse(_message.Message):
    __slots__ = ("post_auth_return_url", "account_key")
    POST_AUTH_RETURN_URL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    post_auth_return_url: str
    account_key: str
    def __init__(self, post_auth_return_url: _Optional[str] = ..., account_key: _Optional[str] = ...) -> None: ...

class CompleteOnePasswordConnectionRequest(_message.Message):
    __slots__ = ("mint_ticket", "service_account_token", "account_uuid", "account_email", "account_url")
    MINT_TICKET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_UUID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_URL_FIELD_NUMBER: _ClassVar[int]
    mint_ticket: str
    service_account_token: str
    account_uuid: str
    account_email: str
    account_url: str
    def __init__(self, mint_ticket: _Optional[str] = ..., service_account_token: _Optional[str] = ..., account_uuid: _Optional[str] = ..., account_email: _Optional[str] = ..., account_url: _Optional[str] = ...) -> None: ...

class CompleteSandBoxStoreMultipartWritesRequest(_message.Message):
    __slots__ = ("completions",)
    COMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    completions: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartWriteCompletion]
    def __init__(self, completions: _Optional[_Iterable[_Union[SandBoxStoreMultipartWriteCompletion, _Mapping]]] = ...) -> None: ...

class CompleteSandBoxStoreMultipartWritesResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartWriteResult]
    def __init__(self, results: _Optional[_Iterable[_Union[SandBoxStoreMultipartWriteResult, _Mapping]]] = ...) -> None: ...

class ConfigureSpendLimitAction(_message.Message):
    __slots__ = ("confirm_label",)
    CONFIRM_LABEL_FIELD_NUMBER: _ClassVar[int]
    confirm_label: str
    def __init__(self, confirm_label: _Optional[str] = ...) -> None: ...

class CreateGrokBotAgentFromTemplateRequest(_message.Message):
    __slots__ = ("share_id", "agent_id", "expected_active_version", "first_party_template", "creator_context", "setup_delegation_supported")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIRST_PARTY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SETUP_DELEGATION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    agent_id: str
    expected_active_version: int
    first_party_template: GrokBotFirstPartyTemplate
    creator_context: str
    setup_delegation_supported: bool
    def __init__(self, share_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., expected_active_version: _Optional[int] = ..., first_party_template: _Optional[_Union[GrokBotFirstPartyTemplate, str]] = ..., creator_context: _Optional[str] = ..., setup_delegation_supported: bool = ...) -> None: ...

class CreateGrokBotAgentFromTemplateResponse(_message.Message):
    __slots__ = ("agent", "blob_get_url", "setup_handled_by_server", "conversational_setup_enabled", "getting_started_trusted")
    AGENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_GET_URL_FIELD_NUMBER: _ClassVar[int]
    SETUP_HANDLED_BY_SERVER_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONAL_SETUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GETTING_STARTED_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    agent: GrokBotAgent
    blob_get_url: str
    setup_handled_by_server: bool
    conversational_setup_enabled: bool
    getting_started_trusted: bool
    def __init__(self, agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ..., blob_get_url: _Optional[str] = ..., setup_handled_by_server: bool = ..., conversational_setup_enabled: bool = ..., getting_started_trusted: bool = ...) -> None: ...

class CreateGrokBotAgentRequest(_message.Message):
    __slots__ = ("legacy_agent_id", "name", "description", "title", "avatar_shape", "avatar_color", "avatar_data_url", "agent_id", "harness", "kickstart_requested", "introduction_suppressed", "purpose", "origin", "language")
    LEGACY_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    AVATAR_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    KICKSTART_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    INTRODUCTION_SUPPRESSED_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    legacy_agent_id: str
    name: str
    description: str
    title: str
    avatar_shape: str
    avatar_color: str
    avatar_data_url: str
    agent_id: str
    harness: GrokBotAgentHarnessKind
    kickstart_requested: bool
    introduction_suppressed: bool
    purpose: str
    origin: str
    language: str
    def __init__(self, legacy_agent_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., avatar_data_url: _Optional[str] = ..., agent_id: _Optional[str] = ..., harness: _Optional[_Union[GrokBotAgentHarnessKind, str]] = ..., kickstart_requested: bool = ..., introduction_suppressed: bool = ..., purpose: _Optional[str] = ..., origin: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class CreateGrokBotAgentResponse(_message.Message):
    __slots__ = ("agent", "harness")
    AGENT_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    agent: GrokBotAgent
    harness: GrokBotAgentHarnessKind
    def __init__(self, agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ..., harness: _Optional[_Union[GrokBotAgentHarnessKind, str]] = ...) -> None: ...

class CreateGrokBotMarketplaceCategoryInternalRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateGrokBotMarketplaceCreatorInternalRequest(_message.Message):
    __slots__ = ("name", "profile_photo_url", "handles")
    class HandlesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    HANDLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    profile_photo_url: str
    handles: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., profile_photo_url: _Optional[str] = ..., handles: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateGrokBotMarketplaceListingInternalRequest(_message.Message):
    __slots__ = ("template_id", "slug", "category", "creator_id", "category_ids")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    slug: str
    category: str
    creator_id: int
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, template_id: _Optional[int] = ..., slug: _Optional[str] = ..., category: _Optional[str] = ..., creator_id: _Optional[int] = ..., category_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateGrokBotRoomRequest(_message.Message):
    __slots__ = ("agent_id", "name", "description", "member_agent_ids", "human_member_user_ids")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    HUMAN_MEMBER_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    description: str
    member_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    human_member_user_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., member_agent_ids: _Optional[_Iterable[str]] = ..., human_member_user_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateGrokBotRoomResponse(_message.Message):
    __slots__ = ("agent",)
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: GrokBotAgent
    def __init__(self, agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ...) -> None: ...

class CreateGrokBotTemplateRequest(_message.Message):
    __slots__ = ("name", "avatar_shape", "avatar_color", "source_agent_id", "blob_content_type", "blob_byte_size", "description", "requested_visibility")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOB_BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    avatar_shape: str
    avatar_color: str
    source_agent_id: str
    blob_content_type: str
    blob_byte_size: int
    description: str
    requested_visibility: GrokBotTemplateVisibility
    def __init__(self, name: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., source_agent_id: _Optional[str] = ..., blob_content_type: _Optional[str] = ..., blob_byte_size: _Optional[int] = ..., description: _Optional[str] = ..., requested_visibility: _Optional[_Union[GrokBotTemplateVisibility, str]] = ...) -> None: ...

class CreateGrokBotTemplateResponse(_message.Message):
    __slots__ = ("template", "blob_put_url", "version")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    BLOB_PUT_URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    template: GrokBotTemplate
    blob_put_url: str
    version: int
    def __init__(self, template: _Optional[_Union[GrokBotTemplate, _Mapping]] = ..., blob_put_url: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class CredentialTargetRule(_message.Message):
    __slots__ = ("kind", "scheme", "host", "port", "registrable_domain")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    REGISTRABLE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    kind: CredentialTargetRuleKind
    scheme: str
    host: str
    port: int
    registrable_domain: str
    def __init__(self, kind: _Optional[_Union[CredentialTargetRuleKind, str]] = ..., scheme: _Optional[str] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., registrable_domain: _Optional[str] = ...) -> None: ...

class CursorBlameSettings(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CursorIgnoreControls(_message.Message):
    __slots__ = ("hierarchical_enabled", "ignore_symlinks")
    HIERARCHICAL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SYMLINKS_FIELD_NUMBER: _ClassVar[int]
    hierarchical_enabled: bool
    ignore_symlinks: bool
    def __init__(self, hierarchical_enabled: bool = ..., ignore_symlinks: bool = ...) -> None: ...

class DailySpendByCategory(_message.Message):
    __slots__ = ("day", "category", "spend_cents", "total_tokens")
    DAY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPEND_CENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    day: int
    category: str
    spend_cents: int
    total_tokens: int
    def __init__(self, day: _Optional[int] = ..., category: _Optional[str] = ..., spend_cents: _Optional[int] = ..., total_tokens: _Optional[int] = ...) -> None: ...

class DashboardAction(_message.Message):
    __slots__ = ("action", "args", "success_message")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    action: str
    args: _containers.ScalarMap[str, str]
    success_message: str
    def __init__(self, action: _Optional[str] = ..., args: _Optional[_Mapping[str, str]] = ..., success_message: _Optional[str] = ...) -> None: ...

class DataRetentionPolicy(_message.Message):
    __slots__ = ("indefinite", "limited")
    class Indefinite(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Limited(_message.Message):
        __slots__ = ("hours",)
        HOURS_FIELD_NUMBER: _ClassVar[int]
        hours: int
        def __init__(self, hours: _Optional[int] = ...) -> None: ...
    INDEFINITE_FIELD_NUMBER: _ClassVar[int]
    LIMITED_FIELD_NUMBER: _ClassVar[int]
    indefinite: DataRetentionPolicy.Indefinite
    limited: DataRetentionPolicy.Limited
    def __init__(self, indefinite: _Optional[_Union[DataRetentionPolicy.Indefinite, _Mapping]] = ..., limited: _Optional[_Union[DataRetentionPolicy.Limited, _Mapping]] = ...) -> None: ...

class DeeplinkControls(_message.Message):
    __slots__ = ("enabled", "allow_public_deeplinks")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PUBLIC_DEEPLINKS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    allow_public_deeplinks: bool
    def __init__(self, enabled: bool = ..., allow_public_deeplinks: bool = ...) -> None: ...

class DeleteGrokBotAgentAutomationRequest(_message.Message):
    __slots__ = ("agent_id", "automation_id", "time_zone")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    automation_id: str
    time_zone: str
    def __init__(self, agent_id: _Optional[str] = ..., automation_id: _Optional[str] = ..., time_zone: _Optional[str] = ...) -> None: ...

class DeleteGrokBotAgentAutomationResponse(_message.Message):
    __slots__ = ("automations",)
    AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    automations: _containers.RepeatedCompositeFieldContainer[GrokBotAgentAutomation]
    def __init__(self, automations: _Optional[_Iterable[_Union[GrokBotAgentAutomation, _Mapping]]] = ...) -> None: ...

class DeleteGrokBotAgentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteGrokBotAgentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteGrokBotMarketplaceListingInternalRequest(_message.Message):
    __slots__ = ("listing_id",)
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    def __init__(self, listing_id: _Optional[int] = ...) -> None: ...

class DeleteGrokBotMarketplaceListingInternalResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteGrokBotSecretRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteGrokBotSecretResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteGrokBotTemplateRequest(_message.Message):
    __slots__ = ("share_id",)
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    def __init__(self, share_id: _Optional[str] = ...) -> None: ...

class DeleteGrokBotTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteGrokBotUserFormVaultEntryRequest(_message.Message):
    __slots__ = ("entry_id",)
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DeleteGrokBotUserFormVaultEntryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMcpOAuthAccountRequest(_message.Message):
    __slots__ = ("server_id", "account_key")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    server_id: int
    account_key: str
    def __init__(self, server_id: _Optional[int] = ..., account_key: _Optional[str] = ...) -> None: ...

class DeleteMcpOAuthAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMcpOAuthTokenRequest(_message.Message):
    __slots__ = ("server_url", "service_account_id", "source", "account_key")
    SERVER_URL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    server_url: str
    service_account_id: str
    source: str
    account_key: str
    def __init__(self, server_url: _Optional[str] = ..., service_account_id: _Optional[str] = ..., source: _Optional[str] = ..., account_key: _Optional[str] = ...) -> None: ...

class DeleteMcpOAuthTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteOnePasswordConnectionRequest(_message.Message):
    __slots__ = ("connection_id",)
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class DeleteTeamSandSetupManifestRequest(_message.Message):
    __slots__ = ("manifest_id", "expected_etag")
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ETAG_FIELD_NUMBER: _ClassVar[int]
    manifest_id: str
    expected_etag: str
    def __init__(self, manifest_id: _Optional[str] = ..., expected_etag: _Optional[str] = ...) -> None: ...

class DeleteTeamSandSetupManifestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeliverGrokBotRoomMemberTurnResultRequest(_message.Message):
    __slots__ = ("room_id", "nonce", "member_agent_id", "outcome", "messages", "error")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    nonce: str
    member_agent_id: str
    outcome: GrokBotRoomMemberTurnOutcome
    messages: _containers.RepeatedScalarFieldContainer[str]
    error: str
    def __init__(self, room_id: _Optional[str] = ..., nonce: _Optional[str] = ..., member_agent_id: _Optional[str] = ..., outcome: _Optional[_Union[GrokBotRoomMemberTurnOutcome, str]] = ..., messages: _Optional[_Iterable[str]] = ..., error: _Optional[str] = ...) -> None: ...

class DeliverGrokBotRoomMemberTurnResultResponse(_message.Message):
    __slots__ = ("intake",)
    INTAKE_FIELD_NUMBER: _ClassVar[int]
    intake: GrokBotRoomMemberTurnResultIntake
    def __init__(self, intake: _Optional[_Union[GrokBotRoomMemberTurnResultIntake, str]] = ...) -> None: ...

class DenyOnePasswordCredentialRequestRequest(_message.Message):
    __slots__ = ("entry_id", "agent_id", "harness")
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    agent_id: str
    harness: SandCredentialDecisionHarness
    def __init__(self, entry_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., harness: _Optional[_Union[SandCredentialDecisionHarness, str]] = ...) -> None: ...

class DiscardGrokBotDraftRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class DiscardGrokBotDraftResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class DismissGrokBotUserFormRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "mode", "session_id", "platform")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    mode: GrokBotUserFormDismissMode
    session_id: str
    platform: GrokBotUserFormClientPlatform
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., mode: _Optional[_Union[GrokBotUserFormDismissMode, str]] = ..., session_id: _Optional[str] = ..., platform: _Optional[_Union[GrokBotUserFormClientPlatform, str]] = ...) -> None: ...

class DismissGrokBotUserFormResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class DismissGrokBotWidgetRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class DismissGrokBotWidgetResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class DownloadIssueTracesRequest(_message.Message):
    __slots__ = ("token", "limit")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    token: str
    limit: int
    def __init__(self, token: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class DownloadIssueTracesResponse(_message.Message):
    __slots__ = ("data", "total_traces", "total_bytes")
    DATA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRACES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    total_traces: int
    total_bytes: int
    def __init__(self, data: _Optional[bytes] = ..., total_traces: _Optional[int] = ..., total_bytes: _Optional[int] = ...) -> None: ...

class EffectivePlugin(_message.Message):
    __slots__ = ("plugin", "is_team_required", "is_enabled", "pinned_git_ref", "configured_variables", "has_team_configured_variables", "inline_content_json", "install_mode", "configured_variable_keys")
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    IS_TEAM_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PINNED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    HAS_TEAM_CONFIGURED_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    INLINE_CONTENT_JSON_FIELD_NUMBER: _ClassVar[int]
    INSTALL_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_VARIABLE_KEYS_FIELD_NUMBER: _ClassVar[int]
    plugin: Plugin
    is_team_required: bool
    is_enabled: bool
    pinned_git_ref: str
    configured_variables: _struct_pb2.Struct
    has_team_configured_variables: bool
    inline_content_json: str
    install_mode: EffectivePluginInstallMode
    configured_variable_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, plugin: _Optional[_Union[Plugin, _Mapping]] = ..., is_team_required: bool = ..., is_enabled: bool = ..., pinned_git_ref: _Optional[str] = ..., configured_variables: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., has_team_configured_variables: bool = ..., inline_content_json: _Optional[str] = ..., install_mode: _Optional[_Union[EffectivePluginInstallMode, str]] = ..., configured_variable_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class EndGrokBotBoxHandoffRequest(_message.Message):
    __slots__ = ("agent_id", "request_id", "trigger")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    request_id: str
    trigger: GrokBotBoxHandBackTrigger
    def __init__(self, agent_id: _Optional[str] = ..., request_id: _Optional[str] = ..., trigger: _Optional[_Union[GrokBotBoxHandBackTrigger, str]] = ...) -> None: ...

class EndGrokBotBoxHandoffResponse(_message.Message):
    __slots__ = ("dispatched", "workflow_id")
    DISPATCHED_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    dispatched: bool
    workflow_id: str
    def __init__(self, dispatched: bool = ..., workflow_id: _Optional[str] = ...) -> None: ...

class EnsureGrokBotBoxHarnessMigrationPassRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class EnsureGrokBotBoxHarnessMigrationPassResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: GrokBotBoxHarnessMigrationPassState
    def __init__(self, state: _Optional[_Union[GrokBotBoxHarnessMigrationPassState, str]] = ...) -> None: ...

class EnsureSandBoxRequest(_message.Message):
    __slots__ = ("wake",)
    WAKE_FIELD_NUMBER: _ClassVar[int]
    wake: bool
    def __init__(self, wake: bool = ...) -> None: ...

class EnsureSandBoxResponse(_message.Message):
    __slots__ = ("cluster", "tenant_id", "pod_id", "network_token", "exec_daemon_auth_token", "exec_daemon_url", "vnc_url", "terminals_folder", "image_update_available", "gateway_url", "gateway_token", "fork_vnc_base_url", "run_state")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    POD_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXEC_DAEMON_AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXEC_DAEMON_URL_FIELD_NUMBER: _ClassVar[int]
    VNC_URL_FIELD_NUMBER: _ClassVar[int]
    TERMINALS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_URL_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FORK_VNC_BASE_URL_FIELD_NUMBER: _ClassVar[int]
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    tenant_id: str
    pod_id: str
    network_token: str
    exec_daemon_auth_token: str
    exec_daemon_url: str
    vnc_url: str
    terminals_folder: str
    image_update_available: bool
    gateway_url: str
    gateway_token: str
    fork_vnc_base_url: str
    run_state: SandBoxRunState
    def __init__(self, cluster: _Optional[str] = ..., tenant_id: _Optional[str] = ..., pod_id: _Optional[str] = ..., network_token: _Optional[str] = ..., exec_daemon_auth_token: _Optional[str] = ..., exec_daemon_url: _Optional[str] = ..., vnc_url: _Optional[str] = ..., terminals_folder: _Optional[str] = ..., image_update_available: bool = ..., gateway_url: _Optional[str] = ..., gateway_token: _Optional[str] = ..., fork_vnc_base_url: _Optional[str] = ..., run_state: _Optional[_Union[SandBoxRunState, str]] = ...) -> None: ...

class EnsureSandBoxWindowRequest(_message.Message):
    __slots__ = ("window_index",)
    WINDOW_INDEX_FIELD_NUMBER: _ClassVar[int]
    window_index: int
    def __init__(self, window_index: _Optional[int] = ...) -> None: ...

class EnvironmentJsonFileLocation(_message.Message):
    __slots__ = ("repo_url", "path")
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    repo_url: str
    path: str
    def __init__(self, repo_url: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class EnvironmentRepoConfig(_message.Message):
    __slots__ = ("repos", "environment_json_location")
    REPOS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_JSON_LOCATION_FIELD_NUMBER: _ClassVar[int]
    repos: _containers.RepeatedCompositeFieldContainer[EnvironmentRepoEntry]
    environment_json_location: EnvironmentJsonFileLocation
    def __init__(self, repos: _Optional[_Iterable[_Union[EnvironmentRepoEntry, _Mapping]]] = ..., environment_json_location: _Optional[_Union[EnvironmentJsonFileLocation, _Mapping]] = ...) -> None: ...

class EnvironmentRepoEntry(_message.Message):
    __slots__ = ("repo_url", "scm_repo_node_id", "git_enterprise_uuid")
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    SCM_REPO_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    GIT_ENTERPRISE_UUID_FIELD_NUMBER: _ClassVar[int]
    repo_url: str
    scm_repo_node_id: str
    git_enterprise_uuid: str
    def __init__(self, repo_url: _Optional[str] = ..., scm_repo_node_id: _Optional[str] = ..., git_enterprise_uuid: _Optional[str] = ...) -> None: ...

class ErrorButton(_message.Message):
    __slots__ = ("label", "upgrade", "switch_model", "configure_spend_limit", "url", "upgrade_choice", "dashboard_action", "reload_window", "client_action")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_FIELD_NUMBER: _ClassVar[int]
    SWITCH_MODEL_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ACTION_FIELD_NUMBER: _ClassVar[int]
    RELOAD_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    label: str
    upgrade: UpgradeAction
    switch_model: SwitchModelAction
    configure_spend_limit: ConfigureSpendLimitAction
    url: UrlAction
    upgrade_choice: UpgradeChoice
    dashboard_action: DashboardAction
    reload_window: ReloadWindowAction
    client_action: ClientAction
    def __init__(self, label: _Optional[str] = ..., upgrade: _Optional[_Union[UpgradeAction, _Mapping]] = ..., switch_model: _Optional[_Union[SwitchModelAction, _Mapping]] = ..., configure_spend_limit: _Optional[_Union[ConfigureSpendLimitAction, _Mapping]] = ..., url: _Optional[_Union[UrlAction, _Mapping]] = ..., upgrade_choice: _Optional[_Union[UpgradeChoice, _Mapping]] = ..., dashboard_action: _Optional[_Union[DashboardAction, _Mapping]] = ..., reload_window: _Optional[_Union[ReloadWindowAction, _Mapping]] = ..., client_action: _Optional[_Union[ClientAction, _Mapping]] = ...) -> None: ...

class EventData(_message.Message):
    __slots__ = ("string_value", "int_value", "bool_value", "double_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    bool_value: bool
    double_value: float
    def __init__(self, string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., bool_value: bool = ..., double_value: _Optional[float] = ...) -> None: ...

class ExecuteSandMcpToolRequest(_message.Message):
    __slots__ = ("server_identifier", "tool_name", "args", "tool_call_id", "agent_id", "turn_id", "mcp_config_json", "grok_bot_plugin_scope")
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    GROK_BOT_PLUGIN_SCOPE_FIELD_NUMBER: _ClassVar[int]
    server_identifier: str
    tool_name: str
    args: _struct_pb2.Struct
    tool_call_id: str
    agent_id: str
    turn_id: str
    mcp_config_json: str
    grok_bot_plugin_scope: GrokBotPluginScope
    def __init__(self, server_identifier: _Optional[str] = ..., tool_name: _Optional[str] = ..., args: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tool_call_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., turn_id: _Optional[str] = ..., mcp_config_json: _Optional[str] = ..., grok_bot_plugin_scope: _Optional[_Union[GrokBotPluginScope, _Mapping]] = ...) -> None: ...

class ExecuteSandMcpToolResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _types_pb2.McpResult
    def __init__(self, result: _Optional[_Union[_types_pb2.McpResult, _Mapping]] = ...) -> None: ...

class ExtensionInstallCooldownSettings(_message.Message):
    __slots__ = ("cooldown_hours",)
    COOLDOWN_HOURS_FIELD_NUMBER: _ClassVar[int]
    cooldown_hours: int
    def __init__(self, cooldown_hours: _Optional[int] = ...) -> None: ...

class ExtensionSigningSettings(_message.Message):
    __slots__ = ("verification_enabled",)
    VERIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    verification_enabled: bool
    def __init__(self, verification_enabled: bool = ...) -> None: ...

class FirstPartyPendingModel(_message.Message):
    __slots__ = ("mcid", "enables_at")
    MCID_FIELD_NUMBER: _ClassVar[int]
    ENABLES_AT_FIELD_NUMBER: _ClassVar[int]
    mcid: str
    enables_at: int
    def __init__(self, mcid: _Optional[str] = ..., enables_at: _Optional[int] = ...) -> None: ...

class FirstPartyPluginConfiguration(_message.Message):
    __slots__ = ("mode", "allowed_plugin_ids")
    MODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_PLUGIN_IDS_FIELD_NUMBER: _ClassVar[int]
    mode: FirstPartyPluginMode
    allowed_plugin_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[_Union[FirstPartyPluginMode, str]] = ..., allowed_plugin_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ForceRecreateSandBoxRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateImageReferenceImage(_message.Message):
    __slots__ = ("data", "mime_type")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    data: str
    mime_type: str
    def __init__(self, data: _Optional[str] = ..., mime_type: _Optional[str] = ...) -> None: ...

class GetAggregatedUsageEventsRequest(_message.Message):
    __slots__ = ("team_id", "start_date", "end_date", "user_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    start_date: int
    end_date: int
    user_id: int
    def __init__(self, team_id: _Optional[int] = ..., start_date: _Optional[int] = ..., end_date: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetAggregatedUsageEventsResponse(_message.Message):
    __slots__ = ("aggregations", "total_input_tokens", "total_output_tokens", "total_cache_write_tokens", "total_cache_read_tokens", "total_cost_cents", "percent_of_burst_used", "total_request_cost")
    class ModelUsageAggregation(_message.Message):
        __slots__ = ("model_intent", "input_tokens", "output_tokens", "cache_write_tokens", "cache_read_tokens", "total_cents", "request_cost", "tier")
        MODEL_INTENT_FIELD_NUMBER: _ClassVar[int]
        INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
        CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
        CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
        REQUEST_COST_FIELD_NUMBER: _ClassVar[int]
        TIER_FIELD_NUMBER: _ClassVar[int]
        model_intent: str
        input_tokens: int
        output_tokens: int
        cache_write_tokens: int
        cache_read_tokens: int
        total_cents: float
        request_cost: float
        tier: int
        def __init__(self, model_intent: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., total_cents: _Optional[float] = ..., request_cost: _Optional[float] = ..., tier: _Optional[int] = ...) -> None: ...
    AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_CENTS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_OF_BURST_USED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REQUEST_COST_FIELD_NUMBER: _ClassVar[int]
    aggregations: _containers.RepeatedCompositeFieldContainer[GetAggregatedUsageEventsResponse.ModelUsageAggregation]
    total_input_tokens: int
    total_output_tokens: int
    total_cache_write_tokens: int
    total_cache_read_tokens: int
    total_cost_cents: float
    percent_of_burst_used: float
    total_request_cost: float
    def __init__(self, aggregations: _Optional[_Iterable[_Union[GetAggregatedUsageEventsResponse.ModelUsageAggregation, _Mapping]]] = ..., total_input_tokens: _Optional[int] = ..., total_output_tokens: _Optional[int] = ..., total_cache_write_tokens: _Optional[int] = ..., total_cache_read_tokens: _Optional[int] = ..., total_cost_cents: _Optional[float] = ..., percent_of_burst_used: _Optional[float] = ..., total_request_cost: _Optional[float] = ...) -> None: ...

class GetAvailableMcpServersRequest(_message.Message):
    __slots__ = ("grok_bot_plugin_scope", "grok_bot_agent_id")
    GROK_BOT_PLUGIN_SCOPE_FIELD_NUMBER: _ClassVar[int]
    GROK_BOT_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    grok_bot_plugin_scope: GrokBotPluginScope
    grok_bot_agent_id: str
    def __init__(self, grok_bot_plugin_scope: _Optional[_Union[GrokBotPluginScope, _Mapping]] = ..., grok_bot_agent_id: _Optional[str] = ...) -> None: ...

class GetAvailableMcpServersResponse(_message.Message):
    __slots__ = ("servers",)
    class McpAccountInfo(_message.Message):
        __slots__ = ("account_key", "server_identifier", "user_has_access_token")
        ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
        SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        USER_HAS_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        account_key: str
        server_identifier: str
        user_has_access_token: bool
        def __init__(self, account_key: _Optional[str] = ..., server_identifier: _Optional[str] = ..., user_has_access_token: bool = ...) -> None: ...
    class McpServerInfo(_message.Message):
        __slots__ = ("id", "name", "is_team_server", "enabled", "type", "command", "args", "url", "plugin_id", "is_unseen", "user_has_access_token", "is_required", "managed_by_team_plugin_policy", "disabled_by_team_admin_policy", "server_identifier", "owning_team_id", "accounts", "has_static_credential_headers", "served_by")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IS_TEAM_SERVER_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
        IS_UNSEEN_FIELD_NUMBER: _ClassVar[int]
        USER_HAS_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        MANAGED_BY_TEAM_PLUGIN_POLICY_FIELD_NUMBER: _ClassVar[int]
        DISABLED_BY_TEAM_ADMIN_POLICY_FIELD_NUMBER: _ClassVar[int]
        SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        OWNING_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
        HAS_STATIC_CREDENTIAL_HEADERS_FIELD_NUMBER: _ClassVar[int]
        SERVED_BY_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        is_team_server: bool
        enabled: bool
        type: str
        command: str
        args: _containers.RepeatedScalarFieldContainer[str]
        url: str
        plugin_id: int
        is_unseen: bool
        user_has_access_token: bool
        is_required: bool
        managed_by_team_plugin_policy: bool
        disabled_by_team_admin_policy: bool
        server_identifier: str
        owning_team_id: int
        accounts: _containers.RepeatedCompositeFieldContainer[GetAvailableMcpServersResponse.McpAccountInfo]
        has_static_credential_headers: bool
        served_by: McpServedBy
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., is_team_server: bool = ..., enabled: bool = ..., type: _Optional[str] = ..., command: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ..., plugin_id: _Optional[int] = ..., is_unseen: bool = ..., user_has_access_token: bool = ..., is_required: bool = ..., managed_by_team_plugin_policy: bool = ..., disabled_by_team_admin_policy: bool = ..., server_identifier: _Optional[str] = ..., owning_team_id: _Optional[int] = ..., accounts: _Optional[_Iterable[_Union[GetAvailableMcpServersResponse.McpAccountInfo, _Mapping]]] = ..., has_static_credential_headers: bool = ..., served_by: _Optional[_Union[McpServedBy, str]] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[GetAvailableMcpServersResponse.McpServerInfo]
    def __init__(self, servers: _Optional[_Iterable[_Union[GetAvailableMcpServersResponse.McpServerInfo, _Mapping]]] = ...) -> None: ...

class GetBackgroundComposerUserSettingsRequest(_message.Message):
    __slots__ = ("expected_scope",)
    EXPECTED_SCOPE_FIELD_NUMBER: _ClassVar[int]
    expected_scope: CloudAgentRequestScope
    def __init__(self, expected_scope: _Optional[_Union[CloudAgentRequestScope, _Mapping]] = ...) -> None: ...

class GetBackgroundComposerUserSettingsResponse(_message.Message):
    __slots__ = ("model_name", "slack_notifications_for_web_enabled", "ci_failure_followup_enabled", "browser_use_enabled", "auto_create_pr_setting", "pr_review_open_destination", "github_artifact_posting", "egress_protection_mode", "egress_policy", "branch_prefix", "quick_action_settings", "allow_private_workers", "default_environment_public_id", "default_environment_settings", "remote_control_enabled", "pr_review_open_surface", "sidebar_named_agent_ids", "default_model_selection", "ask_question_auto_answer_timeout_minutes")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SLACK_NOTIFICATIONS_FOR_WEB_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CI_FAILURE_FOLLOWUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BROWSER_USE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_PR_SETTING_FIELD_NUMBER: _ClassVar[int]
    PR_REVIEW_OPEN_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GITHUB_ARTIFACT_POSTING_FIELD_NUMBER: _ClassVar[int]
    EGRESS_PROTECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    EGRESS_POLICY_FIELD_NUMBER: _ClassVar[int]
    BRANCH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    QUICK_ACTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PRIVATE_WORKERS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ENVIRONMENT_PUBLIC_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ENVIRONMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PR_REVIEW_OPEN_SURFACE_FIELD_NUMBER: _ClassVar[int]
    SIDEBAR_NAMED_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_SELECTION_FIELD_NUMBER: _ClassVar[int]
    ASK_QUESTION_AUTO_ANSWER_TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    slack_notifications_for_web_enabled: bool
    ci_failure_followup_enabled: bool
    browser_use_enabled: bool
    auto_create_pr_setting: AutoCreatePrSetting
    pr_review_open_destination: PrReviewOpenDestinationMode
    github_artifact_posting: GithubArtifactPostingMode
    egress_protection_mode: CloudAgentEgressProtectionMode
    egress_policy: BackgroundComposerUserEgressPolicy
    branch_prefix: str
    quick_action_settings: BackgroundComposerQuickActionSettings
    allow_private_workers: bool
    default_environment_public_id: str
    default_environment_settings: _containers.RepeatedCompositeFieldContainer[BackgroundComposerDefaultEnvironmentSetting]
    remote_control_enabled: bool
    pr_review_open_surface: PrReviewOpenSurfaceMode
    sidebar_named_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    default_model_selection: CloudAgentModelSelection
    ask_question_auto_answer_timeout_minutes: int
    def __init__(self, model_name: _Optional[str] = ..., slack_notifications_for_web_enabled: bool = ..., ci_failure_followup_enabled: bool = ..., browser_use_enabled: bool = ..., auto_create_pr_setting: _Optional[_Union[AutoCreatePrSetting, str]] = ..., pr_review_open_destination: _Optional[_Union[PrReviewOpenDestinationMode, str]] = ..., github_artifact_posting: _Optional[_Union[GithubArtifactPostingMode, str]] = ..., egress_protection_mode: _Optional[_Union[CloudAgentEgressProtectionMode, str]] = ..., egress_policy: _Optional[_Union[BackgroundComposerUserEgressPolicy, _Mapping]] = ..., branch_prefix: _Optional[str] = ..., quick_action_settings: _Optional[_Union[BackgroundComposerQuickActionSettings, _Mapping]] = ..., allow_private_workers: bool = ..., default_environment_public_id: _Optional[str] = ..., default_environment_settings: _Optional[_Iterable[_Union[BackgroundComposerDefaultEnvironmentSetting, _Mapping]]] = ..., remote_control_enabled: bool = ..., pr_review_open_surface: _Optional[_Union[PrReviewOpenSurfaceMode, str]] = ..., sidebar_named_agent_ids: _Optional[_Iterable[str]] = ..., default_model_selection: _Optional[_Union[CloudAgentModelSelection, _Mapping]] = ..., ask_question_auto_answer_timeout_minutes: _Optional[int] = ...) -> None: ...

class GetBulkTeamMemberSandBoxOperationStatusRequest(_message.Message):
    __slots__ = ("team_id", "operation_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    operation_id: str
    def __init__(self, team_id: _Optional[int] = ..., operation_id: _Optional[str] = ...) -> None: ...

class GetBulkTeamMemberSandBoxOperationStatusResponse(_message.Message):
    __slots__ = ("operation_id", "action", "state", "total_count", "queued_count", "running_count", "succeeded_count", "skipped_count", "failed_count", "items")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUEUED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RUNNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    action: BulkTeamMemberSandBoxAction
    state: BulkTeamMemberSandBoxOperationState
    total_count: int
    queued_count: int
    running_count: int
    succeeded_count: int
    skipped_count: int
    failed_count: int
    items: _containers.RepeatedCompositeFieldContainer[BulkTeamMemberSandBoxOperationItem]
    def __init__(self, operation_id: _Optional[str] = ..., action: _Optional[_Union[BulkTeamMemberSandBoxAction, str]] = ..., state: _Optional[_Union[BulkTeamMemberSandBoxOperationState, str]] = ..., total_count: _Optional[int] = ..., queued_count: _Optional[int] = ..., running_count: _Optional[int] = ..., succeeded_count: _Optional[int] = ..., skipped_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., items: _Optional[_Iterable[_Union[BulkTeamMemberSandBoxOperationItem, _Mapping]]] = ...) -> None: ...

class GetCanvasPayloadRequest(_message.Message):
    __slots__ = ("store_id", "canvas_id")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    CANVAS_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    canvas_id: str
    def __init__(self, store_id: _Optional[str] = ..., canvas_id: _Optional[str] = ...) -> None: ...

class GetCanvasPayloadResponse(_message.Message):
    __slots__ = ("metadata", "render_bundle_gzip", "data_json")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RENDER_BUNDLE_GZIP_FIELD_NUMBER: _ClassVar[int]
    DATA_JSON_FIELD_NUMBER: _ClassVar[int]
    metadata: CloudCanvasMetadata
    render_bundle_gzip: bytes
    data_json: bytes
    def __init__(self, metadata: _Optional[_Union[CloudCanvasMetadata, _Mapping]] = ..., render_bundle_gzip: _Optional[bytes] = ..., data_json: _Optional[bytes] = ...) -> None: ...

class GetCurrentPeriodUsageRequest(_message.Message):
    __slots__ = ("team_id", "include_pooled_usage")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_POOLED_USAGE_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    include_pooled_usage: bool
    def __init__(self, team_id: _Optional[int] = ..., include_pooled_usage: bool = ...) -> None: ...

class GetCurrentPeriodUsageResponse(_message.Message):
    __slots__ = ("billing_cycle_start", "billing_cycle_end", "plan_usage", "spend_limit_usage", "display_threshold", "enabled", "display_message", "free_best_of_n_promotion", "auto_model_selected_display_message", "named_model_selected_display_message", "auto_bucket_models")
    class FreeBestOfNPromotion(_message.Message):
        __slots__ = ("trials_used", "trials_remaining")
        TRIALS_USED_FIELD_NUMBER: _ClassVar[int]
        TRIALS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        trials_used: int
        trials_remaining: int
        def __init__(self, trials_used: _Optional[int] = ..., trials_remaining: _Optional[int] = ...) -> None: ...
    class PlanUsage(_message.Message):
        __slots__ = ("total_spend", "included_spend", "bonus_spend", "remaining", "limit", "remaining_bonus", "bonus_tooltip", "auto_spend", "api_spend", "auto_limit", "api_limit", "auto_percent_used", "api_percent_used", "total_percent_used")
        TOTAL_SPEND_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_SPEND_FIELD_NUMBER: _ClassVar[int]
        BONUS_SPEND_FIELD_NUMBER: _ClassVar[int]
        REMAINING_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        REMAINING_BONUS_FIELD_NUMBER: _ClassVar[int]
        BONUS_TOOLTIP_FIELD_NUMBER: _ClassVar[int]
        AUTO_SPEND_FIELD_NUMBER: _ClassVar[int]
        API_SPEND_FIELD_NUMBER: _ClassVar[int]
        AUTO_LIMIT_FIELD_NUMBER: _ClassVar[int]
        API_LIMIT_FIELD_NUMBER: _ClassVar[int]
        AUTO_PERCENT_USED_FIELD_NUMBER: _ClassVar[int]
        API_PERCENT_USED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PERCENT_USED_FIELD_NUMBER: _ClassVar[int]
        total_spend: int
        included_spend: int
        bonus_spend: int
        remaining: int
        limit: int
        remaining_bonus: bool
        bonus_tooltip: str
        auto_spend: int
        api_spend: int
        auto_limit: int
        api_limit: int
        auto_percent_used: float
        api_percent_used: float
        total_percent_used: float
        def __init__(self, total_spend: _Optional[int] = ..., included_spend: _Optional[int] = ..., bonus_spend: _Optional[int] = ..., remaining: _Optional[int] = ..., limit: _Optional[int] = ..., remaining_bonus: bool = ..., bonus_tooltip: _Optional[str] = ..., auto_spend: _Optional[int] = ..., api_spend: _Optional[int] = ..., auto_limit: _Optional[int] = ..., api_limit: _Optional[int] = ..., auto_percent_used: _Optional[float] = ..., api_percent_used: _Optional[float] = ..., total_percent_used: _Optional[float] = ...) -> None: ...
    class SpendLimitUsage(_message.Message):
        __slots__ = ("total_spend", "pooled_limit", "pooled_used", "pooled_remaining", "individual_limit", "individual_used", "individual_remaining", "limit_type", "overall_limit", "overall_used", "overall_remaining")
        TOTAL_SPEND_FIELD_NUMBER: _ClassVar[int]
        POOLED_LIMIT_FIELD_NUMBER: _ClassVar[int]
        POOLED_USED_FIELD_NUMBER: _ClassVar[int]
        POOLED_REMAINING_FIELD_NUMBER: _ClassVar[int]
        INDIVIDUAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
        INDIVIDUAL_USED_FIELD_NUMBER: _ClassVar[int]
        INDIVIDUAL_REMAINING_FIELD_NUMBER: _ClassVar[int]
        LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
        OVERALL_LIMIT_FIELD_NUMBER: _ClassVar[int]
        OVERALL_USED_FIELD_NUMBER: _ClassVar[int]
        OVERALL_REMAINING_FIELD_NUMBER: _ClassVar[int]
        total_spend: int
        pooled_limit: int
        pooled_used: int
        pooled_remaining: int
        individual_limit: int
        individual_used: int
        individual_remaining: int
        limit_type: str
        overall_limit: int
        overall_used: int
        overall_remaining: int
        def __init__(self, total_spend: _Optional[int] = ..., pooled_limit: _Optional[int] = ..., pooled_used: _Optional[int] = ..., pooled_remaining: _Optional[int] = ..., individual_limit: _Optional[int] = ..., individual_used: _Optional[int] = ..., individual_remaining: _Optional[int] = ..., limit_type: _Optional[str] = ..., overall_limit: _Optional[int] = ..., overall_used: _Optional[int] = ..., overall_remaining: _Optional[int] = ...) -> None: ...
    BILLING_CYCLE_START_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_END_FIELD_NUMBER: _ClassVar[int]
    PLAN_USAGE_FIELD_NUMBER: _ClassVar[int]
    SPEND_LIMIT_USAGE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FREE_BEST_OF_N_PROMOTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_MODEL_SELECTED_DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NAMED_MODEL_SELECTED_DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUTO_BUCKET_MODELS_FIELD_NUMBER: _ClassVar[int]
    billing_cycle_start: int
    billing_cycle_end: int
    plan_usage: GetCurrentPeriodUsageResponse.PlanUsage
    spend_limit_usage: GetCurrentPeriodUsageResponse.SpendLimitUsage
    display_threshold: int
    enabled: bool
    display_message: str
    free_best_of_n_promotion: GetCurrentPeriodUsageResponse.FreeBestOfNPromotion
    auto_model_selected_display_message: str
    named_model_selected_display_message: str
    auto_bucket_models: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, billing_cycle_start: _Optional[int] = ..., billing_cycle_end: _Optional[int] = ..., plan_usage: _Optional[_Union[GetCurrentPeriodUsageResponse.PlanUsage, _Mapping]] = ..., spend_limit_usage: _Optional[_Union[GetCurrentPeriodUsageResponse.SpendLimitUsage, _Mapping]] = ..., display_threshold: _Optional[int] = ..., enabled: bool = ..., display_message: _Optional[str] = ..., free_best_of_n_promotion: _Optional[_Union[GetCurrentPeriodUsageResponse.FreeBestOfNPromotion, _Mapping]] = ..., auto_model_selected_display_message: _Optional[str] = ..., named_model_selected_display_message: _Optional[str] = ..., auto_bucket_models: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDailySpendByCategoryRequest(_message.Message):
    __slots__ = ("team_id", "user_id", "period_start_ms", "period_end_ms", "group_by", "spend_type", "service_account_id", "cloud_agent_id", "automation_id", "automation_managed_type", "client_type", "products")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_MS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_MS_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SPEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_MANAGED_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    user_id: int
    period_start_ms: int
    period_end_ms: int
    group_by: SpendGroupByCategory
    spend_type: SpendType
    service_account_id: str
    cloud_agent_id: str
    automation_id: str
    automation_managed_type: str
    client_type: str
    products: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, team_id: _Optional[int] = ..., user_id: _Optional[int] = ..., period_start_ms: _Optional[int] = ..., period_end_ms: _Optional[int] = ..., group_by: _Optional[_Union[SpendGroupByCategory, str]] = ..., spend_type: _Optional[_Union[SpendType, str]] = ..., service_account_id: _Optional[str] = ..., cloud_agent_id: _Optional[str] = ..., automation_id: _Optional[str] = ..., automation_managed_type: _Optional[str] = ..., client_type: _Optional[str] = ..., products: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDailySpendByCategoryResponse(_message.Message):
    __slots__ = ("daily_spend", "categories", "effective_limit_cents")
    DAILY_SPEND_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_LIMIT_CENTS_FIELD_NUMBER: _ClassVar[int]
    daily_spend: _containers.RepeatedCompositeFieldContainer[DailySpendByCategory]
    categories: _containers.RepeatedScalarFieldContainer[str]
    effective_limit_cents: int
    def __init__(self, daily_spend: _Optional[_Iterable[_Union[DailySpendByCategory, _Mapping]]] = ..., categories: _Optional[_Iterable[str]] = ..., effective_limit_cents: _Optional[int] = ...) -> None: ...

class GetEffectiveUserPluginsRequest(_message.Message):
    __slots__ = ("use_replica", "team_id", "exclude_configured_variables")
    USE_REPLICA_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CONFIGURED_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    use_replica: bool
    team_id: int
    exclude_configured_variables: bool
    def __init__(self, use_replica: bool = ..., team_id: _Optional[int] = ..., exclude_configured_variables: bool = ...) -> None: ...

class GetEffectiveUserPluginsResponse(_message.Message):
    __slots__ = ("plugins", "marketplaces")
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACES_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[EffectivePlugin]
    marketplaces: _containers.RepeatedCompositeFieldContainer[Marketplace]
    def __init__(self, plugins: _Optional[_Iterable[_Union[EffectivePlugin, _Mapping]]] = ..., marketplaces: _Optional[_Iterable[_Union[Marketplace, _Mapping]]] = ...) -> None: ...

class GetFirstWindowStatsigDecisionRequest(_message.Message):
    __slots__ = ("operating_system",)
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    operating_system: ClientOS
    def __init__(self, operating_system: _Optional[_Union[ClientOS, str]] = ...) -> None: ...

class GetFirstWindowStatsigDecisionResponse(_message.Message):
    __slots__ = ("variant", "reason")
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    variant: str
    reason: str
    def __init__(self, variant: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class GetGrokBotAgentPluginFileRequest(_message.Message):
    __slots__ = ("agent_id", "plugin_id", "path")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    plugin_id: int
    path: str
    def __init__(self, agent_id: _Optional[str] = ..., plugin_id: _Optional[int] = ..., path: _Optional[str] = ...) -> None: ...

class GetGrokBotAgentPluginFileResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class GetGrokBotAgentPluginsRequest(_message.Message):
    __slots__ = ("agent_id", "include_mcp_config")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MCP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    include_mcp_config: bool
    def __init__(self, agent_id: _Optional[str] = ..., include_mcp_config: bool = ...) -> None: ...

class GetGrokBotAgentPluginsResponse(_message.Message):
    __slots__ = ("marketplace", "plugins")
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ...) -> None: ...

class GetGrokBotHarnessMigrationStatusInternalRequest(_message.Message):
    __slots__ = ("owner_auth_id",)
    OWNER_AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    owner_auth_id: str
    def __init__(self, owner_auth_id: _Optional[str] = ...) -> None: ...

class GetGrokBotHarnessMigrationStatusInternalResponse(_message.Message):
    __slots__ = ("rollout", "hold_state", "agents", "passes", "pass_history_available")
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    HOLD_STATE_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    PASSES_FIELD_NUMBER: _ClassVar[int]
    PASS_HISTORY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    rollout: GrokBotHarnessMigrationRolloutStatus
    hold_state: str
    agents: _containers.RepeatedCompositeFieldContainer[GrokBotHarnessMigrationAgentStatus]
    passes: _containers.RepeatedCompositeFieldContainer[GrokBotHarnessMigrationPassStatus]
    pass_history_available: bool
    def __init__(self, rollout: _Optional[_Union[GrokBotHarnessMigrationRolloutStatus, _Mapping]] = ..., hold_state: _Optional[str] = ..., agents: _Optional[_Iterable[_Union[GrokBotHarnessMigrationAgentStatus, _Mapping]]] = ..., passes: _Optional[_Iterable[_Union[GrokBotHarnessMigrationPassStatus, _Mapping]]] = ..., pass_history_available: bool = ...) -> None: ...

class GetGrokBotMarketplaceCategoryInternalRequest(_message.Message):
    __slots__ = ("category_id",)
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    def __init__(self, category_id: _Optional[int] = ...) -> None: ...

class GetGrokBotMarketplaceCreatorInternalRequest(_message.Message):
    __slots__ = ("creator_id",)
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    creator_id: int
    def __init__(self, creator_id: _Optional[int] = ...) -> None: ...

class GetGrokBotMarketplaceListingInternalRequest(_message.Message):
    __slots__ = ("listing_id",)
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    def __init__(self, listing_id: _Optional[int] = ...) -> None: ...

class GetGrokBotMarketplaceListingSourceTemplateInternalRequest(_message.Message):
    __slots__ = ("listing_id",)
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    def __init__(self, listing_id: _Optional[int] = ...) -> None: ...

class GetGrokBotMarketplaceListingSourceTemplateInternalResponse(_message.Message):
    __slots__ = ("recipe_json", "template_version_id", "version")
    RECIPE_JSON_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    recipe_json: str
    template_version_id: int
    version: int
    def __init__(self, recipe_json: _Optional[str] = ..., template_version_id: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class GetGrokBotMarketplaceListingTemplateInternalRequest(_message.Message):
    __slots__ = ("listing_id",)
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    def __init__(self, listing_id: _Optional[int] = ...) -> None: ...

class GetGrokBotMarketplaceListingTemplateInternalResponse(_message.Message):
    __slots__ = ("recipe_json",)
    RECIPE_JSON_FIELD_NUMBER: _ClassVar[int]
    recipe_json: str
    def __init__(self, recipe_json: _Optional[str] = ...) -> None: ...

class GetGrokBotRuntimeCapabilitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGrokBotRuntimeCapabilitiesResponse(_message.Message):
    __slots__ = ("capabilities",)
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: GrokBotRuntimeCapabilities
    def __init__(self, capabilities: _Optional[_Union[GrokBotRuntimeCapabilities, _Mapping]] = ...) -> None: ...

class GetGrokBotSendStatusRequest(_message.Message):
    __slots__ = ("agent_id", "message_id", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    message_id: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., message_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetGrokBotSendStatusResponse(_message.Message):
    __slots__ = ("status", "echo_entry_id", "rejection_code", "accepted_at_ms")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ECHO_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    REJECTION_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    status: GrokBotSendStatus
    echo_entry_id: str
    rejection_code: str
    accepted_at_ms: int
    def __init__(self, status: _Optional[_Union[GrokBotSendStatus, str]] = ..., echo_entry_id: _Optional[str] = ..., rejection_code: _Optional[str] = ..., accepted_at_ms: _Optional[int] = ...) -> None: ...

class GetGrokBotSlackInstallStateRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class GetGrokBotSlackInstallStateResponse(_message.Message):
    __slots__ = ("status", "slack_team_id", "workspace_name", "workspaces", "needs_manifest_update", "pending_reinstall_approval", "oauth_authorize_url", "approval_request_filed")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    NEEDS_MANIFEST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_REINSTALL_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    OAUTH_AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUEST_FILED_FIELD_NUMBER: _ClassVar[int]
    status: GrokBotSlackInstallStatus
    slack_team_id: str
    workspace_name: str
    workspaces: _containers.RepeatedCompositeFieldContainer[GrokBotSlackWorkspace]
    needs_manifest_update: bool
    pending_reinstall_approval: bool
    oauth_authorize_url: str
    approval_request_filed: bool
    def __init__(self, status: _Optional[_Union[GrokBotSlackInstallStatus, str]] = ..., slack_team_id: _Optional[str] = ..., workspace_name: _Optional[str] = ..., workspaces: _Optional[_Iterable[_Union[GrokBotSlackWorkspace, _Mapping]]] = ..., needs_manifest_update: bool = ..., pending_reinstall_approval: bool = ..., oauth_authorize_url: _Optional[str] = ..., approval_request_filed: bool = ...) -> None: ...

class GetGrokBotTemplateExportPolicyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGrokBotTemplateExportPolicyResponse(_message.Message):
    __slots__ = ("export_policy", "has_team")
    EXPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
    HAS_TEAM_FIELD_NUMBER: _ClassVar[int]
    export_policy: str
    has_team: bool
    def __init__(self, export_policy: _Optional[str] = ..., has_team: bool = ...) -> None: ...

class GetGrokBotTemplateForSourceAgentRequest(_message.Message):
    __slots__ = ("source_agent_id",)
    SOURCE_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    source_agent_id: str
    def __init__(self, source_agent_id: _Optional[str] = ...) -> None: ...

class GetGrokBotTemplateForSourceAgentResponse(_message.Message):
    __slots__ = ("template", "export_policy", "has_team")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
    HAS_TEAM_FIELD_NUMBER: _ClassVar[int]
    template: GrokBotTemplate
    export_policy: str
    has_team: bool
    def __init__(self, template: _Optional[_Union[GrokBotTemplate, _Mapping]] = ..., export_policy: _Optional[str] = ..., has_team: bool = ...) -> None: ...

class GetGrokBotTemplateImportDetailsRequest(_message.Message):
    __slots__ = ("share_id",)
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    def __init__(self, share_id: _Optional[str] = ...) -> None: ...

class GetGrokBotTemplateImportDetailsResponse(_message.Message):
    __slots__ = ("template", "blob_get_url", "expected_active_version", "creator_display_name")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    BLOB_GET_URL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATOR_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    template: GrokBotTemplate
    blob_get_url: str
    expected_active_version: int
    creator_display_name: str
    def __init__(self, template: _Optional[_Union[GrokBotTemplate, _Mapping]] = ..., blob_get_url: _Optional[str] = ..., expected_active_version: _Optional[int] = ..., creator_display_name: _Optional[str] = ...) -> None: ...

class GetGrokBotTemplateVersionRequest(_message.Message):
    __slots__ = ("share_id", "version")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    version: int
    def __init__(self, share_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class GetGrokBotTemplateVersionResponse(_message.Message):
    __slots__ = ("version", "active", "created_at_ms", "blob_object_key", "blob_get_url", "visibility")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    BLOB_OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    BLOB_GET_URL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    version: int
    active: bool
    created_at_ms: int
    blob_object_key: str
    blob_get_url: str
    visibility: GrokBotTemplateVisibility
    def __init__(self, version: _Optional[int] = ..., active: bool = ..., created_at_ms: _Optional[int] = ..., blob_object_key: _Optional[str] = ..., blob_get_url: _Optional[str] = ..., visibility: _Optional[_Union[GrokBotTemplateVisibility, str]] = ...) -> None: ...

class GetGrokBotUserMcpSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGrokBotUserMcpSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: GrokBotUserMcpSettings
    def __init__(self, settings: _Optional[_Union[GrokBotUserMcpSettings, _Mapping]] = ...) -> None: ...

class GetGrokBotUserRuntimeSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGrokBotUserRuntimeSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: GrokBotUserRuntimeSettings
    def __init__(self, settings: _Optional[_Union[GrokBotUserRuntimeSettings, _Mapping]] = ...) -> None: ...

class GetHardLimitRequest(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    def __init__(self, team_id: _Optional[int] = ...) -> None: ...

class GetHardLimitResponse(_message.Message):
    __slots__ = ("hard_limit", "no_usage_based_allowed", "hard_limit_per_user", "per_user_monthly_limit_dollars", "is_dynamic_team_limit", "has_pending_setup_onboarding_credit_claim", "is_setup_promo_active", "setup_promo_amount_cents", "setup_promo_credit_validity_days", "on_demand_spend_disabled_by_organization", "per_user_first_party_models_additional_budget_dollars", "per_user_first_party_models_additional_budget_unlimited")
    HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NO_USAGE_BASED_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    HARD_LIMIT_PER_USER_FIELD_NUMBER: _ClassVar[int]
    PER_USER_MONTHLY_LIMIT_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_TEAM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HAS_PENDING_SETUP_ONBOARDING_CREDIT_CLAIM_FIELD_NUMBER: _ClassVar[int]
    IS_SETUP_PROMO_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SETUP_PROMO_AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    SETUP_PROMO_CREDIT_VALIDITY_DAYS_FIELD_NUMBER: _ClassVar[int]
    ON_DEMAND_SPEND_DISABLED_BY_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    PER_USER_FIRST_PARTY_MODELS_ADDITIONAL_BUDGET_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    PER_USER_FIRST_PARTY_MODELS_ADDITIONAL_BUDGET_UNLIMITED_FIELD_NUMBER: _ClassVar[int]
    hard_limit: int
    no_usage_based_allowed: bool
    hard_limit_per_user: int
    per_user_monthly_limit_dollars: int
    is_dynamic_team_limit: bool
    has_pending_setup_onboarding_credit_claim: bool
    is_setup_promo_active: bool
    setup_promo_amount_cents: int
    setup_promo_credit_validity_days: int
    on_demand_spend_disabled_by_organization: bool
    per_user_first_party_models_additional_budget_dollars: int
    per_user_first_party_models_additional_budget_unlimited: bool
    def __init__(self, hard_limit: _Optional[int] = ..., no_usage_based_allowed: bool = ..., hard_limit_per_user: _Optional[int] = ..., per_user_monthly_limit_dollars: _Optional[int] = ..., is_dynamic_team_limit: bool = ..., has_pending_setup_onboarding_credit_claim: bool = ..., is_setup_promo_active: bool = ..., setup_promo_amount_cents: _Optional[int] = ..., setup_promo_credit_validity_days: _Optional[int] = ..., on_demand_spend_disabled_by_organization: bool = ..., per_user_first_party_models_additional_budget_dollars: _Optional[int] = ..., per_user_first_party_models_additional_budget_unlimited: bool = ...) -> None: ...

class GetManagedSkillsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetManagedSkillsResponse(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[ManagedSkill]
    def __init__(self, skills: _Optional[_Iterable[_Union[ManagedSkill, _Mapping]]] = ...) -> None: ...

class GetMcpConfigRequest(_message.Message):
    __slots__ = ("team_scope", "team_id", "redact_secrets")
    TEAM_SCOPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    REDACT_SECRETS_FIELD_NUMBER: _ClassVar[int]
    team_scope: bool
    team_id: int
    redact_secrets: bool
    def __init__(self, team_scope: bool = ..., team_id: _Optional[int] = ..., redact_secrets: bool = ...) -> None: ...

class GetMcpConfigResponse(_message.Message):
    __slots__ = ("config_json", "server_metadata_by_name")
    class ServerMetadataByNameEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: McpServerMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[McpServerMetadata, _Mapping]] = ...) -> None: ...
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    SERVER_METADATA_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    config_json: str
    server_metadata_by_name: _containers.MessageMap[str, McpServerMetadata]
    def __init__(self, config_json: _Optional[str] = ..., server_metadata_by_name: _Optional[_Mapping[str, McpServerMetadata]] = ...) -> None: ...

class GetMeRequest(_message.Message):
    __slots__ = ("team_id", "source_site_hostname", "include_mobile_app_status")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SITE_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MOBILE_APP_STATUS_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    source_site_hostname: str
    include_mobile_app_status: bool
    def __init__(self, team_id: _Optional[int] = ..., source_site_hostname: _Optional[str] = ..., include_mobile_app_status: bool = ...) -> None: ...

class GetMeResponse(_message.Message):
    __slots__ = ("auth_id", "user_id", "email", "first_name", "last_name", "workos_id", "team_id", "created_at", "is_enterprise_user", "team_name", "email_domain_type", "country", "profile_picture_url", "cursor_review_onboarding_use_cursor_github_app", "organization_id", "organization_public_id", "is_team_admin", "has_active_mobile_session", "public_user_id")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKOS_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ENTERPRISE_USER_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOMAIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    CURSOR_REVIEW_ONBOARDING_USE_CURSOR_GITHUB_APP_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_PUBLIC_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TEAM_ADMIN_FIELD_NUMBER: _ClassVar[int]
    HAS_ACTIVE_MOBILE_SESSION_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_USER_ID_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    user_id: int
    email: str
    first_name: str
    last_name: str
    workos_id: str
    team_id: int
    created_at: str
    is_enterprise_user: bool
    team_name: str
    email_domain_type: str
    country: str
    profile_picture_url: str
    cursor_review_onboarding_use_cursor_github_app: bool
    organization_id: int
    organization_public_id: str
    is_team_admin: bool
    has_active_mobile_session: bool
    public_user_id: str
    def __init__(self, auth_id: _Optional[str] = ..., user_id: _Optional[int] = ..., email: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., workos_id: _Optional[str] = ..., team_id: _Optional[int] = ..., created_at: _Optional[str] = ..., is_enterprise_user: bool = ..., team_name: _Optional[str] = ..., email_domain_type: _Optional[str] = ..., country: _Optional[str] = ..., profile_picture_url: _Optional[str] = ..., cursor_review_onboarding_use_cursor_github_app: bool = ..., organization_id: _Optional[int] = ..., organization_public_id: _Optional[str] = ..., is_team_admin: bool = ..., has_active_mobile_session: bool = ..., public_user_id: _Optional[str] = ...) -> None: ...

class GetMonthlyBillingCycleRequest(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    def __init__(self, team_id: _Optional[int] = ...) -> None: ...

class GetMonthlyBillingCycleResponse(_message.Message):
    __slots__ = ("start_date_epoch_millis", "end_date_epoch_millis")
    START_DATE_EPOCH_MILLIS_FIELD_NUMBER: _ClassVar[int]
    END_DATE_EPOCH_MILLIS_FIELD_NUMBER: _ClassVar[int]
    start_date_epoch_millis: int
    end_date_epoch_millis: int
    def __init__(self, start_date_epoch_millis: _Optional[int] = ..., end_date_epoch_millis: _Optional[int] = ...) -> None: ...

class GetOnePasswordStateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPluginMcpConfigRequest(_message.Message):
    __slots__ = ("plugin_id",)
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    def __init__(self, plugin_id: _Optional[int] = ...) -> None: ...

class GetPluginMcpConfigResponse(_message.Message):
    __slots__ = ("config_json", "commit_sha")
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    config_json: str
    commit_sha: str
    def __init__(self, config_json: _Optional[str] = ..., commit_sha: _Optional[str] = ...) -> None: ...

class GetPublicGrokBotMarketplaceListingRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetPublicGrokBotMarketplaceListingResponse(_message.Message):
    __slots__ = ("listing", "template_get_url")
    LISTING_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_GET_URL_FIELD_NUMBER: _ClassVar[int]
    listing: PublicGrokBotMarketplaceListing
    template_get_url: str
    def __init__(self, listing: _Optional[_Union[PublicGrokBotMarketplaceListing, _Mapping]] = ..., template_get_url: _Optional[str] = ...) -> None: ...

class GetPublicGrokBotTemplateRequest(_message.Message):
    __slots__ = ("share_id",)
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    def __init__(self, share_id: _Optional[str] = ...) -> None: ...

class GetPublicGrokBotTemplateResponse(_message.Message):
    __slots__ = ("template", "owner_display_name")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    template: GrokBotTemplate
    owner_display_name: str
    def __init__(self, template: _Optional[_Union[GrokBotTemplate, _Mapping]] = ..., owner_display_name: _Optional[str] = ...) -> None: ...

class GetSandAccessStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSandAccessStatusResponse(_message.Message):
    __slots__ = ("state", "purchase_channel", "block_reason", "purchasable_tiers", "is_paid_trial_plan", "unpaid_admin_needs_paid_seat", "privacy_disclaimer_required", "can_skip_onboarding", "pro_and_super_grok_plans_grant_access")
    class SandAccessBlockReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAND_ACCESS_BLOCK_REASON_UNSPECIFIED: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_NONE: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_TEAM_PRIVACY_MODE: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_TEAM_SETUP_REQUIRED: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_TEAM_ACCESS_REQUIRED: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_NOT_OFFERED: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_FREE_TRIAL_AVAILABLE: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_PAYWALL_INDIVIDUAL: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_PAYWALL_TEAM_MEMBER: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
        SAND_ACCESS_BLOCK_REASON_PAYWALL_TEAM_ADMIN: _ClassVar[GetSandAccessStatusResponse.SandAccessBlockReason]
    SAND_ACCESS_BLOCK_REASON_UNSPECIFIED: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_NONE: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_TEAM_PRIVACY_MODE: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_TEAM_SETUP_REQUIRED: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_TEAM_ACCESS_REQUIRED: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_NOT_OFFERED: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_FREE_TRIAL_AVAILABLE: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_PAYWALL_INDIVIDUAL: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_PAYWALL_TEAM_MEMBER: GetSandAccessStatusResponse.SandAccessBlockReason
    SAND_ACCESS_BLOCK_REASON_PAYWALL_TEAM_ADMIN: GetSandAccessStatusResponse.SandAccessBlockReason
    class SandAccessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAND_ACCESS_STATE_UNSPECIFIED: _ClassVar[GetSandAccessStatusResponse.SandAccessState]
        SAND_ACCESS_STATE_GRANTED: _ClassVar[GetSandAccessStatusResponse.SandAccessState]
        SAND_ACCESS_STATE_UNAVAILABLE: _ClassVar[GetSandAccessStatusResponse.SandAccessState]
        SAND_ACCESS_STATE_PAYMENT_REQUIRED: _ClassVar[GetSandAccessStatusResponse.SandAccessState]
    SAND_ACCESS_STATE_UNSPECIFIED: GetSandAccessStatusResponse.SandAccessState
    SAND_ACCESS_STATE_GRANTED: GetSandAccessStatusResponse.SandAccessState
    SAND_ACCESS_STATE_UNAVAILABLE: GetSandAccessStatusResponse.SandAccessState
    SAND_ACCESS_STATE_PAYMENT_REQUIRED: GetSandAccessStatusResponse.SandAccessState
    class SandPurchaseChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAND_PURCHASE_CHANNEL_UNSPECIFIED: _ClassVar[GetSandAccessStatusResponse.SandPurchaseChannel]
        SAND_PURCHASE_CHANNEL_IN_APP: _ClassVar[GetSandAccessStatusResponse.SandPurchaseChannel]
        SAND_PURCHASE_CHANNEL_MANAGE_IN_CURSOR: _ClassVar[GetSandAccessStatusResponse.SandPurchaseChannel]
        SAND_PURCHASE_CHANNEL_MANAGE_ON_WEB: _ClassVar[GetSandAccessStatusResponse.SandPurchaseChannel]
    SAND_PURCHASE_CHANNEL_UNSPECIFIED: GetSandAccessStatusResponse.SandPurchaseChannel
    SAND_PURCHASE_CHANNEL_IN_APP: GetSandAccessStatusResponse.SandPurchaseChannel
    SAND_PURCHASE_CHANNEL_MANAGE_IN_CURSOR: GetSandAccessStatusResponse.SandPurchaseChannel
    SAND_PURCHASE_CHANNEL_MANAGE_ON_WEB: GetSandAccessStatusResponse.SandPurchaseChannel
    STATE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    PURCHASABLE_TIERS_FIELD_NUMBER: _ClassVar[int]
    IS_PAID_TRIAL_PLAN_FIELD_NUMBER: _ClassVar[int]
    UNPAID_ADMIN_NEEDS_PAID_SEAT_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_DISCLAIMER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CAN_SKIP_ONBOARDING_FIELD_NUMBER: _ClassVar[int]
    PRO_AND_SUPER_GROK_PLANS_GRANT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    state: GetSandAccessStatusResponse.SandAccessState
    purchase_channel: GetSandAccessStatusResponse.SandPurchaseChannel
    block_reason: GetSandAccessStatusResponse.SandAccessBlockReason
    purchasable_tiers: _containers.RepeatedScalarFieldContainer[str]
    is_paid_trial_plan: bool
    unpaid_admin_needs_paid_seat: bool
    privacy_disclaimer_required: bool
    can_skip_onboarding: bool
    pro_and_super_grok_plans_grant_access: bool
    def __init__(self, state: _Optional[_Union[GetSandAccessStatusResponse.SandAccessState, str]] = ..., purchase_channel: _Optional[_Union[GetSandAccessStatusResponse.SandPurchaseChannel, str]] = ..., block_reason: _Optional[_Union[GetSandAccessStatusResponse.SandAccessBlockReason, str]] = ..., purchasable_tiers: _Optional[_Iterable[str]] = ..., is_paid_trial_plan: bool = ..., unpaid_admin_needs_paid_seat: bool = ..., privacy_disclaimer_required: bool = ..., can_skip_onboarding: bool = ..., pro_and_super_grok_plans_grant_access: bool = ...) -> None: ...

class GetSandBoxRunStateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSandBoxRunStateResponse(_message.Message):
    __slots__ = ("state", "image_update_available")
    STATE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    state: SandBoxRunState
    image_update_available: bool
    def __init__(self, state: _Optional[_Union[SandBoxRunState, str]] = ..., image_update_available: bool = ...) -> None: ...

class GetSandBoxUpgradeScheduleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSandBoxUpgradeScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: SandBoxUpgradeSchedule
    def __init__(self, schedule: _Optional[_Union[SandBoxUpgradeSchedule, _Mapping]] = ...) -> None: ...

class GetSandMachineMessagesEnabledRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class GetSandMachineMessagesEnabledResponse(_message.Message):
    __slots__ = ("messages_enabled",)
    MESSAGES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    messages_enabled: bool
    def __init__(self, messages_enabled: bool = ...) -> None: ...

class GetSandTrialClaimStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSandTrialClaimStatusResponse(_message.Message):
    __slots__ = ("status",)
    class SandTrialClaimStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAND_TRIAL_CLAIM_STATUS_UNSPECIFIED: _ClassVar[GetSandTrialClaimStatusResponse.SandTrialClaimStatus]
        SAND_TRIAL_CLAIM_STATUS_NONE: _ClassVar[GetSandTrialClaimStatusResponse.SandTrialClaimStatus]
        SAND_TRIAL_CLAIM_STATUS_PENDING_CARD: _ClassVar[GetSandTrialClaimStatusResponse.SandTrialClaimStatus]
        SAND_TRIAL_CLAIM_STATUS_GRANTED: _ClassVar[GetSandTrialClaimStatusResponse.SandTrialClaimStatus]
        SAND_TRIAL_CLAIM_STATUS_REJECTED_DUPLICATE_CARD: _ClassVar[GetSandTrialClaimStatusResponse.SandTrialClaimStatus]
        SAND_TRIAL_CLAIM_STATUS_BLOCKED: _ClassVar[GetSandTrialClaimStatusResponse.SandTrialClaimStatus]
    SAND_TRIAL_CLAIM_STATUS_UNSPECIFIED: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    SAND_TRIAL_CLAIM_STATUS_NONE: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    SAND_TRIAL_CLAIM_STATUS_PENDING_CARD: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    SAND_TRIAL_CLAIM_STATUS_GRANTED: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    SAND_TRIAL_CLAIM_STATUS_REJECTED_DUPLICATE_CARD: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    SAND_TRIAL_CLAIM_STATUS_BLOCKED: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: GetSandTrialClaimStatusResponse.SandTrialClaimStatus
    def __init__(self, status: _Optional[_Union[GetSandTrialClaimStatusResponse.SandTrialClaimStatus, str]] = ...) -> None: ...

class GetSandUsageStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSandUsageStatusResponse(_message.Message):
    __slots__ = ("current_period_start", "next_reset_timestamp_utc", "usage_percent", "included_limit_zero", "available_banked_reset_count", "uses_pooled_enterprise_allowance", "has_available_usage", "has_non_zero_included_limit", "upgrade_recommendation", "sand_trial_expires_at", "sand_trial_cancelable", "upgrade_recommendations", "on_demand_settings", "included_usage_super_grok_plan", "grok_plan_label", "is_team_seat", "cursor_plan_name")
    CURRENT_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    NEXT_RESET_TIMESTAMP_UTC_FIELD_NUMBER: _ClassVar[int]
    USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_LIMIT_ZERO_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_BANKED_RESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    USES_POOLED_ENTERPRISE_ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    HAS_AVAILABLE_USAGE_FIELD_NUMBER: _ClassVar[int]
    HAS_NON_ZERO_INCLUDED_LIMIT_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SAND_TRIAL_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    SAND_TRIAL_CANCELABLE_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    ON_DEMAND_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_USAGE_SUPER_GROK_PLAN_FIELD_NUMBER: _ClassVar[int]
    GROK_PLAN_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_TEAM_SEAT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    current_period_start: _timestamp_pb2.Timestamp
    next_reset_timestamp_utc: _timestamp_pb2.Timestamp
    usage_percent: float
    included_limit_zero: bool
    available_banked_reset_count: int
    uses_pooled_enterprise_allowance: bool
    has_available_usage: bool
    has_non_zero_included_limit: bool
    upgrade_recommendation: SandUpgradeRecommendation
    sand_trial_expires_at: _timestamp_pb2.Timestamp
    sand_trial_cancelable: bool
    upgrade_recommendations: _containers.RepeatedCompositeFieldContainer[SandUpgradeRecommendation]
    on_demand_settings: SandOnDemandSettings
    included_usage_super_grok_plan: str
    grok_plan_label: str
    is_team_seat: bool
    cursor_plan_name: str
    def __init__(self, current_period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_reset_timestamp_utc: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., usage_percent: _Optional[float] = ..., included_limit_zero: bool = ..., available_banked_reset_count: _Optional[int] = ..., uses_pooled_enterprise_allowance: bool = ..., has_available_usage: bool = ..., has_non_zero_included_limit: bool = ..., upgrade_recommendation: _Optional[_Union[SandUpgradeRecommendation, _Mapping]] = ..., sand_trial_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sand_trial_cancelable: bool = ..., upgrade_recommendations: _Optional[_Iterable[_Union[SandUpgradeRecommendation, _Mapping]]] = ..., on_demand_settings: _Optional[_Union[SandOnDemandSettings, _Mapping]] = ..., included_usage_super_grok_plan: _Optional[str] = ..., grok_plan_label: _Optional[str] = ..., is_team_seat: bool = ..., cursor_plan_name: _Optional[str] = ...) -> None: ...

class GetTeamAdminSettingsRequest(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    def __init__(self, team_id: _Optional[int] = ...) -> None: ...

class GetTeamAdminSettingsResponse(_message.Message):
    __slots__ = ("allowed_models", "blocked_models", "auto_run_controls", "cursor_ignore_controls", "dot_cursor_protection", "allowed_mcp_configuration", "background_agent_settings", "cli_settings", "mcp_controls", "prompt_deeplink_controls", "command_deeplink_controls", "deeplink_controls", "github_integration_settings", "slack_integration_settings", "linear_integration_settings", "workspace_trust_controls", "gitlab_integration_settings", "browser_features", "byok_disabled", "dashboard_analytics_requires_admin", "shared_conversation_settings", "allowed_extensions", "browser_origin_allowlist", "disable_conversation_insights", "cursor_blame_settings", "network_denylist", "network_allowlist", "extension_signing_settings", "enforce_invite_domain_on_accept", "first_party_plugin_configuration", "attribution_controls", "allow_third_party_plugin_imports", "glass_settings", "new_chat_model_reset_settings", "model_allowlist", "jira_integration_settings", "pull_request_preferences", "browser_settings", "cloud_agent_egress_allowlist", "mirror_sandbox_allowlist_for_egress", "remote_permissions_file_path", "shared_canvas_settings", "invite_link_max_ttl_seconds", "allow_user_local_plugin_imports", "local_permissions_file_path", "remote_permissions_file_paths", "permissions_file_overrides_auto_run", "extension_install_cooldown_settings", "auto_review", "public_profile_settings", "bitbucket_integration_settings", "marketplace_leaderboard_disabled", "new_chat_nudge_all_to_smart_auto", "models_auto_only", "new_chat_nudge_all_to_smart_auto_optimize_for", "restrict_invites_to_admins", "viewer_can_invite_members", "enforce_hooks_readiness", "llm_gateway", "local_tool_controls", "sand_action_audit_settings", "sand_onboarding", "origin_disabled", "sand_network_controls", "user_agent_store_skills_sync_settings", "auto_review_run_mode_reset", "enterprise_grok_bot_trial_available", "sand_group_access_mode", "sand_auto_review_controls", "private_inference", "remote_control_v2_policy", "sand_local_egress_controls")
    ALLOWED_MODELS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_MODELS_FIELD_NUMBER: _ClassVar[int]
    AUTO_RUN_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_IGNORE_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    DOT_CURSOR_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MCP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_AGENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MCP_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_DEEPLINK_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_DEEPLINK_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    DEEPLINK_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    GITHUB_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SLACK_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LINEAR_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_TRUST_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    GITLAB_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BROWSER_FEATURES_FIELD_NUMBER: _ClassVar[int]
    BYOK_DISABLED_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ANALYTICS_REQUIRES_ADMIN_FIELD_NUMBER: _ClassVar[int]
    SHARED_CONVERSATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    BROWSER_ORIGIN_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CONVERSATION_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_BLAME_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_DENYLIST_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_SIGNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_INVITE_DOMAIN_ON_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    FIRST_PARTY_PLUGIN_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_THIRD_PARTY_PLUGIN_IMPORTS_FIELD_NUMBER: _ClassVar[int]
    GLASS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEW_CHAT_MODEL_RESET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    JIRA_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    BROWSER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_AGENT_EGRESS_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    MIRROR_SANDBOX_ALLOWLIST_FOR_EGRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PERMISSIONS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SHARED_CANVAS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INVITE_LINK_MAX_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_USER_LOCAL_PLUGIN_IMPORTS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PERMISSIONS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PERMISSIONS_FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FILE_OVERRIDES_AUTO_RUN_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_INSTALL_COOLDOWN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUTO_REVIEW_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_PROFILE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BITBUCKET_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_LEADERBOARD_DISABLED_FIELD_NUMBER: _ClassVar[int]
    NEW_CHAT_NUDGE_ALL_TO_SMART_AUTO_FIELD_NUMBER: _ClassVar[int]
    MODELS_AUTO_ONLY_FIELD_NUMBER: _ClassVar[int]
    NEW_CHAT_NUDGE_ALL_TO_SMART_AUTO_OPTIMIZE_FOR_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_INVITES_TO_ADMINS_FIELD_NUMBER: _ClassVar[int]
    VIEWER_CAN_INVITE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_HOOKS_READINESS_FIELD_NUMBER: _ClassVar[int]
    LLM_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOOL_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    SAND_ACTION_AUDIT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SAND_ONBOARDING_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SAND_NETWORK_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_STORE_SKILLS_SYNC_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUTO_REVIEW_RUN_MODE_RESET_FIELD_NUMBER: _ClassVar[int]
    ENTERPRISE_GROK_BOT_TRIAL_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SAND_GROUP_ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    SAND_AUTO_REVIEW_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_INFERENCE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_V2_POLICY_FIELD_NUMBER: _ClassVar[int]
    SAND_LOCAL_EGRESS_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    allowed_models: _containers.RepeatedScalarFieldContainer[str]
    blocked_models: _containers.RepeatedScalarFieldContainer[str]
    auto_run_controls: AutoRunControls
    cursor_ignore_controls: CursorIgnoreControls
    dot_cursor_protection: bool
    allowed_mcp_configuration: AllowedMCPConfiguration
    background_agent_settings: BackgroundAgentSettings
    cli_settings: CliSettings
    mcp_controls: MCPControls
    prompt_deeplink_controls: PromptDeeplinkControls
    command_deeplink_controls: CommandDeeplinkControls
    deeplink_controls: DeeplinkControls
    github_integration_settings: GithubIntegrationSettings
    slack_integration_settings: SlackIntegrationSettings
    linear_integration_settings: LinearIntegrationSettings
    workspace_trust_controls: WorkspaceTrustControls
    gitlab_integration_settings: GitlabIntegrationSettings
    browser_features: bool
    byok_disabled: bool
    dashboard_analytics_requires_admin: bool
    shared_conversation_settings: SharedConversationSettings
    allowed_extensions: str
    browser_origin_allowlist: _containers.RepeatedScalarFieldContainer[str]
    disable_conversation_insights: bool
    cursor_blame_settings: CursorBlameSettings
    network_denylist: _containers.RepeatedScalarFieldContainer[str]
    network_allowlist: _containers.RepeatedScalarFieldContainer[str]
    extension_signing_settings: ExtensionSigningSettings
    enforce_invite_domain_on_accept: bool
    first_party_plugin_configuration: FirstPartyPluginConfiguration
    attribution_controls: AttributionControls
    allow_third_party_plugin_imports: bool
    glass_settings: GlassSettings
    new_chat_model_reset_settings: TeamAdminNewChatModelResetSettings
    model_allowlist: ModelAllowlist
    jira_integration_settings: JiraIntegrationSettings
    pull_request_preferences: PullRequestPreferences
    browser_settings: BrowserSettings
    cloud_agent_egress_allowlist: _containers.RepeatedScalarFieldContainer[str]
    mirror_sandbox_allowlist_for_egress: bool
    remote_permissions_file_path: str
    shared_canvas_settings: SharedCanvasSettings
    invite_link_max_ttl_seconds: int
    allow_user_local_plugin_imports: bool
    local_permissions_file_path: _containers.RepeatedScalarFieldContainer[str]
    remote_permissions_file_paths: _containers.RepeatedScalarFieldContainer[str]
    permissions_file_overrides_auto_run: bool
    extension_install_cooldown_settings: ExtensionInstallCooldownSettings
    auto_review: AutoReviewInstructions
    public_profile_settings: PublicProfileSettings
    bitbucket_integration_settings: BitbucketIntegrationSettings
    marketplace_leaderboard_disabled: bool
    new_chat_nudge_all_to_smart_auto: bool
    models_auto_only: bool
    new_chat_nudge_all_to_smart_auto_optimize_for: str
    restrict_invites_to_admins: bool
    viewer_can_invite_members: bool
    enforce_hooks_readiness: bool
    llm_gateway: LlmGatewaySettings
    local_tool_controls: LocalToolControls
    sand_action_audit_settings: SandActionAuditSettings
    sand_onboarding: SandOnboardingState
    origin_disabled: bool
    sand_network_controls: SandNetworkControls
    user_agent_store_skills_sync_settings: UserAgentStoreSkillsSyncSettings
    auto_review_run_mode_reset: AutoReviewRunModeReset
    enterprise_grok_bot_trial_available: bool
    sand_group_access_mode: SandGroupAccessMode
    sand_auto_review_controls: SandAutoReviewControls
    private_inference: PrivateInferenceSettings
    remote_control_v2_policy: RemoteControlV2Policy
    sand_local_egress_controls: SandLocalEgressControls
    def __init__(self, allowed_models: _Optional[_Iterable[str]] = ..., blocked_models: _Optional[_Iterable[str]] = ..., auto_run_controls: _Optional[_Union[AutoRunControls, _Mapping]] = ..., cursor_ignore_controls: _Optional[_Union[CursorIgnoreControls, _Mapping]] = ..., dot_cursor_protection: bool = ..., allowed_mcp_configuration: _Optional[_Union[AllowedMCPConfiguration, _Mapping]] = ..., background_agent_settings: _Optional[_Union[BackgroundAgentSettings, _Mapping]] = ..., cli_settings: _Optional[_Union[CliSettings, _Mapping]] = ..., mcp_controls: _Optional[_Union[MCPControls, _Mapping]] = ..., prompt_deeplink_controls: _Optional[_Union[PromptDeeplinkControls, _Mapping]] = ..., command_deeplink_controls: _Optional[_Union[CommandDeeplinkControls, _Mapping]] = ..., deeplink_controls: _Optional[_Union[DeeplinkControls, _Mapping]] = ..., github_integration_settings: _Optional[_Union[GithubIntegrationSettings, _Mapping]] = ..., slack_integration_settings: _Optional[_Union[SlackIntegrationSettings, _Mapping]] = ..., linear_integration_settings: _Optional[_Union[LinearIntegrationSettings, _Mapping]] = ..., workspace_trust_controls: _Optional[_Union[WorkspaceTrustControls, _Mapping]] = ..., gitlab_integration_settings: _Optional[_Union[GitlabIntegrationSettings, _Mapping]] = ..., browser_features: bool = ..., byok_disabled: bool = ..., dashboard_analytics_requires_admin: bool = ..., shared_conversation_settings: _Optional[_Union[SharedConversationSettings, _Mapping]] = ..., allowed_extensions: _Optional[str] = ..., browser_origin_allowlist: _Optional[_Iterable[str]] = ..., disable_conversation_insights: bool = ..., cursor_blame_settings: _Optional[_Union[CursorBlameSettings, _Mapping]] = ..., network_denylist: _Optional[_Iterable[str]] = ..., network_allowlist: _Optional[_Iterable[str]] = ..., extension_signing_settings: _Optional[_Union[ExtensionSigningSettings, _Mapping]] = ..., enforce_invite_domain_on_accept: bool = ..., first_party_plugin_configuration: _Optional[_Union[FirstPartyPluginConfiguration, _Mapping]] = ..., attribution_controls: _Optional[_Union[AttributionControls, _Mapping]] = ..., allow_third_party_plugin_imports: bool = ..., glass_settings: _Optional[_Union[GlassSettings, _Mapping]] = ..., new_chat_model_reset_settings: _Optional[_Union[TeamAdminNewChatModelResetSettings, _Mapping]] = ..., model_allowlist: _Optional[_Union[ModelAllowlist, _Mapping]] = ..., jira_integration_settings: _Optional[_Union[JiraIntegrationSettings, _Mapping]] = ..., pull_request_preferences: _Optional[_Union[PullRequestPreferences, _Mapping]] = ..., browser_settings: _Optional[_Union[BrowserSettings, _Mapping]] = ..., cloud_agent_egress_allowlist: _Optional[_Iterable[str]] = ..., mirror_sandbox_allowlist_for_egress: bool = ..., remote_permissions_file_path: _Optional[str] = ..., shared_canvas_settings: _Optional[_Union[SharedCanvasSettings, _Mapping]] = ..., invite_link_max_ttl_seconds: _Optional[int] = ..., allow_user_local_plugin_imports: bool = ..., local_permissions_file_path: _Optional[_Iterable[str]] = ..., remote_permissions_file_paths: _Optional[_Iterable[str]] = ..., permissions_file_overrides_auto_run: bool = ..., extension_install_cooldown_settings: _Optional[_Union[ExtensionInstallCooldownSettings, _Mapping]] = ..., auto_review: _Optional[_Union[AutoReviewInstructions, _Mapping]] = ..., public_profile_settings: _Optional[_Union[PublicProfileSettings, _Mapping]] = ..., bitbucket_integration_settings: _Optional[_Union[BitbucketIntegrationSettings, _Mapping]] = ..., marketplace_leaderboard_disabled: bool = ..., new_chat_nudge_all_to_smart_auto: bool = ..., models_auto_only: bool = ..., new_chat_nudge_all_to_smart_auto_optimize_for: _Optional[str] = ..., restrict_invites_to_admins: bool = ..., viewer_can_invite_members: bool = ..., enforce_hooks_readiness: bool = ..., llm_gateway: _Optional[_Union[LlmGatewaySettings, _Mapping]] = ..., local_tool_controls: _Optional[_Union[LocalToolControls, _Mapping]] = ..., sand_action_audit_settings: _Optional[_Union[SandActionAuditSettings, _Mapping]] = ..., sand_onboarding: _Optional[_Union[SandOnboardingState, _Mapping]] = ..., origin_disabled: bool = ..., sand_network_controls: _Optional[_Union[SandNetworkControls, _Mapping]] = ..., user_agent_store_skills_sync_settings: _Optional[_Union[UserAgentStoreSkillsSyncSettings, _Mapping]] = ..., auto_review_run_mode_reset: _Optional[_Union[AutoReviewRunModeReset, _Mapping]] = ..., enterprise_grok_bot_trial_available: bool = ..., sand_group_access_mode: _Optional[_Union[SandGroupAccessMode, str]] = ..., sand_auto_review_controls: _Optional[_Union[SandAutoReviewControls, _Mapping]] = ..., private_inference: _Optional[_Union[PrivateInferenceSettings, _Mapping]] = ..., remote_control_v2_policy: _Optional[_Union[RemoteControlV2Policy, _Mapping]] = ..., sand_local_egress_controls: _Optional[_Union[SandLocalEgressControls, _Mapping]] = ...) -> None: ...

class GetTeamMemberSandBoxMigrationStatusRequest(_message.Message):
    __slots__ = ("team_id", "user_id", "operation_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    user_id: int
    operation_id: str
    def __init__(self, team_id: _Optional[int] = ..., user_id: _Optional[int] = ..., operation_id: _Optional[str] = ...) -> None: ...

class GetTeamMemberSandBoxMigrationStatusResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: SandBoxMigrationEvent
    def __init__(self, event: _Optional[_Union[SandBoxMigrationEvent, _Mapping]] = ...) -> None: ...

class GetTeamMembersRequest(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    def __init__(self, team_id: _Optional[int] = ...) -> None: ...

class GetTeamMembersResponse(_message.Message):
    __slots__ = ("team_members", "user_id", "is_scim_synced")
    TEAM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SCIM_SYNCED_FIELD_NUMBER: _ClassVar[int]
    team_members: _containers.RepeatedCompositeFieldContainer[TeamMember]
    user_id: int
    is_scim_synced: bool
    def __init__(self, team_members: _Optional[_Iterable[_Union[TeamMember, _Mapping]]] = ..., user_id: _Optional[int] = ..., is_scim_synced: bool = ...) -> None: ...

class GetTeamPluginPopularityRequest(_message.Message):
    __slots__ = ("team_id", "use_replica")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USE_REPLICA_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    use_replica: bool
    def __init__(self, team_id: _Optional[int] = ..., use_replica: bool = ...) -> None: ...

class GetTeamPluginPopularityResponse(_message.Message):
    __slots__ = ("counts",)
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    counts: _containers.RepeatedCompositeFieldContainer[TeamPluginPopularityCount]
    def __init__(self, counts: _Optional[_Iterable[_Union[TeamPluginPopularityCount, _Mapping]]] = ...) -> None: ...

class GetTeamsRequest(_message.Message):
    __slots__ = ("active_only",)
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    active_only: bool
    def __init__(self, active_only: bool = ...) -> None: ...

class GetTeamsResponse(_message.Message):
    __slots__ = ("teams",)
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    teams: _containers.RepeatedCompositeFieldContainer[Team]
    def __init__(self, teams: _Optional[_Iterable[_Union[Team, _Mapping]]] = ...) -> None: ...

class GetUserPrivacyModeRequest(_message.Message):
    __slots__ = ("inferred_privacy_mode", "team_id")
    INFERRED_PRIVACY_MODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    inferred_privacy_mode: PrivacyMode
    team_id: int
    def __init__(self, inferred_privacy_mode: _Optional[_Union[PrivacyMode, str]] = ..., team_id: _Optional[int] = ...) -> None: ...

class GetUserPrivacyModeResponse(_message.Message):
    __slots__ = ("privacy_mode", "hours_remaining_in_grace_period", "is_enforced_by_team", "is_not_migrated_to_server_source_of_truth", "partner_data_share", "has_acknowledged_grace_period_disclaimer")
    PRIVACY_MODE_FIELD_NUMBER: _ClassVar[int]
    HOURS_REMAINING_IN_GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    IS_ENFORCED_BY_TEAM_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_MIGRATED_TO_SERVER_SOURCE_OF_TRUTH_FIELD_NUMBER: _ClassVar[int]
    PARTNER_DATA_SHARE_FIELD_NUMBER: _ClassVar[int]
    HAS_ACKNOWLEDGED_GRACE_PERIOD_DISCLAIMER_FIELD_NUMBER: _ClassVar[int]
    privacy_mode: PrivacyMode
    hours_remaining_in_grace_period: int
    is_enforced_by_team: bool
    is_not_migrated_to_server_source_of_truth: bool
    partner_data_share: bool
    has_acknowledged_grace_period_disclaimer: bool
    def __init__(self, privacy_mode: _Optional[_Union[PrivacyMode, str]] = ..., hours_remaining_in_grace_period: _Optional[int] = ..., is_enforced_by_team: bool = ..., is_not_migrated_to_server_source_of_truth: bool = ..., partner_data_share: bool = ..., has_acknowledged_grace_period_disclaimer: bool = ...) -> None: ...

class GithubIntegrationSettings(_message.Message):
    __slots__ = ("hidden",)
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    def __init__(self, hidden: bool = ...) -> None: ...

class GitlabIntegrationSettings(_message.Message):
    __slots__ = ("hidden",)
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    def __init__(self, hidden: bool = ...) -> None: ...

class GlassSettings(_message.Message):
    __slots__ = ("allowed_user_ids", "allow_all_team_members")
    ALLOWED_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_TEAM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    allowed_user_ids: _containers.RepeatedScalarFieldContainer[int]
    allow_all_team_members: bool
    def __init__(self, allowed_user_ids: _Optional[_Iterable[int]] = ..., allow_all_team_members: bool = ...) -> None: ...

class GrokBotAccountAutomationGroup(_message.Message):
    __slots__ = ("agent_id", "automations", "unavailable", "read_individually")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    READ_INDIVIDUALLY_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    automations: _containers.RepeatedCompositeFieldContainer[GrokBotAgentAutomation]
    unavailable: bool
    read_individually: bool
    def __init__(self, agent_id: _Optional[str] = ..., automations: _Optional[_Iterable[_Union[GrokBotAgentAutomation, _Mapping]]] = ..., unavailable: bool = ..., read_individually: bool = ...) -> None: ...

class GrokBotAgent(_message.Message):
    __slots__ = ("id", "legacy_agent_id", "name", "description", "title", "avatar_shape", "avatar_color", "avatar_version", "avatar_url", "created_at_ms", "updated_at_ms", "agent_id", "harness", "role", "visibility", "team_id", "viewer_is_owner", "viewer_session_id", "kind", "member_agent_ids", "owner_display_name", "people")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    AVATAR_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWER_IS_OWNER_FIELD_NUMBER: _ClassVar[int]
    VIEWER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    OWNER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    legacy_agent_id: str
    name: str
    description: str
    title: str
    avatar_shape: str
    avatar_color: str
    avatar_version: str
    avatar_url: str
    created_at_ms: int
    updated_at_ms: int
    agent_id: str
    harness: str
    role: str
    visibility: GrokBotAgentVisibility
    team_id: int
    viewer_is_owner: bool
    viewer_session_id: str
    kind: GrokBotAgentKind
    member_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    owner_display_name: str
    people: _containers.RepeatedCompositeFieldContainer[GrokBotRoomPerson]
    def __init__(self, id: _Optional[str] = ..., legacy_agent_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., avatar_version: _Optional[str] = ..., avatar_url: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., agent_id: _Optional[str] = ..., harness: _Optional[str] = ..., role: _Optional[str] = ..., visibility: _Optional[_Union[GrokBotAgentVisibility, str]] = ..., team_id: _Optional[int] = ..., viewer_is_owner: bool = ..., viewer_session_id: _Optional[str] = ..., kind: _Optional[_Union[GrokBotAgentKind, str]] = ..., member_agent_ids: _Optional[_Iterable[str]] = ..., owner_display_name: _Optional[str] = ..., people: _Optional[_Iterable[_Union[GrokBotRoomPerson, _Mapping]]] = ...) -> None: ...

class GrokBotAgentAutomation(_message.Message):
    __slots__ = ("automation_id", "record_json")
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_JSON_FIELD_NUMBER: _ClassVar[int]
    automation_id: str
    record_json: str
    def __init__(self, automation_id: _Optional[str] = ..., record_json: _Optional[str] = ...) -> None: ...

class GrokBotAgentAwaitingState(_message.Message):
    __slots__ = ("tab_id", "reason", "since_ms")
    TAB_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SINCE_MS_FIELD_NUMBER: _ClassVar[int]
    tab_id: str
    reason: str
    since_ms: int
    def __init__(self, tab_id: _Optional[str] = ..., reason: _Optional[str] = ..., since_ms: _Optional[int] = ...) -> None: ...

class GrokBotAgentClientState(_message.Message):
    __slots__ = ("agent_id", "last_viewed_at_ms", "unread_count", "last_activity_at_ms", "last_entry_id", "last_entry_kind", "last_message_id", "last_message_preview", "notifications_enabled", "notify_on_updates_enabled", "hidden_from_sidebar", "updated_at_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_VIEWED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ENTRY_KIND_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ON_UPDATES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FROM_SIDEBAR_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    last_viewed_at_ms: int
    unread_count: int
    last_activity_at_ms: int
    last_entry_id: str
    last_entry_kind: str
    last_message_id: str
    last_message_preview: str
    notifications_enabled: bool
    notify_on_updates_enabled: bool
    hidden_from_sidebar: bool
    updated_at_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., last_viewed_at_ms: _Optional[int] = ..., unread_count: _Optional[int] = ..., last_activity_at_ms: _Optional[int] = ..., last_entry_id: _Optional[str] = ..., last_entry_kind: _Optional[str] = ..., last_message_id: _Optional[str] = ..., last_message_preview: _Optional[str] = ..., notifications_enabled: bool = ..., notify_on_updates_enabled: bool = ..., hidden_from_sidebar: bool = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotAgentDefinition(_message.Message):
    __slots__ = ("sessions", "room_members", "member_of_rooms", "template_imports", "memory_shards", "routines", "recipe_skills", "mcp_settings", "mcp_servers")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ROOM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OF_ROOMS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_IMPORTS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SHARDS_FIELD_NUMBER: _ClassVar[int]
    ROUTINES_FIELD_NUMBER: _ClassVar[int]
    RECIPE_SKILLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionSession]
    room_members: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionAgentRef]
    member_of_rooms: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionAgentRef]
    template_imports: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionTemplateImport]
    memory_shards: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionMemoryShard]
    routines: _containers.RepeatedCompositeFieldContainer[GrokBotAgentAutomation]
    recipe_skills: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionSkill]
    mcp_settings: GrokBotUserMcpSettings
    mcp_servers: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionMcpServer]
    def __init__(self, sessions: _Optional[_Iterable[_Union[GrokBotAgentDefinitionSession, _Mapping]]] = ..., room_members: _Optional[_Iterable[_Union[GrokBotAgentDefinitionAgentRef, _Mapping]]] = ..., member_of_rooms: _Optional[_Iterable[_Union[GrokBotAgentDefinitionAgentRef, _Mapping]]] = ..., template_imports: _Optional[_Iterable[_Union[GrokBotAgentDefinitionTemplateImport, _Mapping]]] = ..., memory_shards: _Optional[_Iterable[_Union[GrokBotAgentDefinitionMemoryShard, _Mapping]]] = ..., routines: _Optional[_Iterable[_Union[GrokBotAgentAutomation, _Mapping]]] = ..., recipe_skills: _Optional[_Iterable[_Union[GrokBotAgentDefinitionSkill, _Mapping]]] = ..., mcp_settings: _Optional[_Union[GrokBotUserMcpSettings, _Mapping]] = ..., mcp_servers: _Optional[_Iterable[_Union[GrokBotAgentDefinitionMcpServer, _Mapping]]] = ...) -> None: ...

class GrokBotAgentDefinitionAgentRef(_message.Message):
    __slots__ = ("id", "agent_id", "name", "harness", "kind")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    name: str
    harness: str
    kind: str
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., name: _Optional[str] = ..., harness: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class GrokBotAgentDefinitionIdentity(_message.Message):
    __slots__ = ("id", "agent_id", "legacy_agent_id", "auth_id", "user_id", "name", "description", "title", "role", "avatar_shape", "avatar_color", "has_custom_avatar", "harness", "kind", "visibility", "team_id", "created_at_ms", "updated_at_ms", "deleted_at_ms", "slack")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    HAS_CUSTOM_AVATAR_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SLACK_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    legacy_agent_id: str
    auth_id: str
    user_id: int
    name: str
    description: str
    title: str
    role: str
    avatar_shape: str
    avatar_color: str
    has_custom_avatar: bool
    harness: str
    kind: str
    visibility: str
    team_id: int
    created_at_ms: int
    updated_at_ms: int
    deleted_at_ms: int
    slack: GrokBotAgentDefinitionSlack
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., legacy_agent_id: _Optional[str] = ..., auth_id: _Optional[str] = ..., user_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., role: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., has_custom_avatar: bool = ..., harness: _Optional[str] = ..., kind: _Optional[str] = ..., visibility: _Optional[str] = ..., team_id: _Optional[int] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., deleted_at_ms: _Optional[int] = ..., slack: _Optional[_Union[GrokBotAgentDefinitionSlack, _Mapping]] = ...) -> None: ...

class GrokBotAgentDefinitionMcpServer(_message.Message):
    __slots__ = ("id", "name", "type", "scope", "plugin_id", "created_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    scope: str
    plugin_id: str
    created_at_ms: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., scope: _Optional[str] = ..., plugin_id: _Optional[str] = ..., created_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotAgentDefinitionMemoryShard(_message.Message):
    __slots__ = ("scope", "scope_key", "version", "box_backfilled", "updated_at_ms", "folder")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BOX_BACKFILLED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    scope: str
    scope_key: str
    version: int
    box_backfilled: bool
    updated_at_ms: int
    folder: GrokBotMemoryFolder
    def __init__(self, scope: _Optional[str] = ..., scope_key: _Optional[str] = ..., version: _Optional[int] = ..., box_backfilled: bool = ..., updated_at_ms: _Optional[int] = ..., folder: _Optional[_Union[GrokBotMemoryFolder, _Mapping]] = ...) -> None: ...

class GrokBotAgentDefinitionSession(_message.Message):
    __slots__ = ("session_id", "kind", "created_at_ms", "updated_at_ms", "last_activity_at_ms", "box_key")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    kind: str
    created_at_ms: int
    updated_at_ms: int
    last_activity_at_ms: int
    box_key: str
    def __init__(self, session_id: _Optional[str] = ..., kind: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., last_activity_at_ms: _Optional[int] = ..., box_key: _Optional[str] = ...) -> None: ...

class GrokBotAgentDefinitionSkill(_message.Message):
    __slots__ = ("id", "description", "content")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    content: str
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class GrokBotAgentDefinitionSlack(_message.Message):
    __slots__ = ("linked", "app_id", "bot_user_id", "team_id", "workspace_name", "linked_at_ms", "pending_admin_approval", "pending_reinstall")
    LINKED_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    BOT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    LINKED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    PENDING_ADMIN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    PENDING_REINSTALL_FIELD_NUMBER: _ClassVar[int]
    linked: bool
    app_id: str
    bot_user_id: str
    team_id: str
    workspace_name: str
    linked_at_ms: int
    pending_admin_approval: bool
    pending_reinstall: bool
    def __init__(self, linked: bool = ..., app_id: _Optional[str] = ..., bot_user_id: _Optional[str] = ..., team_id: _Optional[str] = ..., workspace_name: _Optional[str] = ..., linked_at_ms: _Optional[int] = ..., pending_admin_approval: bool = ..., pending_reinstall: bool = ...) -> None: ...

class GrokBotAgentDefinitionTemplateImport(_message.Message):
    __slots__ = ("template_id", "template_version_id", "import_type", "imported_at_ms", "template_name", "template_version", "share_id")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    template_version_id: str
    import_type: str
    imported_at_ms: int
    template_name: str
    template_version: int
    share_id: str
    def __init__(self, template_id: _Optional[str] = ..., template_version_id: _Optional[str] = ..., import_type: _Optional[str] = ..., imported_at_ms: _Optional[int] = ..., template_name: _Optional[str] = ..., template_version: _Optional[int] = ..., share_id: _Optional[str] = ...) -> None: ...

class GrokBotAgentInlinePlugin(_message.Message):
    __slots__ = ("name", "display_name", "description", "mcp_config_json")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    mcp_config_json: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., mcp_config_json: _Optional[str] = ...) -> None: ...

class GrokBotAgentLiveActivity(_message.Message):
    __slots__ = ("kind", "tool", "detail", "target", "call_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    kind: str
    tool: str
    detail: str
    target: str
    call_id: str
    def __init__(self, kind: _Optional[str] = ..., tool: _Optional[str] = ..., detail: _Optional[str] = ..., target: _Optional[str] = ..., call_id: _Optional[str] = ...) -> None: ...

class GrokBotAgentLiveState(_message.Message):
    __slots__ = ("agent_id", "is_running", "is_composing_message", "is_retrying", "activity", "awaiting", "updated_at_ms", "stale_after_ms", "box_handoff_request_id", "box_handoff_instruction", "session_id", "active_group_member_id", "has_running_subagents")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    IS_COMPOSING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_RETRYING_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    AWAITING_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    STALE_AFTER_MS_FIELD_NUMBER: _ClassVar[int]
    BOX_HANDOFF_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    BOX_HANDOFF_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_GROUP_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_RUNNING_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    is_running: bool
    is_composing_message: bool
    is_retrying: bool
    activity: GrokBotAgentLiveActivity
    awaiting: GrokBotAgentAwaitingState
    updated_at_ms: int
    stale_after_ms: int
    box_handoff_request_id: str
    box_handoff_instruction: str
    session_id: str
    active_group_member_id: str
    has_running_subagents: bool
    def __init__(self, agent_id: _Optional[str] = ..., is_running: bool = ..., is_composing_message: bool = ..., is_retrying: bool = ..., activity: _Optional[_Union[GrokBotAgentLiveActivity, _Mapping]] = ..., awaiting: _Optional[_Union[GrokBotAgentAwaitingState, _Mapping]] = ..., updated_at_ms: _Optional[int] = ..., stale_after_ms: _Optional[int] = ..., box_handoff_request_id: _Optional[str] = ..., box_handoff_instruction: _Optional[str] = ..., session_id: _Optional[str] = ..., active_group_member_id: _Optional[str] = ..., has_running_subagents: bool = ...) -> None: ...

class GrokBotAgentMarketplace(_message.Message):
    __slots__ = ("marketplace_id", "display_name", "description")
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    marketplace_id: int
    display_name: str
    description: str
    def __init__(self, marketplace_id: _Optional[int] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GrokBotAgentPlugin(_message.Message):
    __slots__ = ("plugin_id", "name", "display_name", "description", "logo_url", "owned_by_marketplace", "install_mode", "variable_names", "is_deprecated", "mcp_config_json", "skills", "mcp_server_names", "is_bot_skills", "connector_type", "variables_json", "has_configured_variables")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    OWNED_BY_MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    INSTALL_MODE_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    IS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_NAMES_FIELD_NUMBER: _ClassVar[int]
    IS_BOT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_JSON_FIELD_NUMBER: _ClassVar[int]
    HAS_CONFIGURED_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    name: str
    display_name: str
    description: str
    logo_url: str
    owned_by_marketplace: bool
    install_mode: str
    variable_names: _containers.RepeatedScalarFieldContainer[str]
    is_deprecated: bool
    mcp_config_json: str
    skills: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPluginSkill]
    mcp_server_names: _containers.RepeatedScalarFieldContainer[str]
    is_bot_skills: bool
    connector_type: GrokBotConnectorType
    variables_json: str
    has_configured_variables: bool
    def __init__(self, plugin_id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ..., owned_by_marketplace: bool = ..., install_mode: _Optional[str] = ..., variable_names: _Optional[_Iterable[str]] = ..., is_deprecated: bool = ..., mcp_config_json: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[GrokBotAgentPluginSkill, _Mapping]]] = ..., mcp_server_names: _Optional[_Iterable[str]] = ..., is_bot_skills: bool = ..., connector_type: _Optional[_Union[GrokBotConnectorType, str]] = ..., variables_json: _Optional[str] = ..., has_configured_variables: bool = ...) -> None: ...

class GrokBotAgentPluginConfigUpdate(_message.Message):
    __slots__ = ("plugin_id", "mcp_config_json")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    mcp_config_json: str
    def __init__(self, plugin_id: _Optional[int] = ..., mcp_config_json: _Optional[str] = ...) -> None: ...

class GrokBotAgentPluginEntry(_message.Message):
    __slots__ = ("plugin_id", "inline", "config_update")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    INLINE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_UPDATE_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    inline: GrokBotAgentInlinePlugin
    config_update: GrokBotAgentPluginConfigUpdate
    def __init__(self, plugin_id: _Optional[int] = ..., inline: _Optional[_Union[GrokBotAgentInlinePlugin, _Mapping]] = ..., config_update: _Optional[_Union[GrokBotAgentPluginConfigUpdate, _Mapping]] = ...) -> None: ...

class GrokBotAgentPluginSkill(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url", "content", "environments")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    content: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ..., content: _Optional[str] = ..., environments: _Optional[_Iterable[str]] = ...) -> None: ...

class GrokBotAgentSession(_message.Message):
    __slots__ = ("agent_id", "session_id", "kind", "created_at_ms", "updated_at_ms", "last_activity_at_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    kind: GrokBotAgentSessionKind
    created_at_ms: int
    updated_at_ms: int
    last_activity_at_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ..., kind: _Optional[_Union[GrokBotAgentSessionKind, str]] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., last_activity_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotAgentSkill(_message.Message):
    __slots__ = ("id", "name", "description", "body", "source")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    body: str
    source: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., body: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class GrokBotBoxState(_message.Message):
    __slots__ = ("run_state", "recreate_in_flight", "image_update_available", "host_version", "host_update_available", "disk_pressure", "updated_at_ms")
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    RECREATE_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    HOST_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOST_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DISK_PRESSURE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    run_state: SandBoxRunState
    recreate_in_flight: bool
    image_update_available: bool
    host_version: str
    host_update_available: bool
    disk_pressure: GrokBotBoxDiskPressureLevel
    updated_at_ms: int
    def __init__(self, run_state: _Optional[_Union[SandBoxRunState, str]] = ..., recreate_in_flight: bool = ..., image_update_available: bool = ..., host_version: _Optional[str] = ..., host_update_available: bool = ..., disk_pressure: _Optional[_Union[GrokBotBoxDiskPressureLevel, str]] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotComputerAction(_message.Message):
    __slots__ = ("agent_id", "type", "x", "y", "button", "count", "at_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    type: str
    x: float
    y: float
    button: str
    count: int
    at_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., type: _Optional[str] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., button: _Optional[str] = ..., count: _Optional[int] = ..., at_ms: _Optional[int] = ...) -> None: ...

class GrokBotEmailDraft(_message.Message):
    __slots__ = ("to", "cc", "subject", "body")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    CC_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    to: _containers.RepeatedScalarFieldContainer[str]
    cc: _containers.RepeatedScalarFieldContainer[str]
    subject: str
    body: str
    def __init__(self, to: _Optional[_Iterable[str]] = ..., cc: _Optional[_Iterable[str]] = ..., subject: _Optional[str] = ..., body: _Optional[str] = ..., **kwargs) -> None: ...

class GrokBotHarnessMigrationAgentStatus(_message.Message):
    __slots__ = ("agent_row_id", "public_agent_id", "harness", "kind", "updated_at_ms")
    AGENT_ROW_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_row_id: str
    public_agent_id: str
    harness: str
    kind: str
    updated_at_ms: int
    def __init__(self, agent_row_id: _Optional[str] = ..., public_agent_id: _Optional[str] = ..., harness: _Optional[str] = ..., kind: _Optional[str] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotHarnessMigrationPassAgentResult(_message.Message):
    __slots__ = ("agent_row_id", "outcome", "deferral_reason", "duration_ms", "copied_blobs", "copied_bytes", "closure_blobs", "prewarmed_blobs")
    AGENT_ROW_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    DEFERRAL_REASON_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    COPIED_BLOBS_FIELD_NUMBER: _ClassVar[int]
    COPIED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLOSURE_BLOBS_FIELD_NUMBER: _ClassVar[int]
    PREWARMED_BLOBS_FIELD_NUMBER: _ClassVar[int]
    agent_row_id: str
    outcome: str
    deferral_reason: str
    duration_ms: int
    copied_blobs: int
    copied_bytes: int
    closure_blobs: int
    prewarmed_blobs: int
    def __init__(self, agent_row_id: _Optional[str] = ..., outcome: _Optional[str] = ..., deferral_reason: _Optional[str] = ..., duration_ms: _Optional[int] = ..., copied_blobs: _Optional[int] = ..., copied_bytes: _Optional[int] = ..., closure_blobs: _Optional[int] = ..., prewarmed_blobs: _Optional[int] = ...) -> None: ...

class GrokBotHarnessMigrationPassStatus(_message.Message):
    __slots__ = ("workflow_id", "run_id", "status", "started_at_ms", "closed_at_ms", "skipped_reason", "budget_exhausted", "agents")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_REASON_FIELD_NUMBER: _ClassVar[int]
    BUDGET_EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    run_id: str
    status: str
    started_at_ms: int
    closed_at_ms: int
    skipped_reason: str
    budget_exhausted: bool
    agents: _containers.RepeatedCompositeFieldContainer[GrokBotHarnessMigrationPassAgentResult]
    def __init__(self, workflow_id: _Optional[str] = ..., run_id: _Optional[str] = ..., status: _Optional[str] = ..., started_at_ms: _Optional[int] = ..., closed_at_ms: _Optional[int] = ..., skipped_reason: _Optional[str] = ..., budget_exhausted: bool = ..., agents: _Optional[_Iterable[_Union[GrokBotHarnessMigrationPassAgentResult, _Mapping]]] = ...) -> None: ...

class GrokBotHarnessMigrationRolloutStatus(_message.Message):
    __slots__ = ("migration_gate_enabled", "identity_reads_enabled", "temporal_harness_mode", "host_update_trigger_enabled", "ineligibility")
    MIGRATION_GATE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_READS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_HARNESS_MODE_FIELD_NUMBER: _ClassVar[int]
    HOST_UPDATE_TRIGGER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INELIGIBILITY_FIELD_NUMBER: _ClassVar[int]
    migration_gate_enabled: bool
    identity_reads_enabled: bool
    temporal_harness_mode: str
    host_update_trigger_enabled: bool
    ineligibility: str
    def __init__(self, migration_gate_enabled: bool = ..., identity_reads_enabled: bool = ..., temporal_harness_mode: _Optional[str] = ..., host_update_trigger_enabled: bool = ..., ineligibility: _Optional[str] = ...) -> None: ...

class GrokBotHarnessRefusal(_message.Message):
    __slots__ = ("failure_code", "message")
    FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    failure_code: str
    message: str
    def __init__(self, failure_code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GrokBotMarketplaceCategory(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GrokBotMarketplaceCreator(_message.Message):
    __slots__ = ("id", "name", "profile_photo_url", "handles", "created_at_ms", "updated_at_ms")
    class HandlesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    HANDLES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    profile_photo_url: str
    handles: _containers.ScalarMap[str, str]
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., profile_photo_url: _Optional[str] = ..., handles: _Optional[_Mapping[str, str]] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotMarketplaceDefaultAvatar(_message.Message):
    __slots__ = ("shape", "color")
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    shape: str
    color: str
    def __init__(self, shape: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class GrokBotMarketplaceListing(_message.Message):
    __slots__ = ("id", "template_id", "pinned_template_version_id", "blob_object_key", "name", "description", "image_url", "default_avatar", "status", "slug", "category", "created_at_ms", "updated_at_ms", "creator_id", "share_id", "categories")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PINNED_TEMPLATE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AVATAR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    id: int
    template_id: int
    pinned_template_version_id: int
    blob_object_key: str
    name: str
    description: str
    image_url: str
    default_avatar: GrokBotMarketplaceDefaultAvatar
    status: GrokBotMarketplaceListingStatus
    slug: str
    category: str
    created_at_ms: int
    updated_at_ms: int
    creator_id: int
    share_id: str
    categories: _containers.RepeatedCompositeFieldContainer[GrokBotMarketplaceCategory]
    def __init__(self, id: _Optional[int] = ..., template_id: _Optional[int] = ..., pinned_template_version_id: _Optional[int] = ..., blob_object_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., image_url: _Optional[str] = ..., default_avatar: _Optional[_Union[GrokBotMarketplaceDefaultAvatar, _Mapping]] = ..., status: _Optional[_Union[GrokBotMarketplaceListingStatus, str]] = ..., slug: _Optional[str] = ..., category: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., creator_id: _Optional[int] = ..., share_id: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[GrokBotMarketplaceCategory, _Mapping]]] = ...) -> None: ...

class GrokBotMemoryFolder(_message.Message):
    __slots__ = ("profile", "logs")
    class LogsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    profile: str
    logs: _containers.ScalarMap[str, str]
    def __init__(self, profile: _Optional[str] = ..., logs: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GrokBotMemoryShard(_message.Message):
    __slots__ = ("agent_id", "harness", "folder", "version")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    harness: GrokBotAgentHarnessKind
    folder: GrokBotMemoryFolder
    version: int
    def __init__(self, agent_id: _Optional[str] = ..., harness: _Optional[_Union[GrokBotAgentHarnessKind, str]] = ..., folder: _Optional[_Union[GrokBotMemoryFolder, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class GrokBotOrphanedSlackApp(_message.Message):
    __slots__ = ("agent_id", "auth_id", "owner_email", "slack_app_id", "slack_team_id", "slack_workspace_name", "deleted_at_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SLACK_APP_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    auth_id: str
    owner_email: str
    slack_app_id: str
    slack_team_id: str
    slack_workspace_name: str
    deleted_at_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., auth_id: _Optional[str] = ..., owner_email: _Optional[str] = ..., slack_app_id: _Optional[str] = ..., slack_team_id: _Optional[str] = ..., slack_workspace_name: _Optional[str] = ..., deleted_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotPinnedAgents(_message.Message):
    __slots__ = ("agent_ids",)
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GrokBotPluginScope(_message.Message):
    __slots__ = ("agent_id", "session_kind")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KIND_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_kind: str
    def __init__(self, agent_id: _Optional[str] = ..., session_kind: _Optional[str] = ...) -> None: ...

class GrokBotRoomMemberTurnMessage(_message.Message):
    __slots__ = ("speaker_kind", "speaker_name", "is_self", "text", "reply_to")
    class SpeakerKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEAKER_KIND_UNSPECIFIED: _ClassVar[GrokBotRoomMemberTurnMessage.SpeakerKind]
        SPEAKER_KIND_HUMAN: _ClassVar[GrokBotRoomMemberTurnMessage.SpeakerKind]
        SPEAKER_KIND_AGENT: _ClassVar[GrokBotRoomMemberTurnMessage.SpeakerKind]
    SPEAKER_KIND_UNSPECIFIED: GrokBotRoomMemberTurnMessage.SpeakerKind
    SPEAKER_KIND_HUMAN: GrokBotRoomMemberTurnMessage.SpeakerKind
    SPEAKER_KIND_AGENT: GrokBotRoomMemberTurnMessage.SpeakerKind
    class ReplyTarget(_message.Message):
        __slots__ = ("speaker_kind", "speaker_name", "is_self", "quote")
        SPEAKER_KIND_FIELD_NUMBER: _ClassVar[int]
        SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_SELF_FIELD_NUMBER: _ClassVar[int]
        QUOTE_FIELD_NUMBER: _ClassVar[int]
        speaker_kind: GrokBotRoomMemberTurnMessage.SpeakerKind
        speaker_name: str
        is_self: bool
        quote: str
        def __init__(self, speaker_kind: _Optional[_Union[GrokBotRoomMemberTurnMessage.SpeakerKind, str]] = ..., speaker_name: _Optional[str] = ..., is_self: bool = ..., quote: _Optional[str] = ...) -> None: ...
    SPEAKER_KIND_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    speaker_kind: GrokBotRoomMemberTurnMessage.SpeakerKind
    speaker_name: str
    is_self: bool
    text: str
    reply_to: GrokBotRoomMemberTurnMessage.ReplyTarget
    def __init__(self, speaker_kind: _Optional[_Union[GrokBotRoomMemberTurnMessage.SpeakerKind, str]] = ..., speaker_name: _Optional[str] = ..., is_self: bool = ..., text: _Optional[str] = ..., reply_to: _Optional[_Union[GrokBotRoomMemberTurnMessage.ReplyTarget, _Mapping]] = ...) -> None: ...

class GrokBotRoomMemberTurnPeer(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GrokBotRoomMemberTurnRoom(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GrokBotRoomPerson(_message.Message):
    __slots__ = ("display_name", "avatar_url", "is_viewer")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    IS_VIEWER_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    avatar_url: str
    is_viewer: bool
    def __init__(self, display_name: _Optional[str] = ..., avatar_url: _Optional[str] = ..., is_viewer: bool = ...) -> None: ...

class GrokBotRuntimeCapabilities(_message.Message):
    __slots__ = ("durable_identity_enabled", "durable_identity_writes_enabled", "temporal_creation_enabled", "agent_messaging_enabled", "server_rooms_enabled")
    DURABLE_IDENTITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DURABLE_IDENTITY_WRITES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_CREATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVER_ROOMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    durable_identity_enabled: bool
    durable_identity_writes_enabled: bool
    temporal_creation_enabled: bool
    agent_messaging_enabled: bool
    server_rooms_enabled: bool
    def __init__(self, durable_identity_enabled: bool = ..., durable_identity_writes_enabled: bool = ..., temporal_creation_enabled: bool = ..., agent_messaging_enabled: bool = ..., server_rooms_enabled: bool = ...) -> None: ...

class GrokBotSecret(_message.Message):
    __slots__ = ("name", "description", "created_at_ms", "updated_at_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotSessionBox(_message.Message):
    __slots__ = ("agent_id", "session_id", "auth_id", "tenant_id", "store_id", "provisioned_at_ms", "last_activity_at_ms", "reap_claimed_at_ms", "reap_claim_fresh", "deleted_at_ms", "agent_deleted", "pod_state", "pod", "pod_count", "failed_clusters", "credential_state", "owner_missing", "lookup_error", "box_key", "viewer_box")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REAP_CLAIMED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REAP_CLAIM_FRESH_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    AGENT_DELETED_FIELD_NUMBER: _ClassVar[int]
    POD_STATE_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_MISSING_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    VIEWER_BOX_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    auth_id: str
    tenant_id: str
    store_id: str
    provisioned_at_ms: int
    last_activity_at_ms: int
    reap_claimed_at_ms: int
    reap_claim_fresh: bool
    deleted_at_ms: int
    agent_deleted: bool
    pod_state: GrokBotSessionBoxPodState
    pod: GrokBotSessionBoxPod
    pod_count: int
    failed_clusters: _containers.RepeatedScalarFieldContainer[str]
    credential_state: GrokBotSessionBoxCredentialState
    owner_missing: bool
    lookup_error: str
    box_key: str
    viewer_box: bool
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ..., auth_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., store_id: _Optional[str] = ..., provisioned_at_ms: _Optional[int] = ..., last_activity_at_ms: _Optional[int] = ..., reap_claimed_at_ms: _Optional[int] = ..., reap_claim_fresh: bool = ..., deleted_at_ms: _Optional[int] = ..., agent_deleted: bool = ..., pod_state: _Optional[_Union[GrokBotSessionBoxPodState, str]] = ..., pod: _Optional[_Union[GrokBotSessionBoxPod, _Mapping]] = ..., pod_count: _Optional[int] = ..., failed_clusters: _Optional[_Iterable[str]] = ..., credential_state: _Optional[_Union[GrokBotSessionBoxCredentialState, str]] = ..., owner_missing: bool = ..., lookup_error: _Optional[str] = ..., box_key: _Optional[str] = ..., viewer_box: bool = ...) -> None: ...

class GrokBotSessionBoxPod(_message.Message):
    __slots__ = ("cluster", "pod_id", "phase", "creation_timestamp_ms", "deletion_timestamp_ms", "node_id")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    POD_ID_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    DELETION_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    pod_id: str
    phase: str
    creation_timestamp_ms: int
    deletion_timestamp_ms: int
    node_id: str
    def __init__(self, cluster: _Optional[str] = ..., pod_id: _Optional[str] = ..., phase: _Optional[str] = ..., creation_timestamp_ms: _Optional[int] = ..., deletion_timestamp_ms: _Optional[int] = ..., node_id: _Optional[str] = ...) -> None: ...

class GrokBotSidebarSection(_message.Message):
    __slots__ = ("id", "name", "agent_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., agent_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GrokBotSidebarSections(_message.Message):
    __slots__ = ("sections",)
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    sections: _containers.RepeatedCompositeFieldContainer[GrokBotSidebarSection]
    def __init__(self, sections: _Optional[_Iterable[_Union[GrokBotSidebarSection, _Mapping]]] = ...) -> None: ...

class GrokBotSlackAppRemoval(_message.Message):
    __slots__ = ("slack_app_id", "slack_team_id", "slack_workspace_name", "status", "slack_error")
    SLACK_APP_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SLACK_ERROR_FIELD_NUMBER: _ClassVar[int]
    slack_app_id: str
    slack_team_id: str
    slack_workspace_name: str
    status: str
    slack_error: str
    def __init__(self, slack_app_id: _Optional[str] = ..., slack_team_id: _Optional[str] = ..., slack_workspace_name: _Optional[str] = ..., status: _Optional[str] = ..., slack_error: _Optional[str] = ...) -> None: ...

class GrokBotSlackConnection(_message.Message):
    __slots__ = ("agent_id", "connected", "workspace_name", "install_url", "unavailable_reason", "pending_admin_approval", "needs_manifest_update", "reinstall_url")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTALL_URL_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASON_FIELD_NUMBER: _ClassVar[int]
    PENDING_ADMIN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    NEEDS_MANIFEST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    REINSTALL_URL_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    connected: bool
    workspace_name: str
    install_url: str
    unavailable_reason: str
    pending_admin_approval: bool
    needs_manifest_update: bool
    reinstall_url: str
    def __init__(self, agent_id: _Optional[str] = ..., connected: bool = ..., workspace_name: _Optional[str] = ..., install_url: _Optional[str] = ..., unavailable_reason: _Optional[str] = ..., pending_admin_approval: bool = ..., needs_manifest_update: bool = ..., reinstall_url: _Optional[str] = ...) -> None: ...

class GrokBotSlackDraft(_message.Message):
    __slots__ = ("workspace", "target", "thread", "body")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    target: str
    thread: str
    body: str
    def __init__(self, workspace: _Optional[str] = ..., target: _Optional[str] = ..., thread: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...

class GrokBotSlackWorkspace(_message.Message):
    __slots__ = ("slack_team_id", "slack_team_name", "manager_auth_updated_at_ms")
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    MANAGER_AUTH_UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    slack_team_id: str
    slack_team_name: str
    manager_auth_updated_at_ms: int
    def __init__(self, slack_team_id: _Optional[str] = ..., slack_team_name: _Optional[str] = ..., manager_auth_updated_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotStripeLinkPaymentMethod(_message.Message):
    __slots__ = ("id", "name", "is_default", "kind", "brand", "last4", "exp_month", "exp_year")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    LAST4_FIELD_NUMBER: _ClassVar[int]
    EXP_MONTH_FIELD_NUMBER: _ClassVar[int]
    EXP_YEAR_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    is_default: bool
    kind: GrokBotStripeLinkPaymentMethodKind
    brand: str
    last4: str
    exp_month: int
    exp_year: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., is_default: bool = ..., kind: _Optional[_Union[GrokBotStripeLinkPaymentMethodKind, str]] = ..., brand: _Optional[str] = ..., last4: _Optional[str] = ..., exp_month: _Optional[int] = ..., exp_year: _Optional[int] = ...) -> None: ...

class GrokBotTeamAgent(_message.Message):
    __slots__ = ("identity", "owner_email", "last_activity_at_ms", "sessions", "routines", "owner_multiplayer_gate")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ROUTINES_FIELD_NUMBER: _ClassVar[int]
    OWNER_MULTIPLAYER_GATE_FIELD_NUMBER: _ClassVar[int]
    identity: GrokBotAgentDefinitionIdentity
    owner_email: str
    last_activity_at_ms: int
    sessions: GrokBotTeamAgentSessionCounts
    routines: GrokBotTeamAgentRoutineCounts
    owner_multiplayer_gate: bool
    def __init__(self, identity: _Optional[_Union[GrokBotAgentDefinitionIdentity, _Mapping]] = ..., owner_email: _Optional[str] = ..., last_activity_at_ms: _Optional[int] = ..., sessions: _Optional[_Union[GrokBotTeamAgentSessionCounts, _Mapping]] = ..., routines: _Optional[_Union[GrokBotTeamAgentRoutineCounts, _Mapping]] = ..., owner_multiplayer_gate: bool = ...) -> None: ...

class GrokBotTeamAgentParticipant(_message.Message):
    __slots__ = ("session_id", "kind", "user_id", "user_email", "standing", "box_key", "box_provisioned", "created_at_ms", "last_activity_at_ms")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STANDING_FIELD_NUMBER: _ClassVar[int]
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    BOX_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    kind: str
    user_id: int
    user_email: str
    standing: str
    box_key: str
    box_provisioned: bool
    created_at_ms: int
    last_activity_at_ms: int
    def __init__(self, session_id: _Optional[str] = ..., kind: _Optional[str] = ..., user_id: _Optional[int] = ..., user_email: _Optional[str] = ..., standing: _Optional[str] = ..., box_key: _Optional[str] = ..., box_provisioned: bool = ..., created_at_ms: _Optional[int] = ..., last_activity_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotTeamAgentRoutineCounts(_message.Message):
    __slots__ = ("total", "teammate_created")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TEAMMATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    total: int
    teammate_created: int
    def __init__(self, total: _Optional[int] = ..., teammate_created: _Optional[int] = ...) -> None: ...

class GrokBotTeamAgentSessionCounts(_message.Message):
    __slots__ = ("total", "teammate_dms", "slack_dms", "slack_threads", "boxes_provisioned")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TEAMMATE_DMS_FIELD_NUMBER: _ClassVar[int]
    SLACK_DMS_FIELD_NUMBER: _ClassVar[int]
    SLACK_THREADS_FIELD_NUMBER: _ClassVar[int]
    BOXES_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
    total: int
    teammate_dms: int
    slack_dms: int
    slack_threads: int
    boxes_provisioned: int
    def __init__(self, total: _Optional[int] = ..., teammate_dms: _Optional[int] = ..., slack_dms: _Optional[int] = ..., slack_threads: _Optional[int] = ..., boxes_provisioned: _Optional[int] = ...) -> None: ...

class GrokBotTeamAgentSharedBox(_message.Message):
    __slots__ = ("box_key", "kind", "session_ids")
    BOX_KEY_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SESSION_IDS_FIELD_NUMBER: _ClassVar[int]
    box_key: str
    kind: str
    session_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, box_key: _Optional[str] = ..., kind: _Optional[str] = ..., session_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GrokBotTeamAgentSharedRoutine(_message.Message):
    __slots__ = ("automation_id", "name", "enabled", "creator_auth_id", "creator_email", "creator_is_owner", "session_id", "trigger_description", "prompt", "created_at_ms", "last_run_at_ms")
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CREATOR_IS_OWNER_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_MS_FIELD_NUMBER: _ClassVar[int]
    automation_id: str
    name: str
    enabled: bool
    creator_auth_id: str
    creator_email: str
    creator_is_owner: bool
    session_id: str
    trigger_description: str
    prompt: str
    created_at_ms: int
    last_run_at_ms: int
    def __init__(self, automation_id: _Optional[str] = ..., name: _Optional[str] = ..., enabled: bool = ..., creator_auth_id: _Optional[str] = ..., creator_email: _Optional[str] = ..., creator_is_owner: bool = ..., session_id: _Optional[str] = ..., trigger_description: _Optional[str] = ..., prompt: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., last_run_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotTeamAgentSharedState(_message.Message):
    __slots__ = ("participants", "agent_memory", "marketplace", "plugins", "routines", "recipe_skills", "boxes", "participants_truncated")
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MEMORY_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    ROUTINES_FIELD_NUMBER: _ClassVar[int]
    RECIPE_SKILLS_FIELD_NUMBER: _ClassVar[int]
    BOXES_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[GrokBotTeamAgentParticipant]
    agent_memory: GrokBotAgentDefinitionMemoryShard
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    routines: _containers.RepeatedCompositeFieldContainer[GrokBotTeamAgentSharedRoutine]
    recipe_skills: _containers.RepeatedCompositeFieldContainer[GrokBotAgentDefinitionSkill]
    boxes: _containers.RepeatedCompositeFieldContainer[GrokBotTeamAgentSharedBox]
    participants_truncated: bool
    def __init__(self, participants: _Optional[_Iterable[_Union[GrokBotTeamAgentParticipant, _Mapping]]] = ..., agent_memory: _Optional[_Union[GrokBotAgentDefinitionMemoryShard, _Mapping]] = ..., marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ..., routines: _Optional[_Iterable[_Union[GrokBotTeamAgentSharedRoutine, _Mapping]]] = ..., recipe_skills: _Optional[_Iterable[_Union[GrokBotAgentDefinitionSkill, _Mapping]]] = ..., boxes: _Optional[_Iterable[_Union[GrokBotTeamAgentSharedBox, _Mapping]]] = ..., participants_truncated: bool = ...) -> None: ...

class GrokBotTemplate(_message.Message):
    __slots__ = ("share_id", "name", "avatar_shape", "avatar_color", "source_agent_id", "created_at_ms", "updated_at_ms", "blob_object_key", "published", "active_version", "description", "visibility", "owner_type", "image_url")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    BLOB_OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    OWNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    name: str
    avatar_shape: str
    avatar_color: str
    source_agent_id: str
    created_at_ms: int
    updated_at_ms: int
    blob_object_key: str
    published: bool
    active_version: int
    description: str
    visibility: GrokBotTemplateVisibility
    owner_type: GrokBotTemplateOwnerType
    image_url: str
    def __init__(self, share_id: _Optional[str] = ..., name: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., source_agent_id: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., blob_object_key: _Optional[str] = ..., published: bool = ..., active_version: _Optional[int] = ..., description: _Optional[str] = ..., visibility: _Optional[_Union[GrokBotTemplateVisibility, str]] = ..., owner_type: _Optional[_Union[GrokBotTemplateOwnerType, str]] = ..., image_url: _Optional[str] = ...) -> None: ...

class GrokBotTranscriptCursor(_message.Message):
    __slots__ = ("agent_id", "generation", "after_updated_seq", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    AFTER_UPDATED_SEQ_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    generation: int
    after_updated_seq: int
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., generation: _Optional[int] = ..., after_updated_seq: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class GrokBotTranscriptEntry(_message.Message):
    __slots__ = ("seq", "entry_kind", "body", "blob_hash", "updated_seq", "entry_id", "body_omitted")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    ENTRY_KIND_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    BLOB_HASH_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SEQ_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    BODY_OMITTED_FIELD_NUMBER: _ClassVar[int]
    seq: int
    entry_kind: str
    body: bytes
    blob_hash: str
    updated_seq: int
    entry_id: str
    body_omitted: bool
    def __init__(self, seq: _Optional[int] = ..., entry_kind: _Optional[str] = ..., body: _Optional[bytes] = ..., blob_hash: _Optional[str] = ..., updated_seq: _Optional[int] = ..., entry_id: _Optional[str] = ..., body_omitted: bool = ...) -> None: ...

class GrokBotTranscriptEntryDelete(_message.Message):
    __slots__ = ("seq", "updated_seq", "entry_id")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SEQ_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    seq: int
    updated_seq: int
    entry_id: str
    def __init__(self, seq: _Optional[int] = ..., updated_seq: _Optional[int] = ..., entry_id: _Optional[str] = ...) -> None: ...

class GrokBotTranscriptEntryRejection(_message.Message):
    __slots__ = ("seq", "current_updated_seq")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    CURRENT_UPDATED_SEQ_FIELD_NUMBER: _ClassVar[int]
    seq: int
    current_updated_seq: int
    def __init__(self, seq: _Optional[int] = ..., current_updated_seq: _Optional[int] = ...) -> None: ...

class GrokBotTranscriptWatchAgentState(_message.Message):
    __slots__ = ("live", "snapshot", "client")
    LIVE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    live: _containers.RepeatedCompositeFieldContainer[GrokBotAgentLiveState]
    snapshot: bool
    client: _containers.RepeatedCompositeFieldContainer[GrokBotAgentClientState]
    def __init__(self, live: _Optional[_Iterable[_Union[GrokBotAgentLiveState, _Mapping]]] = ..., snapshot: bool = ..., client: _Optional[_Iterable[_Union[GrokBotAgentClientState, _Mapping]]] = ...) -> None: ...

class GrokBotTranscriptWatchAgentStateChanged(_message.Message):
    __slots__ = ("agent_id", "families", "changed_at_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    CHANGED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    families: _containers.RepeatedScalarFieldContainer[str]
    changed_at_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., families: _Optional[_Iterable[str]] = ..., changed_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotTranscriptWatchBoxState(_message.Message):
    __slots__ = ("state", "snapshot")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    state: GrokBotBoxState
    snapshot: bool
    def __init__(self, state: _Optional[_Union[GrokBotBoxState, _Mapping]] = ..., snapshot: bool = ...) -> None: ...

class GrokBotTranscriptWatchCleared(_message.Message):
    __slots__ = ("agent_id", "new_generation", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_GENERATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    new_generation: int
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., new_generation: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class GrokBotTranscriptWatchComputerActions(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[GrokBotComputerAction]
    def __init__(self, actions: _Optional[_Iterable[_Union[GrokBotComputerAction, _Mapping]]] = ...) -> None: ...

class GrokBotTranscriptWatchConnected(_message.Message):
    __slots__ = ("stream_id", "server_time_ms", "absolute_lifetime_ms")
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_LIFETIME_MS_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    server_time_ms: int
    absolute_lifetime_ms: int
    def __init__(self, stream_id: _Optional[str] = ..., server_time_ms: _Optional[int] = ..., absolute_lifetime_ms: _Optional[int] = ...) -> None: ...

class GrokBotTranscriptWatchCursorTooOld(_message.Message):
    __slots__ = ("agent_id", "generation", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    generation: int
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., generation: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class GrokBotTranscriptWatchFrame(_message.Message):
    __slots__ = ("connected", "rows", "cleared", "cursor_too_old", "heartbeat", "agent_state", "computer_actions", "agent_state_changed", "turn_failed", "roster_changed", "box_state")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    CLEARED_FIELD_NUMBER: _ClassVar[int]
    CURSOR_TOO_OLD_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATE_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    TURN_FAILED_FIELD_NUMBER: _ClassVar[int]
    ROSTER_CHANGED_FIELD_NUMBER: _ClassVar[int]
    BOX_STATE_FIELD_NUMBER: _ClassVar[int]
    connected: GrokBotTranscriptWatchConnected
    rows: GrokBotTranscriptWatchRows
    cleared: GrokBotTranscriptWatchCleared
    cursor_too_old: GrokBotTranscriptWatchCursorTooOld
    heartbeat: GrokBotTranscriptWatchHeartbeat
    agent_state: GrokBotTranscriptWatchAgentState
    computer_actions: GrokBotTranscriptWatchComputerActions
    agent_state_changed: GrokBotTranscriptWatchAgentStateChanged
    turn_failed: GrokBotTranscriptWatchTurnFailed
    roster_changed: GrokBotTranscriptWatchRosterChanged
    box_state: GrokBotTranscriptWatchBoxState
    def __init__(self, connected: _Optional[_Union[GrokBotTranscriptWatchConnected, _Mapping]] = ..., rows: _Optional[_Union[GrokBotTranscriptWatchRows, _Mapping]] = ..., cleared: _Optional[_Union[GrokBotTranscriptWatchCleared, _Mapping]] = ..., cursor_too_old: _Optional[_Union[GrokBotTranscriptWatchCursorTooOld, _Mapping]] = ..., heartbeat: _Optional[_Union[GrokBotTranscriptWatchHeartbeat, _Mapping]] = ..., agent_state: _Optional[_Union[GrokBotTranscriptWatchAgentState, _Mapping]] = ..., computer_actions: _Optional[_Union[GrokBotTranscriptWatchComputerActions, _Mapping]] = ..., agent_state_changed: _Optional[_Union[GrokBotTranscriptWatchAgentStateChanged, _Mapping]] = ..., turn_failed: _Optional[_Union[GrokBotTranscriptWatchTurnFailed, _Mapping]] = ..., roster_changed: _Optional[_Union[GrokBotTranscriptWatchRosterChanged, _Mapping]] = ..., box_state: _Optional[_Union[GrokBotTranscriptWatchBoxState, _Mapping]] = ...) -> None: ...

class GrokBotTranscriptWatchHeartbeat(_message.Message):
    __slots__ = ("server_time_ms",)
    SERVER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    server_time_ms: int
    def __init__(self, server_time_ms: _Optional[int] = ...) -> None: ...

class GrokBotTranscriptWatchRosterChanged(_message.Message):
    __slots__ = ("kind", "agent_id", "changed_at_ms", "agent", "changed_fields")
    KIND_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    kind: GrokBotRosterChangeKind
    agent_id: str
    changed_at_ms: int
    agent: GrokBotAgent
    changed_fields: _containers.RepeatedScalarFieldContainer[GrokBotUserSettingsField]
    def __init__(self, kind: _Optional[_Union[GrokBotRosterChangeKind, str]] = ..., agent_id: _Optional[str] = ..., changed_at_ms: _Optional[int] = ..., agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ..., changed_fields: _Optional[_Iterable[_Union[GrokBotUserSettingsField, str]]] = ...) -> None: ...

class GrokBotTranscriptWatchRows(_message.Message):
    __slots__ = ("agent_id", "generation", "entries", "deletes", "replay", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DELETES_FIELD_NUMBER: _ClassVar[int]
    REPLAY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    generation: int
    entries: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptEntry]
    deletes: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptEntryDelete]
    replay: bool
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., generation: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[GrokBotTranscriptEntry, _Mapping]]] = ..., deletes: _Optional[_Iterable[_Union[GrokBotTranscriptEntryDelete, _Mapping]]] = ..., replay: bool = ..., session_id: _Optional[str] = ...) -> None: ...

class GrokBotTranscriptWatchTurnFailed(_message.Message):
    __slots__ = ("agent_id", "session_id", "turn_id", "code", "summary", "failed_at_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FAILED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    session_id: str
    turn_id: str
    code: GrokBotTurnFailureCode
    summary: str
    failed_at_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., session_id: _Optional[str] = ..., turn_id: _Optional[str] = ..., code: _Optional[_Union[GrokBotTurnFailureCode, str]] = ..., summary: _Optional[str] = ..., failed_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotUserAutoReviewInstructions(_message.Message):
    __slots__ = ("is_enabled", "allow_instructions", "block_instructions")
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    is_enabled: bool
    allow_instructions: _containers.RepeatedScalarFieldContainer[str]
    block_instructions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_enabled: bool = ..., allow_instructions: _Optional[_Iterable[str]] = ..., block_instructions: _Optional[_Iterable[str]] = ...) -> None: ...

class GrokBotUserComputerCancel(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GrokBotUserComputerCapabilities(_message.Message):
    __slots__ = ("messages_op", "messages_op_generation", "local_standing_grants")
    MESSAGES_OP_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_OP_GENERATION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_STANDING_GRANTS_FIELD_NUMBER: _ClassVar[int]
    messages_op: bool
    messages_op_generation: int
    local_standing_grants: bool
    def __init__(self, messages_op: bool = ..., messages_op_generation: _Optional[int] = ..., local_standing_grants: bool = ...) -> None: ...

class GrokBotUserComputerClientMessage(_message.Message):
    __slots__ = ("message_json",)
    MESSAGE_JSON_FIELD_NUMBER: _ClassVar[int]
    message_json: str
    def __init__(self, message_json: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerControlMessage(_message.Message):
    __slots__ = ("message_json", "cwd_state")
    MESSAGE_JSON_FIELD_NUMBER: _ClassVar[int]
    CWD_STATE_FIELD_NUMBER: _ClassVar[int]
    message_json: str
    cwd_state: str
    def __init__(self, message_json: _Optional[str] = ..., cwd_state: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerDownload(_message.Message):
    __slots__ = ("path", "approval_id", "authorized_by_standing", "authorized_by_approval")
    PATH_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_STANDING_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    path: str
    approval_id: str
    authorized_by_standing: bool
    authorized_by_approval: bool
    def __init__(self, path: _Optional[str] = ..., approval_id: _Optional[str] = ..., authorized_by_standing: bool = ..., authorized_by_approval: bool = ...) -> None: ...

class GrokBotUserComputerExec(_message.Message):
    __slots__ = ("server_message_json", "approval_id", "authorized_by_standing", "authorized_by_approval")
    SERVER_MESSAGE_JSON_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_STANDING_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    server_message_json: str
    approval_id: str
    authorized_by_standing: bool
    authorized_by_approval: bool
    def __init__(self, server_message_json: _Optional[str] = ..., approval_id: _Optional[str] = ..., authorized_by_standing: bool = ..., authorized_by_approval: bool = ...) -> None: ...

class GrokBotUserComputerFile(_message.Message):
    __slots__ = ("data", "seq", "last")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    seq: int
    last: bool
    def __init__(self, data: _Optional[bytes] = ..., seq: _Optional[int] = ..., last: bool = ...) -> None: ...

class GrokBotUserComputerFileError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerHello(_message.Message):
    __slots__ = ("label", "local_root", "terminals_folder", "standing", "supervised", "variant", "server_authoritative", "capabilities")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROOT_FIELD_NUMBER: _ClassVar[int]
    TERMINALS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    STANDING_FIELD_NUMBER: _ClassVar[int]
    SUPERVISED_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    SERVER_AUTHORITATIVE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    label: str
    local_root: str
    terminals_folder: str
    standing: str
    supervised: bool
    variant: str
    server_authoritative: bool
    capabilities: GrokBotUserComputerCapabilities
    def __init__(self, label: _Optional[str] = ..., local_root: _Optional[str] = ..., terminals_folder: _Optional[str] = ..., standing: _Optional[str] = ..., supervised: bool = ..., variant: _Optional[str] = ..., server_authoritative: bool = ..., capabilities: _Optional[_Union[GrokBotUserComputerCapabilities, _Mapping]] = ...) -> None: ...

class GrokBotUserComputerMessagesAccepted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GrokBotUserComputerMessagesConsentResult(_message.Message):
    __slots__ = ("verdict", "reason")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    verdict: GrokBotUserComputerMessagesConsentVerdict
    reason: str
    def __init__(self, verdict: _Optional[_Union[GrokBotUserComputerMessagesConsentVerdict, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerMessagesError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerMessagesOp(_message.Message):
    __slots__ = ("op_json", "approval_id", "send_key")
    OP_JSON_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_KEY_FIELD_NUMBER: _ClassVar[int]
    op_json: str
    approval_id: str
    send_key: str
    def __init__(self, op_json: _Optional[str] = ..., approval_id: _Optional[str] = ..., send_key: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerMessagesResult(_message.Message):
    __slots__ = ("result_json",)
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    result_json: str
    def __init__(self, result_json: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerPresence(_message.Message):
    __slots__ = ("machine_id", "hello", "last_seen_at_ms")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_MS_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    hello: GrokBotUserComputerHello
    last_seen_at_ms: int
    def __init__(self, machine_id: _Optional[str] = ..., hello: _Optional[_Union[GrokBotUserComputerHello, _Mapping]] = ..., last_seen_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotUserComputerQueuedRequest(_message.Message):
    __slots__ = ("id", "frame", "enqueued_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    ENQUEUED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    frame: GrokBotUserComputerRequestFrame
    enqueued_at_ms: int
    def __init__(self, id: _Optional[str] = ..., frame: _Optional[_Union[GrokBotUserComputerRequestFrame, _Mapping]] = ..., enqueued_at_ms: _Optional[int] = ...) -> None: ...

class GrokBotUserComputerRequestFrame(_message.Message):
    __slots__ = ("request_id", "exec", "upload", "download", "retire_approval", "cancel", "messages_op")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    RETIRE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_OP_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    exec: GrokBotUserComputerExec
    upload: GrokBotUserComputerUpload
    download: GrokBotUserComputerDownload
    retire_approval: GrokBotUserComputerRetireApproval
    cancel: GrokBotUserComputerCancel
    messages_op: GrokBotUserComputerMessagesOp
    def __init__(self, request_id: _Optional[str] = ..., exec: _Optional[_Union[GrokBotUserComputerExec, _Mapping]] = ..., upload: _Optional[_Union[GrokBotUserComputerUpload, _Mapping]] = ..., download: _Optional[_Union[GrokBotUserComputerDownload, _Mapping]] = ..., retire_approval: _Optional[_Union[GrokBotUserComputerRetireApproval, _Mapping]] = ..., cancel: _Optional[_Union[GrokBotUserComputerCancel, _Mapping]] = ..., messages_op: _Optional[_Union[GrokBotUserComputerMessagesOp, _Mapping]] = ...) -> None: ...

class GrokBotUserComputerResponseFrame(_message.Message):
    __slots__ = ("request_id", "client", "control", "file", "file_error", "messages_result", "messages_error", "messages_consent_result", "messages_accepted")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_CONSENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    client: GrokBotUserComputerClientMessage
    control: GrokBotUserComputerControlMessage
    file: GrokBotUserComputerFile
    file_error: GrokBotUserComputerFileError
    messages_result: GrokBotUserComputerMessagesResult
    messages_error: GrokBotUserComputerMessagesError
    messages_consent_result: GrokBotUserComputerMessagesConsentResult
    messages_accepted: GrokBotUserComputerMessagesAccepted
    def __init__(self, request_id: _Optional[str] = ..., client: _Optional[_Union[GrokBotUserComputerClientMessage, _Mapping]] = ..., control: _Optional[_Union[GrokBotUserComputerControlMessage, _Mapping]] = ..., file: _Optional[_Union[GrokBotUserComputerFile, _Mapping]] = ..., file_error: _Optional[_Union[GrokBotUserComputerFileError, _Mapping]] = ..., messages_result: _Optional[_Union[GrokBotUserComputerMessagesResult, _Mapping]] = ..., messages_error: _Optional[_Union[GrokBotUserComputerMessagesError, _Mapping]] = ..., messages_consent_result: _Optional[_Union[GrokBotUserComputerMessagesConsentResult, _Mapping]] = ..., messages_accepted: _Optional[_Union[GrokBotUserComputerMessagesAccepted, _Mapping]] = ...) -> None: ...

class GrokBotUserComputerRetireApproval(_message.Message):
    __slots__ = ("approval_id",)
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    approval_id: str
    def __init__(self, approval_id: _Optional[str] = ...) -> None: ...

class GrokBotUserComputerUpload(_message.Message):
    __slots__ = ("path", "approval_id", "data", "authorized_by_standing", "authorized_by_approval")
    PATH_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_STANDING_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_BY_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    path: str
    approval_id: str
    data: bytes
    authorized_by_standing: bool
    authorized_by_approval: bool
    def __init__(self, path: _Optional[str] = ..., approval_id: _Optional[str] = ..., data: _Optional[bytes] = ..., authorized_by_standing: bool = ..., authorized_by_approval: bool = ...) -> None: ...

class GrokBotUserFormVaultEntry(_message.Message):
    __slots__ = ("entry_id", "kind", "label", "extra_key", "value", "created_at_ms", "last_used_at_ms", "origin_host")
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_HOST_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    kind: str
    label: str
    extra_key: str
    value: str
    created_at_ms: int
    last_used_at_ms: int
    origin_host: str
    def __init__(self, entry_id: _Optional[str] = ..., kind: _Optional[str] = ..., label: _Optional[str] = ..., extra_key: _Optional[str] = ..., value: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., last_used_at_ms: _Optional[int] = ..., origin_host: _Optional[str] = ...) -> None: ...

class GrokBotUserFormVaultKey(_message.Message):
    __slots__ = ("extra_key", "origin_host")
    EXTRA_KEY_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_HOST_FIELD_NUMBER: _ClassVar[int]
    extra_key: str
    origin_host: str
    def __init__(self, extra_key: _Optional[str] = ..., origin_host: _Optional[str] = ...) -> None: ...

class GrokBotUserMcpServerSettings(_message.Message):
    __slots__ = ("server_id", "custom_instructions", "disabled_tools")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    custom_instructions: str
    disabled_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_id: _Optional[str] = ..., custom_instructions: _Optional[str] = ..., disabled_tools: _Optional[_Iterable[str]] = ...) -> None: ...

class GrokBotUserMcpSettings(_message.Message):
    __slots__ = ("servers", "custom_instructions_by_name", "user_time_zone", "user_time_zone_override", "updated_at_ms", "auto_review_instructions")
    class CustomInstructionsByNameEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_INSTRUCTIONS_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    USER_TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    AUTO_REVIEW_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[GrokBotUserMcpServerSettings]
    custom_instructions_by_name: _containers.ScalarMap[str, str]
    user_time_zone: str
    user_time_zone_override: str
    updated_at_ms: int
    auto_review_instructions: GrokBotUserAutoReviewInstructions
    def __init__(self, servers: _Optional[_Iterable[_Union[GrokBotUserMcpServerSettings, _Mapping]]] = ..., custom_instructions_by_name: _Optional[_Mapping[str, str]] = ..., user_time_zone: _Optional[str] = ..., user_time_zone_override: _Optional[str] = ..., updated_at_ms: _Optional[int] = ..., auto_review_instructions: _Optional[_Union[GrokBotUserAutoReviewInstructions, _Mapping]] = ...) -> None: ...

class GrokBotUserRuntimeSettings(_message.Message):
    __slots__ = ("updated_at_ms", "pinned_agents", "sidebar_sections", "has_seen_onboarding")
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    PINNED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    SIDEBAR_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_SEEN_ONBOARDING_FIELD_NUMBER: _ClassVar[int]
    updated_at_ms: int
    pinned_agents: GrokBotPinnedAgents
    sidebar_sections: GrokBotSidebarSections
    has_seen_onboarding: bool
    def __init__(self, updated_at_ms: _Optional[int] = ..., pinned_agents: _Optional[_Union[GrokBotPinnedAgents, _Mapping]] = ..., sidebar_sections: _Optional[_Union[GrokBotSidebarSections, _Mapping]] = ..., has_seen_onboarding: bool = ...) -> None: ...

class HookDescriptor(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class IngestConversationRequest(_message.Message):
    __slots__ = ("conversation_id", "transcript", "transcript_json", "mode", "model", "last_updated_at")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_JSON_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    transcript: str
    transcript_json: str
    mode: str
    model: str
    last_updated_at: int
    def __init__(self, conversation_id: _Optional[str] = ..., transcript: _Optional[str] = ..., transcript_json: _Optional[str] = ..., mode: _Optional[str] = ..., model: _Optional[str] = ..., last_updated_at: _Optional[int] = ...) -> None: ...

class IngestConversationResponse(_message.Message):
    __slots__ = ("success", "summary", "detailed_summary", "error_message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAILED_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    summary: str
    detailed_summary: str
    error_message: str
    def __init__(self, success: bool = ..., summary: _Optional[str] = ..., detailed_summary: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class InstallGrokBotSlackAppRequest(_message.Message):
    __slots__ = ("agent_id", "slack_team_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    slack_team_id: str
    def __init__(self, agent_id: _Optional[str] = ..., slack_team_id: _Optional[str] = ...) -> None: ...

class InstallGrokBotSlackAppResponse(_message.Message):
    __slots__ = ("outcome", "slack_team_id", "workspace_name", "oauth_authorize_url", "workspaces", "slack_error", "retry_after_seconds", "approval_request_filed", "app_removed")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    OAUTH_AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    SLACK_ERROR_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUEST_FILED_FIELD_NUMBER: _ClassVar[int]
    APP_REMOVED_FIELD_NUMBER: _ClassVar[int]
    outcome: GrokBotSlackInstallOutcome
    slack_team_id: str
    workspace_name: str
    oauth_authorize_url: str
    workspaces: _containers.RepeatedCompositeFieldContainer[GrokBotSlackWorkspace]
    slack_error: str
    retry_after_seconds: int
    approval_request_filed: bool
    app_removed: bool
    def __init__(self, outcome: _Optional[_Union[GrokBotSlackInstallOutcome, str]] = ..., slack_team_id: _Optional[str] = ..., workspace_name: _Optional[str] = ..., oauth_authorize_url: _Optional[str] = ..., workspaces: _Optional[_Iterable[_Union[GrokBotSlackWorkspace, _Mapping]]] = ..., slack_error: _Optional[str] = ..., retry_after_seconds: _Optional[int] = ..., approval_request_filed: bool = ..., app_removed: bool = ...) -> None: ...

class InstallUserPluginRequest(_message.Message):
    __slots__ = ("plugin_id", "pinned_git_ref", "variables")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    PINNED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    pinned_git_ref: str
    variables: _struct_pb2.Struct
    def __init__(self, plugin_id: _Optional[int] = ..., pinned_git_ref: _Optional[str] = ..., variables: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class InstallUserPluginResponse(_message.Message):
    __slots__ = ("install",)
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    install: UserPluginInstall
    def __init__(self, install: _Optional[_Union[UserPluginInstall, _Mapping]] = ...) -> None: ...

class InterruptGrokBotAgentRunRequest(_message.Message):
    __slots__ = ("agent_id", "reason", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    reason: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., reason: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class InterruptGrokBotAgentRunResponse(_message.Message):
    __slots__ = ("had_active_run",)
    HAD_ACTIVE_RUN_FIELD_NUMBER: _ClassVar[int]
    had_active_run: bool
    def __init__(self, had_active_run: bool = ...) -> None: ...

class InvalidateGrokBotUserSkillsCacheRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InvalidateGrokBotUserSkillsCacheResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IssueGrokBotUserComputerCredentialRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class IssueGrokBotUserComputerCredentialResponse(_message.Message):
    __slots__ = ("credential", "expires_at_ms", "server_authoritative")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SERVER_AUTHORITATIVE_FIELD_NUMBER: _ClassVar[int]
    credential: str
    expires_at_ms: int
    server_authoritative: bool
    def __init__(self, credential: _Optional[str] = ..., expires_at_ms: _Optional[int] = ..., server_authoritative: bool = ...) -> None: ...

class JiraIntegrationSettings(_message.Message):
    __slots__ = ("hidden",)
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    def __init__(self, hidden: bool = ...) -> None: ...

class KillTeamMemberSandBoxRequest(_message.Message):
    __slots__ = ("team_id", "user_id", "pod_id", "cluster")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    POD_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    user_id: int
    pod_id: str
    cluster: str
    def __init__(self, team_id: _Optional[int] = ..., user_id: _Optional[int] = ..., pod_id: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class KillTeamMemberSandBoxResponse(_message.Message):
    __slots__ = ("killed", "reason", "deleted_count")
    KILLED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    killed: bool
    reason: str
    deleted_count: int
    def __init__(self, killed: bool = ..., reason: _Optional[str] = ..., deleted_count: _Optional[int] = ...) -> None: ...

class LinearIntegrationSettings(_message.Message):
    __slots__ = ("hidden",)
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    def __init__(self, hidden: bool = ...) -> None: ...

class ListGrokBotAccountAutomationsRequest(_message.Message):
    __slots__ = ("time_zone", "agent_ids")
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, time_zone: _Optional[str] = ..., agent_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListGrokBotAccountAutomationsResponse(_message.Message):
    __slots__ = ("agents",)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[GrokBotAccountAutomationGroup]
    def __init__(self, agents: _Optional[_Iterable[_Union[GrokBotAccountAutomationGroup, _Mapping]]] = ...) -> None: ...

class ListGrokBotAgentAutomationsRequest(_message.Message):
    __slots__ = ("agent_id", "time_zone")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    time_zone: str
    def __init__(self, agent_id: _Optional[str] = ..., time_zone: _Optional[str] = ...) -> None: ...

class ListGrokBotAgentAutomationsResponse(_message.Message):
    __slots__ = ("automations",)
    AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    automations: _containers.RepeatedCompositeFieldContainer[GrokBotAgentAutomation]
    def __init__(self, automations: _Optional[_Iterable[_Union[GrokBotAgentAutomation, _Mapping]]] = ...) -> None: ...

class ListGrokBotAgentSessionsRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class ListGrokBotAgentSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[GrokBotAgentSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[GrokBotAgentSession, _Mapping]]] = ...) -> None: ...

class ListGrokBotAgentSkillsRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class ListGrokBotAgentSkillsResponse(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[GrokBotAgentSkill]
    def __init__(self, skills: _Optional[_Iterable[_Union[GrokBotAgentSkill, _Mapping]]] = ...) -> None: ...

class ListGrokBotAgentsRequest(_message.Message):
    __slots__ = ("role", "include_team_agents")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TEAM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    role: str
    include_team_agents: bool
    def __init__(self, role: _Optional[str] = ..., include_team_agents: bool = ...) -> None: ...

class ListGrokBotAgentsResponse(_message.Message):
    __slots__ = ("agents", "slack_connections")
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    SLACK_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[GrokBotAgent]
    slack_connections: _containers.RepeatedCompositeFieldContainer[GrokBotSlackConnection]
    def __init__(self, agents: _Optional[_Iterable[_Union[GrokBotAgent, _Mapping]]] = ..., slack_connections: _Optional[_Iterable[_Union[GrokBotSlackConnection, _Mapping]]] = ...) -> None: ...

class ListGrokBotAgentTodosRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class ListGrokBotAgentTodosResponse(_message.Message):
    __slots__ = ("todos",)
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[_types_pb2.TodoItem]
    def __init__(self, todos: _Optional[_Iterable[_Union[_types_pb2.TodoItem, _Mapping]]] = ...) -> None: ...

class ListGrokBotMarketplaceCategoriesInternalRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGrokBotMarketplaceCategoriesInternalResponse(_message.Message):
    __slots__ = ("categories", "next_page_token")
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[GrokBotMarketplaceCategory]
    next_page_token: str
    def __init__(self, categories: _Optional[_Iterable[_Union[GrokBotMarketplaceCategory, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListGrokBotMarketplaceCreatorsInternalRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGrokBotMarketplaceCreatorsInternalResponse(_message.Message):
    __slots__ = ("creators", "next_page_token")
    CREATORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    creators: _containers.RepeatedCompositeFieldContainer[GrokBotMarketplaceCreator]
    next_page_token: str
    def __init__(self, creators: _Optional[_Iterable[_Union[GrokBotMarketplaceCreator, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListGrokBotMarketplaceListingsInternalRequest(_message.Message):
    __slots__ = ("status", "category", "template_id", "page_size", "page_token")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    status: GrokBotMarketplaceListingStatus
    category: str
    template_id: int
    page_size: int
    page_token: str
    def __init__(self, status: _Optional[_Union[GrokBotMarketplaceListingStatus, str]] = ..., category: _Optional[str] = ..., template_id: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGrokBotMarketplaceListingsInternalResponse(_message.Message):
    __slots__ = ("listings", "next_page_token")
    LISTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    listings: _containers.RepeatedCompositeFieldContainer[GrokBotMarketplaceListing]
    next_page_token: str
    def __init__(self, listings: _Optional[_Iterable[_Union[GrokBotMarketplaceListing, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListGrokBotMemoryShardsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGrokBotMemoryShardsResponse(_message.Message):
    __slots__ = ("shards",)
    SHARDS_FIELD_NUMBER: _ClassVar[int]
    shards: _containers.RepeatedCompositeFieldContainer[GrokBotMemoryShard]
    def __init__(self, shards: _Optional[_Iterable[_Union[GrokBotMemoryShard, _Mapping]]] = ...) -> None: ...

class ListGrokBotSecretsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListGrokBotSecretsResponse(_message.Message):
    __slots__ = ("secrets",)
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    secrets: _containers.RepeatedCompositeFieldContainer[GrokBotSecret]
    def __init__(self, secrets: _Optional[_Iterable[_Union[GrokBotSecret, _Mapping]]] = ...) -> None: ...

class ListGrokBotStripeLinkPaymentMethodsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGrokBotStripeLinkPaymentMethodsResponse(_message.Message):
    __slots__ = ("outcome", "payment_methods", "unavailable_count")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    outcome: GrokBotStripeLinkPaymentMethodsOutcome
    payment_methods: _containers.RepeatedCompositeFieldContainer[GrokBotStripeLinkPaymentMethod]
    unavailable_count: int
    def __init__(self, outcome: _Optional[_Union[GrokBotStripeLinkPaymentMethodsOutcome, str]] = ..., payment_methods: _Optional[_Iterable[_Union[GrokBotStripeLinkPaymentMethod, _Mapping]]] = ..., unavailable_count: _Optional[int] = ...) -> None: ...

class ListGrokBotTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGrokBotTemplatesResponse(_message.Message):
    __slots__ = ("templates", "export_policy")
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[GrokBotTemplate]
    export_policy: str
    def __init__(self, templates: _Optional[_Iterable[_Union[GrokBotTemplate, _Mapping]]] = ..., export_policy: _Optional[str] = ...) -> None: ...

class ListGrokBotTranscriptEntriesRequest(_message.Message):
    __slots__ = ("agent_id", "generation", "before_seq", "limit", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    BEFORE_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    generation: int
    before_seq: int
    limit: int
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., generation: _Optional[int] = ..., before_seq: _Optional[int] = ..., limit: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class ListGrokBotTranscriptEntriesResponse(_message.Message):
    __slots__ = ("entries", "generation")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptEntry]
    generation: int
    def __init__(self, entries: _Optional[_Iterable[_Union[GrokBotTranscriptEntry, _Mapping]]] = ..., generation: _Optional[int] = ...) -> None: ...

class ListGrokBotUserComputersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGrokBotUserComputersResponse(_message.Message):
    __slots__ = ("computers",)
    COMPUTERS_FIELD_NUMBER: _ClassVar[int]
    computers: _containers.RepeatedCompositeFieldContainer[GrokBotUserComputerPresence]
    def __init__(self, computers: _Optional[_Iterable[_Union[GrokBotUserComputerPresence, _Mapping]]] = ...) -> None: ...

class ListGrokBotUserFormVaultEntriesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGrokBotUserFormVaultEntriesResponse(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[GrokBotUserFormVaultEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[GrokBotUserFormVaultEntry, _Mapping]]] = ...) -> None: ...

class ListGrokBotUserFormVaultKeysRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGrokBotUserFormVaultKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[GrokBotUserFormVaultKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[GrokBotUserFormVaultKey, _Mapping]]] = ...) -> None: ...

class ListMarketplacePluginsRequest(_message.Message):
    __slots__ = ("search", "tags", "page_size", "page_token", "marketplace_id", "publisher_id", "skip_team_admin_filter", "exclude_cloud_agent_plugins")
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_TEAM_ADMIN_FILTER_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CLOUD_AGENT_PLUGINS_FIELD_NUMBER: _ClassVar[int]
    search: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    marketplace_id: int
    publisher_id: int
    skip_team_admin_filter: bool
    exclude_cloud_agent_plugins: bool
    def __init__(self, search: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., marketplace_id: _Optional[int] = ..., publisher_id: _Optional[int] = ..., skip_team_admin_filter: bool = ..., exclude_cloud_agent_plugins: bool = ...) -> None: ...

class ListMarketplacePluginsResponse(_message.Message):
    __slots__ = ("plugins", "next_page_token", "has_more")
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[Plugin]
    next_page_token: str
    has_more: bool
    def __init__(self, plugins: _Optional[_Iterable[_Union[Plugin, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: bool = ...) -> None: ...

class ListMarketplacesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListMarketplacesResponse(_message.Message):
    __slots__ = ("marketplaces",)
    MARKETPLACES_FIELD_NUMBER: _ClassVar[int]
    marketplaces: _containers.RepeatedCompositeFieldContainer[Marketplace]
    def __init__(self, marketplaces: _Optional[_Iterable[_Union[Marketplace, _Mapping]]] = ...) -> None: ...

class ListPublicGrokBotMarketplaceListingsRequest(_message.Message):
    __slots__ = ("category", "page_size", "page_token")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    category: str
    page_size: int
    page_token: str
    def __init__(self, category: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPublicGrokBotMarketplaceListingsResponse(_message.Message):
    __slots__ = ("featured_listings", "listings", "next_page_token", "all_categories_order")
    FEATURED_LISTINGS_FIELD_NUMBER: _ClassVar[int]
    LISTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ALL_CATEGORIES_ORDER_FIELD_NUMBER: _ClassVar[int]
    featured_listings: _containers.RepeatedCompositeFieldContainer[PublicGrokBotMarketplaceListing]
    listings: _containers.RepeatedCompositeFieldContainer[PublicGrokBotMarketplaceListing]
    next_page_token: str
    all_categories_order: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, featured_listings: _Optional[_Iterable[_Union[PublicGrokBotMarketplaceListing, _Mapping]]] = ..., listings: _Optional[_Iterable[_Union[PublicGrokBotMarketplaceListing, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., all_categories_order: _Optional[_Iterable[str]] = ...) -> None: ...

class ListSandBoxesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSandBoxesResponse(_message.Message):
    __slots__ = ("boxes",)
    BOXES_FIELD_NUMBER: _ClassVar[int]
    boxes: _containers.RepeatedCompositeFieldContainer[SandBoxDescriptor]
    def __init__(self, boxes: _Optional[_Iterable[_Union[SandBoxDescriptor, _Mapping]]] = ...) -> None: ...

class ListSandBoxStoreObjectsRequest(_message.Message):
    __slots__ = ("prefix", "cursor", "max_entries")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    cursor: str
    max_entries: int
    def __init__(self, prefix: _Optional[str] = ..., cursor: _Optional[str] = ..., max_entries: _Optional[int] = ...) -> None: ...

class ListSandBoxStoreObjectsResponse(_message.Message):
    __slots__ = ("entries", "next_cursor", "truncated")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[SandBoxStoreObjectEntry]
    next_cursor: str
    truncated: bool
    def __init__(self, entries: _Optional[_Iterable[_Union[SandBoxStoreObjectEntry, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., truncated: bool = ...) -> None: ...

class ListSandMachinesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSandMachinesResponse(_message.Message):
    __slots__ = ("machines",)
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    machines: _containers.RepeatedCompositeFieldContainer[SandMachine]
    def __init__(self, machines: _Optional[_Iterable[_Union[SandMachine, _Mapping]]] = ...) -> None: ...

class ListSandMcpToolsRequest(_message.Message):
    __slots__ = ("server_identifiers", "mcp_config_json", "grok_bot_plugin_scope")
    SERVER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    GROK_BOT_PLUGIN_SCOPE_FIELD_NUMBER: _ClassVar[int]
    server_identifiers: _containers.RepeatedScalarFieldContainer[str]
    mcp_config_json: str
    grok_bot_plugin_scope: GrokBotPluginScope
    def __init__(self, server_identifiers: _Optional[_Iterable[str]] = ..., mcp_config_json: _Optional[str] = ..., grok_bot_plugin_scope: _Optional[_Union[GrokBotPluginScope, _Mapping]] = ...) -> None: ...

class ListSandMcpToolsResponse(_message.Message):
    __slots__ = ("servers",)
    class Server(_message.Message):
        __slots__ = ("server_identifier", "status", "tools", "account_label", "row_server_identifier", "served_by")
        SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TOOLS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LABEL_FIELD_NUMBER: _ClassVar[int]
        ROW_SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        SERVED_BY_FIELD_NUMBER: _ClassVar[int]
        server_identifier: str
        status: str
        tools: _containers.RepeatedCompositeFieldContainer[_types_pb2.McpToolDefinition]
        account_label: str
        row_server_identifier: str
        served_by: McpServedBy
        def __init__(self, server_identifier: _Optional[str] = ..., status: _Optional[str] = ..., tools: _Optional[_Iterable[_Union[_types_pb2.McpToolDefinition, _Mapping]]] = ..., account_label: _Optional[str] = ..., row_server_identifier: _Optional[str] = ..., served_by: _Optional[_Union[McpServedBy, str]] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[ListSandMcpToolsResponse.Server]
    def __init__(self, servers: _Optional[_Iterable[_Union[ListSandMcpToolsResponse.Server, _Mapping]]] = ...) -> None: ...

class ListSandSetupManifestsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSandSetupManifestsResponse(_message.Message):
    __slots__ = ("schema_version", "manifests")
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    schema_version: int
    manifests: _containers.RepeatedCompositeFieldContainer[SandAssignedSetupManifest]
    def __init__(self, schema_version: _Optional[int] = ..., manifests: _Optional[_Iterable[_Union[SandAssignedSetupManifest, _Mapping]]] = ...) -> None: ...

class ListTeamMemberSandBoxesRequest(_message.Message):
    __slots__ = ("team_id", "user_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    user_id: int
    def __init__(self, team_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class ListTeamMemberSandBoxesResponse(_message.Message):
    __slots__ = ("user_id", "email", "name", "boxes", "scan_incomplete")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BOXES_FIELD_NUMBER: _ClassVar[int]
    SCAN_INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    email: str
    name: str
    boxes: _containers.RepeatedCompositeFieldContainer[TeamMemberSandBoxPod]
    scan_incomplete: bool
    def __init__(self, user_id: _Optional[int] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., boxes: _Optional[_Iterable[_Union[TeamMemberSandBoxPod, _Mapping]]] = ..., scan_incomplete: bool = ...) -> None: ...

class ListTeamSandSetupManifestsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTeamSandSetupManifestsResponse(_message.Message):
    __slots__ = ("team_id", "can_manage", "manifests")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    can_manage: bool
    manifests: _containers.RepeatedCompositeFieldContainer[SandTeamSetupManifest]
    def __init__(self, team_id: _Optional[str] = ..., can_manage: bool = ..., manifests: _Optional[_Iterable[_Union[SandTeamSetupManifest, _Mapping]]] = ...) -> None: ...

class ListUserCanvasesRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "shared_only")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHARED_ONLY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    shared_only: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., shared_only: bool = ...) -> None: ...

class ListUserCanvasesResponse(_message.Message):
    __slots__ = ("store_id", "canvases", "next_page_token")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    CANVASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    canvases: _containers.RepeatedCompositeFieldContainer[CloudCanvasMetadata]
    next_page_token: str
    def __init__(self, store_id: _Optional[str] = ..., canvases: _Optional[_Iterable[_Union[CloudCanvasMetadata, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class LlmGatewayRoutedModelEntry(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class LlmGatewayRouting(_message.Message):
    __slots__ = ("providers",)
    class ProvidersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: LlmGatewayRoutingProviderEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[LlmGatewayRoutingProviderEntry, _Mapping]] = ...) -> None: ...
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.MessageMap[str, LlmGatewayRoutingProviderEntry]
    def __init__(self, providers: _Optional[_Mapping[str, LlmGatewayRoutingProviderEntry]] = ...) -> None: ...

class LlmGatewayRoutingProviderEntry(_message.Message):
    __slots__ = ("enabled", "models")
    class ModelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: LlmGatewayRoutedModelEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[LlmGatewayRoutedModelEntry, _Mapping]] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    models: _containers.MessageMap[str, LlmGatewayRoutedModelEntry]
    def __init__(self, enabled: bool = ..., models: _Optional[_Mapping[str, LlmGatewayRoutedModelEntry]] = ...) -> None: ...

class LlmGatewaySettings(_message.Message):
    __slots__ = ("enabled", "endpoints", "audience", "routing", "can_enable", "auth_mode", "team_credential_status", "credential_source_strategy", "outbound_model_prefixes", "outbound_model_rewrites")
    class EndpointsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OutboundModelPrefixesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OutboundModelRewritesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_FIELD_NUMBER: _ClassVar[int]
    CAN_ENABLE_FIELD_NUMBER: _ClassVar[int]
    AUTH_MODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_CREDENTIAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_SOURCE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_MODEL_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_MODEL_REWRITES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    endpoints: _containers.ScalarMap[str, str]
    audience: str
    routing: LlmGatewayRouting
    can_enable: bool
    auth_mode: LlmGatewayAuthMode
    team_credential_status: LlmGatewayTeamCredentialStatus
    credential_source_strategy: LlmGatewayCredentialSourceStrategy
    outbound_model_prefixes: _containers.ScalarMap[str, str]
    outbound_model_rewrites: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., endpoints: _Optional[_Mapping[str, str]] = ..., audience: _Optional[str] = ..., routing: _Optional[_Union[LlmGatewayRouting, _Mapping]] = ..., can_enable: bool = ..., auth_mode: _Optional[_Union[LlmGatewayAuthMode, str]] = ..., team_credential_status: _Optional[_Union[LlmGatewayTeamCredentialStatus, _Mapping]] = ..., credential_source_strategy: _Optional[_Union[LlmGatewayCredentialSourceStrategy, str]] = ..., outbound_model_prefixes: _Optional[_Mapping[str, str]] = ..., outbound_model_rewrites: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LlmGatewayTeamCredentialStatus(_message.Message):
    __slots__ = ("configured",)
    CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    configured: bool
    def __init__(self, configured: bool = ...) -> None: ...

class LocalToolControls(_message.Message):
    __slots__ = ("permission_ceiling",)
    PERMISSION_CEILING_FIELD_NUMBER: _ClassVar[int]
    permission_ceiling: LocalToolPermissionCeiling
    def __init__(self, permission_ceiling: _Optional[_Union[LocalToolPermissionCeiling, str]] = ...) -> None: ...

class ManagedSkill(_message.Message):
    __slots__ = ("id", "description", "content", "disable_model_invocation", "environments", "disabled_environments", "enabled", "custom_mode", "resources")
    class ResourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MODEL_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MODE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    content: str
    disable_model_invocation: bool
    environments: _containers.RepeatedScalarFieldContainer[str]
    disabled_environments: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    custom_mode: _types_pb2.CustomModeDescriptor
    resources: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., content: _Optional[str] = ..., disable_model_invocation: bool = ..., environments: _Optional[_Iterable[str]] = ..., disabled_environments: _Optional[_Iterable[str]] = ..., enabled: bool = ..., custom_mode: _Optional[_Union[_types_pb2.CustomModeDescriptor, _Mapping]] = ..., resources: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Marketplace(_message.Message):
    __slots__ = ("id", "name", "display_name", "description", "git_url", "git_ref", "user_id", "team_id", "logo_url", "created_at", "updated_at", "last_indexed_at", "last_indexed_commit_sha", "team_config", "required_plugin_installs", "auto_reindex", "distribution_git_url", "is_default", "allow_user_publish")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GIT_URL_FIELD_NUMBER: _ClassVar[int]
    GIT_REF_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_INDEXED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_INDEXED_COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    TEAM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PLUGIN_INSTALLS_FIELD_NUMBER: _ClassVar[int]
    AUTO_REINDEX_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_GIT_URL_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_USER_PUBLISH_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    display_name: str
    description: str
    git_url: str
    git_ref: str
    user_id: int
    team_id: int
    logo_url: str
    created_at: int
    updated_at: int
    last_indexed_at: int
    last_indexed_commit_sha: str
    team_config: TeamMarketplaceConfig
    required_plugin_installs: _containers.RepeatedCompositeFieldContainer[MarketplaceRequiredPluginInstall]
    auto_reindex: bool
    distribution_git_url: str
    is_default: bool
    allow_user_publish: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., git_url: _Optional[str] = ..., git_ref: _Optional[str] = ..., user_id: _Optional[int] = ..., team_id: _Optional[int] = ..., logo_url: _Optional[str] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., last_indexed_at: _Optional[int] = ..., last_indexed_commit_sha: _Optional[str] = ..., team_config: _Optional[_Union[TeamMarketplaceConfig, _Mapping]] = ..., required_plugin_installs: _Optional[_Iterable[_Union[MarketplaceRequiredPluginInstall, _Mapping]]] = ..., auto_reindex: bool = ..., distribution_git_url: _Optional[str] = ..., is_default: bool = ..., allow_user_publish: bool = ...) -> None: ...

class MarketplaceAccessGrant(_message.Message):
    __slots__ = ("principal_kind", "principal_id")
    PRINCIPAL_KIND_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    principal_kind: MarketplaceAccessPrincipalKind
    principal_id: str
    def __init__(self, principal_kind: _Optional[_Union[MarketplaceAccessPrincipalKind, str]] = ..., principal_id: _Optional[str] = ...) -> None: ...

class MarketplaceRequiredPluginInstall(_message.Message):
    __slots__ = ("plugin_id", "directory_group_ids")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    directory_group_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, plugin_id: _Optional[int] = ..., directory_group_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class MCPControls(_message.Message):
    __slots__ = ("enabled", "allowed_tools")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    allowed_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: bool = ..., allowed_tools: _Optional[_Iterable[str]] = ...) -> None: ...

class McpDescriptor(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class McpServerMetadata(_message.Message):
    __slots__ = ("plugin_id", "server_id")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    server_id: int
    def __init__(self, plugin_id: _Optional[int] = ..., server_id: _Optional[int] = ...) -> None: ...

class MintSandVoiceCallSecretRequest(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str
    def __init__(self, model: _Optional[str] = ...) -> None: ...

class MintSandVoiceCallSecretResponse(_message.Message):
    __slots__ = ("client_secret", "expires_at_unix_seconds", "model", "websocket_url")
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_UNIX_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    WEBSOCKET_URL_FIELD_NUMBER: _ClassVar[int]
    client_secret: str
    expires_at_unix_seconds: int
    model: str
    websocket_url: str
    def __init__(self, client_secret: _Optional[str] = ..., expires_at_unix_seconds: _Optional[int] = ..., model: _Optional[str] = ..., websocket_url: _Optional[str] = ...) -> None: ...

class ModelAllowlist(_message.Message):
    __slots__ = ("new_provider_default", "new_model_default", "providers", "byok", "new_model_default_enabled_at", "new_first_party_model_default", "can_set_first_party_default_manually", "new_first_party_model_default_enabled_at", "first_party_pending_models")
    class DefaultBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_BEHAVIOR_UNSPECIFIED: _ClassVar[ModelAllowlist.DefaultBehavior]
        DEFAULT_BEHAVIOR_ENABLED: _ClassVar[ModelAllowlist.DefaultBehavior]
        DEFAULT_BEHAVIOR_DISABLED: _ClassVar[ModelAllowlist.DefaultBehavior]
    DEFAULT_BEHAVIOR_UNSPECIFIED: ModelAllowlist.DefaultBehavior
    DEFAULT_BEHAVIOR_ENABLED: ModelAllowlist.DefaultBehavior
    DEFAULT_BEHAVIOR_DISABLED: ModelAllowlist.DefaultBehavior
    class FirstPartyModelDefault(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRST_PARTY_MODEL_DEFAULT_UNSPECIFIED: _ClassVar[ModelAllowlist.FirstPartyModelDefault]
        FIRST_PARTY_MODEL_DEFAULT_IMMEDIATELY: _ClassVar[ModelAllowlist.FirstPartyModelDefault]
        FIRST_PARTY_MODEL_DEFAULT_AFTER_7_DAYS: _ClassVar[ModelAllowlist.FirstPartyModelDefault]
        FIRST_PARTY_MODEL_DEFAULT_MANUALLY: _ClassVar[ModelAllowlist.FirstPartyModelDefault]
    FIRST_PARTY_MODEL_DEFAULT_UNSPECIFIED: ModelAllowlist.FirstPartyModelDefault
    FIRST_PARTY_MODEL_DEFAULT_IMMEDIATELY: ModelAllowlist.FirstPartyModelDefault
    FIRST_PARTY_MODEL_DEFAULT_AFTER_7_DAYS: ModelAllowlist.FirstPartyModelDefault
    FIRST_PARTY_MODEL_DEFAULT_MANUALLY: ModelAllowlist.FirstPartyModelDefault
    class ProvidersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelAllowlistProviderEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ModelAllowlistProviderEntry, _Mapping]] = ...) -> None: ...
    NEW_PROVIDER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    NEW_MODEL_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    BYOK_FIELD_NUMBER: _ClassVar[int]
    NEW_MODEL_DEFAULT_ENABLED_AT_FIELD_NUMBER: _ClassVar[int]
    NEW_FIRST_PARTY_MODEL_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CAN_SET_FIRST_PARTY_DEFAULT_MANUALLY_FIELD_NUMBER: _ClassVar[int]
    NEW_FIRST_PARTY_MODEL_DEFAULT_ENABLED_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_PARTY_PENDING_MODELS_FIELD_NUMBER: _ClassVar[int]
    new_provider_default: ModelAllowlist.DefaultBehavior
    new_model_default: ModelAllowlist.DefaultBehavior
    providers: _containers.MessageMap[str, ModelAllowlistProviderEntry]
    byok: ModelAllowlistByok
    new_model_default_enabled_at: int
    new_first_party_model_default: ModelAllowlist.FirstPartyModelDefault
    can_set_first_party_default_manually: bool
    new_first_party_model_default_enabled_at: int
    first_party_pending_models: _containers.RepeatedCompositeFieldContainer[FirstPartyPendingModel]
    def __init__(self, new_provider_default: _Optional[_Union[ModelAllowlist.DefaultBehavior, str]] = ..., new_model_default: _Optional[_Union[ModelAllowlist.DefaultBehavior, str]] = ..., providers: _Optional[_Mapping[str, ModelAllowlistProviderEntry]] = ..., byok: _Optional[_Union[ModelAllowlistByok, _Mapping]] = ..., new_model_default_enabled_at: _Optional[int] = ..., new_first_party_model_default: _Optional[_Union[ModelAllowlist.FirstPartyModelDefault, str]] = ..., can_set_first_party_default_manually: bool = ..., new_first_party_model_default_enabled_at: _Optional[int] = ..., first_party_pending_models: _Optional[_Iterable[_Union[FirstPartyPendingModel, _Mapping]]] = ...) -> None: ...

class ModelAllowlistByok(_message.Message):
    __slots__ = ("openai", "anthropic", "google", "azure", "bedrock")
    OPENAI_FIELD_NUMBER: _ClassVar[int]
    ANTHROPIC_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_FIELD_NUMBER: _ClassVar[int]
    openai: ModelAllowlistByokEntry
    anthropic: ModelAllowlistByokEntry
    google: ModelAllowlistByokEntry
    azure: ModelAllowlistByokEntry
    bedrock: ModelAllowlistByokEntry
    def __init__(self, openai: _Optional[_Union[ModelAllowlistByokEntry, _Mapping]] = ..., anthropic: _Optional[_Union[ModelAllowlistByokEntry, _Mapping]] = ..., google: _Optional[_Union[ModelAllowlistByokEntry, _Mapping]] = ..., azure: _Optional[_Union[ModelAllowlistByokEntry, _Mapping]] = ..., bedrock: _Optional[_Union[ModelAllowlistByokEntry, _Mapping]] = ...) -> None: ...

class ModelAllowlistByokEntry(_message.Message):
    __slots__ = ("enabled", "models")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    models: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: bool = ..., models: _Optional[_Iterable[str]] = ...) -> None: ...

class ModelAllowlistModelEntry(_message.Message):
    __slots__ = ("enabled", "parameter_restrictions", "parameter_grants", "default_parameter_values")
    class ParameterRestrictionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelAllowlistParameterRestriction
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ModelAllowlistParameterRestriction, _Mapping]] = ...) -> None: ...
    class ParameterGrantsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelAllowlistParameterGrant
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ModelAllowlistParameterGrant, _Mapping]] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_GRANTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARAMETER_VALUES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    parameter_restrictions: _containers.MessageMap[str, ModelAllowlistParameterRestriction]
    parameter_grants: _containers.MessageMap[str, ModelAllowlistParameterGrant]
    default_parameter_values: _containers.RepeatedCompositeFieldContainer[TeamAdminModelRef.ModelParameterValue]
    def __init__(self, enabled: bool = ..., parameter_restrictions: _Optional[_Mapping[str, ModelAllowlistParameterRestriction]] = ..., parameter_grants: _Optional[_Mapping[str, ModelAllowlistParameterGrant]] = ..., default_parameter_values: _Optional[_Iterable[_Union[TeamAdminModelRef.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class ModelAllowlistParameterGrant(_message.Message):
    __slots__ = ("granted_values",)
    GRANTED_VALUES_FIELD_NUMBER: _ClassVar[int]
    granted_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, granted_values: _Optional[_Iterable[str]] = ...) -> None: ...

class ModelAllowlistParameterRestriction(_message.Message):
    __slots__ = ("allowed_values",)
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowed_values: _Optional[_Iterable[str]] = ...) -> None: ...

class ModelAllowlistProviderEntry(_message.Message):
    __slots__ = ("enabled", "models")
    class ModelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelAllowlistModelEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ModelAllowlistModelEntry, _Mapping]] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    models: _containers.MessageMap[str, ModelAllowlistModelEntry]
    def __init__(self, enabled: bool = ..., models: _Optional[_Mapping[str, ModelAllowlistModelEntry]] = ...) -> None: ...

class ModelParameterDefinition(_message.Message):
    __slots__ = ("id", "name", "markdown_tooltip", "parameter_type", "is_cycleable_by_hotkey")
    class BooleanParameterDefinition(_message.Message):
        __slots__ = ("values",)
        class BooleanParameterValue(_message.Message):
            __slots__ = ("value", "display_name", "increases_model_cost", "default_blocked_in_admin_allowlist", "hide_from_user_picker_when_admin_blocked", "blocked_by_admin_allowlist")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            INCREASES_MODEL_COST_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_BLOCKED_IN_ADMIN_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
            HIDE_FROM_USER_PICKER_WHEN_ADMIN_BLOCKED_FIELD_NUMBER: _ClassVar[int]
            BLOCKED_BY_ADMIN_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
            value: str
            display_name: str
            increases_model_cost: bool
            default_blocked_in_admin_allowlist: bool
            hide_from_user_picker_when_admin_blocked: bool
            blocked_by_admin_allowlist: bool
            def __init__(self, value: _Optional[str] = ..., display_name: _Optional[str] = ..., increases_model_cost: bool = ..., default_blocked_in_admin_allowlist: bool = ..., hide_from_user_picker_when_admin_blocked: bool = ..., blocked_by_admin_allowlist: bool = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[ModelParameterDefinition.BooleanParameterDefinition.BooleanParameterValue]
        def __init__(self, values: _Optional[_Iterable[_Union[ModelParameterDefinition.BooleanParameterDefinition.BooleanParameterValue, _Mapping]]] = ...) -> None: ...
    class EnumParameterDefinition(_message.Message):
        __slots__ = ("values",)
        class EnumParameterValue(_message.Message):
            __slots__ = ("value", "display_name", "increases_model_cost", "blocked_by_admin_allowlist", "markdown_tooltip", "model_picker_badges")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            INCREASES_MODEL_COST_FIELD_NUMBER: _ClassVar[int]
            BLOCKED_BY_ADMIN_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
            MARKDOWN_TOOLTIP_FIELD_NUMBER: _ClassVar[int]
            MODEL_PICKER_BADGES_FIELD_NUMBER: _ClassVar[int]
            value: str
            display_name: str
            increases_model_cost: bool
            blocked_by_admin_allowlist: bool
            markdown_tooltip: str
            model_picker_badges: _containers.RepeatedCompositeFieldContainer[AvailableModelsResponse.ModelPickerBadge]
            def __init__(self, value: _Optional[str] = ..., display_name: _Optional[str] = ..., increases_model_cost: bool = ..., blocked_by_admin_allowlist: bool = ..., markdown_tooltip: _Optional[str] = ..., model_picker_badges: _Optional[_Iterable[_Union[AvailableModelsResponse.ModelPickerBadge, _Mapping]]] = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[ModelParameterDefinition.EnumParameterDefinition.EnumParameterValue]
        def __init__(self, values: _Optional[_Iterable[_Union[ModelParameterDefinition.EnumParameterDefinition.EnumParameterValue, _Mapping]]] = ...) -> None: ...
    class ModelParameterType(_message.Message):
        __slots__ = ("boolean_parameter", "enum_parameter")
        BOOLEAN_PARAMETER_FIELD_NUMBER: _ClassVar[int]
        ENUM_PARAMETER_FIELD_NUMBER: _ClassVar[int]
        boolean_parameter: ModelParameterDefinition.BooleanParameterDefinition
        enum_parameter: ModelParameterDefinition.EnumParameterDefinition
        def __init__(self, boolean_parameter: _Optional[_Union[ModelParameterDefinition.BooleanParameterDefinition, _Mapping]] = ..., enum_parameter: _Optional[_Union[ModelParameterDefinition.EnumParameterDefinition, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN_TOOLTIP_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CYCLEABLE_BY_HOTKEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    markdown_tooltip: str
    parameter_type: ModelParameterDefinition.ModelParameterType
    is_cycleable_by_hotkey: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., markdown_tooltip: _Optional[str] = ..., parameter_type: _Optional[_Union[ModelParameterDefinition.ModelParameterType, _Mapping]] = ..., is_cycleable_by_hotkey: bool = ...) -> None: ...

class NotifySandAgentTurnFinishedRequest(_message.Message):
    __slots__ = ("agent_id", "agent_name", "message_preview", "last_message_id", "awaiting_user_response", "member_agent_ids", "sender_agent_id", "message_content_json")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AWAITING_USER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    SENDER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CONTENT_JSON_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    agent_name: str
    message_preview: str
    last_message_id: str
    awaiting_user_response: bool
    member_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    sender_agent_id: str
    message_content_json: str
    def __init__(self, agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., message_preview: _Optional[str] = ..., last_message_id: _Optional[str] = ..., awaiting_user_response: bool = ..., member_agent_ids: _Optional[_Iterable[str]] = ..., sender_agent_id: _Optional[str] = ..., message_content_json: _Optional[str] = ...) -> None: ...

class NotifySandAgentTurnFinishedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnePasswordConnection(_message.Message):
    __slots__ = ("connection_id", "account_uuid", "account_email", "account_url", "vault_id", "vault_name", "item_count", "catalog_revision", "last_successful_sync_at_ms", "last_sync_error_code", "credential_generation", "issued_at_ms", "expires_at_ms", "renew_by_at_ms", "reminder_at_ms", "lifecycle_state", "expiration_mode", "provider_expiry_requested", "always_allow")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_UUID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_URL_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    CATALOG_REVISION_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_SYNC_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_GENERATION_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    RENEW_BY_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REMINDER_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXPIRY_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ALLOW_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    account_uuid: str
    account_email: str
    account_url: str
    vault_id: str
    vault_name: str
    item_count: int
    catalog_revision: str
    last_successful_sync_at_ms: int
    last_sync_error_code: str
    credential_generation: int
    issued_at_ms: int
    expires_at_ms: int
    renew_by_at_ms: int
    reminder_at_ms: int
    lifecycle_state: CredentialLifecycleState
    expiration_mode: CredentialExpirationMode
    provider_expiry_requested: bool
    always_allow: bool
    def __init__(self, connection_id: _Optional[str] = ..., account_uuid: _Optional[str] = ..., account_email: _Optional[str] = ..., account_url: _Optional[str] = ..., vault_id: _Optional[str] = ..., vault_name: _Optional[str] = ..., item_count: _Optional[int] = ..., catalog_revision: _Optional[str] = ..., last_successful_sync_at_ms: _Optional[int] = ..., last_sync_error_code: _Optional[str] = ..., credential_generation: _Optional[int] = ..., issued_at_ms: _Optional[int] = ..., expires_at_ms: _Optional[int] = ..., renew_by_at_ms: _Optional[int] = ..., reminder_at_ms: _Optional[int] = ..., lifecycle_state: _Optional[_Union[CredentialLifecycleState, str]] = ..., expiration_mode: _Optional[_Union[CredentialExpirationMode, str]] = ..., provider_expiry_requested: bool = ..., always_allow: bool = ...) -> None: ...

class OnePasswordCredentialDecisionResponse(_message.Message):
    __slots__ = ("ok", "detail")
    OK_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    detail: str
    def __init__(self, ok: bool = ..., detail: _Optional[str] = ...) -> None: ...

class OnePasswordCredentialItem(_message.Message):
    __slots__ = ("credential_id", "title", "category", "sites", "target_rules", "vault_name", "connection_id", "catalog_revision")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SITES_FIELD_NUMBER: _ClassVar[int]
    TARGET_RULES_FIELD_NUMBER: _ClassVar[int]
    VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_REVISION_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    title: str
    category: str
    sites: _containers.RepeatedScalarFieldContainer[str]
    target_rules: _containers.RepeatedCompositeFieldContainer[CredentialTargetRule]
    vault_name: str
    connection_id: str
    catalog_revision: str
    def __init__(self, credential_id: _Optional[str] = ..., title: _Optional[str] = ..., category: _Optional[str] = ..., sites: _Optional[_Iterable[str]] = ..., target_rules: _Optional[_Iterable[_Union[CredentialTargetRule, _Mapping]]] = ..., vault_name: _Optional[str] = ..., connection_id: _Optional[str] = ..., catalog_revision: _Optional[str] = ...) -> None: ...

class OnePasswordState(_message.Message):
    __slots__ = ("connections", "items")
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[OnePasswordConnection]
    items: _containers.RepeatedCompositeFieldContainer[OnePasswordCredentialItem]
    def __init__(self, connections: _Optional[_Iterable[_Union[OnePasswordConnection, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[OnePasswordCredentialItem, _Mapping]]] = ...) -> None: ...

class OpenGrokBotUserComputerRequestRequest(_message.Message):
    __slots__ = ("machine_id", "frame", "idempotency_key")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    frame: GrokBotUserComputerRequestFrame
    idempotency_key: str
    def __init__(self, machine_id: _Optional[str] = ..., frame: _Optional[_Union[GrokBotUserComputerRequestFrame, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class Plugin(_message.Message):
    __slots__ = ("id", "name", "display_name", "description", "status", "repository_url", "tags", "logo_url", "primary_color", "is_published", "created_at", "updated_at", "publisher_id", "publisher", "is_deprecated", "deprecation_message", "deprecated_at", "replaced_by_plugin_id", "marketplace_id", "marketplace", "git_url", "git_ref", "git_path", "full_ref", "skills", "subagents", "hooks", "rules", "mcp_servers", "commands", "release_repo", "release_asset", "release_tag", "curated_category_keys", "variables", "team_marketplace_install_mode", "team_marketplace_configured_variables", "lifecycle_state", "min_client_versions", "published_by_user")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    IS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_AT_FIELD_NUMBER: _ClassVar[int]
    REPLACED_BY_PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    GIT_URL_FIELD_NUMBER: _ClassVar[int]
    GIT_REF_FIELD_NUMBER: _ClassVar[int]
    GIT_PATH_FIELD_NUMBER: _ClassVar[int]
    FULL_REF_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_REPO_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ASSET_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TAG_FIELD_NUMBER: _ClassVar[int]
    CURATED_CATEGORY_KEYS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    TEAM_MARKETPLACE_INSTALL_MODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_MARKETPLACE_CONFIGURED_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    MIN_CLIENT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    display_name: str
    description: str
    status: PluginStatus
    repository_url: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    logo_url: str
    primary_color: str
    is_published: bool
    created_at: int
    updated_at: int
    publisher_id: int
    publisher: Publisher
    is_deprecated: bool
    deprecation_message: str
    deprecated_at: int
    replaced_by_plugin_id: int
    marketplace_id: int
    marketplace: Marketplace
    git_url: str
    git_ref: str
    git_path: str
    full_ref: str
    skills: _containers.RepeatedCompositeFieldContainer[SkillDescriptor]
    subagents: _containers.RepeatedCompositeFieldContainer[SubagentDescriptor]
    hooks: _containers.RepeatedCompositeFieldContainer[HookDescriptor]
    rules: _containers.RepeatedCompositeFieldContainer[RuleDescriptor]
    mcp_servers: _containers.RepeatedCompositeFieldContainer[McpDescriptor]
    commands: _containers.RepeatedCompositeFieldContainer[CommandDescriptor]
    release_repo: str
    release_asset: str
    release_tag: str
    curated_category_keys: _containers.RepeatedScalarFieldContainer[str]
    variables: _struct_pb2.Struct
    team_marketplace_install_mode: TeamMarketplacePluginInstallMode
    team_marketplace_configured_variables: _struct_pb2.Struct
    lifecycle_state: PluginLifecycleState
    min_client_versions: PluginMinClientVersions
    published_by_user: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[PluginStatus, str]] = ..., repository_url: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., logo_url: _Optional[str] = ..., primary_color: _Optional[str] = ..., is_published: bool = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., publisher_id: _Optional[int] = ..., publisher: _Optional[_Union[Publisher, _Mapping]] = ..., is_deprecated: bool = ..., deprecation_message: _Optional[str] = ..., deprecated_at: _Optional[int] = ..., replaced_by_plugin_id: _Optional[int] = ..., marketplace_id: _Optional[int] = ..., marketplace: _Optional[_Union[Marketplace, _Mapping]] = ..., git_url: _Optional[str] = ..., git_ref: _Optional[str] = ..., git_path: _Optional[str] = ..., full_ref: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[SkillDescriptor, _Mapping]]] = ..., subagents: _Optional[_Iterable[_Union[SubagentDescriptor, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[HookDescriptor, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[RuleDescriptor, _Mapping]]] = ..., mcp_servers: _Optional[_Iterable[_Union[McpDescriptor, _Mapping]]] = ..., commands: _Optional[_Iterable[_Union[CommandDescriptor, _Mapping]]] = ..., release_repo: _Optional[str] = ..., release_asset: _Optional[str] = ..., release_tag: _Optional[str] = ..., curated_category_keys: _Optional[_Iterable[str]] = ..., variables: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., team_marketplace_install_mode: _Optional[_Union[TeamMarketplacePluginInstallMode, str]] = ..., team_marketplace_configured_variables: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., lifecycle_state: _Optional[_Union[PluginLifecycleState, str]] = ..., min_client_versions: _Optional[_Union[PluginMinClientVersions, _Mapping]] = ..., published_by_user: bool = ...) -> None: ...

class PluginMinClientVersions(_message.Message):
    __slots__ = ("cursor", "sand")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    SAND_FIELD_NUMBER: _ClassVar[int]
    cursor: str
    sand: str
    def __init__(self, cursor: _Optional[str] = ..., sand: _Optional[str] = ...) -> None: ...

class PollGrokBotUserComputerRequestsRequest(_message.Message):
    __slots__ = ("machine_id", "credential", "ack_ids", "limit")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    ACK_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    credential: str
    ack_ids: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    def __init__(self, machine_id: _Optional[str] = ..., credential: _Optional[str] = ..., ack_ids: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ...) -> None: ...

class PollGrokBotUserComputerRequestsResponse(_message.Message):
    __slots__ = ("requests",)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[GrokBotUserComputerQueuedRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[GrokBotUserComputerQueuedRequest, _Mapping]]] = ...) -> None: ...

class PresignGrokBotMarketplaceCreatorProfileUploadInternalRequest(_message.Message):
    __slots__ = ("content_type", "byte_size")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    content_type: str
    byte_size: int
    def __init__(self, content_type: _Optional[str] = ..., byte_size: _Optional[int] = ...) -> None: ...

class PresignGrokBotMarketplaceImageUploadInternalRequest(_message.Message):
    __slots__ = ("listing_id", "image_kind", "content_type", "byte_size")
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_KIND_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    image_kind: GrokBotMarketplaceImageKind
    content_type: str
    byte_size: int
    def __init__(self, listing_id: _Optional[int] = ..., image_kind: _Optional[_Union[GrokBotMarketplaceImageKind, str]] = ..., content_type: _Optional[str] = ..., byte_size: _Optional[int] = ...) -> None: ...

class PresignGrokBotMarketplaceImageUploadInternalResponse(_message.Message):
    __slots__ = ("put_url", "public_url")
    PUT_URL_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_URL_FIELD_NUMBER: _ClassVar[int]
    put_url: str
    public_url: str
    def __init__(self, put_url: _Optional[str] = ..., public_url: _Optional[str] = ...) -> None: ...

class PresignSandBoxStoreReadsRequest(_message.Message):
    __slots__ = ("rel_paths",)
    REL_PATHS_FIELD_NUMBER: _ClassVar[int]
    rel_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rel_paths: _Optional[_Iterable[str]] = ...) -> None: ...

class PresignSandBoxStoreReadsResponse(_message.Message):
    __slots__ = ("instructions",)
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    instructions: _containers.RepeatedCompositeFieldContainer[SandBoxStoreReadInstruction]
    def __init__(self, instructions: _Optional[_Iterable[_Union[SandBoxStoreReadInstruction, _Mapping]]] = ...) -> None: ...

class PresignSandBoxStoreWritesRequest(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[SandBoxStoreWriteFile]
    def __init__(self, files: _Optional[_Iterable[_Union[SandBoxStoreWriteFile, _Mapping]]] = ...) -> None: ...

class PresignSandBoxStoreWritesResponse(_message.Message):
    __slots__ = ("instructions",)
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    instructions: _containers.RepeatedCompositeFieldContainer[SandBoxStoreWriteInstruction]
    def __init__(self, instructions: _Optional[_Iterable[_Union[SandBoxStoreWriteInstruction, _Mapping]]] = ...) -> None: ...

class PreviewGrokBotMarketplaceSourceInternalRequest(_message.Message):
    __slots__ = ("source_ref",)
    SOURCE_REF_FIELD_NUMBER: _ClassVar[int]
    source_ref: str
    def __init__(self, source_ref: _Optional[str] = ...) -> None: ...

class PreviewGrokBotMarketplaceSourceInternalResponse(_message.Message):
    __slots__ = ("template_id", "share_id", "name", "description", "avatar_shape", "avatar_color", "published", "active_version", "eligible", "ineligibility_reason")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    INELIGIBILITY_REASON_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    share_id: str
    name: str
    description: str
    avatar_shape: str
    avatar_color: str
    published: bool
    active_version: int
    eligible: bool
    ineligibility_reason: str
    def __init__(self, template_id: _Optional[int] = ..., share_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., published: bool = ..., active_version: _Optional[int] = ..., eligible: bool = ..., ineligibility_reason: _Optional[str] = ...) -> None: ...

class PrivateInferenceSettings(_message.Message):
    __slots__ = ("enabled", "can_enable")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAN_ENABLE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    can_enable: bool
    def __init__(self, enabled: bool = ..., can_enable: bool = ...) -> None: ...

class PromptDeeplinkControls(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class PublicGrokBotMarketplaceCreator(_message.Message):
    __slots__ = ("name", "profile_photo_url", "handles")
    class HandlesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    HANDLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    profile_photo_url: str
    handles: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., profile_photo_url: _Optional[str] = ..., handles: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PublicGrokBotMarketplaceListing(_message.Message):
    __slots__ = ("slug", "name", "description", "image_url", "default_avatar", "category", "created_at_ms", "updated_at_ms", "share_id", "creator", "categories")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AVATAR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    slug: str
    name: str
    description: str
    image_url: str
    default_avatar: GrokBotMarketplaceDefaultAvatar
    category: str
    created_at_ms: int
    updated_at_ms: int
    share_id: str
    creator: PublicGrokBotMarketplaceCreator
    categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, slug: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., image_url: _Optional[str] = ..., default_avatar: _Optional[_Union[GrokBotMarketplaceDefaultAvatar, _Mapping]] = ..., category: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., share_id: _Optional[str] = ..., creator: _Optional[_Union[PublicGrokBotMarketplaceCreator, _Mapping]] = ..., categories: _Optional[_Iterable[str]] = ...) -> None: ...

class PublicProfileSettings(_message.Message):
    __slots__ = ("public_visibility_allowed", "policy")
    PUBLIC_VISIBILITY_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    public_visibility_allowed: bool
    policy: str
    def __init__(self, public_visibility_allowed: bool = ..., policy: _Optional[str] = ...) -> None: ...

class Publisher(_message.Message):
    __slots__ = ("id", "name", "display_name", "description", "owner_user_id", "owner_team_id", "is_verified", "verified_at", "verified_domain", "logo_url", "website_url", "support_url", "created_at", "updated_at", "is_user_owned")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_USER_OWNED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    display_name: str
    description: str
    owner_user_id: int
    owner_team_id: int
    is_verified: bool
    verified_at: int
    verified_domain: str
    logo_url: str
    website_url: str
    support_url: str
    created_at: int
    updated_at: int
    is_user_owned: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., owner_user_id: _Optional[int] = ..., owner_team_id: _Optional[int] = ..., is_verified: bool = ..., verified_at: _Optional[int] = ..., verified_domain: _Optional[str] = ..., logo_url: _Optional[str] = ..., website_url: _Optional[str] = ..., support_url: _Optional[str] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., is_user_owned: bool = ...) -> None: ...

class PublishGrokBotUserSkillsSnapshotRequest(_message.Message):
    __slots__ = ("fingerprint",)
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    def __init__(self, fingerprint: _Optional[str] = ...) -> None: ...

class PublishGrokBotUserSkillsSnapshotResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PullRequestPreferences(_message.Message):
    __slots__ = ("pr_review_open_destination",)
    PR_REVIEW_OPEN_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    pr_review_open_destination: PrReviewOpenDestinationMode
    def __init__(self, pr_review_open_destination: _Optional[_Union[PrReviewOpenDestinationMode, str]] = ...) -> None: ...

class PutGrokBotMemoryShardRequest(_message.Message):
    __slots__ = ("agent_id", "folder")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    folder: GrokBotMemoryFolder
    def __init__(self, agent_id: _Optional[str] = ..., folder: _Optional[_Union[GrokBotMemoryFolder, _Mapping]] = ...) -> None: ...

class PutGrokBotMemoryShardResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class PutGrokBotSecretRequest(_message.Message):
    __slots__ = ("id", "name", "description", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    value: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class PutGrokBotSecretResponse(_message.Message):
    __slots__ = ("secret",)
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: GrokBotSecret
    def __init__(self, secret: _Optional[_Union[GrokBotSecret, _Mapping]] = ...) -> None: ...

class RaiseGrokBotVirtualCardRequest(_message.Message):
    __slots__ = ("agent_id", "amount_cents", "currency", "merchant_name", "merchant_url", "context")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_NAME_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_URL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    amount_cents: int
    currency: str
    merchant_name: str
    merchant_url: str
    context: str
    def __init__(self, agent_id: _Optional[str] = ..., amount_cents: _Optional[int] = ..., currency: _Optional[str] = ..., merchant_name: _Optional[str] = ..., merchant_url: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class RaiseGrokBotVirtualCardResponse(_message.Message):
    __slots__ = ("outcome", "request_id", "merchant_name", "superseded_request_id")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    outcome: GrokBotVirtualCardRaiseOutcome
    request_id: str
    merchant_name: str
    superseded_request_id: str
    def __init__(self, outcome: _Optional[_Union[GrokBotVirtualCardRaiseOutcome, str]] = ..., request_id: _Optional[str] = ..., merchant_name: _Optional[str] = ..., superseded_request_id: _Optional[str] = ...) -> None: ...

class ReactToGrokBotMessageRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "emoji", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    emoji: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., emoji: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ReactToGrokBotMessageResponse(_message.Message):
    __slots__ = ("refusal",)
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    refusal: GrokBotHarnessRefusal
    def __init__(self, refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class ReadGrokBotAgentAttachmentChunkRequest(_message.Message):
    __slots__ = ("path", "offset", "length", "session_id")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    length: int
    session_id: str
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class ReadGrokBotAgentAttachmentChunkResponse(_message.Message):
    __slots__ = ("data", "total_size")
    DATA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    total_size: int
    def __init__(self, data: _Optional[bytes] = ..., total_size: _Optional[int] = ...) -> None: ...

class RecreateSandBoxRequest(_message.Message):
    __slots__ = ("preserve_data", "force", "acknowledge_terminal_upgrade_schedule")
    PRESERVE_DATA_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGE_TERMINAL_UPGRADE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    preserve_data: bool
    force: bool
    acknowledge_terminal_upgrade_schedule: bool
    def __init__(self, preserve_data: bool = ..., force: bool = ..., acknowledge_terminal_upgrade_schedule: bool = ...) -> None: ...

class RecreateSandBoxResponse(_message.Message):
    __slots__ = ("started", "reason", "operation_id")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    started: bool
    reason: str
    operation_id: str
    def __init__(self, started: bool = ..., reason: _Optional[str] = ..., operation_id: _Optional[str] = ...) -> None: ...

class RecreateTeamMemberSandBoxRequest(_message.Message):
    __slots__ = ("team_id", "user_id", "force")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    user_id: int
    force: bool
    def __init__(self, team_id: _Optional[int] = ..., user_id: _Optional[int] = ..., force: bool = ...) -> None: ...

class RegisterSandMachineRequest(_message.Message):
    __slots__ = ("label", "local_tool_permission", "messages_enabled")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOOL_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    label: str
    local_tool_permission: str
    messages_enabled: bool
    def __init__(self, label: _Optional[str] = ..., local_tool_permission: _Optional[str] = ..., messages_enabled: bool = ...) -> None: ...

class RegisterSandMachineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReinstallGrokBotSlackAppRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class ReinstallGrokBotSlackAppResponse(_message.Message):
    __slots__ = ("outcome", "slack_team_id", "workspace_name", "slack_error", "retry_after_seconds", "oauth_authorize_url", "approval_request_filed")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    SLACK_ERROR_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    OAUTH_AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUEST_FILED_FIELD_NUMBER: _ClassVar[int]
    outcome: GrokBotSlackReinstallOutcome
    slack_team_id: str
    workspace_name: str
    slack_error: str
    retry_after_seconds: int
    oauth_authorize_url: str
    approval_request_filed: bool
    def __init__(self, outcome: _Optional[_Union[GrokBotSlackReinstallOutcome, str]] = ..., slack_team_id: _Optional[str] = ..., workspace_name: _Optional[str] = ..., slack_error: _Optional[str] = ..., retry_after_seconds: _Optional[int] = ..., oauth_authorize_url: _Optional[str] = ..., approval_request_filed: bool = ...) -> None: ...

class ReloadWindowAction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoteControlV2Policy(_message.Message):
    __slots__ = ("enabled", "automatic_registration_enabled", "available", "automatic_registration_released", "remote_control_denying_org_name", "automatic_registration_denying_org_name")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_REGISTRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_REGISTRATION_RELEASED_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_DENYING_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_REGISTRATION_DENYING_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    automatic_registration_enabled: bool
    available: bool
    automatic_registration_released: bool
    remote_control_denying_org_name: str
    automatic_registration_denying_org_name: str
    def __init__(self, enabled: bool = ..., automatic_registration_enabled: bool = ..., available: bool = ..., automatic_registration_released: bool = ..., remote_control_denying_org_name: _Optional[str] = ..., automatic_registration_denying_org_name: _Optional[str] = ...) -> None: ...

class RemoveGrokBotAgentSkillRequest(_message.Message):
    __slots__ = ("agent_id", "name")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RemoveGrokBotAgentSkillResponse(_message.Message):
    __slots__ = ("marketplace", "plugins")
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ...) -> None: ...

class RenameMcpOAuthAccountRequest(_message.Message):
    __slots__ = ("server_id", "account_key", "new_account_key")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    NEW_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    server_id: int
    account_key: str
    new_account_key: str
    def __init__(self, server_id: _Optional[int] = ..., account_key: _Optional[str] = ..., new_account_key: _Optional[str] = ...) -> None: ...

class RenameMcpOAuthAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportClientNumericMetricsRequest(_message.Message):
    __slots__ = ("metrics",)
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[ClientNumericMetric]
    def __init__(self, metrics: _Optional[_Iterable[_Union[ClientNumericMetric, _Mapping]]] = ...) -> None: ...

class ReportClientNumericMetricsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportGrokBotClientPresenceRequest(_message.Message):
    __slots__ = ("agent_id", "viewing", "surface")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWING_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    viewing: bool
    surface: str
    def __init__(self, agent_id: _Optional[str] = ..., viewing: bool = ..., surface: _Optional[str] = ...) -> None: ...

class ReportGrokBotClientPresenceResponse(_message.Message):
    __slots__ = ("presence_ttl_ms",)
    PRESENCE_TTL_MS_FIELD_NUMBER: _ClassVar[int]
    presence_ttl_ms: int
    def __init__(self, presence_ttl_ms: _Optional[int] = ...) -> None: ...

class ReportSandBoxHostStateRequest(_message.Message):
    __slots__ = ("disk_pressure", "host_version", "host_update_available")
    DISK_PRESSURE_FIELD_NUMBER: _ClassVar[int]
    HOST_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOST_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    disk_pressure: GrokBotBoxDiskPressureLevel
    host_version: str
    host_update_available: bool
    def __init__(self, disk_pressure: _Optional[_Union[GrokBotBoxDiskPressureLevel, str]] = ..., host_version: _Optional[str] = ..., host_update_available: bool = ...) -> None: ...

class ReportSandBoxHostStateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportSandProcessMetricsRequest(_message.Message):
    __slots__ = ("sample_start", "sample_end", "num_subsamples", "sample_seqno", "session_id", "rows", "os", "os_version", "arch", "client_version", "client_id")
    SAMPLE_START_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_END_FIELD_NUMBER: _ClassVar[int]
    NUM_SUBSAMPLES_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SEQNO_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    sample_start: int
    sample_end: int
    num_subsamples: int
    sample_seqno: int
    session_id: str
    rows: _containers.RepeatedCompositeFieldContainer[SandProcessMetricsRowRequest]
    os: str
    os_version: str
    arch: str
    client_version: str
    client_id: str
    def __init__(self, sample_start: _Optional[int] = ..., sample_end: _Optional[int] = ..., num_subsamples: _Optional[int] = ..., sample_seqno: _Optional[int] = ..., session_id: _Optional[str] = ..., rows: _Optional[_Iterable[_Union[SandProcessMetricsRowRequest, _Mapping]]] = ..., os: _Optional[str] = ..., os_version: _Optional[str] = ..., arch: _Optional[str] = ..., client_version: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class ReportSandProcessMetricsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestGrokBotRoomMemberTurnRequest(_message.Message):
    __slots__ = ("nonce", "room", "member_agent_id", "peers", "new_messages", "is_winding_down", "deadline_ms", "parent_request_id", "root_parent_request_id")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PEERS_FIELD_NUMBER: _ClassVar[int]
    NEW_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    IS_WINDING_DOWN_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_MS_FIELD_NUMBER: _ClassVar[int]
    PARENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PARENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    nonce: str
    room: GrokBotRoomMemberTurnRoom
    member_agent_id: str
    peers: _containers.RepeatedCompositeFieldContainer[GrokBotRoomMemberTurnPeer]
    new_messages: _containers.RepeatedCompositeFieldContainer[GrokBotRoomMemberTurnMessage]
    is_winding_down: bool
    deadline_ms: int
    parent_request_id: str
    root_parent_request_id: str
    def __init__(self, nonce: _Optional[str] = ..., room: _Optional[_Union[GrokBotRoomMemberTurnRoom, _Mapping]] = ..., member_agent_id: _Optional[str] = ..., peers: _Optional[_Iterable[_Union[GrokBotRoomMemberTurnPeer, _Mapping]]] = ..., new_messages: _Optional[_Iterable[_Union[GrokBotRoomMemberTurnMessage, _Mapping]]] = ..., is_winding_down: bool = ..., deadline_ms: _Optional[int] = ..., parent_request_id: _Optional[str] = ..., root_parent_request_id: _Optional[str] = ...) -> None: ...

class RequestGrokBotRoomMemberTurnResponse(_message.Message):
    __slots__ = ("dispatch", "member_agent_id", "workflow_id")
    DISPATCH_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    dispatch: GrokBotRoomMemberTurnDispatch
    member_agent_id: str
    workflow_id: str
    def __init__(self, dispatch: _Optional[_Union[GrokBotRoomMemberTurnDispatch, str]] = ..., member_agent_id: _Optional[str] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class RescheduleSandBoxUpgradeRequest(_message.Message):
    __slots__ = ("timezone", "local_time", "recurring")
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_FIELD_NUMBER: _ClassVar[int]
    RECURRING_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    local_time: str
    recurring: bool
    def __init__(self, timezone: _Optional[str] = ..., local_time: _Optional[str] = ..., recurring: bool = ...) -> None: ...

class RescheduleSandBoxUpgradeResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: SandBoxUpgradeSchedule
    def __init__(self, schedule: _Optional[_Union[SandBoxUpgradeSchedule, _Mapping]] = ...) -> None: ...

class ResolveGrokBotAutoReviewApprovalRequest(_message.Message):
    __slots__ = ("agent_id", "request_id", "resolution", "approval_platform", "approved_command", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    APPROVED_COMMAND_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    request_id: str
    resolution: GrokBotAutoReviewApprovalResolution
    approval_platform: str
    approved_command: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., request_id: _Optional[str] = ..., resolution: _Optional[_Union[GrokBotAutoReviewApprovalResolution, str]] = ..., approval_platform: _Optional[str] = ..., approved_command: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ResolveGrokBotAutoReviewApprovalResponse(_message.Message):
    __slots__ = ("dispatched", "workflow_id")
    DISPATCHED_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    dispatched: bool
    workflow_id: str
    def __init__(self, dispatched: bool = ..., workflow_id: _Optional[str] = ...) -> None: ...

class ResolveGrokBotCredentialRequestRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "resolution", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    resolution: GrokBotCredentialRequestResolution
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., resolution: _Optional[_Union[GrokBotCredentialRequestResolution, str]] = ..., session_id: _Optional[str] = ...) -> None: ...

class ResolveGrokBotCredentialRequestResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class ResolveGrokBotLocalToolPermissionRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "request_id", "resolution", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    request_id: str
    resolution: GrokBotLocalToolPermissionCardResolution
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., request_id: _Optional[str] = ..., resolution: _Optional[_Union[GrokBotLocalToolPermissionCardResolution, str]] = ..., session_id: _Optional[str] = ...) -> None: ...

class ResolveGrokBotLocalToolPermissionResponse(_message.Message):
    __slots__ = ("dispatched", "workflow_id", "refusal")
    DISPATCHED_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    dispatched: bool
    workflow_id: str
    refusal: GrokBotHarnessRefusal
    def __init__(self, dispatched: bool = ..., workflow_id: _Optional[str] = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class ResolveGrokBotVirtualCardApprovalRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "request_id", "resolution", "payment_method_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    request_id: str
    resolution: GrokBotVirtualCardResolution
    payment_method_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., request_id: _Optional[str] = ..., resolution: _Optional[_Union[GrokBotVirtualCardResolution, str]] = ..., payment_method_id: _Optional[str] = ...) -> None: ...

class ResolveGrokBotVirtualCardApprovalResponse(_message.Message):
    __slots__ = ("outcome", "spend_request_id", "approval_url", "message", "refusal")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    SPEND_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_URL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    outcome: GrokBotVirtualCardOutcome
    spend_request_id: str
    approval_url: str
    message: str
    refusal: GrokBotHarnessRefusal
    def __init__(self, outcome: _Optional[_Union[GrokBotVirtualCardOutcome, str]] = ..., spend_request_id: _Optional[str] = ..., approval_url: _Optional[str] = ..., message: _Optional[str] = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class RespondGrokBotWidgetRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "value", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    value: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., value: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RespondGrokBotWidgetResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class RuleDescriptor(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class RunGenerateImageError(_message.Message):
    __slots__ = ("error", "model_restricted")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MODEL_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
    error: str
    model_restricted: bool
    def __init__(self, error: _Optional[str] = ..., model_restricted: bool = ...) -> None: ...

class RunGenerateImageRequest(_message.Message):
    __slots__ = ("description", "reference_images", "model_id", "max_mode", "aspect_ratio")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_MODE_FIELD_NUMBER: _ClassVar[int]
    ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    description: str
    reference_images: _containers.RepeatedCompositeFieldContainer[GenerateImageReferenceImage]
    model_id: str
    max_mode: bool
    aspect_ratio: str
    def __init__(self, description: _Optional[str] = ..., reference_images: _Optional[_Iterable[_Union[GenerateImageReferenceImage, _Mapping]]] = ..., model_id: _Optional[str] = ..., max_mode: bool = ..., aspect_ratio: _Optional[str] = ...) -> None: ...

class RunGenerateImageResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: RunGenerateImageSuccess
    error: RunGenerateImageError
    def __init__(self, success: _Optional[_Union[RunGenerateImageSuccess, _Mapping]] = ..., error: _Optional[_Union[RunGenerateImageError, _Mapping]] = ...) -> None: ...

class RunGenerateImageSuccess(_message.Message):
    __slots__ = ("image_data", "mime_type")
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    image_data: str
    mime_type: str
    def __init__(self, image_data: _Optional[str] = ..., mime_type: _Optional[str] = ...) -> None: ...

class SandActionAuditSettings(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class SandAssignedSetupManifest(_message.Message):
    __slots__ = ("scope_kind", "scope_id", "manifest_id", "revision", "entries")
    SCOPE_KIND_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    scope_kind: SandSetupManifestScopeKind
    scope_id: str
    manifest_id: str
    revision: str
    entries: _containers.RepeatedCompositeFieldContainer[SandSetupManifestEntry]
    def __init__(self, scope_kind: _Optional[_Union[SandSetupManifestScopeKind, str]] = ..., scope_id: _Optional[str] = ..., manifest_id: _Optional[str] = ..., revision: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[SandSetupManifestEntry, _Mapping]]] = ...) -> None: ...

class SandAutoReviewControls(_message.Message):
    __slots__ = ("enforce_enabled", "allow_instructions", "block_instructions", "update_instructions")
    ENFORCE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    enforce_enabled: bool
    allow_instructions: _containers.RepeatedScalarFieldContainer[str]
    block_instructions: _containers.RepeatedScalarFieldContainer[str]
    update_instructions: bool
    def __init__(self, enforce_enabled: bool = ..., allow_instructions: _Optional[_Iterable[str]] = ..., block_instructions: _Optional[_Iterable[str]] = ..., update_instructions: bool = ...) -> None: ...

class SandBoxDescriptor(_message.Message):
    __slots__ = ("running",)
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    running: bool
    def __init__(self, running: bool = ...) -> None: ...

class SandBoxMigrationEvent(_message.Message):
    __slots__ = ("phase", "detail", "at_ms", "offset_key", "operation_id")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    AT_MS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    phase: SandBoxMigrationPhase
    detail: str
    at_ms: int
    offset_key: str
    operation_id: str
    def __init__(self, phase: _Optional[_Union[SandBoxMigrationPhase, str]] = ..., detail: _Optional[str] = ..., at_ms: _Optional[int] = ..., offset_key: _Optional[str] = ..., operation_id: _Optional[str] = ...) -> None: ...

class SandBoxStoreManifestVersion(_message.Message):
    __slots__ = ("version_id", "last_modified_ms", "size_bytes", "is_latest", "etag", "entry_count", "total_bytes", "fully_hydrated", "parse_error")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_MS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_LATEST_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    FULLY_HYDRATED_FIELD_NUMBER: _ClassVar[int]
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    last_modified_ms: int
    size_bytes: int
    is_latest: bool
    etag: str
    entry_count: int
    total_bytes: int
    fully_hydrated: bool
    parse_error: str
    def __init__(self, version_id: _Optional[str] = ..., last_modified_ms: _Optional[int] = ..., size_bytes: _Optional[int] = ..., is_latest: bool = ..., etag: _Optional[str] = ..., entry_count: _Optional[int] = ..., total_bytes: _Optional[int] = ..., fully_hydrated: bool = ..., parse_error: _Optional[str] = ...) -> None: ...

class SandBoxStoreMultipartAbortResult(_message.Message):
    __slots__ = ("input_index", "rel_path", "success", "failure")
    INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    input_index: int
    rel_path: str
    success: SandBoxStoreMultipartAbortSuccess
    failure: SandBoxStoreMultipartOperationFailure
    def __init__(self, input_index: _Optional[int] = ..., rel_path: _Optional[str] = ..., success: _Optional[_Union[SandBoxStoreMultipartAbortSuccess, _Mapping]] = ..., failure: _Optional[_Union[SandBoxStoreMultipartOperationFailure, _Mapping]] = ...) -> None: ...

class SandBoxStoreMultipartAbortSuccess(_message.Message):
    __slots__ = ("already_finished",)
    ALREADY_FINISHED_FIELD_NUMBER: _ClassVar[int]
    already_finished: bool
    def __init__(self, already_finished: bool = ...) -> None: ...

class SandBoxStoreMultipartOperationFailure(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: SandBoxStoreMultipartOperationFailureCode
    def __init__(self, code: _Optional[_Union[SandBoxStoreMultipartOperationFailureCode, str]] = ...) -> None: ...

class SandBoxStoreMultipartPart(_message.Message):
    __slots__ = ("part_number", "size_bytes", "sha256")
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    part_number: int
    size_bytes: int
    sha256: str
    def __init__(self, part_number: _Optional[int] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ...) -> None: ...

class SandBoxStoreMultipartUploadContext(_message.Message):
    __slots__ = ("upload_id", "rel_path", "size_bytes", "sha256", "expected_part_count", "part_sha256s", "if_match_etag", "expect_absent", "session_id")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PART_COUNT_FIELD_NUMBER: _ClassVar[int]
    PART_SHA256S_FIELD_NUMBER: _ClassVar[int]
    IF_MATCH_ETAG_FIELD_NUMBER: _ClassVar[int]
    EXPECT_ABSENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    rel_path: str
    size_bytes: int
    sha256: str
    expected_part_count: int
    part_sha256s: _containers.RepeatedScalarFieldContainer[str]
    if_match_etag: str
    expect_absent: bool
    session_id: str
    def __init__(self, upload_id: _Optional[str] = ..., rel_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., sha256: _Optional[str] = ..., expected_part_count: _Optional[int] = ..., part_sha256s: _Optional[_Iterable[str]] = ..., if_match_etag: _Optional[str] = ..., expect_absent: bool = ..., session_id: _Optional[str] = ...) -> None: ...

class SandBoxStoreMultipartUploadedPart(_message.Message):
    __slots__ = ("part_number", "etag")
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    part_number: int
    etag: str
    def __init__(self, part_number: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...

class SandBoxStoreMultipartUploadPartInstruction(_message.Message):
    __slots__ = ("part_number", "url", "headers", "offset_bytes", "size_bytes")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    part_number: int
    url: str
    headers: _containers.ScalarMap[str, str]
    offset_bytes: int
    size_bytes: int
    def __init__(self, part_number: _Optional[int] = ..., url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., offset_bytes: _Optional[int] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class SandBoxStoreMultipartWriteAbort(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: SandBoxStoreMultipartUploadContext
    def __init__(self, context: _Optional[_Union[SandBoxStoreMultipartUploadContext, _Mapping]] = ...) -> None: ...

class SandBoxStoreMultipartWriteCompletion(_message.Message):
    __slots__ = ("context", "parts")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    context: SandBoxStoreMultipartUploadContext
    parts: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartUploadedPart]
    def __init__(self, context: _Optional[_Union[SandBoxStoreMultipartUploadContext, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[SandBoxStoreMultipartUploadedPart, _Mapping]]] = ...) -> None: ...

class SandBoxStoreMultipartWriteInstruction(_message.Message):
    __slots__ = ("context", "parts", "part_urls_expires_at_ms")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    PART_URLS_EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    context: SandBoxStoreMultipartUploadContext
    parts: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartUploadPartInstruction]
    part_urls_expires_at_ms: int
    def __init__(self, context: _Optional[_Union[SandBoxStoreMultipartUploadContext, _Mapping]] = ..., parts: _Optional[_Iterable[_Union[SandBoxStoreMultipartUploadPartInstruction, _Mapping]]] = ..., part_urls_expires_at_ms: _Optional[int] = ...) -> None: ...

class SandBoxStoreMultipartWriteResult(_message.Message):
    __slots__ = ("input_index", "rel_path", "success", "failure")
    INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    input_index: int
    rel_path: str
    success: SandBoxStoreMultipartWriteSuccess
    failure: SandBoxStoreMultipartOperationFailure
    def __init__(self, input_index: _Optional[int] = ..., rel_path: _Optional[str] = ..., success: _Optional[_Union[SandBoxStoreMultipartWriteSuccess, _Mapping]] = ..., failure: _Optional[_Union[SandBoxStoreMultipartOperationFailure, _Mapping]] = ...) -> None: ...

class SandBoxStoreMultipartWriteSuccess(_message.Message):
    __slots__ = ("etag",)
    ETAG_FIELD_NUMBER: _ClassVar[int]
    etag: str
    def __init__(self, etag: _Optional[str] = ...) -> None: ...

class SandBoxStoreObjectEntry(_message.Message):
    __slots__ = ("rel_path", "etag", "size_bytes", "last_modified_ms")
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_MS_FIELD_NUMBER: _ClassVar[int]
    rel_path: str
    etag: str
    size_bytes: int
    last_modified_ms: int
    def __init__(self, rel_path: _Optional[str] = ..., etag: _Optional[str] = ..., size_bytes: _Optional[int] = ..., last_modified_ms: _Optional[int] = ...) -> None: ...

class SandBoxStoreReadInstruction(_message.Message):
    __slots__ = ("rel_path", "url", "expires_at_ms")
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    rel_path: str
    url: str
    expires_at_ms: int
    def __init__(self, rel_path: _Optional[str] = ..., url: _Optional[str] = ..., expires_at_ms: _Optional[int] = ...) -> None: ...

class SandBoxStoreWriteFile(_message.Message):
    __slots__ = ("rel_path", "sha256", "size_bytes", "content_addressed", "if_match_etag", "expect_absent", "multipart_parts")
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ADDRESSED_FIELD_NUMBER: _ClassVar[int]
    IF_MATCH_ETAG_FIELD_NUMBER: _ClassVar[int]
    EXPECT_ABSENT_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_PARTS_FIELD_NUMBER: _ClassVar[int]
    rel_path: str
    sha256: str
    size_bytes: int
    content_addressed: bool
    if_match_etag: str
    expect_absent: bool
    multipart_parts: _containers.RepeatedCompositeFieldContainer[SandBoxStoreMultipartPart]
    def __init__(self, rel_path: _Optional[str] = ..., sha256: _Optional[str] = ..., size_bytes: _Optional[int] = ..., content_addressed: bool = ..., if_match_etag: _Optional[str] = ..., expect_absent: bool = ..., multipart_parts: _Optional[_Iterable[_Union[SandBoxStoreMultipartPart, _Mapping]]] = ...) -> None: ...

class SandBoxStoreWriteInstruction(_message.Message):
    __slots__ = ("rel_path", "url", "headers", "expires_at_ms", "multipart")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    rel_path: str
    url: str
    headers: _containers.ScalarMap[str, str]
    expires_at_ms: int
    multipart: SandBoxStoreMultipartWriteInstruction
    def __init__(self, rel_path: _Optional[str] = ..., url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., expires_at_ms: _Optional[int] = ..., multipart: _Optional[_Union[SandBoxStoreMultipartWriteInstruction, _Mapping]] = ...) -> None: ...

class SandBoxUpgradeSchedule(_message.Message):
    __slots__ = ("timezone", "local_time", "recurring", "target_image_tag", "next_fire_at_ms", "state", "last_completed_image_tag", "failure_reason")
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_FIELD_NUMBER: _ClassVar[int]
    RECURRING_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIRE_AT_MS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLETED_IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    local_time: str
    recurring: bool
    target_image_tag: str
    next_fire_at_ms: int
    state: SandBoxUpgradeScheduleState
    last_completed_image_tag: str
    failure_reason: str
    def __init__(self, timezone: _Optional[str] = ..., local_time: _Optional[str] = ..., recurring: bool = ..., target_image_tag: _Optional[str] = ..., next_fire_at_ms: _Optional[int] = ..., state: _Optional[_Union[SandBoxUpgradeScheduleState, str]] = ..., last_completed_image_tag: _Optional[str] = ..., failure_reason: _Optional[str] = ...) -> None: ...

class SandLocalEgressControls(_message.Message):
    __slots__ = ("allowed",)
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    def __init__(self, allowed: bool = ...) -> None: ...

class SandMachine(_message.Message):
    __slots__ = ("machine_id", "label", "local_tool_permission", "messages_enabled")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOOL_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    label: str
    local_tool_permission: str
    messages_enabled: bool
    def __init__(self, machine_id: _Optional[str] = ..., label: _Optional[str] = ..., local_tool_permission: _Optional[str] = ..., messages_enabled: bool = ...) -> None: ...

class SandNetworkControls(_message.Message):
    __slots__ = ("egress_mode", "allowlist", "locked")
    EGRESS_MODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    egress_mode: SandEgressMode
    allowlist: _containers.RepeatedScalarFieldContainer[str]
    locked: bool
    def __init__(self, egress_mode: _Optional[_Union[SandEgressMode, str]] = ..., allowlist: _Optional[_Iterable[str]] = ..., locked: bool = ...) -> None: ...

class SandOnboardingState(_message.Message):
    __slots__ = ("completed", "seen", "checked_setup_checklist_items", "skipped_setup_checklist_items", "has_ever_completed")
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    SEEN_FIELD_NUMBER: _ClassVar[int]
    CHECKED_SETUP_CHECKLIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_SETUP_CHECKLIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    HAS_EVER_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    seen: bool
    checked_setup_checklist_items: _containers.RepeatedScalarFieldContainer[str]
    skipped_setup_checklist_items: _containers.RepeatedScalarFieldContainer[str]
    has_ever_completed: bool
    def __init__(self, completed: bool = ..., seen: bool = ..., checked_setup_checklist_items: _Optional[_Iterable[str]] = ..., skipped_setup_checklist_items: _Optional[_Iterable[str]] = ..., has_ever_completed: bool = ...) -> None: ...

class SandOnDemandSettings(_message.Message):
    __slots__ = ("visible", "eligible", "enabled", "dashboard_url")
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_URL_FIELD_NUMBER: _ClassVar[int]
    visible: bool
    eligible: bool
    enabled: bool
    dashboard_url: str
    def __init__(self, visible: bool = ..., eligible: bool = ..., enabled: bool = ..., dashboard_url: _Optional[str] = ...) -> None: ...

class SandProcessMetricsRowRequest(_message.Message):
    __slots__ = ("pid", "ppid", "process_name", "process_name_hash", "sample_cpu_time_ms", "sample_avg_mem_mb", "sample_peak_mem_mb", "session_peak_mem_mb", "memory_during_sample_peak_mb", "cpu_during_sample_peak_pct")
    PID_FIELD_NUMBER: _ClassVar[int]
    PPID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_CPU_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_AVG_MEM_MB_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_PEAK_MEM_MB_FIELD_NUMBER: _ClassVar[int]
    SESSION_PEAK_MEM_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_DURING_SAMPLE_PEAK_MB_FIELD_NUMBER: _ClassVar[int]
    CPU_DURING_SAMPLE_PEAK_PCT_FIELD_NUMBER: _ClassVar[int]
    pid: int
    ppid: int
    process_name: str
    process_name_hash: str
    sample_cpu_time_ms: int
    sample_avg_mem_mb: float
    sample_peak_mem_mb: float
    session_peak_mem_mb: float
    memory_during_sample_peak_mb: float
    cpu_during_sample_peak_pct: float
    def __init__(self, pid: _Optional[int] = ..., ppid: _Optional[int] = ..., process_name: _Optional[str] = ..., process_name_hash: _Optional[str] = ..., sample_cpu_time_ms: _Optional[int] = ..., sample_avg_mem_mb: _Optional[float] = ..., sample_peak_mem_mb: _Optional[float] = ..., session_peak_mem_mb: _Optional[float] = ..., memory_during_sample_peak_mb: _Optional[float] = ..., cpu_during_sample_peak_pct: _Optional[float] = ...) -> None: ...

class SandSetupManifestEntry(_message.Message):
    __slots__ = ("id", "setup", "check")
    ID_FIELD_NUMBER: _ClassVar[int]
    SETUP_FIELD_NUMBER: _ClassVar[int]
    CHECK_FIELD_NUMBER: _ClassVar[int]
    id: str
    setup: str
    check: str
    def __init__(self, id: _Optional[str] = ..., setup: _Optional[str] = ..., check: _Optional[str] = ...) -> None: ...

class SandTeamSetupManifest(_message.Message):
    __slots__ = ("manifest_id", "revision", "etag", "entries")
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    manifest_id: str
    revision: str
    etag: str
    entries: _containers.RepeatedCompositeFieldContainer[SandSetupManifestEntry]
    def __init__(self, manifest_id: _Optional[str] = ..., revision: _Optional[str] = ..., etag: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[SandSetupManifestEntry, _Mapping]]] = ...) -> None: ...

class SandUpgradeRecommendation(_message.Message):
    __slots__ = ("cta", "disabled", "supporting_text", "kind")
    CTA_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    SUPPORTING_TEXT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    cta: ErrorButton
    disabled: bool
    supporting_text: str
    kind: str
    def __init__(self, cta: _Optional[_Union[ErrorButton, _Mapping]] = ..., disabled: bool = ..., supporting_text: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class SaveTeamSandSetupManifestRequest(_message.Message):
    __slots__ = ("manifest_id", "expected_etag", "entries")
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ETAG_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    manifest_id: str
    expected_etag: str
    entries: _containers.RepeatedCompositeFieldContainer[SandSetupManifestEntry]
    def __init__(self, manifest_id: _Optional[str] = ..., expected_etag: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[SandSetupManifestEntry, _Mapping]]] = ...) -> None: ...

class SaveTeamSandSetupManifestResponse(_message.Message):
    __slots__ = ("manifest",)
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    manifest: SandTeamSetupManifest
    def __init__(self, manifest: _Optional[_Union[SandTeamSetupManifest, _Mapping]] = ...) -> None: ...

class ScheduleSandBoxUpgradeRequest(_message.Message):
    __slots__ = ("timezone", "local_time", "recurring")
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_FIELD_NUMBER: _ClassVar[int]
    RECURRING_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    local_time: str
    recurring: bool
    def __init__(self, timezone: _Optional[str] = ..., local_time: _Optional[str] = ..., recurring: bool = ...) -> None: ...

class ScheduleSandBoxUpgradeResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: SandBoxUpgradeSchedule
    def __init__(self, schedule: _Optional[_Union[SandBoxUpgradeSchedule, _Mapping]] = ...) -> None: ...

class SendGrokBotAgentMessageRequest(_message.Message):
    __slots__ = ("from_agent_id", "to_agent_id", "message_id", "text", "sent_at_ms")
    FROM_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TO_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_MS_FIELD_NUMBER: _ClassVar[int]
    from_agent_id: str
    to_agent_id: str
    message_id: str
    text: str
    sent_at_ms: int
    def __init__(self, from_agent_id: _Optional[str] = ..., to_agent_id: _Optional[str] = ..., message_id: _Optional[str] = ..., text: _Optional[str] = ..., sent_at_ms: _Optional[int] = ...) -> None: ...

class SendGrokBotAgentMessageResponse(_message.Message):
    __slots__ = ("delivery", "target_agent_id", "target_name", "workflow_id")
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    delivery: GrokBotAgentMessageDelivery
    target_agent_id: str
    target_name: str
    workflow_id: str
    def __init__(self, delivery: _Optional[_Union[GrokBotAgentMessageDelivery, str]] = ..., target_agent_id: _Optional[str] = ..., target_name: _Optional[str] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class SendGrokBotDraftRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "session_id", "email", "slack")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SLACK_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    session_id: str
    email: GrokBotEmailDraft
    slack: GrokBotSlackDraft
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., session_id: _Optional[str] = ..., email: _Optional[_Union[GrokBotEmailDraft, _Mapping]] = ..., slack: _Optional[_Union[GrokBotSlackDraft, _Mapping]] = ...) -> None: ...

class SendGrokBotDraftResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class SendGrokBotUserMessageRequest(_message.Message):
    __slots__ = ("agent_id", "message_id", "text", "sent_at_ms", "rich_text", "reply_to_id", "is_fork", "attachment_paths", "attachment_names", "traceparent", "enter_epoch_ms", "composed_at_ms", "source", "mcp_config_json", "session_id", "machine_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_MS_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORK_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_PATHS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    TRACEPARENT_FIELD_NUMBER: _ClassVar[int]
    ENTER_EPOCH_MS_FIELD_NUMBER: _ClassVar[int]
    COMPOSED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    message_id: str
    text: str
    sent_at_ms: int
    rich_text: str
    reply_to_id: str
    is_fork: bool
    attachment_paths: _containers.RepeatedScalarFieldContainer[str]
    attachment_names: _containers.RepeatedScalarFieldContainer[str]
    traceparent: str
    enter_epoch_ms: int
    composed_at_ms: int
    source: GrokBotClientSurface
    mcp_config_json: str
    session_id: str
    machine_id: str
    def __init__(self, agent_id: _Optional[str] = ..., message_id: _Optional[str] = ..., text: _Optional[str] = ..., sent_at_ms: _Optional[int] = ..., rich_text: _Optional[str] = ..., reply_to_id: _Optional[str] = ..., is_fork: bool = ..., attachment_paths: _Optional[_Iterable[str]] = ..., attachment_names: _Optional[_Iterable[str]] = ..., traceparent: _Optional[str] = ..., enter_epoch_ms: _Optional[int] = ..., composed_at_ms: _Optional[int] = ..., source: _Optional[_Union[GrokBotClientSurface, str]] = ..., mcp_config_json: _Optional[str] = ..., session_id: _Optional[str] = ..., machine_id: _Optional[str] = ...) -> None: ...

class SendGrokBotUserMessageResponse(_message.Message):
    __slots__ = ("dispatched", "mode", "workflow_id", "delivery", "refusal")
    DISPATCHED_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    dispatched: bool
    mode: GrokBotTemporalHarnessMode
    workflow_id: str
    delivery: GrokBotUserMessageDelivery
    refusal: GrokBotHarnessRefusal
    def __init__(self, dispatched: bool = ..., mode: _Optional[_Union[GrokBotTemporalHarnessMode, str]] = ..., workflow_id: _Optional[str] = ..., delivery: _Optional[_Union[GrokBotUserMessageDelivery, str]] = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class SetGrokBotAgentAutomationEnabledRequest(_message.Message):
    __slots__ = ("agent_id", "automation_id", "is_enabled", "time_zone")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    automation_id: str
    is_enabled: bool
    time_zone: str
    def __init__(self, agent_id: _Optional[str] = ..., automation_id: _Optional[str] = ..., is_enabled: bool = ..., time_zone: _Optional[str] = ...) -> None: ...

class SetGrokBotAgentAutomationEnabledResponse(_message.Message):
    __slots__ = ("automations",)
    AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    automations: _containers.RepeatedCompositeFieldContainer[GrokBotAgentAutomation]
    def __init__(self, automations: _Optional[_Iterable[_Union[GrokBotAgentAutomation, _Mapping]]] = ...) -> None: ...

class SetGrokBotAgentClientStateRequest(_message.Message):
    __slots__ = ("agent_id", "mark_read", "mark_unread", "notifications_enabled", "notify_on_updates_enabled", "hidden_from_sidebar")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MARK_READ_FIELD_NUMBER: _ClassVar[int]
    MARK_UNREAD_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ON_UPDATES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FROM_SIDEBAR_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    mark_read: bool
    mark_unread: bool
    notifications_enabled: bool
    notify_on_updates_enabled: bool
    hidden_from_sidebar: bool
    def __init__(self, agent_id: _Optional[str] = ..., mark_read: bool = ..., mark_unread: bool = ..., notifications_enabled: bool = ..., notify_on_updates_enabled: bool = ..., hidden_from_sidebar: bool = ...) -> None: ...

class SetGrokBotAgentClientStateResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: GrokBotAgentClientState
    def __init__(self, state: _Optional[_Union[GrokBotAgentClientState, _Mapping]] = ...) -> None: ...

class SetGrokBotAgentPluginsRequest(_message.Message):
    __slots__ = ("agent_id", "plugins")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPluginEntry]
    def __init__(self, agent_id: _Optional[str] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPluginEntry, _Mapping]]] = ...) -> None: ...

class SetGrokBotAgentPluginsResponse(_message.Message):
    __slots__ = ("marketplace", "plugins")
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ...) -> None: ...

class SetGrokBotAgentPluginVariablesRequest(_message.Message):
    __slots__ = ("agent_id", "plugin_id", "variables")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    plugin_id: int
    variables: _struct_pb2.Struct
    def __init__(self, agent_id: _Optional[str] = ..., plugin_id: _Optional[int] = ..., variables: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SetGrokBotAgentPluginVariablesResponse(_message.Message):
    __slots__ = ("marketplace", "plugins")
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ...) -> None: ...

class SetGrokBotAgentVisibilityRequest(_message.Message):
    __slots__ = ("agent_id", "visibility")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    visibility: GrokBotAgentVisibility
    def __init__(self, agent_id: _Optional[str] = ..., visibility: _Optional[_Union[GrokBotAgentVisibility, str]] = ...) -> None: ...

class SetGrokBotAgentVisibilityResponse(_message.Message):
    __slots__ = ("agent", "outcome")
    AGENT_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    agent: GrokBotAgent
    outcome: SetGrokBotAgentVisibilityOutcome
    def __init__(self, agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ..., outcome: _Optional[_Union[SetGrokBotAgentVisibilityOutcome, str]] = ...) -> None: ...

class SetGrokBotMarketplaceListingStatusInternalRequest(_message.Message):
    __slots__ = ("listing_id", "status")
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    status: GrokBotMarketplaceListingStatus
    def __init__(self, listing_id: _Optional[int] = ..., status: _Optional[_Union[GrokBotMarketplaceListingStatus, str]] = ...) -> None: ...

class SetGrokBotRoomMembersRequest(_message.Message):
    __slots__ = ("agent_id", "member_agent_ids")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    member_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_id: _Optional[str] = ..., member_agent_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SetGrokBotRoomMembersResponse(_message.Message):
    __slots__ = ("agent",)
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: GrokBotAgent
    def __init__(self, agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ...) -> None: ...

class SetGrokBotTemplateVisibilityRequest(_message.Message):
    __slots__ = ("share_id", "visibility")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    visibility: GrokBotTemplateVisibility
    def __init__(self, share_id: _Optional[str] = ..., visibility: _Optional[_Union[GrokBotTemplateVisibility, str]] = ...) -> None: ...

class SetGrokBotTemplateVisibilityResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: GrokBotTemplate
    def __init__(self, template: _Optional[_Union[GrokBotTemplate, _Mapping]] = ...) -> None: ...

class SetGrokBotUserMcpSettingsRequest(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: GrokBotUserMcpSettings
    def __init__(self, settings: _Optional[_Union[GrokBotUserMcpSettings, _Mapping]] = ...) -> None: ...

class SetGrokBotUserMcpSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: GrokBotUserMcpSettings
    def __init__(self, settings: _Optional[_Union[GrokBotUserMcpSettings, _Mapping]] = ...) -> None: ...

class SetHardLimitRequest(_message.Message):
    __slots__ = ("team_id", "hard_limit", "no_usage_based_allowed", "hard_limit_per_user", "preserve_hard_limit_per_user", "per_user_monthly_limit_dollars", "clear_per_user_monthly_limit_dollars", "is_dynamic_team_limit", "clear_conflicting_policy", "auto_alerts_enabled", "per_user_first_party_models_additional_budget_dollars", "clear_per_user_first_party_models_additional_budget_dollars", "per_user_first_party_models_additional_budget_unlimited", "clear_per_user_first_party_models_additional_budget_unlimited")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NO_USAGE_BASED_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    HARD_LIMIT_PER_USER_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_HARD_LIMIT_PER_USER_FIELD_NUMBER: _ClassVar[int]
    PER_USER_MONTHLY_LIMIT_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PER_USER_MONTHLY_LIMIT_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_TEAM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CONFLICTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    AUTO_ALERTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PER_USER_FIRST_PARTY_MODELS_ADDITIONAL_BUDGET_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PER_USER_FIRST_PARTY_MODELS_ADDITIONAL_BUDGET_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    PER_USER_FIRST_PARTY_MODELS_ADDITIONAL_BUDGET_UNLIMITED_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PER_USER_FIRST_PARTY_MODELS_ADDITIONAL_BUDGET_UNLIMITED_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    hard_limit: int
    no_usage_based_allowed: bool
    hard_limit_per_user: int
    preserve_hard_limit_per_user: bool
    per_user_monthly_limit_dollars: int
    clear_per_user_monthly_limit_dollars: bool
    is_dynamic_team_limit: bool
    clear_conflicting_policy: bool
    auto_alerts_enabled: bool
    per_user_first_party_models_additional_budget_dollars: int
    clear_per_user_first_party_models_additional_budget_dollars: bool
    per_user_first_party_models_additional_budget_unlimited: bool
    clear_per_user_first_party_models_additional_budget_unlimited: bool
    def __init__(self, team_id: _Optional[int] = ..., hard_limit: _Optional[int] = ..., no_usage_based_allowed: bool = ..., hard_limit_per_user: _Optional[int] = ..., preserve_hard_limit_per_user: bool = ..., per_user_monthly_limit_dollars: _Optional[int] = ..., clear_per_user_monthly_limit_dollars: bool = ..., is_dynamic_team_limit: bool = ..., clear_conflicting_policy: bool = ..., auto_alerts_enabled: bool = ..., per_user_first_party_models_additional_budget_dollars: _Optional[int] = ..., clear_per_user_first_party_models_additional_budget_dollars: bool = ..., per_user_first_party_models_additional_budget_unlimited: bool = ..., clear_per_user_first_party_models_additional_budget_unlimited: bool = ...) -> None: ...

class SetHardLimitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetMcpConfigRequest(_message.Message):
    __slots__ = ("team_scope", "team_id", "config_json", "server_renames", "server_ids_by_name")
    class ServerRenamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ServerIdsByNameEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TEAM_SCOPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    SERVER_RENAMES_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDS_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    team_scope: bool
    team_id: int
    config_json: str
    server_renames: _containers.ScalarMap[str, str]
    server_ids_by_name: _containers.ScalarMap[str, int]
    def __init__(self, team_scope: bool = ..., team_id: _Optional[int] = ..., config_json: _Optional[str] = ..., server_renames: _Optional[_Mapping[str, str]] = ..., server_ids_by_name: _Optional[_Mapping[str, int]] = ...) -> None: ...

class SetMcpConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetOnePasswordAlwaysAllowRequest(_message.Message):
    __slots__ = ("connection_id", "always_allow")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ALLOW_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    always_allow: bool
    def __init__(self, connection_id: _Optional[str] = ..., always_allow: bool = ...) -> None: ...

class SharedCanvasSettings(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class SharedConversationSettings(_message.Message):
    __slots__ = ("enabled", "allowed_visibilities", "allow_public_indexing")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VISIBILITIES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PUBLIC_INDEXING_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    allowed_visibilities: _containers.RepeatedScalarFieldContainer[SharedConversationVisibility]
    allow_public_indexing: bool
    def __init__(self, enabled: bool = ..., allowed_visibilities: _Optional[_Iterable[_Union[SharedConversationVisibility, str]]] = ..., allow_public_indexing: bool = ...) -> None: ...

class SkillDescriptor(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url", "environments", "disabled_environments", "custom_mode", "display_name", "icon", "color", "content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    disabled_environments: _containers.RepeatedScalarFieldContainer[str]
    custom_mode: _types_pb2.CustomModeDescriptor
    display_name: str
    icon: str
    color: str
    content: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ..., environments: _Optional[_Iterable[str]] = ..., disabled_environments: _Optional[_Iterable[str]] = ..., custom_mode: _Optional[_Union[_types_pb2.CustomModeDescriptor, _Mapping]] = ..., display_name: _Optional[str] = ..., icon: _Optional[str] = ..., color: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class SlackIntegrationSettings(_message.Message):
    __slots__ = ("hidden",)
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    def __init__(self, hidden: bool = ...) -> None: ...

class StartBulkTeamMemberSandBoxOperationRequest(_message.Message):
    __slots__ = ("team_id", "user_ids", "action", "force", "operation_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    user_ids: _containers.RepeatedScalarFieldContainer[int]
    action: BulkTeamMemberSandBoxAction
    force: bool
    operation_id: str
    def __init__(self, team_id: _Optional[int] = ..., user_ids: _Optional[_Iterable[int]] = ..., action: _Optional[_Union[BulkTeamMemberSandBoxAction, str]] = ..., force: bool = ..., operation_id: _Optional[str] = ...) -> None: ...

class StartBulkTeamMemberSandBoxOperationResponse(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class StartGrokBotSlackConnectRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class StartGrokBotSlackConnectResponse(_message.Message):
    __slots__ = ("url", "outcome")
    URL_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    url: str
    outcome: GrokBotSlackConnectOutcome
    def __init__(self, url: _Optional[str] = ..., outcome: _Optional[_Union[GrokBotSlackConnectOutcome, str]] = ...) -> None: ...

class StatSandBoxStoreObjectRequest(_message.Message):
    __slots__ = ("rel_path",)
    REL_PATH_FIELD_NUMBER: _ClassVar[int]
    rel_path: str
    def __init__(self, rel_path: _Optional[str] = ...) -> None: ...

class StatSandBoxStoreObjectResponse(_message.Message):
    __slots__ = ("exists", "etag", "size_bytes", "last_modified_ms")
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_MS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    etag: str
    size_bytes: int
    last_modified_ms: int
    def __init__(self, exists: bool = ..., etag: _Optional[str] = ..., size_bytes: _Optional[int] = ..., last_modified_ms: _Optional[int] = ...) -> None: ...

class SubagentDescriptor(_message.Message):
    __slots__ = ("name", "description", "source_path", "source_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_path: str
    source_url: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source_path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class SubmitGrokBotSecretRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "value", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    value: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., value: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class SubmitGrokBotSecretResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class SubmitGrokBotUserComputerResponsesRequest(_message.Message):
    __slots__ = ("machine_id", "credential", "frames")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    credential: str
    frames: _containers.RepeatedCompositeFieldContainer[GrokBotUserComputerResponseFrame]
    def __init__(self, machine_id: _Optional[str] = ..., credential: _Optional[str] = ..., frames: _Optional[_Iterable[_Union[GrokBotUserComputerResponseFrame, _Mapping]]] = ...) -> None: ...

class SubmitGrokBotUserComputerResponsesResponse(_message.Message):
    __slots__ = ("accepted_count",)
    ACCEPTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    accepted_count: int
    def __init__(self, accepted_count: _Optional[int] = ...) -> None: ...

class SubmitGrokBotUserFormRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "values", "session_id", "platform")
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    values: _containers.ScalarMap[str, str]
    session_id: str
    platform: GrokBotUserFormClientPlatform
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ..., session_id: _Optional[str] = ..., platform: _Optional[_Union[GrokBotUserFormClientPlatform, str]] = ...) -> None: ...

class SubmitGrokBotUserFormResponse(_message.Message):
    __slots__ = ("accepted", "refusal")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    refusal: GrokBotHarnessRefusal
    def __init__(self, accepted: bool = ..., refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class SubmitLogsRequest(_message.Message):
    __slots__ = ("logs",)
    LOGS_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[ClientLogEntry]
    def __init__(self, logs: _Optional[_Iterable[_Union[ClientLogEntry, _Mapping]]] = ...) -> None: ...

class SubmitLogsResponse(_message.Message):
    __slots__ = ("success", "error_message", "logs_processed", "logs_dropped")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOGS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    LOGS_DROPPED_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    logs_processed: int
    logs_dropped: int
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ..., logs_processed: _Optional[int] = ..., logs_dropped: _Optional[int] = ...) -> None: ...

class SwitchModelAction(_message.Message):
    __slots__ = ("suggested_model", "parameters", "max_mode")
    class ModelParameterValue(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: str
        value: str
        def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUGGESTED_MODEL_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MAX_MODE_FIELD_NUMBER: _ClassVar[int]
    suggested_model: str
    parameters: _containers.RepeatedCompositeFieldContainer[SwitchModelAction.ModelParameterValue]
    max_mode: bool
    def __init__(self, suggested_model: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[SwitchModelAction.ModelParameterValue, _Mapping]]] = ..., max_mode: bool = ...) -> None: ...

class SyncOnePasswordConnectionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Team(_message.Message):
    __slots__ = ("name", "id", "role", "seats", "has_billing", "request_quota_per_seat", "privacy_mode_forced", "allow_sso", "admin_only_usage_pricing", "subscription_status", "bedrock_iam_role", "verified", "is_enterprise", "privacy_mode_migration_opted_out", "bedrock_external_id", "membership_type", "purchased_seats", "billing_cycle_start", "billing_cycle_end", "pricing_strategy", "total_committed_dollars", "data_sharing_discount_eligible", "dashboard_analytics_requires_admin", "individual_spend_limits_blocked", "allow_domain_join", "domain_join_domains", "sso_enabled", "customer_balance_cents", "scim_require_user_directory", "self_serve_tiered_pricing_enabled", "new_member_usage_promo_eligible", "deleted_at_ms", "granted_permissions", "is_direct_member", "team_slug", "private_inference_enablement")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    HAS_BILLING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_QUOTA_PER_SEAT_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_MODE_FORCED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SSO_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ONLY_USAGE_PRICING_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_ENTERPRISE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_MODE_MIGRATION_OPTED_OUT_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_SEATS_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_START_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_END_FIELD_NUMBER: _ClassVar[int]
    PRICING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COMMITTED_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    DATA_SHARING_DISCOUNT_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ANALYTICS_REQUIRES_ADMIN_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_SPEND_LIMITS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DOMAIN_JOIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_JOIN_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    SSO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_BALANCE_CENTS_FIELD_NUMBER: _ClassVar[int]
    SCIM_REQUIRE_USER_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SELF_SERVE_TIERED_PRICING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NEW_MEMBER_USAGE_PROMO_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    TEAM_SLUG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_INFERENCE_ENABLEMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: int
    role: TeamRole
    seats: int
    has_billing: bool
    request_quota_per_seat: int
    privacy_mode_forced: bool
    allow_sso: bool
    admin_only_usage_pricing: bool
    subscription_status: str
    bedrock_iam_role: str
    verified: bool
    is_enterprise: bool
    privacy_mode_migration_opted_out: bool
    bedrock_external_id: str
    membership_type: str
    purchased_seats: int
    billing_cycle_start: int
    billing_cycle_end: int
    pricing_strategy: str
    total_committed_dollars: int
    data_sharing_discount_eligible: bool
    dashboard_analytics_requires_admin: bool
    individual_spend_limits_blocked: bool
    allow_domain_join: bool
    domain_join_domains: _containers.RepeatedScalarFieldContainer[str]
    sso_enabled: bool
    customer_balance_cents: int
    scim_require_user_directory: bool
    self_serve_tiered_pricing_enabled: bool
    new_member_usage_promo_eligible: bool
    deleted_at_ms: int
    granted_permissions: _containers.RepeatedScalarFieldContainer[str]
    is_direct_member: bool
    team_slug: str
    private_inference_enablement: PrivateInferenceEnablement
    def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., role: _Optional[_Union[TeamRole, str]] = ..., seats: _Optional[int] = ..., has_billing: bool = ..., request_quota_per_seat: _Optional[int] = ..., privacy_mode_forced: bool = ..., allow_sso: bool = ..., admin_only_usage_pricing: bool = ..., subscription_status: _Optional[str] = ..., bedrock_iam_role: _Optional[str] = ..., verified: bool = ..., is_enterprise: bool = ..., privacy_mode_migration_opted_out: bool = ..., bedrock_external_id: _Optional[str] = ..., membership_type: _Optional[str] = ..., purchased_seats: _Optional[int] = ..., billing_cycle_start: _Optional[int] = ..., billing_cycle_end: _Optional[int] = ..., pricing_strategy: _Optional[str] = ..., total_committed_dollars: _Optional[int] = ..., data_sharing_discount_eligible: bool = ..., dashboard_analytics_requires_admin: bool = ..., individual_spend_limits_blocked: bool = ..., allow_domain_join: bool = ..., domain_join_domains: _Optional[_Iterable[str]] = ..., sso_enabled: bool = ..., customer_balance_cents: _Optional[int] = ..., scim_require_user_directory: bool = ..., self_serve_tiered_pricing_enabled: bool = ..., new_member_usage_promo_eligible: bool = ..., deleted_at_ms: _Optional[int] = ..., granted_permissions: _Optional[_Iterable[str]] = ..., is_direct_member: bool = ..., team_slug: _Optional[str] = ..., private_inference_enablement: _Optional[_Union[PrivateInferenceEnablement, str]] = ...) -> None: ...

class TeamAdminModelRef(_message.Message):
    __slots__ = ("model_id", "parameters")
    class ModelParameterValue(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: str
        value: str
        def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    parameters: _containers.RepeatedCompositeFieldContainer[TeamAdminModelRef.ModelParameterValue]
    def __init__(self, model_id: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[TeamAdminModelRef.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class TeamAdminNewChatModelResetRule(_message.Message):
    __slots__ = ("source_model", "target_model")
    SOURCE_MODEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODEL_FIELD_NUMBER: _ClassVar[int]
    source_model: TeamAdminModelRef
    target_model: TeamAdminModelRef
    def __init__(self, source_model: _Optional[_Union[TeamAdminModelRef, _Mapping]] = ..., target_model: _Optional[_Union[TeamAdminModelRef, _Mapping]] = ...) -> None: ...

class TeamAdminNewChatModelResetSettings(_message.Message):
    __slots__ = ("enabled", "rules")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    rules: _containers.RepeatedCompositeFieldContainer[TeamAdminNewChatModelResetRule]
    def __init__(self, enabled: bool = ..., rules: _Optional[_Iterable[_Union[TeamAdminNewChatModelResetRule, _Mapping]]] = ...) -> None: ...

class TeamMarketplaceConfig(_message.Message):
    __slots__ = ("directory_group_ids", "configured_by", "created_at", "updated_at", "access_grants")
    DIRECTORY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_GRANTS_FIELD_NUMBER: _ClassVar[int]
    directory_group_ids: _containers.RepeatedScalarFieldContainer[int]
    configured_by: int
    created_at: int
    updated_at: int
    access_grants: _containers.RepeatedCompositeFieldContainer[MarketplaceAccessGrant]
    def __init__(self, directory_group_ids: _Optional[_Iterable[int]] = ..., configured_by: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., access_grants: _Optional[_Iterable[_Union[MarketplaceAccessGrant, _Mapping]]] = ...) -> None: ...

class TeamMember(_message.Message):
    __slots__ = ("name", "id", "role", "email", "is_removed", "billing_tier", "pending_billing_tier", "role_is_managed")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_REMOVED_FIELD_NUMBER: _ClassVar[int]
    BILLING_TIER_FIELD_NUMBER: _ClassVar[int]
    PENDING_BILLING_TIER_FIELD_NUMBER: _ClassVar[int]
    ROLE_IS_MANAGED_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: int
    role: TeamRole
    email: str
    is_removed: bool
    billing_tier: TeamMemberBillingTier
    pending_billing_tier: TeamMemberBillingTier
    role_is_managed: bool
    def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., role: _Optional[_Union[TeamRole, str]] = ..., email: _Optional[str] = ..., is_removed: bool = ..., billing_tier: _Optional[_Union[TeamMemberBillingTier, str]] = ..., pending_billing_tier: _Optional[_Union[TeamMemberBillingTier, str]] = ..., role_is_managed: bool = ...) -> None: ...

class TeamMemberSandBoxPod(_message.Message):
    __slots__ = ("cluster", "pod_id", "tenant_id", "flavor", "run_state", "image_tag", "created_at_ms", "last_active_at_ms", "node_id", "failure_reason")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    POD_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_MS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    pod_id: str
    tenant_id: str
    flavor: str
    run_state: str
    image_tag: str
    created_at_ms: int
    last_active_at_ms: int
    node_id: str
    failure_reason: str
    def __init__(self, cluster: _Optional[str] = ..., pod_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., flavor: _Optional[str] = ..., run_state: _Optional[str] = ..., image_tag: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., last_active_at_ms: _Optional[int] = ..., node_id: _Optional[str] = ..., failure_reason: _Optional[str] = ...) -> None: ...

class TeamPluginPopularityCount(_message.Message):
    __slots__ = ("plugin_id", "member_install_count")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_INSTALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    member_install_count: int
    def __init__(self, plugin_id: _Optional[int] = ..., member_install_count: _Optional[int] = ...) -> None: ...

class TextToSpeechRequest(_message.Message):
    __slots__ = ("text", "voice_id", "language", "speed")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    text: str
    voice_id: str
    language: str
    speed: float
    def __init__(self, text: _Optional[str] = ..., voice_id: _Optional[str] = ..., language: _Optional[str] = ..., speed: _Optional[float] = ...) -> None: ...

class TextToSpeechResponse(_message.Message):
    __slots__ = ("audio", "mime_type", "synthesis_time_ms")
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SYNTHESIS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    mime_type: str
    synthesis_time_ms: int
    def __init__(self, audio: _Optional[bytes] = ..., mime_type: _Optional[str] = ..., synthesis_time_ms: _Optional[int] = ...) -> None: ...

class TrackEventsRequest(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AnalyticsEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[AnalyticsEvent, _Mapping]]] = ...) -> None: ...

class TrackEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TranscribeAudioRequest(_message.Message):
    __slots__ = ("audio", "mime_type", "language")
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    mime_type: str
    language: str
    def __init__(self, audio: _Optional[bytes] = ..., mime_type: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class TranscribeAudioResponse(_message.Message):
    __slots__ = ("text", "transcription_time_ms")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    text: str
    transcription_time_ms: int
    def __init__(self, text: _Optional[str] = ..., transcription_time_ms: _Optional[int] = ...) -> None: ...

class UninstallGrokBotSlackAppRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class UninstallGrokBotSlackAppResponse(_message.Message):
    __slots__ = ("outcome", "slack_team_id", "slack_error", "retry_after_seconds")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    SLACK_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_ERROR_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    outcome: GrokBotSlackUninstallOutcome
    slack_team_id: str
    slack_error: str
    retry_after_seconds: int
    def __init__(self, outcome: _Optional[_Union[GrokBotSlackUninstallOutcome, str]] = ..., slack_team_id: _Optional[str] = ..., slack_error: _Optional[str] = ..., retry_after_seconds: _Optional[int] = ...) -> None: ...

class UninstallUserPluginRequest(_message.Message):
    __slots__ = ("plugin_id",)
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    def __init__(self, plugin_id: _Optional[int] = ...) -> None: ...

class UninstallUserPluginResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class UpdateGrokBotAgentMarketplaceRequest(_message.Message):
    __slots__ = ("agent_id", "display_name", "description")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    display_name: str
    description: str
    def __init__(self, agent_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateGrokBotAgentMarketplaceResponse(_message.Message):
    __slots__ = ("marketplace",)
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ...) -> None: ...

class UpdateGrokBotAgentRequest(_message.Message):
    __slots__ = ("id", "name", "description", "title", "avatar_shape", "avatar_color", "clear_avatar", "avatar_data_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    CLEAR_AVATAR_FIELD_NUMBER: _ClassVar[int]
    AVATAR_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    title: str
    avatar_shape: str
    avatar_color: str
    clear_avatar: _empty_pb2.Empty
    avatar_data_url: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., avatar_shape: _Optional[str] = ..., avatar_color: _Optional[str] = ..., clear_avatar: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., avatar_data_url: _Optional[str] = ...) -> None: ...

class UpdateGrokBotAgentResponse(_message.Message):
    __slots__ = ("agent",)
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: GrokBotAgent
    def __init__(self, agent: _Optional[_Union[GrokBotAgent, _Mapping]] = ...) -> None: ...

class UpdateGrokBotAgentSkillRequest(_message.Message):
    __slots__ = ("agent_id", "name", "description", "content")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    description: str
    content: str
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class UpdateGrokBotAgentSkillResponse(_message.Message):
    __slots__ = ("marketplace", "plugins", "skill")
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    marketplace: GrokBotAgentMarketplace
    plugins: _containers.RepeatedCompositeFieldContainer[GrokBotAgentPlugin]
    skill: GrokBotAgentPluginSkill
    def __init__(self, marketplace: _Optional[_Union[GrokBotAgentMarketplace, _Mapping]] = ..., plugins: _Optional[_Iterable[_Union[GrokBotAgentPlugin, _Mapping]]] = ..., skill: _Optional[_Union[GrokBotAgentPluginSkill, _Mapping]] = ...) -> None: ...

class UpdateGrokBotMarketplaceCategoryInternalRequest(_message.Message):
    __slots__ = ("category_id", "name")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    name: str
    def __init__(self, category_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateGrokBotMarketplaceCreatorInternalRequest(_message.Message):
    __slots__ = ("creator_id", "name", "profile_photo_url", "handles", "replace_handles")
    class HandlesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    HANDLES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_HANDLES_FIELD_NUMBER: _ClassVar[int]
    creator_id: int
    name: str
    profile_photo_url: str
    handles: _containers.ScalarMap[str, str]
    replace_handles: bool
    def __init__(self, creator_id: _Optional[int] = ..., name: _Optional[str] = ..., profile_photo_url: _Optional[str] = ..., handles: _Optional[_Mapping[str, str]] = ..., replace_handles: bool = ...) -> None: ...

class UpdateGrokBotMarketplaceListingInternalRequest(_message.Message):
    __slots__ = ("listing_id", "slug", "category", "name", "description", "image_url", "default_avatar", "creator_id", "category_ids", "replace_categories")
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AVATAR_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    slug: str
    category: str
    name: str
    description: str
    image_url: str
    default_avatar: GrokBotMarketplaceDefaultAvatar
    creator_id: int
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    replace_categories: bool
    def __init__(self, listing_id: _Optional[int] = ..., slug: _Optional[str] = ..., category: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., image_url: _Optional[str] = ..., default_avatar: _Optional[_Union[GrokBotMarketplaceDefaultAvatar, _Mapping]] = ..., creator_id: _Optional[int] = ..., category_ids: _Optional[_Iterable[int]] = ..., replace_categories: bool = ...) -> None: ...

class UpdateGrokBotMarketplaceListingTemplateInternalRequest(_message.Message):
    __slots__ = ("listing_id", "recipe_json")
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_JSON_FIELD_NUMBER: _ClassVar[int]
    listing_id: int
    recipe_json: str
    def __init__(self, listing_id: _Optional[int] = ..., recipe_json: _Optional[str] = ...) -> None: ...

class UpdateGrokBotUserRuntimeSettingsRequest(_message.Message):
    __slots__ = ("pinned_agents", "sidebar_sections", "has_seen_onboarding")
    PINNED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    SIDEBAR_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_SEEN_ONBOARDING_FIELD_NUMBER: _ClassVar[int]
    pinned_agents: GrokBotPinnedAgents
    sidebar_sections: GrokBotSidebarSections
    has_seen_onboarding: bool
    def __init__(self, pinned_agents: _Optional[_Union[GrokBotPinnedAgents, _Mapping]] = ..., sidebar_sections: _Optional[_Union[GrokBotSidebarSections, _Mapping]] = ..., has_seen_onboarding: bool = ...) -> None: ...

class UpdateGrokBotUserRuntimeSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: GrokBotUserRuntimeSettings
    def __init__(self, settings: _Optional[_Union[GrokBotUserRuntimeSettings, _Mapping]] = ...) -> None: ...

class UpdateSandMachineLabelRequest(_message.Message):
    __slots__ = ("machine_id", "label")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    label: str
    def __init__(self, machine_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class UpdateSandMachineLabelResponse(_message.Message):
    __slots__ = ("machine",)
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    machine: SandMachine
    def __init__(self, machine: _Optional[_Union[SandMachine, _Mapping]] = ...) -> None: ...

class UpdateSandMachineLocalToolPermissionRequest(_message.Message):
    __slots__ = ("machine_id", "local_tool_permission")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TOOL_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    local_tool_permission: str
    def __init__(self, machine_id: _Optional[str] = ..., local_tool_permission: _Optional[str] = ...) -> None: ...

class UpdateSandMachineLocalToolPermissionResponse(_message.Message):
    __slots__ = ("machine",)
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    machine: SandMachine
    def __init__(self, machine: _Optional[_Union[SandMachine, _Mapping]] = ...) -> None: ...

class UpdateSandMachineMessagesEnabledRequest(_message.Message):
    __slots__ = ("machine_id", "messages_enabled")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    messages_enabled: bool
    def __init__(self, machine_id: _Optional[str] = ..., messages_enabled: bool = ...) -> None: ...

class UpdateSandMachineMessagesEnabledResponse(_message.Message):
    __slots__ = ("machine",)
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    machine: SandMachine
    def __init__(self, machine: _Optional[_Union[SandMachine, _Mapping]] = ...) -> None: ...

class UpdateUserNameRequest(_message.Message):
    __slots__ = ("first_name", "last_name")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class UpdateUserNameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserPluginInstallRequest(_message.Message):
    __slots__ = ("plugin_id", "is_enabled", "pinned_git_ref", "variables")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PINNED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    plugin_id: int
    is_enabled: bool
    pinned_git_ref: str
    variables: _struct_pb2.Struct
    def __init__(self, plugin_id: _Optional[int] = ..., is_enabled: bool = ..., pinned_git_ref: _Optional[str] = ..., variables: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateUserPluginInstallResponse(_message.Message):
    __slots__ = ("install",)
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    install: UserPluginInstall
    def __init__(self, install: _Optional[_Union[UserPluginInstall, _Mapping]] = ...) -> None: ...

class UpgradeAction(_message.Message):
    __slots__ = ("membership_to_upgrade_to", "try_immediate_upgrade", "allow_trial", "dashboard_action")
    MEMBERSHIP_TO_UPGRADE_TO_FIELD_NUMBER: _ClassVar[int]
    TRY_IMMEDIATE_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TRIAL_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ACTION_FIELD_NUMBER: _ClassVar[int]
    membership_to_upgrade_to: str
    try_immediate_upgrade: bool
    allow_trial: bool
    dashboard_action: DashboardAction
    def __init__(self, membership_to_upgrade_to: _Optional[str] = ..., try_immediate_upgrade: bool = ..., allow_trial: bool = ..., dashboard_action: _Optional[_Union[DashboardAction, _Mapping]] = ...) -> None: ...

class UpgradeChoice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadGrokBotAgentAttachmentChunkRequest(_message.Message):
    __slots__ = ("agent_id", "upload_id", "file_name", "offset", "total_size", "data", "sha256_hex", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SHA256_HEX_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    upload_id: str
    file_name: str
    offset: int
    total_size: int
    data: bytes
    sha256_hex: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., file_name: _Optional[str] = ..., offset: _Optional[int] = ..., total_size: _Optional[int] = ..., data: _Optional[bytes] = ..., sha256_hex: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UploadGrokBotAgentAttachmentChunkResponse(_message.Message):
    __slots__ = ("received_bytes", "path")
    RECEIVED_BYTES_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    received_bytes: int
    path: str
    def __init__(self, received_bytes: _Optional[int] = ..., path: _Optional[str] = ...) -> None: ...

class UploadIssueTraceRequest(_message.Message):
    __slots__ = ("token", "payload", "payload_hash")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_HASH_FIELD_NUMBER: _ClassVar[int]
    token: str
    payload: str
    payload_hash: str
    def __init__(self, token: _Optional[str] = ..., payload: _Optional[str] = ..., payload_hash: _Optional[str] = ...) -> None: ...

class UploadIssueTraceResponse(_message.Message):
    __slots__ = ("event_id", "size")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    size: int
    def __init__(self, event_id: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class UpsertGrokBotUserFormVaultEntryRequest(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: GrokBotUserFormVaultEntry
    def __init__(self, entry: _Optional[_Union[GrokBotUserFormVaultEntry, _Mapping]] = ...) -> None: ...

class UpsertGrokBotUserFormVaultEntryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UrlAction(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class UserAgentStoreSkillsSyncSettings(_message.Message):
    __slots__ = ("allowed",)
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    def __init__(self, allowed: bool = ...) -> None: ...

class UserPluginInstall(_message.Message):
    __slots__ = ("user_id", "plugin_id", "is_enabled", "created_at", "updated_at", "plugin", "pinned_git_ref")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    PINNED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    plugin_id: int
    is_enabled: bool
    created_at: int
    updated_at: int
    plugin: Plugin
    pinned_git_ref: str
    def __init__(self, user_id: _Optional[int] = ..., plugin_id: _Optional[int] = ..., is_enabled: bool = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., plugin: _Optional[_Union[Plugin, _Mapping]] = ..., pinned_git_ref: _Optional[str] = ...) -> None: ...

class ValidateMcpOAuthTokensRequest(_message.Message):
    __slots__ = ("server_urls", "service_account_id", "targets", "server_identifiers")
    class Target(_message.Message):
        __slots__ = ("server_url", "account_key")
        SERVER_URL_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
        server_url: str
        account_key: str
        def __init__(self, server_url: _Optional[str] = ..., account_key: _Optional[str] = ...) -> None: ...
    SERVER_URLS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    server_urls: _containers.RepeatedScalarFieldContainer[str]
    service_account_id: str
    targets: _containers.RepeatedCompositeFieldContainer[ValidateMcpOAuthTokensRequest.Target]
    server_identifiers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_urls: _Optional[_Iterable[str]] = ..., service_account_id: _Optional[str] = ..., targets: _Optional[_Iterable[_Union[ValidateMcpOAuthTokensRequest.Target, _Mapping]]] = ..., server_identifiers: _Optional[_Iterable[str]] = ...) -> None: ...

class ValidateMcpOAuthTokensResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("server_url", "has_valid_token", "account_key", "server_identifier", "served_by")
        SERVER_URL_FIELD_NUMBER: _ClassVar[int]
        HAS_VALID_TOKEN_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
        SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        SERVED_BY_FIELD_NUMBER: _ClassVar[int]
        server_url: str
        has_valid_token: bool
        account_key: str
        server_identifier: str
        served_by: McpServedBy
        def __init__(self, server_url: _Optional[str] = ..., has_valid_token: bool = ..., account_key: _Optional[str] = ..., server_identifier: _Optional[str] = ..., served_by: _Optional[_Union[McpServedBy, str]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ValidateMcpOAuthTokensResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ValidateMcpOAuthTokensResponse.Result, _Mapping]]] = ...) -> None: ...

class VoteGrokBotFeedbackRequest(_message.Message):
    __slots__ = ("agent_id", "entry_id", "action", "categories", "comment", "session_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    entry_id: str
    action: GrokBotFeedbackAction
    categories: _containers.RepeatedScalarFieldContainer[str]
    comment: str
    session_id: str
    def __init__(self, agent_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., action: _Optional[_Union[GrokBotFeedbackAction, str]] = ..., categories: _Optional[_Iterable[str]] = ..., comment: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class VoteGrokBotFeedbackResponse(_message.Message):
    __slots__ = ("refusal",)
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    refusal: GrokBotHarnessRefusal
    def __init__(self, refusal: _Optional[_Union[GrokBotHarnessRefusal, _Mapping]] = ...) -> None: ...

class WatchGrokBotTranscriptsRequest(_message.Message):
    __slots__ = ("cursors", "include_unlisted_agents", "inline_body_max_bytes")
    CURSORS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNLISTED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    INLINE_BODY_MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    cursors: _containers.RepeatedCompositeFieldContainer[GrokBotTranscriptCursor]
    include_unlisted_agents: bool
    inline_body_max_bytes: int
    def __init__(self, cursors: _Optional[_Iterable[_Union[GrokBotTranscriptCursor, _Mapping]]] = ..., include_unlisted_agents: bool = ..., inline_body_max_bytes: _Optional[int] = ...) -> None: ...

class WatchGrokBotUserComputerConnected(_message.Message):
    __slots__ = ("pending_request_count",)
    PENDING_REQUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    pending_request_count: int
    def __init__(self, pending_request_count: _Optional[int] = ...) -> None: ...

class WatchGrokBotUserComputerHeartbeat(_message.Message):
    __slots__ = ("pending_request_count",)
    PENDING_REQUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    pending_request_count: int
    def __init__(self, pending_request_count: _Optional[int] = ...) -> None: ...

class WatchGrokBotUserComputerNotify(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchGrokBotUserComputerRequestsEvent(_message.Message):
    __slots__ = ("connected", "notify", "heartbeat")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    connected: WatchGrokBotUserComputerConnected
    notify: WatchGrokBotUserComputerNotify
    heartbeat: WatchGrokBotUserComputerHeartbeat
    def __init__(self, connected: _Optional[_Union[WatchGrokBotUserComputerConnected, _Mapping]] = ..., notify: _Optional[_Union[WatchGrokBotUserComputerNotify, _Mapping]] = ..., heartbeat: _Optional[_Union[WatchGrokBotUserComputerHeartbeat, _Mapping]] = ...) -> None: ...

class WatchGrokBotUserComputerRequestsRequest(_message.Message):
    __slots__ = ("machine_id", "credential", "hello")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    credential: str
    hello: GrokBotUserComputerHello
    def __init__(self, machine_id: _Optional[str] = ..., credential: _Optional[str] = ..., hello: _Optional[_Union[GrokBotUserComputerHello, _Mapping]] = ...) -> None: ...

class WatchSandBoxMigrationRequest(_message.Message):
    __slots__ = ("from_offset_key", "include_finished")
    FROM_OFFSET_KEY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    from_offset_key: str
    include_finished: bool
    def __init__(self, from_offset_key: _Optional[str] = ..., include_finished: bool = ...) -> None: ...

class WorkspaceTrustControls(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...
