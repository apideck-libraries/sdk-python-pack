"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InvoicesFilterTypedDict(TypedDict):
    updated_since: NotRequired[datetime]
    created_since: NotRequired[datetime]
    number: NotRequired[str]
    r"""Invoice number to search for"""


class InvoicesFilter(BaseModel):
    updated_since: Annotated[Optional[datetime], FieldMetadata(query=True)] = None

    created_since: Annotated[Optional[datetime], FieldMetadata(query=True)] = None

    number: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Invoice number to search for"""
