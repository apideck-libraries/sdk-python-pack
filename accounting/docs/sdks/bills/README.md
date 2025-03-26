# Bills
(*accounting.bills*)

## Overview

### Available Operations

* [get](#get) - Get Bill
* [update](#update) - Update Bill
* [delete](#delete) - Delete Bill

## get

Get Bill

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.bills.get(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", fields="id,updated_at")

    assert res.get_bill_response is not None

    # Handle response
    print(res.get_bill_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ID of the record you are acting upon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `consumer_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ID of the consumer which you want to get or push data from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | test-consumer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `app_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The ID of your Unify application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `service_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | salesforce                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `raw`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Include raw response. Mostly used for debugging purposes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.AccountingBillsOneResponse](../../models/accountingbillsoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## update

Update Bill

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import dateutil.parser
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.bills.update(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", bill_number="10001", supplier={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "address": {
            "id": "123",
            "type": apideck_unify.Type.PRIMARY,
            "string": "25 Spring Street, Blackburn, VIC 3130",
            "name": "HQ US",
            "line1": "Main street",
            "line2": "apt #",
            "line3": "Suite #",
            "line4": "delivery instructions",
            "street_number": "25",
            "city": "San Francisco",
            "state": "CA",
            "postal_code": "94104",
            "country": "US",
            "latitude": "40.759211",
            "longitude": "-73.984638",
            "county": "Santa Clara",
            "contact_name": "Elon Musk",
            "salutation": "Mr",
            "phone_number": "111-111-1111",
            "fax": "122-111-1111",
            "email": "elon@musk.com",
            "website": "https://elonmusk.com",
            "notes": "Address notes or delivery instructions.",
            "row_version": "1-12345",
        },
    }, company_id="12345", currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, bill_date=dateutil.parser.parse("2020-09-30").date(), due_date=dateutil.parser.parse("2020-10-30").date(), paid_date=dateutil.parser.parse("2020-10-30").date(), po_number="90000117", reference="123456", line_items=[
        {
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
            "location_id": "1234",
            "department_id": "1234",
            "item": {
                "id": "12344",
                "code": "120-C",
                "name": "Model Y",
            },
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "ledger_account": {
                "id": "123456",
                "nominal_code": "N091",
                "code": "453",
            },
            "tracking_categories": [
                {
                    "id": "123456",
                    "name": "New York",
                },
                {
                    "id": "123456",
                    "name": "New York",
                },
            ],
            "row_version": "1-12345",
        },
        {
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
            "location_id": "1234",
            "department_id": "1234",
            "item": {
                "id": "12344",
                "code": "120-C",
                "name": "Model Y",
            },
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "ledger_account": {
                "id": "123456",
                "nominal_code": "N091",
                "code": "453",
            },
            "tracking_categories": [
                {
                    "id": "123456",
                    "name": "New York",
                },
                {
                    "id": "123456",
                    "name": "New York",
                },
            ],
            "row_version": "1-12345",
        },
        {
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
            "location_id": "1234",
            "department_id": "1234",
            "item": {
                "id": "12344",
                "code": "120-C",
                "name": "Model Y",
            },
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "ledger_account": {
                "id": "123456",
                "nominal_code": "N091",
                "code": "453",
            },
            "tracking_categories": [
                {
                    "id": "123456",
                    "name": "New York",
                },
                {
                    "id": "123456",
                    "name": "New York",
                },
                {
                    "id": "123456",
                    "name": "New York",
                },
            ],
            "row_version": "1-12345",
        },
    ], terms="Net 30 days", balance=27500, deposit=0, sub_total=27500, total_tax=2500, total=27500, tax_code="1234", notes="Some notes about this bill.", status=apideck_unify.BillStatus.DRAFT, ledger_account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, payment_method="cash", channel="email", language="EN", accounting_by_row=False, bank_account={
        "bank_name": "Monzo",
        "account_number": "123465",
        "account_name": "SPACEX LLC",
        "account_type": apideck_unify.AccountType.CREDIT_CARD,
        "iban": "CH2989144532982975332",
        "bic": "AUDSCHGGXXX",
        "routing_number": "012345678",
        "bsb_number": "062-001",
        "branch_identifier": "001",
        "bank_code": "BNH",
        "currency": apideck_unify.Currency.USD,
    }, discount_percentage=5.5, source_document_url="https://www.invoicesolution.com/bill/123456", tracking_categories=[
        {
            "id": "123456",
            "name": "New York",
        },
        {
            "id": "123456",
            "name": "New York",
        },
    ], row_version="1-12345", custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": {},
        },
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": [
                {},
            ],
        },
    ], pass_through=[
        {
            "service_id": "<id>",
            "extend_paths": [
                {
                    "path": "$.nested.property",
                    "value": {
                        "TaxClassificationRef": {
                            "value": "EUC-99990201-V1-00020000",
                        },
                    },
                },
            ],
        },
    ], accounting_period="01-24")

    assert res.update_bill_response is not None

    # Handle response
    print(res.update_bill_response)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | ID of the record you are acting upon.                                                                                                                            |                                                                                                                                                                  |
| `consumer_id`                                                                                                                                                    | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | ID of the consumer which you want to get or push data from                                                                                                       | test-consumer                                                                                                                                                    |
| `app_id`                                                                                                                                                         | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | The ID of your Unify application                                                                                                                                 | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                          |
| `service_id`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                    | salesforce                                                                                                                                                       |
| `raw`                                                                                                                                                            | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Include raw response. Mostly used for debugging purposes                                                                                                         |                                                                                                                                                                  |
| `bill_number`                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Reference to supplier bill number                                                                                                                                | 10001                                                                                                                                                            |
| `supplier`                                                                                                                                                       | [OptionalNullable[models.LinkedSupplierInput]](../../models/linkedsupplierinput.md)                                                                              | :heavy_minus_sign:                                                                                                                                               | The supplier this entity is linked to.                                                                                                                           |                                                                                                                                                                  |
| `company_id`                                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | The company or subsidiary id the transaction belongs to                                                                                                          | 12345                                                                                                                                                            |
| `currency`                                                                                                                                                       | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                               | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                               | USD                                                                                                                                                              |
| `currency_rate`                                                                                                                                                  | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Currency Exchange Rate at the time entity was recorded/generated.                                                                                                | 0.69                                                                                                                                                             |
| `tax_inclusive`                                                                                                                                                  | *OptionalNullable[bool]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                               | Amounts are including tax                                                                                                                                        | true                                                                                                                                                             |
| `bill_date`                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | Date bill was issued - YYYY-MM-DD.                                                                                                                               | 2020-09-30                                                                                                                                                       |
| `due_date`                                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD.                                                                            | 2020-10-30                                                                                                                                                       |
| `paid_date`                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.                                                                              | 2020-10-30                                                                                                                                                       |
| `po_number`                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | 90000117                                                                                                                                                         |
| `reference`                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Optional bill reference.                                                                                                                                         | 123456                                                                                                                                                           |
| `line_items`                                                                                                                                                     | List[[models.BillLineItemInput](../../models/billlineiteminput.md)]                                                                                              | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `terms`                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Terms of payment.                                                                                                                                                | Net 30 days                                                                                                                                                      |
| `balance`                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Balance of bill due.                                                                                                                                             | 27500                                                                                                                                                            |
| `deposit`                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Amount of deposit made to this bill.                                                                                                                             | 0                                                                                                                                                                |
| `sub_total`                                                                                                                                                      | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Sub-total amount, normally before tax.                                                                                                                           | 27500                                                                                                                                                            |
| `total_tax`                                                                                                                                                      | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Total tax amount applied to this bill.                                                                                                                           | 2500                                                                                                                                                             |
| `total`                                                                                                                                                          | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Total amount of bill, including tax.                                                                                                                             | 27500                                                                                                                                                            |
| `tax_code`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                                     | 1234                                                                                                                                                             |
| `notes`                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              | Some notes about this bill.                                                                                                                                      |
| `status`                                                                                                                                                         | [OptionalNullable[models.BillStatus]](../../models/billstatus.md)                                                                                                | :heavy_minus_sign:                                                                                                                                               | Invoice status                                                                                                                                                   | draft                                                                                                                                                            |
| `ledger_account`                                                                                                                                                 | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                                    | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `payment_method`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Payment method used for the transaction, such as cash, credit card, bank transfer, or check                                                                      | cash                                                                                                                                                             |
| `channel`                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | The channel through which the transaction is processed.                                                                                                          | email                                                                                                                                                            |
| `language`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | language code according to ISO 639-1. For the United States - EN                                                                                                 | EN                                                                                                                                                               |
| `accounting_by_row`                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                               | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.                | false                                                                                                                                                            |
| `bank_account`                                                                                                                                                   | [Optional[models.BankAccount]](../../models/bankaccount.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `discount_percentage`                                                                                                                                            | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Discount percentage applied to this transaction.                                                                                                                 | 5.5                                                                                                                                                              |
| `source_document_url`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.                                             | https://www.invoicesolution.com/bill/123456                                                                                                                      |
| `tracking_categories`                                                                                                                                            | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                          | :heavy_minus_sign:                                                                                                                                               | A list of linked tracking categories.                                                                                                                            |                                                                                                                                                                  |
| `row_version`                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.                       | 1-12345                                                                                                                                                          |
| `custom_fields`                                                                                                                                                  | List[[models.CustomField](../../models/customfield.md)]                                                                                                          | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `pass_through`                                                                                                                                                   | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                                  | :heavy_minus_sign:                                                                                                                                               | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources.          |                                                                                                                                                                  |
| `accounting_period`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Accounting period                                                                                                                                                | 01-24                                                                                                                                                            |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.AccountingBillsUpdateResponse](../../models/accountingbillsupdateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## delete

Delete Bill

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.bills.delete(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce")

    assert res.delete_bill_response is not None

    # Handle response
    print(res.delete_bill_response)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `consumer_id`                                                                                                                                 | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | ID of the consumer which you want to get or push data from                                                                                    | test-consumer                                                                                                                                 |
| `app_id`                                                                                                                                      | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The ID of your Unify application                                                                                                              | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                       |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingBillsDeleteResponse](../../models/accountingbillsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |