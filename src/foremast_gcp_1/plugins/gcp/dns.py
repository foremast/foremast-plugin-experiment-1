"""GCP Cloud DNS."""
from foremast.plugins.dns import BaseDns


class Dns(BaseDns):
    """GCP Cloud DNS configuration."""

    def create(self):
        """Create GCP Cloud DNS Records."""
        return 'Created GCP Cloud DNS Record.'

    def delete(self):
        """Delete GCP Cloud DNS Records."""
        return 'Deleted GCP Cloud DNS Record.'

    def update(self):
        """Update GCP Cloud DNS Records."""
        return 'Updated GCP Cloud DNS Record.'
