"""This is an example using PluginBase

Install the necessary package with
$ pip install pluginbase
"""
from itertools import product

from pluginbase import PluginBase


plugin_base = PluginBase(package='foremast.plugins')


services = ['dns', 'loadbalancer']
providers = ['aws', 'gcp']
all_plugins = []
for service, provider in list(product(services, providers)):
    path = './foremast/{}/provider/{}'.format(service, provider)
    all_plugins.append(path)


plugin_source = plugin_base.make_plugin_source(
    searchpath=all_plugins)

print('List all plugins')
for plugin in plugin_source.list_plugins():
    print(plugin)

print('Call plugin directly.')
my_plugin = plugin_source.load_plugin('dns')
dns = my_plugin.Dns()
print(dns.create())
