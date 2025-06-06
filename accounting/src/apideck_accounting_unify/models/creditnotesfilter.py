"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreditNotesFilterTypedDict(TypedDict):
    updated_since: NotRequired[datetime]


class CreditNotesFilter(BaseModel):
    updated_since: Annotated[Optional[datetime], FieldMetadata(query=True)] = None
