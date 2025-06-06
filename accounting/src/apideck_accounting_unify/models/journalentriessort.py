"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sortdirection import SortDirection
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class JournalEntriesSortBy(str, Enum):
    r"""The field on which to sort the Journal Entries."""

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"


class JournalEntriesSortTypedDict(TypedDict):
    by: NotRequired[JournalEntriesSortBy]
    r"""The field on which to sort the Journal Entries."""
    direction: NotRequired[SortDirection]
    r"""The direction in which to sort the results"""


class JournalEntriesSort(BaseModel):
    by: Annotated[Optional[JournalEntriesSortBy], FieldMetadata(query=True)] = None
    r"""The field on which to sort the Journal Entries."""

    direction: Annotated[Optional[SortDirection], FieldMetadata(query=True)] = (
        SortDirection.ASC
    )
    r"""The direction in which to sort the results"""
