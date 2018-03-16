'''
@author: Hien Le
@group: 55
@id: 2594428
@email: hien.le@student.auc.nl
Assignment 3.2 (Distance Vector) - Computer Networks 2018 - Vrije Universiteit Amsterdam
'''

class RoutingTable(object):
    def __init__(self, own_address):
        self.own_address = own_address

    # get and transform elems of routing packets
    @staticmethod
    def read_r_packets(packet):
        packet_lst = packet.split()
        source_address = packet_lst[1]
        K = int(packet_lst[2]) # delay/distance to current machine
        entries_unsplit = packet_lst[4:]
        entries = [entries_unsplit[i] + " " + entries_unsplit[i + 1] for i in range(0, len(entries_unsplit), 2)]
        return source_address, K, entries

    # get destination of data packets
    @staticmethod
    def read_d_packets(packet):
        packet_lst = packet.split()
        dest_address = packet_lst[2]
        return dest_address

    def construct_routing_table(self, vectors):
        # table of vectors has been updated, now compare and add values to routing table
        main_routing_table = {}
        for (line, table) in vectors.items():
            for dest in table:
                if dest == self.own_address:
                    main_routing_table[line] = (table[dest], line)
                elif dest not in main_routing_table:
                    main_routing_table[dest] = (table[dest], line)
                elif table[dest] < main_routing_table[dest][0]:
                    main_routing_table[dest] = (table[dest], line)
        return main_routing_table


def main():
    own_address = input()
    num_packets = int(input())
    packets = [input() for i in range(num_packets)]
    neighbour_vectors = {}
    for packet in packets:
        if packet[0] == 'R':
            print('THANK YOU')
            source_r_address, delay_to_cur, entries = RoutingTable.read_r_packets(packet)
            packet_table = {}
            for entry in entries:
                entry_dest = entry.split()[0]
                entry_delay = int(entry.split()[1])
                if entry_dest == own_address:
                    packet_table[entry_dest] = entry_delay
                else:
                    packet_table[entry_dest] = entry_delay + delay_to_cur
            neighbour_vectors[source_r_address] = packet_table
        rt = RoutingTable(own_address)
        routing_table = rt.construct_routing_table(neighbour_vectors)
        if packet[0] == 'D':
            dest_d_address = RoutingTable.read_d_packets(packet)
            if dest_d_address not in routing_table:
                print('NO ROUTE')
            else:
                route = routing_table[dest_d_address]
                print(route[1] + " " + str(route[0]))


main()