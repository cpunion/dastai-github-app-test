"""Small fixture for the provider-event foundation live acceptance test."""


def completion_percentage(completed: int, total: int) -> float:
    """Return the percentage complete; an empty batch should report 0.0."""
    return round(completed / total * 100, 2)
