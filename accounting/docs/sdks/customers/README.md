# Customers
(*accounting.customers*)

## Overview

### Available Operations

* [get](#get) - Get Customer
* [update](#update) - Update Customer
* [delete](#delete) - Delete Customer

## get

Get Customer

### Example Usage

```python
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.customers.get(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", fields="id,updated_at")

    assert res.get_customer_response is not None

    # Handle response
    print(res.get_customer_response)

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

**[models.AccountingCustomersOneResponse](../../models/accountingcustomersoneresponse.md)**

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

Update Customer

### Example Usage

```python
import apideck_accounting_unify
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.customers.update(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", display_id="EMP00101", display_name="Windsurf Shop", company_name="SpaceX", company_id="12345", title="CEO", first_name="Elon", middle_name="D.", last_name="Musk", suffix="Jr.", individual=True, project=False, addresses=[
        {
            "id": "123",
            "type": apideck_accounting_unify.Type.PRIMARY,
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
        {
            "id": "123",
            "type": apideck_accounting_unify.Type.PRIMARY,
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
        {
            "id": "123",
            "type": apideck_accounting_unify.Type.PRIMARY,
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
    ], phone_numbers=[
        {
            "number": "111-111-1111",
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "extension": "105",
            "type": apideck_accounting_unify.PhoneNumberType.PRIMARY,
        },
        {
            "number": "111-111-1111",
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "extension": "105",
            "type": apideck_accounting_unify.PhoneNumberType.PRIMARY,
        },
    ], emails=[
        {
            "email": "elon@musk.com",
            "id": "123",
            "type": apideck_accounting_unify.EmailType.PRIMARY,
        },
        {
            "email": "elon@musk.com",
            "id": "123",
            "type": apideck_accounting_unify.EmailType.PRIMARY,
        },
    ], websites=[
        {
            "url": "http://example.com",
            "id": "12345",
            "type": apideck_accounting_unify.WebsiteType.PRIMARY,
        },
        {
            "url": "http://example.com",
            "id": "12345",
            "type": apideck_accounting_unify.WebsiteType.PRIMARY,
        },
        {
            "url": "http://example.com",
            "id": "12345",
            "type": apideck_accounting_unify.WebsiteType.PRIMARY,
        },
    ], bank_accounts=[
        {
            "bank_name": "Monzo",
            "account_number": "123465",
            "account_name": "SPACEX LLC",
            "account_type": apideck_accounting_unify.AccountType.CREDIT_CARD,
            "iban": "CH2989144532982975332",
            "bic": "AUDSCHGGXXX",
            "routing_number": "012345678",
            "bsb_number": "062-001",
            "branch_identifier": "001",
            "bank_code": "BNH",
            "currency": apideck_accounting_unify.Currency.USD,
        },
        {
            "bank_name": "Monzo",
            "account_number": "123465",
            "account_name": "SPACEX LLC",
            "account_type": apideck_accounting_unify.AccountType.CREDIT_CARD,
            "iban": "CH2989144532982975332",
            "bic": "AUDSCHGGXXX",
            "routing_number": "012345678",
            "bsb_number": "062-001",
            "branch_identifier": "001",
            "bank_code": "BNH",
            "currency": apideck_accounting_unify.Currency.USD,
        },
    ], notes="Some notes about this customer", tax_rate={
        "id": "123456",
        "rate": 10,
    }, tax_number="US123945459", currency=apideck_accounting_unify.Currency.USD, account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, parent={
        "id": "12345",
        "name": "Windsurf Shop",
    }, status=apideck_accounting_unify.CustomerStatus.ACTIVE, payment_method="cash", channel="email", custom_fields=[
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
    ], row_version="1-12345", pass_through=[
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
    ])

    assert res.update_customer_response is not None

    # Handle response
    print(res.update_customer_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `display_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Display ID                                                                                                                                              | EMP00101                                                                                                                                                |
| `display_name`                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Display name                                                                                                                                            | Windsurf Shop                                                                                                                                           |
| `company_name`                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The name of the company.                                                                                                                                | SpaceX                                                                                                                                                  |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `title`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The job title of the person.                                                                                                                            | CEO                                                                                                                                                     |
| `first_name`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The first name of the person.                                                                                                                           | Elon                                                                                                                                                    |
| `middle_name`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Middle name of the person.                                                                                                                              | D.                                                                                                                                                      |
| `last_name`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The last name of the person.                                                                                                                            | Musk                                                                                                                                                    |
| `suffix`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | Jr.                                                                                                                                                     |
| `individual`                                                                                                                                            | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Is this an individual or business customer                                                                                                              | true                                                                                                                                                    |
| `project`                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | If true, indicates this is a Project.                                                                                                                   | false                                                                                                                                                   |
| `addresses`                                                                                                                                             | List[[models.Address](../../models/address.md)]                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `phone_numbers`                                                                                                                                         | List[[models.PhoneNumber](../../models/phonenumber.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `emails`                                                                                                                                                | List[[models.Email](../../models/email.md)]                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `websites`                                                                                                                                              | List[[models.Website](../../models/website.md)]                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `bank_accounts`                                                                                                                                         | List[[models.BankAccount](../../models/bankaccount.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `notes`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Some notes about this customer                                                                                                                          | Some notes about this customer                                                                                                                          |
| `tax_rate`                                                                                                                                              | [Optional[models.LinkedTaxRateInput]](../../models/linkedtaxrateinput.md)                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `tax_number`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | US123945459                                                                                                                                             |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `account`                                                                                                                                               | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                           | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `parent`                                                                                                                                                | [OptionalNullable[models.LinkedParentCustomer]](../../models/linkedparentcustomer.md)                                                                   | :heavy_minus_sign:                                                                                                                                      | The parent customer this entity is linked to.                                                                                                           |                                                                                                                                                         |
| `status`                                                                                                                                                | [OptionalNullable[models.CustomerStatus]](../../models/customerstatus.md)                                                                               | :heavy_minus_sign:                                                                                                                                      | Customer status                                                                                                                                         | active                                                                                                                                                  |
| `payment_method`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Payment method used for the transaction, such as cash, credit card, bank transfer, or check                                                             | cash                                                                                                                                                    |
| `channel`                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The channel through which the transaction is processed.                                                                                                 | email                                                                                                                                                   |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingCustomersUpdateResponse](../../models/accountingcustomersupdateresponse.md)**

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

Delete Customer

### Example Usage

```python
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.customers.delete(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce")

    assert res.delete_customer_response is not None

    # Handle response
    print(res.delete_customer_response)

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

**[models.AccountingCustomersDeleteResponse](../../models/accountingcustomersdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |