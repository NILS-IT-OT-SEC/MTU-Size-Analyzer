# MTU Size Analyzer
 Analyzes the MTU Size in PCAP files by running a loop through the packets which are containing an ip address and saving the packet size in a variable. If there is a packet which is bigger than any other packet before then the variable will be overwritten with the new packet size.

 Example use case: Analyzing the MTU size in OT network projects to discover whether jumbo frames are used.

 Usage: Just open the tool and fill in the path to your pcap file. Then press enter. The MTU size of the biggest packet will be shown.

 Dependencies: Python 3, Scapy library for Python.

 Please note that MTU size may be slightly smaller than the shown value due to packet headers. For the most use cases calculating the header does not make so much sense. So I didn't.
 
