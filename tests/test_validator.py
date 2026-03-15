from api_contract_monitor.validator import compare_contract


def test_compare_contract_flags_missing_and_unexpected_keys() -> None:
    result = compare_contract(
        expected={"id": "string", "status": "string"},
        actual={"id": "abc", "extra": True},
    )

    assert result["missing"] == ["status"]
    assert result["unexpected"] == ["extra"]


def test_compare_contract_supports_nested_shapes() -> None:
    result = compare_contract(
        expected={"data": {"id": "string", "status": "string"}},
        actual={"data": {"id": "123"}, "meta": {"count": 1}},
    )

    assert "data.status" in result["missing"]
    assert "meta" in result["unexpected"]
