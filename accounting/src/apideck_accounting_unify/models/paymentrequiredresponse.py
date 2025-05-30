"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_accounting_unify.types import BaseModel
from typing import Optional


class PaymentRequiredResponseData(BaseModel):
    status_code: Optional[float] = None
    r"""HTTP status code"""

    error: Optional[str] = None
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""

    type_name: Optional[str] = None
    r"""The type of error returned"""

    message: Optional[str] = None
    r"""A human-readable message providing more details about the error."""

    detail: Optional[str] = None
    r"""Contains parameter or domain specific information related to the error and why it occurred."""

    ref: Optional[str] = None
    r"""Link to documentation of error type"""


class PaymentRequiredResponse(Exception):
    r"""Payment Required"""

    data: PaymentRequiredResponseData

    def __init__(self, data: PaymentRequiredResponseData):
        self.data = data

    def __str__(self) -> str:
        return self.data.message if self.data.message is not None else "unknown error"
