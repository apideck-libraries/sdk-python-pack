"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .bankaccount import BankAccount, BankAccountTypedDict
from .currency import Currency
from .customfield import CustomField, CustomFieldTypedDict
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .deprecatedlinkedtrackingcategory import (
    DeprecatedLinkedTrackingCategory,
    DeprecatedLinkedTrackingCategoryTypedDict,
)
from .invoicelineitem import (
    InvoiceLineItem,
    InvoiceLineItemInput,
    InvoiceLineItemInputTypedDict,
    InvoiceLineItemTypedDict,
)
from .linkedcustomer import LinkedCustomer, LinkedCustomerTypedDict
from .linkedcustomer_input import LinkedCustomerInput, LinkedCustomerInputTypedDict
from .linkedledgeraccount import LinkedLedgerAccount, LinkedLedgerAccountTypedDict
from .linkedledgeraccount_input import (
    LinkedLedgerAccountInput,
    LinkedLedgerAccountInputTypedDict,
)
from .linkedtrackingcategory import (
    LinkedTrackingCategory,
    LinkedTrackingCategoryTypedDict,
)
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from datetime import date, datetime
from enum import Enum
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InvoiceType(str, Enum):
    r"""Invoice type"""

    STANDARD = "standard"
    CREDIT = "credit"
    SERVICE = "service"
    PRODUCT = "product"
    SUPPLIER = "supplier"
    OTHER = "other"


class InvoiceStatus(str, Enum):
    r"""Invoice status"""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    AUTHORISED = "authorised"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    VOID = "void"
    CREDIT = "credit"
    DELETED = "deleted"


class InvoiceTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""
    type: NotRequired[Nullable[InvoiceType]]
    r"""Invoice type"""
    number: NotRequired[Nullable[str]]
    r"""Invoice number."""
    customer: NotRequired[Nullable[LinkedCustomerTypedDict]]
    r"""The customer this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    invoice_date: NotRequired[Nullable[date]]
    r"""Date invoice was issued - YYYY-MM-DD."""
    due_date: NotRequired[Nullable[date]]
    r"""The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD."""
    terms: NotRequired[Nullable[str]]
    r"""Terms of payment."""
    po_number: NotRequired[Nullable[str]]
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""
    reference: NotRequired[Nullable[str]]
    r"""Optional invoice reference."""
    status: NotRequired[Nullable[InvoiceStatus]]
    r"""Invoice status"""
    invoice_sent: NotRequired[bool]
    r"""Invoice sent to contact/customer."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this invoice."""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    discount_percentage: NotRequired[Nullable[float]]
    r"""Discount percentage applied to this invoice."""
    discount_amount: NotRequired[Nullable[float]]
    r"""Discount amount applied to this invoice."""
    total: NotRequired[Nullable[float]]
    r"""Total amount of invoice, including tax."""
    balance: NotRequired[Nullable[float]]
    r"""Balance of invoice due."""
    deposit: NotRequired[Nullable[float]]
    r"""Amount of deposit made to this invoice."""
    customer_memo: NotRequired[Nullable[str]]
    r"""Customer memo"""
    tracking_category: NotRequired[Nullable[DeprecatedLinkedTrackingCategoryTypedDict]]
    tracking_categories: NotRequired[
        Nullable[List[Nullable[LinkedTrackingCategoryTypedDict]]]
    ]
    r"""A list of linked tracking categories."""
    line_items: NotRequired[List[InvoiceLineItemTypedDict]]
    billing_address: NotRequired[AddressTypedDict]
    shipping_address: NotRequired[AddressTypedDict]
    template_id: NotRequired[Nullable[str]]
    r"""Optional invoice template"""
    source_document_url: NotRequired[Nullable[str]]
    r"""URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    language: NotRequired[Nullable[str]]
    r"""language code according to ISO 639-1. For the United States - EN"""
    accounting_by_row: NotRequired[Nullable[bool]]
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""
    bank_account: NotRequired[BankAccountTypedDict]
    ledger_account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
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


class Invoice(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    type: OptionalNullable[InvoiceType] = UNSET
    r"""Invoice type"""

    number: OptionalNullable[str] = UNSET
    r"""Invoice number."""

    customer: OptionalNullable[LinkedCustomer] = UNSET
    r"""The customer this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    invoice_date: OptionalNullable[date] = UNSET
    r"""Date invoice was issued - YYYY-MM-DD."""

    due_date: OptionalNullable[date] = UNSET
    r"""The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD."""

    terms: OptionalNullable[str] = UNSET
    r"""Terms of payment."""

    po_number: OptionalNullable[str] = UNSET
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional invoice reference."""

    status: OptionalNullable[InvoiceStatus] = UNSET
    r"""Invoice status"""

    invoice_sent: Optional[bool] = None
    r"""Invoice sent to contact/customer."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this invoice."""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    discount_percentage: OptionalNullable[float] = UNSET
    r"""Discount percentage applied to this invoice."""

    discount_amount: OptionalNullable[float] = UNSET
    r"""Discount amount applied to this invoice."""

    total: OptionalNullable[float] = UNSET
    r"""Total amount of invoice, including tax."""

    balance: OptionalNullable[float] = UNSET
    r"""Balance of invoice due."""

    deposit: OptionalNullable[float] = UNSET
    r"""Amount of deposit made to this invoice."""

    customer_memo: OptionalNullable[str] = UNSET
    r"""Customer memo"""

    tracking_category: Annotated[
        OptionalNullable[DeprecatedLinkedTrackingCategory],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET

    tracking_categories: OptionalNullable[List[Nullable[LinkedTrackingCategory]]] = (
        UNSET
    )
    r"""A list of linked tracking categories."""

    line_items: Optional[List[InvoiceLineItem]] = None

    billing_address: Optional[Address] = None

    shipping_address: Optional[Address] = None

    template_id: OptionalNullable[str] = UNSET
    r"""Optional invoice template"""

    source_document_url: OptionalNullable[str] = UNSET
    r"""URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    language: OptionalNullable[str] = UNSET
    r"""language code according to ISO 639-1. For the United States - EN"""

    accounting_by_row: OptionalNullable[bool] = UNSET
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""

    bank_account: Optional[BankAccount] = None

    ledger_account: OptionalNullable[LinkedLedgerAccount] = UNSET

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    custom_fields: Optional[List[CustomField]] = None

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
            "downstream_id",
            "type",
            "number",
            "customer",
            "company_id",
            "invoice_date",
            "due_date",
            "terms",
            "po_number",
            "reference",
            "status",
            "invoice_sent",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "discount_percentage",
            "discount_amount",
            "total",
            "balance",
            "deposit",
            "customer_memo",
            "tracking_category",
            "tracking_categories",
            "line_items",
            "billing_address",
            "shipping_address",
            "template_id",
            "source_document_url",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "bank_account",
            "ledger_account",
            "custom_mappings",
            "custom_fields",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "downstream_id",
            "type",
            "number",
            "customer",
            "company_id",
            "invoice_date",
            "due_date",
            "terms",
            "po_number",
            "reference",
            "status",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "discount_percentage",
            "discount_amount",
            "total",
            "balance",
            "deposit",
            "customer_memo",
            "tracking_category",
            "tracking_categories",
            "template_id",
            "source_document_url",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "ledger_account",
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

        for n, f in self.model_fields.items():
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


class InvoiceInputTypedDict(TypedDict):
    type: NotRequired[Nullable[InvoiceType]]
    r"""Invoice type"""
    number: NotRequired[Nullable[str]]
    r"""Invoice number."""
    customer: NotRequired[Nullable[LinkedCustomerInputTypedDict]]
    r"""The customer this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    invoice_date: NotRequired[Nullable[date]]
    r"""Date invoice was issued - YYYY-MM-DD."""
    due_date: NotRequired[Nullable[date]]
    r"""The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD."""
    terms: NotRequired[Nullable[str]]
    r"""Terms of payment."""
    po_number: NotRequired[Nullable[str]]
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""
    reference: NotRequired[Nullable[str]]
    r"""Optional invoice reference."""
    status: NotRequired[Nullable[InvoiceStatus]]
    r"""Invoice status"""
    invoice_sent: NotRequired[bool]
    r"""Invoice sent to contact/customer."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this invoice."""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    discount_percentage: NotRequired[Nullable[float]]
    r"""Discount percentage applied to this invoice."""
    discount_amount: NotRequired[Nullable[float]]
    r"""Discount amount applied to this invoice."""
    total: NotRequired[Nullable[float]]
    r"""Total amount of invoice, including tax."""
    balance: NotRequired[Nullable[float]]
    r"""Balance of invoice due."""
    deposit: NotRequired[Nullable[float]]
    r"""Amount of deposit made to this invoice."""
    customer_memo: NotRequired[Nullable[str]]
    r"""Customer memo"""
    tracking_category: NotRequired[Nullable[DeprecatedLinkedTrackingCategoryTypedDict]]
    tracking_categories: NotRequired[
        Nullable[List[Nullable[LinkedTrackingCategoryTypedDict]]]
    ]
    r"""A list of linked tracking categories."""
    line_items: NotRequired[List[InvoiceLineItemInputTypedDict]]
    billing_address: NotRequired[AddressTypedDict]
    shipping_address: NotRequired[AddressTypedDict]
    template_id: NotRequired[Nullable[str]]
    r"""Optional invoice template"""
    source_document_url: NotRequired[Nullable[str]]
    r"""URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    language: NotRequired[Nullable[str]]
    r"""language code according to ISO 639-1. For the United States - EN"""
    accounting_by_row: NotRequired[Nullable[bool]]
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""
    bank_account: NotRequired[BankAccountTypedDict]
    ledger_account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class InvoiceInput(BaseModel):
    type: OptionalNullable[InvoiceType] = UNSET
    r"""Invoice type"""

    number: OptionalNullable[str] = UNSET
    r"""Invoice number."""

    customer: OptionalNullable[LinkedCustomerInput] = UNSET
    r"""The customer this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    invoice_date: OptionalNullable[date] = UNSET
    r"""Date invoice was issued - YYYY-MM-DD."""

    due_date: OptionalNullable[date] = UNSET
    r"""The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD."""

    terms: OptionalNullable[str] = UNSET
    r"""Terms of payment."""

    po_number: OptionalNullable[str] = UNSET
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional invoice reference."""

    status: OptionalNullable[InvoiceStatus] = UNSET
    r"""Invoice status"""

    invoice_sent: Optional[bool] = None
    r"""Invoice sent to contact/customer."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this invoice."""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    discount_percentage: OptionalNullable[float] = UNSET
    r"""Discount percentage applied to this invoice."""

    discount_amount: OptionalNullable[float] = UNSET
    r"""Discount amount applied to this invoice."""

    total: OptionalNullable[float] = UNSET
    r"""Total amount of invoice, including tax."""

    balance: OptionalNullable[float] = UNSET
    r"""Balance of invoice due."""

    deposit: OptionalNullable[float] = UNSET
    r"""Amount of deposit made to this invoice."""

    customer_memo: OptionalNullable[str] = UNSET
    r"""Customer memo"""

    tracking_category: Annotated[
        OptionalNullable[DeprecatedLinkedTrackingCategory],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET

    tracking_categories: OptionalNullable[List[Nullable[LinkedTrackingCategory]]] = (
        UNSET
    )
    r"""A list of linked tracking categories."""

    line_items: Optional[List[InvoiceLineItemInput]] = None

    billing_address: Optional[Address] = None

    shipping_address: Optional[Address] = None

    template_id: OptionalNullable[str] = UNSET
    r"""Optional invoice template"""

    source_document_url: OptionalNullable[str] = UNSET
    r"""URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    language: OptionalNullable[str] = UNSET
    r"""language code according to ISO 639-1. For the United States - EN"""

    accounting_by_row: OptionalNullable[bool] = UNSET
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""

    bank_account: Optional[BankAccount] = None

    ledger_account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    custom_fields: Optional[List[CustomField]] = None

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "type",
            "number",
            "customer",
            "company_id",
            "invoice_date",
            "due_date",
            "terms",
            "po_number",
            "reference",
            "status",
            "invoice_sent",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "discount_percentage",
            "discount_amount",
            "total",
            "balance",
            "deposit",
            "customer_memo",
            "tracking_category",
            "tracking_categories",
            "line_items",
            "billing_address",
            "shipping_address",
            "template_id",
            "source_document_url",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "bank_account",
            "ledger_account",
            "custom_fields",
            "row_version",
            "pass_through",
        ]
        nullable_fields = [
            "type",
            "number",
            "customer",
            "company_id",
            "invoice_date",
            "due_date",
            "terms",
            "po_number",
            "reference",
            "status",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "discount_percentage",
            "discount_amount",
            "total",
            "balance",
            "deposit",
            "customer_memo",
            "tracking_category",
            "tracking_categories",
            "template_id",
            "source_document_url",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "ledger_account",
            "row_version",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
