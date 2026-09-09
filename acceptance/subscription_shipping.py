"""Fixture for automatic review on first non-draft PR creation."""

def qualifies_for_free_shipping(order_total: int) -> bool:
    """Orders of 50 or more qualify for free shipping."""
    return order_total > 50
