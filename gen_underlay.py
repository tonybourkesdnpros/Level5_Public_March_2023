import yaml
from termcolor import colored

underlay_file = open('underlay.yml', 'r')


underlay = yaml.safe_load(underlay_file)


for switch in underlay['devices']:
    print(colored("Config", 'red'))
    for iface in underlay['devices'][switch]['interfaces']:
        print("interface", iface)
        print("  ip address", underlay['devices'][switch]['interfaces'][iface])
    print("")