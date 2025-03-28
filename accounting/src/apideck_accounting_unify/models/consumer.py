"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .consumerconnection import ConsumerConnection, ConsumerConnectionTypedDict
from .consumermetadata import ConsumerMetadata, ConsumerMetadataTypedDict
from .requestcountallocation import (
    RequestCountAllocation,
    RequestCountAllocationTypedDict,
)
from apideck_accounting_unify.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ConsumerTypedDict(TypedDict):
    consumer_id: str
    r"""Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn't exist yet, Vault will upsert a consumer based on your ID."""
    application_id: NotRequired[str]
    r"""ID of your Apideck Application"""
    metadata: NotRequired[ConsumerMetadataTypedDict]
    r"""The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended."""
    connections: NotRequired[List[ConsumerConnectionTypedDict]]
    services: NotRequired[List[str]]
    aggregated_request_count: NotRequired[float]
    request_counts: NotRequired[RequestCountAllocationTypedDict]
    created: NotRequired[str]
    modified: NotRequired[str]
    request_count_updated: NotRequired[str]


class Consumer(BaseModel):
    consumer_id: str
    r"""Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn't exist yet, Vault will upsert a consumer based on your ID."""

    application_id: Optional[str] = None
    r"""ID of your Apideck Application"""

    metadata: Optional[ConsumerMetadata] = None
    r"""The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended."""

    connections: Optional[List[ConsumerConnection]] = None

    services: Optional[List[str]] = None

    aggregated_request_count: Optional[float] = None

    request_counts: Optional[RequestCountAllocation] = None

    created: Optional[str] = None

    modified: Optional[str] = None

    request_count_updated: Optional[str] = None
