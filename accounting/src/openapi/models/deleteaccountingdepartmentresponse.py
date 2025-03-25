"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedid import UnifiedID, UnifiedIDTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Any, Dict
from typing_extensions import Annotated, NotRequired, TypedDict


class DeleteAccountingDepartmentResponseTypedDict(TypedDict):
    r"""Department deleted"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    service: str
    r"""Apideck ID of service provider"""
    resource: str
    r"""Unified API resource name"""
    operation: str
    r"""Operation performed"""
    data: UnifiedIDTypedDict
    r"""A object containing a unique identifier for the resource that was created, updated, or deleted."""
    raw: NotRequired[Nullable[Dict[str, Any]]]
    r"""Raw response from the integration when raw=true query param is provided"""


class DeleteAccountingDepartmentResponse(BaseModel):
    r"""Department deleted"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    service: str
    r"""Apideck ID of service provider"""

    resource: str
    r"""Unified API resource name"""

    operation: str
    r"""Operation performed"""

    data: UnifiedID
    r"""A object containing a unique identifier for the resource that was created, updated, or deleted."""

    raw: Annotated[OptionalNullable[Dict[str, Any]], pydantic.Field(alias="_raw")] = (
        UNSET
    )
    r"""Raw response from the integration when raw=true query param is provided"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["_raw"]
        nullable_fields = ["_raw"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
