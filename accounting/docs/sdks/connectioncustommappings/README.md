# ConnectionCustomMappings
(*vault.connection_custom_mappings*)

## Overview

### Available Operations

* [list](#list) - List connection custom mappings

## list

This endpoint returns a list of custom mappings for a connection.

### Example Usage

```python
from apideck_accounting_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.vault.connection_custom_mappings.list(unified_api="crm", service_id="pipedrive", resource="leads", resource_id="1234")

    assert res.get_custom_mappings_response is not None

    # Handle response
    print(res.get_custom_mappings_response)

```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        | Example                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `unified_api`                                                                                                                                                                      | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | Unified API                                                                                                                                                                        | crm                                                                                                                                                                                |
| `service_id`                                                                                                                                                                       | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | Service ID of the resource to return                                                                                                                                               | pipedrive                                                                                                                                                                          |
| `resource`                                                                                                                                                                         | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | Name of the resource (plural)                                                                                                                                                      | leads                                                                                                                                                                              |
| `consumer_id`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | ID of the consumer which you want to get or push data from                                                                                                                         | test-consumer                                                                                                                                                                      |
| `app_id`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | The ID of your Unify application                                                                                                                                                   | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                                            |
| `resource_id`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id. | 1234                                                                                                                                                                               |
| `retries`                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                |                                                                                                                                                                                    |

### Response

**[models.VaultConnectionCustomMappingsAllResponse](../../models/vaultconnectioncustommappingsallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |