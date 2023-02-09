ITON - RSWE - ENSA => This is the content for CCNA -> if you finisht he course and still want to do it, email tony and he an get it sorted

Cyberops next sem aswell, helps with this.


in an IP -> 192.168.1.255

192 = network address
255 = Host address (255 FFFF (or all 1's on binary)) is the broadcast adress
0 = network adress - 255 = broadcast adress, in IP's you can't use these as they're already in  use.


OSI layers:

APSTNDP

7 Application - Data
6 Presentation - Data
5 Session - Data
4 Transport - port 80 HTTP (webtraffic) - 443 HTTPS - Segments (this is the traffic name)
3 Network - Router - Uses IP addresses - data moving around here are called packets
2 Data-Link - Switch - Mac adress - Frames collisions - NIC (Netword Interface Card)
1 Physical- bits ( the 1's and 0's ) - NIC (Netword Interface Card) <- turns 1's and 0's into a format that can be read
(like what goes through the internet cables, eletrical pulses, whereas wifi would be radio signals)



programmers, do not throw sausage pizza away
https://lms.netacad.com/course/view.php?id=1778923



IP Adressing -> 3 classes

A: 1- 126  N - H - H - H / 8 (the 8 is the subnet mask and determines the size of the network.) 255.0.0.0 (the first 8 bits are 1's')

B: 128 - 191 n - n - h - h / 16 (first 16's are the subnet mask determining the size of the network.) 255.255.0.0

C: 192 - 223    192.168.10.1 - n - n - n - h /24 ''

CIDR -> classless method
Classless inter-domain routing

private IPs: 10.x.x.x (class A)

172-16 -> 172-31 . x . x (class B)

192.168.x.x (class C)


SMB -> Server message block

MAC address = Media Access Control


For assessment - Protocols on OSI model a few bullet points
- > find the answers at the ciriculum search bar (the cisco power points spot) (for example physical layer is 4.1)
Most of the answers will be on cisco for the assessment (part 2)

Q3: TCP / IP reference model

binary and hexadecimal explanation -> few sentences
Show the working out for each conversion
    (do the 8/4/2/1 + 8/4/2/1)
https://contenthub.netacad.com/itn-dl/5.2.2
/\ video exapling it all.

With the hexadecimal conversion A) you use 2 sets of 8 so your max number would be 32768 -> 1
    you split each piece into 4 bits for the above, so instead of 16 or 2 8's you do the 4 bits of 1/2/4/8

https://contenthub.netacad.com/itn-dl/12.2.1

SMB + FTP

Server message block - a form of transfering information - 139 445 ports used
File transfer protocol -> 21 - 20 (ports used)) - 20 is the actual data (come second) 21 sets up the "highway" for data.

example given for client - server model ->
your student ID is your unique ID and you can log in at the gold coast campus and the brisbane campus
It uses the password and student id to connect to the server from the client spot (the pc you're using)

DHCP -> IP address (68, 67 port)
DNS -> Searching the net (53 port)
http -> port 80
https -> port 443
You would use all of these on the pc however these sources aren't stored on this pc rather the server they connect to.

Peer to peer you could share a document and not know who has the most up to date
client to server you would have an update of a read only doc for others however it is always up to date



smd:
= start authenticate and terminate session.
control file and printer access.
allow an aplication to send or recieve messages to or from another device.

14.1.5
UDP -> User Datagram Protocol
IP -> Internet protocol
both of these don't care if someone is listening they will send it to the spot.
they're known as connectionless

packet tacer - router command lines

enable confit t int fa0/0 ip address 192.168.1.1 255.255.255.0 no shutdown

en - config t - int s0/0/0 - ip add - 192.168.5.1 255.255.255.252

you use the 255.255.255.252 when using the /30 subnet mask.
the /30 makes it a very small network


Route acrynom and symbol

RIP -> R -> trust worthiness [120/1] -> the lower the first number the btter, means more secure.
OSPF -> O -> 110/1
EIGRP -> D -> 90/1
Static -> ? -> 1/1 (super secure)

when there's a routing protocol (R) you are sharing information to other routers.

tracert ipaddresshere -> will show the connection route to said IP in the cmd
tracert 192.168.1.0

sh ip command -> check rip
