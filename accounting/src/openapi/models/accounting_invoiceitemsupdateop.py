"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .invoiceitem import InvoiceItemInput, InvoiceItemInputTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updateinvoiceitemsresponse import (
    UpdateInvoiceItemsResponse,
    UpdateInvoiceItemsResponseTypedDict,
)
from openapi.types import BaseModel
from openapi.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class AccountingInvoiceItemsUpdateGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingInvoiceItemsUpdateGlobals(BaseModel):
    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""

    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class AccountingInvoiceItemsUpdateRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    invoice_item: InvoiceItemInputTypedDict
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""


class AccountingInvoiceItemsUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    invoice_item: Annotated[
        InvoiceItemInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""

    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""

    service_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-service-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""


AccountingInvoiceItemsUpdateResponseTypedDict = TypeAliasType(
    "AccountingInvoiceItemsUpdateResponseTypedDict",
    Union[UnexpectedErrorResponseTypedDict, UpdateInvoiceItemsResponseTypedDict],
)


AccountingInvoiceItemsUpdateResponse = TypeAliasType(
    "AccountingInvoiceItemsUpdateResponse",
    Union[UnexpectedErrorResponse, UpdateInvoiceItemsResponse],
)
