# CLI testing

Here you have a device like a router, or some other box connected to the network.
Normally you would telnet to it and then interactively test the various commands to see
if they work. In addition you might be able to fetch the raw configuration information
where you can validate if the configuration values were written correctly.




Going even further after you configured the device somehow you can test it if the new
behavior of the device really can be observed: You connect other devices and ping this
box or try to send packets and see if they get to the correct location.



* Telnet to device
* Use SNMP to monitor/configure the device
* Prepare external entities on 2 or more sides of the device
* Send packets
* Check if the packets were received correctly
