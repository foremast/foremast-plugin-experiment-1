"""This is an example using PluginBase

Install the necessary package with
$ pip install pluginbase
"""
from pluginbase import PluginBase


plugin_base = PluginBase(package='foremast.plugins')

plugin_source = plugin_base.make_plugin_source(
    searchpath=['./foremast_1_aws/plugins/aws'])

print('List all plugins')
for plugin in plugin_source.list_plugins():
    print(plugin)

print('Call plugin directly.')
my_plugin = plugin_source.load_plugin('dns')
dns = my_plugin.Dns()
print(dns.create())
