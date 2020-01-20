# Testing networking devices
{id: testing-network}

## Elements
{id: network-test-elements}

* Do some hardware setup, connect some wires
* Access the administrative interface to configure the device
* Configure devices on all sides of our box
* Run test
* Check results



## Network testing
{id: manual-network-testing}


There are many kinds of networking appliances and applications that need testing.

Firewalls will normally need 3 computers - one on each side of the firewall.
One would configure the firewall and then send packets from one side to the
other side. Then check if the packets got through or not.

Routers or switches might need more computers connected to the device under testing.

Proxies can be tested in a way similar to firewalls.





## Hardware setup
{id: hardware-setup}


We cannot yet fully automate this part.





## Access the administrative interface
{id: administrative-interface}

* CLI - Command Line Interface (telnet)
* SNMP
* Web server with web GUI
* Proprietary protocol with a Java Applet loaded from the box
* Proprietary protocol with some locally installed GUI



## CLI testing
{id: manual-cli-testing}


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





## Configure devices on all sides of our box
{id: configure-devices}

* Traffic generators (e.g. SmartBits can be configured using Tcl, 
* Web/ftp/... servers
* Use Telnet/SSH



## Run tests
{id: networking-run-test}

```
```


Still requires the same telnet connection to the various elements in your test setup.




## Check results
{id: networking-check-results}

* Parse log files
* Compute throughput
* Compare files copied




## Expect.pm
{id: networking-expect}
{i: expect}


As we saw earlier Expect.pm with some low level networking protocol can be used to
access any device that can be connected via some cable.

Or without a cable.

But you might not want to implement the whole protocol, or you might not
have a command line tool that can access the device remotely.
Or you don't want to use it as you'd like to test that separately.


You can use the built-in telnet/ssh/ftp/tftp clinets in your Unix/Linux machine.




## Networking
{id: networking-cpan-modules}

* Net::*
* Net::Telnet
* Net::FTP
* Net::SSH::Perl
* Net::SNMP
* SNMP::*
* TFTP
* IO::* low level I/O modules



## Network devices
{id: network-devices}

* Cisco::*
* Net::Telnet::Cisco



## Devices connected to Serial or Parallel port
{id: serial-port-parallel-port}

* Device::*
* Device::SerialPort
* Win32::SerialPort
* Device::Modem
* Device::Gsm
* Device::ParallelPort



## X10 protocol
{id: x10-protocol}

* ControlX10::CM11  (AC power line)
* ControlX10::CM17  Firecracker (RF)






