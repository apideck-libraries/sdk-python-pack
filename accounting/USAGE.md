<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from apideck_accounting_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.tax_rates.get(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", fields="id,updated_at")

    assert res.get_tax_rate_response is not None

    # Handle response
    print(res.get_tax_rate_response)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from apideck_accounting_unify import Apideck
import asyncio
import os

async def main():

    async with Apideck(
        api_key=os.getenv("APIDECK_API_KEY", ""),
        consumer_id="test-consumer",
        app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    ) as apideck:

        res = await apideck.accounting.tax_rates.get_async(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", fields="id,updated_at")

        assert res.get_tax_rate_response is not None

        # Handle response
        print(res.get_tax_rate_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->