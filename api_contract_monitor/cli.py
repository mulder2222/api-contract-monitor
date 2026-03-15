import argparse
import json

from api_contract_monitor.contracts import load_contract
from api_contract_monitor.reporting import render_report
from api_contract_monitor.validator import compare_contract


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="api-contract-monitor")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="Compare an API response to an expected contract.")
    check_parser.add_argument("--contract", required=True, help="Path to expected contract JSON.")
    check_parser.add_argument("--payload", required=True, help="JSON payload string to validate.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "check":
        expected = load_contract(args.contract)
        actual = json.loads(args.payload)
        print(render_report(compare_contract(expected, actual)))


if __name__ == "__main__":
    main()
