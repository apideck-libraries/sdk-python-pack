"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_accounting_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class EmailType(str, Enum):
    r"""Email type"""

    PRIMARY = "primary"
    SECONDARY = "secondary"
    WORK = "work"
    PERSONAL = "personal"
    BILLING = "billing"
    OTHER = "other"


class EmailTypedDict(TypedDict):
    email: Nullable[str]
    r"""Email address"""
    id: NotRequired[Nullable[str]]
    r"""Unique identifier for the email address"""
    type: NotRequired[Nullable[EmailType]]
    r"""Email type"""


class Email(BaseModel):
    email: Nullable[str]
    r"""Email address"""

    id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the email address"""

    type: OptionalNullable[EmailType] = UNSET
    r"""Email type"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "type"]
        nullable_fields = ["id", "email", "type"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
