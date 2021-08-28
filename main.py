from core import Core

"""
this tool uses jsonmerger library to merge two json files based on different 
merging schemas.


Microkernel(plugin) architecture is used so that it is possible to add more schemas in the future.
NB: The schemas are availabe during runtime when the plugins are used by the core system

usage:
python main.py 

"""

PLUGINS = [
    'plugins.plugin1',
    'plugins.plugin2',
    'plugins.default',
]

def main():
    core = Core(plugins=PLUGINS)
    core.run()
    

if __name__ == '__main__':
    main()