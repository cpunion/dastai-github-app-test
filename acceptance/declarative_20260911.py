"""Synthetic acceptance fixture; never imported by production code."""

def acceptance_percentage(completed, total):
    """Return completion percentage; an empty batch should produce zero."""
    return completed / total * 100
