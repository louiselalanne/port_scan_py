# Port Scanner using Socket (python)

Port scanning may be defined as a surveillance technique, which is used in order to locate the open ports available on a particular host. Network administrator, penetration tester or a hacker can use this technique. We can configure the port scanner according to our requirements to get maximum information from the target system.

Now, consider the information we can get after running the port scan
- Information about open ports.
- Information about the services running on each port.
- Information about OS and MAC address of the target host.

Port scanning is just like a thief who wants to enter into a house by checking every door and window to see which ones are open. As discussed earlier, TCP/IP protocol suite, use for communication over internet, is made up of two protocols namely TCP and UDP. Both of the protocols have 0 to 65535 ports. As it always advisable to close unnecessary ports of our system hence essentially, there are more than 65000 doors (ports) to lock. These 65535 ports can be divided into the following three ranges −

- System or well-known ports: from 0 to 1023
- User or registered ports: from 1024 to 49151
- Dynamic or private ports: all > 49151

OBS: When we run the above script, it will prompt for the hostname, you can provide any hostname like name of any website but be careful because port scanning can be seen as, or construed as, a crime. We should never execute a port scanner against any website or IP address without explicit, written permission from the owner of the server or computer that you are targeting. Port scanning is akin to going to someone’s house and checking their doors and windows. That is why it is advisable to use port scanner on localhost or your own website (if any).
