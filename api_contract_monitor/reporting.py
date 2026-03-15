def render_report(result: dict[str, list[str]]) -> str:
    if not result["missing"] and not result["unexpected"]:
        return "Contract check passed."

    return (
        f"Missing keys: {', '.join(result['missing']) or 'none'} | "
        f"Unexpected keys: {', '.join(result['unexpected']) or 'none'}"
    )
