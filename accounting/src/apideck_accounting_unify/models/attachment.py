"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attachmentreference import AttachmentReference, AttachmentReferenceTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck_accounting_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AttachmentTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    display_id: NotRequired[Nullable[str]]
    r"""The display id of the file"""
    name: NotRequired[Nullable[str]]
    r"""The name of the file"""
    mime_type: NotRequired[Nullable[str]]
    r"""The MIME type of the file."""
    size: NotRequired[Nullable[int]]
    r"""The size of the file in bytes"""
    reference: NotRequired[AttachmentReferenceTypedDict]
    description: NotRequired[Nullable[str]]
    r"""Optional description of the file"""
    parent_folder_id: NotRequired[Nullable[str]]
    r"""The folder id where this attachment belong to"""
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


class Attachment(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    display_id: OptionalNullable[str] = UNSET
    r"""The display id of the file"""

    name: OptionalNullable[str] = UNSET
    r"""The name of the file"""

    mime_type: OptionalNullable[str] = UNSET
    r"""The MIME type of the file."""

    size: OptionalNullable[int] = UNSET
    r"""The size of the file in bytes"""

    reference: Optional[AttachmentReference] = None

    description: OptionalNullable[str] = UNSET
    r"""Optional description of the file"""

    parent_folder_id: OptionalNullable[str] = UNSET
    r"""The folder id where this attachment belong to"""

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
            "display_id",
            "name",
            "mime_type",
            "size",
            "reference",
            "description",
            "parent_folder_id",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "display_id",
            "name",
            "mime_type",
            "size",
            "description",
            "parent_folder_id",
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
