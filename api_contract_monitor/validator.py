def _flatten(data: dict, prefix: str = "") -> set[str]:
    keys: set[str] = set()

    for key, value in data.items():
        path = f"{prefix}.{key}" if prefix else key
        keys.add(path)

        if isinstance(value, dict):
            keys.update(_flatten(value, path))

    return keys


def compare_contract(expected: dict, actual: dict) -> dict[str, list[str]]:
    expected_keys = _flatten(expected)
    actual_keys = _flatten(actual)

    missing = sorted(expected_keys - actual_keys)
    unexpected = sorted(actual_keys - expected_keys)

    return {
        "missing": missing,
        "unexpected": unexpected,
    }
