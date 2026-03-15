# api-contract-monitor

Python tool for checking API responses against expected contracts and surfacing schema drift before it becomes a production problem.

## Overview

`api-contract-monitor` is a Python-first monitoring and validation tool for checking whether third-party or internal APIs still conform to expected response shapes.

It is designed for teams dealing with fragile integrations where upstream changes can silently break consumers.

## Why This Repo Exists

This project shows a different but still relevant Python skill set:

- HTTP integration work
- schema validation
- operational diagnostics
- CLI-oriented tooling

It complements backend/API work instead of distracting from it.

## Features

- define expected response contracts in JSON
- run checks against one or more endpoints
- report missing or unexpected keys
- produce clear terminal summaries

## Example Usage

```bash
python -m api_contract_monitor.cli check --contract examples/order-status.json --url https://example.test/api/order-status
```

## Architecture

- `cli.py` parses commands
- `contracts.py` loads expected contracts
- `validator.py` compares expected and actual payload shapes
- `reporting.py` formats results

## Tradeoffs

- key-shape validation instead of full JSON Schema in v1
- standard-library implementation for clarity
- single-endpoint checks before batch monitoring

## Future Improvements

- batch config files
- JSON Schema support
- CI mode for contract regression checks
- Slack or webhook notifications
