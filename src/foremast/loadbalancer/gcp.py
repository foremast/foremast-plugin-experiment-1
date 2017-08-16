"""Google Cloud Platform Load Balancers."""
from foremast.loadbalancer.base import BaseLoadBalancer


class LoadBalancer(BaseLoadBalancer):
    """GCP LB configuration."""

    def create(self):
        """Create GCP LB."""
        return 'Created GCP Load Balancer.'

    def delete(self):
        """Delete GCP LB."""
        return 'Deleted GCP Load Balancer.'

    def update(self):
        """Update GCP LB."""
        return 'Updated GCP Load Balancer.'
