"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getlogsresponse import GetLogsResponse, GetLogsResponseTypedDict
from .logsfilter import LogsFilter, LogsFilterTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from openapi.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultLogsAllGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""


class VaultLogsAllGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""

    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""


class VaultLogsAllRequestTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    filter_: NotRequired[LogsFilterTypedDict]
    r"""Filter results"""
    cursor: NotRequired[Nullable[str]]
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""
    limit: NotRequired[int]
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""


class VaultLogsAllRequest(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""

    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""

    filter_: Annotated[
        Optional[LogsFilter],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Filter results"""

    cursor: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["appId", "consumerId", "filter", "cursor", "limit"]
        nullable_fields = ["cursor"]
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


VaultLogsAllResponseResultTypedDict = TypeAliasType(
    "VaultLogsAllResponseResultTypedDict",
    Union[GetLogsResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultLogsAllResponseResult = TypeAliasType(
    "VaultLogsAllResponseResult", Union[GetLogsResponse, UnexpectedErrorResponse]
)


class VaultLogsAllResponseTypedDict(TypedDict):
    result: VaultLogsAllResponseResultTypedDict


class VaultLogsAllResponse(BaseModel):
    next: Callable[[], Optional[VaultLogsAllResponse]]

    result: VaultLogsAllResponseResult
