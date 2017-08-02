"""AWS Route 53."""
from foremast.dns.base import BaseDns


class Dns(BaseDns):
    """AWS Route 53 configuration."""

    def create(self):
        """Create AWS Route 53 Records."""
        return 'Created AWS Route 53 Record.'

    def delete(self):
        """Delete AWS Route 53 Records."""
        return 'Deleted AWS Route 53 Record.'

    def update(self):
        """Update AWS Route 53 Records."""
        return 'Updated AWS Route 53 Record.'
