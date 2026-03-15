def render_report(result: dict[str, list[str]]) -> str:
    if not result["missing"] and not result["unexpected"]:
        return "Contract check passed."

    return (
        f"Missing keys: {', '.join(result['missing']) or 'none'} | "
        f"Unexpected keys: {', '.join(result['unexpected']) or 'none'}"
    )


def render_batch_report(results: list[tuple[str, dict[str, list[str]]]]) -> str:
    lines: list[str] = []

    for label, result in results:
        lines.append(f"{label}: {render_report(result)}")

    return "\n".join(lines)
