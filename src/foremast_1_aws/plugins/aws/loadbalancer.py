"""AWS Elastic Load Balancers."""
from foremast.loadbalancer.base import BaseLoadBalancer


class LoadBalancer(BaseLoadBalancer):
    """AWS ELB configuration."""

    def create(self):
        """Create AWS ELB."""
        return 'Created AWS ELB.'

    def delete(self):
        """Delete AWS ELB."""
        return 'Deleted AWS ELB.'

    def update(self):
        """Update AWS ELB."""
        return 'Updated AWS ELB.'
