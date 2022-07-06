import unittest
#importing file database.py to fetch values 
import database as d 
from datetime import datetime

class TestInstance(unittest.TestCase):
    def test_class1(self):
        val = d.values # copying data values
        message = "Error"
        self.assertEqual(type(val[0]),datetime,message) #testing whether Date_Time is of type datetime
        self.assertEqual(type(val[1]),float,message)    #testing whether Close is of type float
        self.assertEqual(type(val[2]),float,message)
        self.assertEqual(type(val[3]),float,message)
        self.assertEqual(type(val[4]),float,message)
        self.assertEqual(type(val[5]),float,message)
        self.assertEqual(type(val[6]),str,message)      #testing whether Instrument is of type str
    


if __name__=='__main__':
    unittest.main()