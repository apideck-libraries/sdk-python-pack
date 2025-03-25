"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attachmentreferencetype import AttachmentReferenceType
from openapi.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AttachmentReferenceTypedDict(TypedDict):
    type: NotRequired[AttachmentReferenceType]
    id: NotRequired[str]
    r"""A unique identifier for an object."""


class AttachmentReference(BaseModel):
    type: Optional[AttachmentReferenceType] = None

    id: Optional[str] = None
    r"""A unique identifier for an object."""
