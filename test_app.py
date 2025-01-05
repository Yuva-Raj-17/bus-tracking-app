# test_app.py

import unittest
from app import get_bus_details

class TestBusTracking(unittest.TestCase):
    def test_get_bus_details(self):
        # Test existing bus
        self.assertEqual(get_bus_details("101"), {"route": "Main Street", "location": "Downtown", "status": "On time"})
        
        # Test non-existing bus
        self.assertEqual(get_bus_details("999"), "Bus ID not found.")
        
if __name__ == "__main__":
    unittest.main()
