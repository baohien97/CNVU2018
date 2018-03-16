'''
@author: Hien Le
@group: 55
@id: 2594428
@email: hien.le@student.auc.nl
Assignment 2 - Computer Networks 2018 - Vrije Universiteit Amsterdam
'''
# dest = 2 bytes
# source = 2 bytes
# length = 2 bytes
# payload = 0-64 bytes
# checksum = 1 byte

def backward_learning():
    num_ports = int(input())
    num_mess = int(input())
    frame_list = [input() for i in range(num_mess)]
    all_ports = [i for i in range(num_ports)]
    mac_dict = {} # hash table
    for port in all_ports:
        mac_dict[port] = []
    output = []
    for frame in frame_list:
        source_port = int(frame.split()[0])  # port on which frame is received
        source_address = frame.split()[1][4:8]  # address of current machine
        target_address = frame.split()[1][0:4]  # address of target machine
        mac_dict[source_port].append(source_address)
        location_seen = False
        output_frame = ""
        for (key, val) in mac_dict.items():
            if target_address in val:
                location_seen = True
                if key == source_port:
                    output_frame = frame.split()[1]
                else:
                    target_port = str(key)
                    output_frame = frame.split()[1] + " " + target_port
        if location_seen == False: # location unknown => flooding
            output_frame = frame.split()[1] + " " + " ".join(str(i) for i in all_ports if i != source_port)
        output.append(output_frame + "\n")
        #print(output_frame)
    print("".join(frame for frame in output)[:-1])

backward_learning()
