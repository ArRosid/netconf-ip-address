from ncclient import manager
import xmltodict
import json
import yaml

IETF_INTERFACE_TYPES = {
        "loopback": "ianaift:softwareLoopback",
        "ethernet": "ianaift:ethernetCsmacd"
    }

with open('inventory.yml') as f:
	inventory = f.read()

inventory_dict = yaml.load(inventory)
print(json.dumps(inventory_dict,indent=4))
'''
netconf_template = open('ip_address_template.xml').read()


netconf_payload = netconf_template.format(int_name='Loopback0',
										int_desc='Loopback Address',
										ip_addr='172.16.255.1',
										subnetmask='255.255.255.255',
										int_type=IETF_INTERFACE_TYPES['loopback'])

print("Configuration Payload: ")
print('-----------------------')
print(netconf_payload)

with manager.connect(host='192.168.122.10', port='830',
					username='cisco', password='cisco',
					hostkey_verify=False) as m:

	netconf_reply = m.edit_config(netconf_payload, target='running')

	print(netconf_reply)
'''