"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .requestcountallocation import (
    RequestCountAllocation,
    RequestCountAllocationTypedDict,
)
from apideck_accounting_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConsumerRequestCountsInDateRangeResponseDataTypedDict(TypedDict):
    application_id: NotRequired[str]
    consumer_id: NotRequired[str]
    start_datetime: NotRequired[str]
    end_datetime: NotRequired[str]
    aggregated_request_count: NotRequired[float]
    request_counts: NotRequired[RequestCountAllocationTypedDict]


class ConsumerRequestCountsInDateRangeResponseData(BaseModel):
    application_id: Optional[str] = None

    consumer_id: Optional[str] = None

    start_datetime: Optional[str] = None

    end_datetime: Optional[str] = None

    aggregated_request_count: Optional[float] = None

    request_counts: Optional[RequestCountAllocation] = None


class ConsumerRequestCountsInDateRangeResponseTypedDict(TypedDict):
    r"""Consumers Request Counts within Date Range"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: ConsumerRequestCountsInDateRangeResponseDataTypedDict
    raw: NotRequired[Nullable[Dict[str, Any]]]
    r"""Raw response from the integration when raw=true query param is provided"""


class ConsumerRequestCountsInDateRangeResponse(BaseModel):
    r"""Consumers Request Counts within Date Range"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: ConsumerRequestCountsInDateRangeResponseData

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
