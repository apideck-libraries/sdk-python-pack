"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sortdirection import SortDirection
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InvoicesSortBy(str, Enum):
    r"""The field on which to sort the Invoices"""

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"


class InvoicesSortTypedDict(TypedDict):
    by: NotRequired[InvoicesSortBy]
    r"""The field on which to sort the Invoices"""
    direction: NotRequired[SortDirection]
    r"""The direction in which to sort the results"""


class InvoicesSort(BaseModel):
    by: Annotated[Optional[InvoicesSortBy], FieldMetadata(query=True)] = None
    r"""The field on which to sort the Invoices"""

    direction: Annotated[Optional[SortDirection], FieldMetadata(query=True)] = (
        SortDirection.ASC
    )
    r"""The direction in which to sort the results"""
