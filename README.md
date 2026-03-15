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
- validate flat and nested response shapes
- run single checks from the CLI
- run batch checks from a config file
- report missing or unexpected keys
- produce clear terminal summaries

## Example Usage

```bash
python -m api_contract_monitor.cli check --contract examples/order-status.json --payload '{"id":"100","status":"paid","updated_at":"2026-03-15T20:00:00Z"}'
python -m api_contract_monitor.cli batch --config examples/batch-checks.json
```

## Architecture

- `cli.py` parses commands
- `contracts.py` loads expected contracts and batch configs
- `validator.py` compares expected and actual payload shapes
- `reporting.py` formats individual and batch results

## Tradeoffs

- key-shape validation instead of full JSON Schema in v1
- standard-library implementation for clarity
- single-endpoint checks before batch monitoring

## Future Improvements

- JSON Schema support
- CI mode for contract regression checks
- Slack or webhook notifications
