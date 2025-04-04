"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .authtype import AuthType
from .connectionstate import ConnectionState
from apideck_accounting_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class ConsumerConnectionTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    icon: NotRequired[str]
    logo: NotRequired[str]
    website: NotRequired[str]
    tag_line: NotRequired[str]
    service_id: NotRequired[str]
    unified_api: NotRequired[str]
    consumer_id: NotRequired[str]
    auth_type: NotRequired[AuthType]
    r"""Type of authorization used by the connector"""
    enabled: NotRequired[bool]
    settings: NotRequired[Nullable[Dict[str, Any]]]
    r"""Connection settings. Values will persist to `form_fields` with corresponding id"""
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Attach your own consumer specific metadata"""
    created_at: NotRequired[str]
    updated_at: NotRequired[Nullable[str]]
    state: NotRequired[ConnectionState]
    r"""[Connection state flow](#section/Connection-state)"""


class ConsumerConnection(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    icon: Optional[str] = None

    logo: Optional[str] = None

    website: Optional[str] = None

    tag_line: Optional[str] = None

    service_id: Optional[str] = None

    unified_api: Optional[str] = None

    consumer_id: Optional[str] = None

    auth_type: Optional[AuthType] = None
    r"""Type of authorization used by the connector"""

    enabled: Optional[bool] = None

    settings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Connection settings. Values will persist to `form_fields` with corresponding id"""

    metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Attach your own consumer specific metadata"""

    created_at: Optional[str] = None

    updated_at: OptionalNullable[str] = UNSET

    state: Optional[ConnectionState] = None
    r"""[Connection state flow](#section/Connection-state)"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "name",
            "icon",
            "logo",
            "website",
            "tag_line",
            "service_id",
            "unified_api",
            "consumer_id",
            "auth_type",
            "enabled",
            "settings",
            "metadata",
            "created_at",
            "updated_at",
            "state",
        ]
        nullable_fields = ["settings", "metadata", "updated_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
