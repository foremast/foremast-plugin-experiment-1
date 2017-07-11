#!/usr/bin/env python
"""Test script."""
import importlib


def main():
    """Main."""
    provider = 'aws'
    resource = 'dns'

    import_path = '.'.join(['foremast_{0}_1'.format(provider), 'plugins', provider, resource])
    aws_dns_module = importlib.import_module(import_path)
    aws_dns = aws_dns_module.Dns()
    print(aws_dns.create())

    provider = 'gcp'

    import_path = '.'.join(['foremast_{0}_2'.format(provider), 'plugins', resource, provider])
    gcp_dns_module = importlib.import_module(import_path)
    gcp_dns = gcp_dns_module.Dns()
    print(gcp_dns.create())


if __name__ == '__main__':
    main()
