"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PurchaseOrdersFilterTypedDict(TypedDict):
    updated_since: NotRequired[datetime]
    supplier_id: NotRequired[str]


class PurchaseOrdersFilter(BaseModel):
    updated_since: Annotated[Optional[datetime], FieldMetadata(query=True)] = None

    supplier_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
