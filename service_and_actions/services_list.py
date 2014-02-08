"""This script generates wiki markup to describe the services and actions"""

import inspect

from soco import services
from soco import SoCo

def main():
    soc = SoCo('192.168.0.12')

    # Get a list of service classes
    classes = []
    for item in inspect.getmembers(services):
        if inspect.isclass(item[1]) and issubclass(item[1], services.Service):
            classes.append(item)

    # Generate the table of contents
    print '**Table of contents**\n'
    for cls in classes:
        print '* [Service: {0}](#{0})'.format(cls[0])
        service = cls[1](soc)
        for action, _, _ in service.iter_actions():
            print '  * [Action: {0}](#{0})'.format(action)

    print
    # Generate the description of the services and actions
    for cls in classes:
        print '# {0}\n\n'\
            'The {0} service has the following actions:\n'.format(cls[0])
        service = cls[1](soc)
        for action, in_args, out_args in service.iter_actions():
            print '## {}\n'.format(action)
            print "| **Direction** | **Name**                         | **Type** |"
            print "| ------------- | -------------------------------- | -------- |"
            for arg in in_args:
                print '| input         | {: <32} | {: <8} |'.format(
                    arg[0], arg[1])
            for arg in out_args:
                print '| output        | {: <32} | {: <8} |'.format(
                    arg[0], arg[1])
            print
        print

if __name__ == '__main__':
    main()
