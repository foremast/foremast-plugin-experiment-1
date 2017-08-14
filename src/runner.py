#!/usr/bin/env python
"""Test script."""
import importlib


def plugin_manager(provider, resource):
    """Import provider resource modules"""
    import_path = '.'.join(['foremast', resource, 'provider', provider, resource])
    _module = importlib.import_module(import_path)
    return _module


def main():
    """Main."""
    provider = 'aws'
    resource = 'dns'

    aws_dns_module = plugin_manager(provider, resource)
    aws_dns = aws_dns_module.Dns()
    print(aws_dns.create())

    provider = 'gcp'

    gcp_dns_module = plugin_manager(provider, resource)
    gcp_dns = gcp_dns_module.Dns()
    print(gcp_dns.create())


if __name__ == '__main__':
    main()
