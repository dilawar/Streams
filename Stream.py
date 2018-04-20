"""Stream.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"


class Stream():

    def __init__(self):
        self.x = 0
        self.mean = 0.0
        self.std = 0.0
        self.N = 0

    def add(self, val):
        self.x = val
        self.N += 1
        self.compute( )

    def compute( self ):
        self.mean = (self.mean*(self.N-1)+self.x)/self.N



