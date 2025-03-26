# Consumers
(*vault.consumers*)

## Overview

### Available Operations

* [get](#get) - Get consumer
* [update](#update) - Update consumer
* [delete](#delete) - Delete consumer

## get

Consumer detail including their aggregated counts with the connections they have authorized.


### Example Usage

```python
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.consumers.get(consumer_id="test_user_id", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.get_consumer_response is not None

    # Handle response
    print(res.get_consumer_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `consumer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the consumer to return                                        | test_user_id                                                        |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConsumersOneResponse](../../models/vaultconsumersoneresponse.md)**

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

Update consumer metadata such as name and email.

### Example Usage

```python
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.consumers.update(consumer_id="test_user_id", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", metadata={
        "account_name": "SpaceX",
        "user_name": "Elon Musk",
        "email": "elon@musk.com",
        "image": "https://www.spacex.com/static/images/share.jpg",
    })

    assert res.update_consumer_response is not None

    # Handle response
    print(res.update_consumer_response)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `consumer_id`                                                                                                         | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | ID of the consumer to return                                                                                          | test_user_id                                                                                                          |
| `app_id`                                                                                                              | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | The ID of your Unify application                                                                                      | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                               |
| `metadata`                                                                                                            | [Optional[models.ConsumerMetadata]](../../models/consumermetadata.md)                                                 | :heavy_minus_sign:                                                                                                    | The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended. |                                                                                                                       |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.VaultConsumersUpdateResponse](../../models/vaultconsumersupdateresponse.md)**

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

Delete consumer and all their connections, including credentials.

### Example Usage

```python
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.consumers.delete(consumer_id="test_user_id", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.delete_consumer_response is not None

    # Handle response
    print(res.delete_consumer_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `consumer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the consumer to return                                        | test_user_id                                                        |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConsumersDeleteResponse](../../models/vaultconsumersdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |