"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .outstandingbalancebycurrency import (
    OutstandingBalanceByCurrency,
    OutstandingBalanceByCurrencyTypedDict,
)
from apideck_accounting_unify.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class OutstandingBalanceBySupplierTypedDict(TypedDict):
    supplier_id: NotRequired[str]
    r"""Unique identifier for the supplier."""
    supplier_name: NotRequired[str]
    r"""Full name of the supplier."""
    outstanding_balances_by_currency: NotRequired[
        List[OutstandingBalanceByCurrencyTypedDict]
    ]


class OutstandingBalanceBySupplier(BaseModel):
    supplier_id: Optional[str] = None
    r"""Unique identifier for the supplier."""

    supplier_name: Optional[str] = None
    r"""Full name of the supplier."""

    outstanding_balances_by_currency: Optional[List[OutstandingBalanceByCurrency]] = (
        None
    )
