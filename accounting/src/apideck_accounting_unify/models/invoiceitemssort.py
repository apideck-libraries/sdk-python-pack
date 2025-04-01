"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sortdirection import SortDirection
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InvoiceItemsSortBy(str, Enum):
    r"""The field on which to sort the Invoice Items"""

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"


class InvoiceItemsSortTypedDict(TypedDict):
    by: NotRequired[InvoiceItemsSortBy]
    r"""The field on which to sort the Invoice Items"""
    direction: NotRequired[SortDirection]
    r"""The direction in which to sort the results"""


class InvoiceItemsSort(BaseModel):
    by: Annotated[Optional[InvoiceItemsSortBy], FieldMetadata(query=True)] = None
    r"""The field on which to sort the Invoice Items"""

    direction: Annotated[Optional[SortDirection], FieldMetadata(query=True)] = (
        SortDirection.ASC
    )
    r"""The direction in which to sort the results"""
