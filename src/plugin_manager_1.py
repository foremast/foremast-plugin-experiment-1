"""This is an example using PluginBase

Install the necessary package with
$ pip install pluginbase
"""
from pluginbase import PluginBase


plugin_base = PluginBase(package='foremast.plugins')


services = ['dns', 'loadbalancer']
all_plugins = []
for service in services:
    path = './foremast/{}'.format(service)
    all_plugins.append(path)


plugin_source = plugin_base.make_plugin_source(
    searchpath=all_plugins)

print('List all plugins')
for plugin in plugin_source.list_plugins():
    print(plugin)

print('Call plugin directly.')
for provider in ('aws', 'gcp'):
    my_plugin = plugin_source.load_plugin(provider)
    dns = my_plugin.Dns()
    print(dns.create())
