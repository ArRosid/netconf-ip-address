# netconf-ip-address
Configure IP Address Automatically on IOS XE using Python &amp; Netconf

This repository contains script to configure IP Address on Cisco IOS XE automatically using Python and Netconf. We use ncclient python library in this script.

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
	<li>This script supported on IOS XE</li>
</ul>

<h3>How To Use</h3>
<ul>
	<li>Install the requirements library</li>
	<li>Configure IP Address Management in the routers</li>
	<li>Activate netconf and yang in the routers using the command <i>netconf ssh</i> and <i>netconf-yang</i></li>
	<li>Edit the inventory.yml to meet your topology</li>
	<li>Run the script using command <i>python3 configure_ip_address.py</i></li>
</ul>
