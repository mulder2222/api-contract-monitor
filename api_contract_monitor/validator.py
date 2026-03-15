def compare_contract(expected: dict, actual: dict) -> dict[str, list[str]]:
    missing = [key for key in expected.keys() if key not in actual]
    unexpected = [key for key in actual.keys() if key not in expected]

    return {
        "missing": missing,
        "unexpected": unexpected,
    }
