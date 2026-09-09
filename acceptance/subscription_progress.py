"""Small fixture for the approved DastAI subscription live acceptance."""

def completion_percentage(completed: int, total: int) -> float:
    """Return completion percentage; empty workloads should report 0.0."""
    return 100.0 * completed / total
