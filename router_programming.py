'''
@author: Hien Le
@group: 55
@id: 2594428
@email: hien.le@student.auc.nl
Assignment 3.1 (Router Programming) - Computer Networks 2018 - Vrije Universiteit Amsterdam
'''

'''
Answers to 3.1 (more detailed/clearly structured answers can be found in the attached pdf file)

1. Looking at this table, I see two rows, corresponding to two routes. As my computer is
connected to the Internet, one of these two routes is the default route, and the other one
represents the Internet interface. Specifically, the default destination 0.0.0.0 with gate-
way 10.0.0.1 defines the packet forwarding rule when no route can be determined for a
given IP destination address, this gateway is the default IP address for my network router.
Meanwhile, the destination 10.0.0.0 with gateway 0.0.0.0, this gateway generally means
”unspecified”, or there is no gateway. So any packets sent to this destination don’t need to
be routed and can be sent directly on the local network.

2. Destination corresponds to Network destination, Gateway corresponds to Gateway,
and Genmask corresponds to Subnet mask.

3. The slash32 part signifies that 32 bits are used by network (i.e. network portion) and is also the
length of the prefix. 145.94.162.184 is the network prefix, this could be obtained by ANDing
the subnet mask with the IP address.
1001001.01011110.10100001.10111000 AND
11111111.11111111.11111111.11111111
= 1001001.0101110.10100001.10111000

'''

def choose_gateway():

    # getting and reading stdin
    first_line = input().split()
    num_rows = int(first_line[0])
    num_dest = int(first_line[1])
    rt_rows = [input() for i in range(num_rows)]
    dest_ips = [input() for i in range(num_dest)]
    for ip in dest_ips:

        # table of all destinations that can be reached with the provided IP address
        reachable_dest = {}
        for row in rt_rows:
            prefix_address = row.split()[0]
            gateway = row.split()[2]
            net_mask = row.split()[1]

            # from here on there's a lot of converting to binary while doing bitwise operation (AND)
            bin_prefix_address = "".join(format(int(num), '08b') for num in prefix_address.split('.'))
            prefix_length = sum([bin(int(n)).count('1') for n in net_mask.split('.')])
            bitwise_AND_result = "".join([format(int(ip.split('.')[i]) & int(net_mask.split('.')[i]), '08b') for i in range(len(ip.split('.')))])
            if bitwise_AND_result[:prefix_length] == bin_prefix_address[:prefix_length]:
                reachable_dest[gateway] = prefix_length

        # in case IP address matches multiple ranges, choose the most exclusive range
        print(max(reachable_dest, key=lambda k: reachable_dest[k]))


choose_gateway()