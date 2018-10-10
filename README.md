# netconf-ip-address
Configure IP Address Automatically on IOS XE devices using Python &amp; NETCONF

This repository contains scripts to configure IP Address on Cisco IOS XE devices automatically using Python and NETCONF. We use the ncclient python library in this script.

<h3>Requirements</h3>
<ul>
	<li>ncclient 0.6.3+</li>
	<li>Python 2.7 or Python 3.4+</li>
	<li>setuptools 0.6+</li>
	<li>Paramiko 1.7+</li>
	<li>lxml 3.3.0+</li>
	<li>libxml2</li>
	<li>libxslt</li>
</ul>

<h3>Supported Devices</h3>
<ul>
	<li>This script tested with Cisco IOS XE devices</li>
</ul>

<h3>How To Use</h3>
<ul>
	<li>Install the libraries listed in the requirements</li>
	<li>Configure IP Address Management in the router</li>
	<li>Activate NETCONF and YANG in the router using the commands <i>netconf ssh</i> and <i>netconf-yang</i></li>
	<li>Edit the inventory.yml to meet your topology</li>
	<li>Run the script using the command <i>python3 configure_ip_address.py</i></li>
</ul>
