'''
The goal of this assignment is to simulate a MAC protocol under varying workloads. You should implement one
of the following MAC protocols:
• MACA
• CSMA/CA
• 1-persistent CSMA
• non persistent CSMA
• p-persistent CSMA
For the assignment, you simulate an arbitrary number of nodes connected to a single channel.

Initial idea of the simulator:
1. Display list of all stations
2. Display (contention) slots
3. Display which station wants to send frames
4. Display slot allocation
5. Display results/summary

TODO: READ MORE ON WHICH PROTOCOL TO IMPLEMENT AND HOW.
REFERENCE: https://github.com/Thundercats/LAN-MAC-Protocol-Simulator/blob/master/src/lmp/Network.java

'''

import random
import numpy as np

class Station(object):
    """
    Type: node
    """
    def __init__(self):
        self.frames_transmitted = 0
        self.wait_time = 0.0
        self.decision = 'wait'
        self.frame_lst = []

    def poisson(self, param):
        prob = -1 * np.log(random.random()) * param
        return prob

    def send(self, param):
        self.wait_time += self.poisson(param)

    def generate_frame(self, time):
        frame = Frame(self, time)
        return frame

    def add_frame(self, frame):
        self.frame_lst.append(frame)


class Frame(object):
    def __init__(self, station, time):
        self.station = station
        #self.status = ''
        self.contention_interval = time
        self.transmitted_time = 0.0
        self.num_collision = 0

    def get_station(self):
        return self.station

    def get_transmitted_time(self):
        return self.transmitted_time

    def increase_collision(self):
        self.num_collision += 1

    def set_contention_interval(self, interval):
        self.contention_interval = interval

class Channel(object):
    """
    Slotted channel that adheres to a MAC protocol
    """
    NUM_OF_STATIONS = 5
    SLOT_TIME = 4

    def __init__(self, num_slots):
        self.status = '' # idle or not
        self.num_slots = num_slots
        self.frames_transmitted = 0
        self.frames_lst = [] # from 5 stations
        self.num_stations = Channel.NUM_OF_STATIONS
        self.stations = []

    def send_packets(self, param):
        for i in range(self.num_stations):
            station = Station()
            self.stations.append(station)
            station.send(param)

    def simulate(self, param):
        self.send_packets(param)







def simulate():
    ...