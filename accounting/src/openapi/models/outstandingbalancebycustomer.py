"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .outstandingbalancebycurrency import (
    OutstandingBalanceByCurrency,
    OutstandingBalanceByCurrencyTypedDict,
)
from openapi.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class OutstandingBalanceByCustomerTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""Unique identifier for the customer."""
    customer_name: NotRequired[str]
    r"""Full name of the customer."""
    outstanding_balances_by_currency: NotRequired[
        List[OutstandingBalanceByCurrencyTypedDict]
    ]


class OutstandingBalanceByCustomer(BaseModel):
    customer_id: Optional[str] = None
    r"""Unique identifier for the customer."""

    customer_name: Optional[str] = None
    r"""Full name of the customer."""

    outstanding_balances_by_currency: Optional[List[OutstandingBalanceByCurrency]] = (
        None
    )
