# FABRIC

# Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| FABRIC | l3leaf | borderleaf1-DC1 | 192.168.0.25/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | borderleaf1-DC2 | 192.168.0.35/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | borderleaf2-DC1 | 192.168.0.26/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | borderleaf2-DC2 | 192.168.0.36/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf1-DC1 | 192.168.0.21/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf1-DC2 | 192.168.0.31/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf2-DC1 | 192.168.0.22/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf2-DC2 | 192.168.0.32/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf3-DC1 | 192.168.0.23/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf3-DC2 | 192.168.0.33/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf4-DC1 | 192.168.0.24/24 | cEOS-LAB | Provisioned |
| FABRIC | l3leaf | leaf4-DC2 | 192.168.0.34/24 | cEOS-LAB | Provisioned |
| FABRIC | spine | spine1-DC1 | 192.168.0.11/24 | cEOS-LAB | Provisioned |
| FABRIC | spine | spine1-DC2 | 192.168.0.14/24 | cEOS-LAB | Provisioned |
| FABRIC | spine | spine2-DC1 | 192.168.0.12/24 | cEOS-LAB | Provisioned |
| FABRIC | spine | spine2-DC2 | 192.168.0.15/24 | cEOS-LAB | Provisioned |
| FABRIC | spine | spine3-DC1 | 192.168.0.13/24 | cEOS-LAB | Provisioned |
| FABRIC | spine | spine3-DC2 | 192.168.0.16/24 | cEOS-LAB | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | borderleaf1-DC1 | Ethernet1 | mlag_peer | borderleaf2-DC1 | Ethernet1 |
| l3leaf | borderleaf1-DC1 | Ethernet2 | mlag_peer | borderleaf2-DC1 | Ethernet2 |
| l3leaf | borderleaf1-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet6 |
| l3leaf | borderleaf1-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet6 |
| l3leaf | borderleaf1-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet6 |
| l3leaf | borderleaf1-DC2 | Ethernet1 | mlag_peer | borderleaf2-DC2 | Ethernet1 |
| l3leaf | borderleaf1-DC2 | Ethernet2 | mlag_peer | borderleaf2-DC2 | Ethernet2 |
| l3leaf | borderleaf1-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet6 |
| l3leaf | borderleaf1-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet6 |
| l3leaf | borderleaf1-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet6 |
| l3leaf | borderleaf2-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet7 |
| l3leaf | borderleaf2-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet7 |
| l3leaf | borderleaf2-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet7 |
| l3leaf | borderleaf2-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet7 |
| l3leaf | borderleaf2-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet7 |
| l3leaf | borderleaf2-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet7 |
| l3leaf | leaf1-DC1 | Ethernet1 | mlag_peer | leaf2-DC1 | Ethernet1 |
| l3leaf | leaf1-DC1 | Ethernet2 | mlag_peer | leaf2-DC1 | Ethernet2 |
| l3leaf | leaf1-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet2 |
| l3leaf | leaf1-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet2 |
| l3leaf | leaf1-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet1 | mlag_peer | leaf2-DC2 | Ethernet1 |
| l3leaf | leaf1-DC2 | Ethernet2 | mlag_peer | leaf2-DC2 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet2 |
| l3leaf | leaf2-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet3 |
| l3leaf | leaf2-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet3 |
| l3leaf | leaf2-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet3 |
| l3leaf | leaf2-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet3 |
| l3leaf | leaf2-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet3 |
| l3leaf | leaf2-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet3 |
| l3leaf | leaf3-DC1 | Ethernet1 | mlag_peer | leaf4-DC1 | Ethernet1 |
| l3leaf | leaf3-DC1 | Ethernet2 | mlag_peer | leaf4-DC1 | Ethernet2 |
| l3leaf | leaf3-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet4 |
| l3leaf | leaf3-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet4 |
| l3leaf | leaf3-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet4 |
| l3leaf | leaf3-DC2 | Ethernet1 | mlag_peer | leaf4-DC2 | Ethernet1 |
| l3leaf | leaf3-DC2 | Ethernet2 | mlag_peer | leaf4-DC2 | Ethernet2 |
| l3leaf | leaf3-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet4 |
| l3leaf | leaf3-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet4 |
| l3leaf | leaf3-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet4 |
| l3leaf | leaf4-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet5 |
| l3leaf | leaf4-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet5 |
| l3leaf | leaf4-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet5 |
| l3leaf | leaf4-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet5 |
| l3leaf | leaf4-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet5 |
| l3leaf | leaf4-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet5 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.103.0/24 | 256 | 0 | 0.0 % |
| 192.168.203.0/24 | 256 | 0 | 0.0 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 9 | 3.52 % |
| 192.168.201.0/24 | 256 | 9 | 3.52 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | borderleaf1-DC1 | 192.168.101.5/32 |
| FABRIC | borderleaf1-DC2 | 192.168.201.11/32 |
| FABRIC | borderleaf2-DC1 | 192.168.101.6/32 |
| FABRIC | borderleaf2-DC2 | 192.168.201.12/32 |
| FABRIC | leaf1-DC1 | 192.168.101.1/32 |
| FABRIC | leaf1-DC2 | 192.168.201.7/32 |
| FABRIC | leaf2-DC1 | 192.168.101.2/32 |
| FABRIC | leaf2-DC2 | 192.168.201.8/32 |
| FABRIC | leaf3-DC1 | 192.168.101.3/32 |
| FABRIC | leaf3-DC2 | 192.168.201.9/32 |
| FABRIC | leaf4-DC1 | 192.168.101.4/32 |
| FABRIC | leaf4-DC2 | 192.168.201.10/32 |
| FABRIC | spine1-DC1 | 192.168.101.111/32 |
| FABRIC | spine1-DC2 | 192.168.201.114/32 |
| FABRIC | spine2-DC1 | 192.168.101.112/32 |
| FABRIC | spine2-DC2 | 192.168.201.115/32 |
| FABRIC | spine3-DC1 | 192.168.101.113/32 |
| FABRIC | spine3-DC2 | 192.168.201.116/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 6 | 2.35 % |
| 192.168.202.0/24 | 256 | 6 | 2.35 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | borderleaf1-DC1 | 192.168.102.5/32 |
| FABRIC | borderleaf1-DC2 | 192.168.202.11/32 |
| FABRIC | borderleaf2-DC1 | 192.168.102.5/32 |
| FABRIC | borderleaf2-DC2 | 192.168.202.11/32 |
| FABRIC | leaf1-DC1 | 192.168.102.1/32 |
| FABRIC | leaf1-DC2 | 192.168.202.7/32 |
| FABRIC | leaf2-DC1 | 192.168.102.1/32 |
| FABRIC | leaf2-DC2 | 192.168.202.7/32 |
| FABRIC | leaf3-DC1 | 192.168.102.3/32 |
| FABRIC | leaf3-DC2 | 192.168.202.9/32 |
| FABRIC | leaf4-DC1 | 192.168.102.3/32 |
| FABRIC | leaf4-DC2 | 192.168.202.9/32 |
