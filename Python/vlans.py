#!/usr/bin/python3

import pyeapi

connect = pyeapi.connect_to('leaf1-DC1')

file = open('vlans.list', 'r')

vlan_list = file.readlines()

for vlan_id in vlan_list:
    result = connect.api("vlans").create(vlan_id)
    if result == True:
        print("Successfully added VLAN!", vlan_id)
    else:
        print("some type of error occured with", vlan_id)