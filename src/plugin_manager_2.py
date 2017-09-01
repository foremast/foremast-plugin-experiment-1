"""This is an example using Pike

Install the necessary package with
$ pip install pike

Currently unable to get it working.

"""

from pike.manager import PikeManager
 
if __name__ == "__main__":


    services = ['dns', 'loadbalancer']
    all_plugins = []
    for service in services:
        path = './foremast/{}'.format(service)
        all_plugins.append(path)

    print(all_plugins)

    with PikeManager(all_plugins) as mgr:
        classes = mgr.get_classes()
        print(classes)
 
        for item in classes:
            obj = item()
            print(obj.create())

