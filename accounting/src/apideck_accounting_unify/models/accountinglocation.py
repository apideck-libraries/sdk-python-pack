"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from .subsidiaryreference import SubsidiaryReference, SubsidiaryReferenceTypedDict
from .subsidiaryreference_input import (
    SubsidiaryReferenceInput,
    SubsidiaryReferenceInputTypedDict,
)
from apideck_accounting_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class LocationStatus(str, Enum):
    r"""Based on the status some functionality is enabled or disabled."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class AccountingLocationTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    parent_id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company."""
    display_name: NotRequired[Nullable[str]]
    r"""The display name of the location."""
    status: NotRequired[LocationStatus]
    r"""Based on the status some functionality is enabled or disabled."""
    addresses: NotRequired[List[AddressTypedDict]]
    subsidiaries: NotRequired[List[SubsidiaryReferenceTypedDict]]
    custom_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    updated_by: NotRequired[Nullable[str]]
    r"""The user who last updated the object."""
    created_by: NotRequired[Nullable[str]]
    r"""The user who created the object."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class AccountingLocation(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    parent_id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company."""

    display_name: OptionalNullable[str] = UNSET
    r"""The display name of the location."""

    status: Optional[LocationStatus] = None
    r"""Based on the status some functionality is enabled or disabled."""

    addresses: Optional[List[Address]] = None

    subsidiaries: Optional[List[SubsidiaryReference]] = None

    custom_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    updated_by: OptionalNullable[str] = UNSET
    r"""The user who last updated the object."""

    created_by: OptionalNullable[str] = UNSET
    r"""The user who created the object."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "parent_id",
            "company_name",
            "display_name",
            "status",
            "addresses",
            "subsidiaries",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "parent_id",
            "company_name",
            "display_name",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
        ]
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


class AccountingLocationInputTypedDict(TypedDict):
    parent_id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company."""
    display_name: NotRequired[Nullable[str]]
    r"""The display name of the location."""
    status: NotRequired[LocationStatus]
    r"""Based on the status some functionality is enabled or disabled."""
    addresses: NotRequired[List[AddressTypedDict]]
    subsidiaries: NotRequired[List[SubsidiaryReferenceInputTypedDict]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class AccountingLocationInput(BaseModel):
    parent_id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company."""

    display_name: OptionalNullable[str] = UNSET
    r"""The display name of the location."""

    status: Optional[LocationStatus] = None
    r"""Based on the status some functionality is enabled or disabled."""

    addresses: Optional[List[Address]] = None

    subsidiaries: Optional[List[SubsidiaryReferenceInput]] = None

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "parent_id",
            "company_name",
            "display_name",
            "status",
            "addresses",
            "subsidiaries",
            "row_version",
            "pass_through",
        ]
        nullable_fields = ["parent_id", "company_name", "display_name", "row_version"]
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
