# Ad-Hoc AVD Lab

This part of the repo can serve as an ad-hoc lab for AVD. 

Make sure to run the https://github.com/tonybourkesdnpros/ATD-Reset-Level5 reset script before, so the leafs and spines have the default configlets only (BASE and ATD-INFRA)

# Building a Fabric for L5

The process is as follow:

* Build the config with the build_config.yml playbook
* Deploy the config with the deploy_config.yml playbook

Configure host1-DC1 with a 4-port L3 port channel (no switchport) and IP of 10.1.10.11/24. Configure host2-DC2 with a 4-port L3 port channel and IP of 10.1.20.12/24. 

Add a static route on both: 

    host1-DC1> ip route 10.1.20.0/24 10.1.10.1
    host2-DC1> ip route 10.1.10.0/24 10.1.20.1
    
You should be able to point host1-DC1 to host2-DC1. 

Now modify the setup to have DC2. You will need to fill out the DC2.yml directory (use 192.168.20X.0/24 for any IPs). REmember Ids need to be unique and match the management addresses with what's shown in /etc/hosts. 

You will need to modify:
* inventory.yml
* DC2.yml

Build and deploy the new config. Then run the "deploy_DCI.yml" playbook to add the static DCI configs. 
