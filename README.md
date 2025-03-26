# Python SDK Pack

This repository contains optimized Python SDKs for Apideck's Unify APIs, designed for specific use cases where you need a lightweight and focused implementation.

## When to Use This SDK Pack

This SDK pack is particularly useful in the following scenarios:

1. **Limited Environments**
   - When working with environments that have cold start constraints (e.g., AWS Lambda)
   - When you need to minimize package size and dependencies
   - When startup time is critical for your application

2. **Single API Focus**
   - When you only need to interact with a specific Unify API (e.g., only Accounting or only CRM)
   - When you want to keep your dependencies minimal by including only the API components you need

## Getting Started

1. Choose the Unify API you want to use:
   - [Accounting](./accounting/README.md)
   - [ATS](./ats/README.md)
   - [CRM](./crm/README.md)
   - [Vault](./vault/README.md)
   - etc.

2. Navigate to the corresponding directory and follow the specific README instructions.

For example, if you want to use the Accounting API:
```bash
cd accounting
# Follow the instructions in accounting/README.md
```

## Benefits

- 🚀 Faster cold starts in serverless environments
- 📦 Smaller package sizes

## Documentation

Each API module has its own documentation in its respective directory. For detailed implementation guides and API references, please refer to the README in each API's directory.

For example:
- Accounting API documentation: [accounting/README.md](./accounting/README.md)


