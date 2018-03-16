'''
The goal of this assignment is to simulate a MAC protocol under varying workloads. You should implement one
of the following MAC protocols:
• MACA
• CSMA/CA
• 1-persistent CSMA
• non persistent CSMA
• p-persistent CSMA
For the assignment, you simulate an arbitrary number of nodes connected to a single channel.
'''


class MACA(object):
    def __init__(self, nodes, link):
        self.nodes = nodes
        self.link = link

    