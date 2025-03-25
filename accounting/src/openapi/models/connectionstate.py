"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class ConnectionState(str, Enum):
    r"""[Connection state flow](#section/Connection-state)"""

    AVAILABLE = "available"
    CALLABLE = "callable"
    ADDED = "added"
    AUTHORIZED = "authorized"
    INVALID = "invalid"
