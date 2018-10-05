from ncclient import manager
import xmltodict
import json
import yaml


with open('inventory.yml') as f:
	inventory = f.read()

inventory_dict = yaml.load(inventory)
#print(json.dumps(inventory_dict,indent=4))

device_list = inventory_dict['CORE']

netconf_template = open('ip_address_template.xml').read()

for device in device_list:
	host = device['host']
	interface_list = device['int_config']

	print('----------------------------------------')
	print(f'Configuring IP Address on {host}')
	print('----------------------------------------')

	#add <config> to the payload
	netconf_payload_list = ['<config>'] 

	for intf in interface_list:
		intf_netconf_payload = netconf_template.format(int_name=intf['interface'],
												int_desc=intf['description'],
												ip_addr=intf['ip_address'],
												subnetmask=intf['subnetmask'],
												int_type=intf['type'])
		print(intf_netconf_payload)
		#add payload for all interface
		netconf_payload_list.append(intf_netconf_payload)

	#add the close </config> to the payload
	netconf_payload_list.append('</config>')

	#join the payload_list
	netconf_payload = ''.join(netconf_payload_list)

	print(netconf_payload)

	#send the payload to the host
	with manager.connect(host=host, port='830',
						username='cisco', password='cisco',
						hostkey_verify=False) as m:

		netconf_reply = m.edit_config(netconf_payload, target='running')
		print(netconf_reply)