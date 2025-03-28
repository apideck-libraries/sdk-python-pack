"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_accounting_unify.types import BaseModel
from apideck_accounting_unify.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ProfitAndLossFilterTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""Filter by customer id"""
    start_date: NotRequired[str]
    r"""Filter by start date. If start date is given, end date is required."""
    end_date: NotRequired[str]
    r"""Filter by end date. If end date is given, start date is required."""


class ProfitAndLossFilter(BaseModel):
    customer_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Filter by customer id"""

    start_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Filter by start date. If start date is given, end date is required."""

    end_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Filter by end date. If end date is given, start date is required."""
