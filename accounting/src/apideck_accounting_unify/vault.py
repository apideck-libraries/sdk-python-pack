"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from apideck_accounting_unify.connectioncustommappings import ConnectionCustomMappings
from apideck_accounting_unify.connections import Connections
from apideck_accounting_unify.connectionsettings import ConnectionSettings
from apideck_accounting_unify.consumerrequestcounts import ConsumerRequestCounts
from apideck_accounting_unify.consumers import Consumers
from apideck_accounting_unify.createcallback import CreateCallback
from apideck_accounting_unify.customfields import CustomFields
from apideck_accounting_unify.custommappings_sdk import CustomMappingsSDK
from apideck_accounting_unify.logs import Logs
from apideck_accounting_unify.sessions import Sessions
from apideck_accounting_unify.validateconnection import ValidateConnection


class Vault(BaseSDK):
    consumers: Consumers
    consumer_request_counts: ConsumerRequestCounts
    connections: Connections
    validate_connection: ValidateConnection
    create_callback: CreateCallback
    connection_settings: ConnectionSettings
    custom_fields: CustomFields
    connection_custom_mappings: ConnectionCustomMappings
    custom_mappings: CustomMappingsSDK
    sessions: Sessions
    logs: Logs

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.consumers = Consumers(self.sdk_configuration)
        self.consumer_request_counts = ConsumerRequestCounts(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.validate_connection = ValidateConnection(self.sdk_configuration)
        self.create_callback = CreateCallback(self.sdk_configuration)
        self.connection_settings = ConnectionSettings(self.sdk_configuration)
        self.custom_fields = CustomFields(self.sdk_configuration)
        self.connection_custom_mappings = ConnectionCustomMappings(
            self.sdk_configuration
        )
        self.custom_mappings = CustomMappingsSDK(self.sdk_configuration)
        self.sessions = Sessions(self.sdk_configuration)
        self.logs = Logs(self.sdk_configuration)
