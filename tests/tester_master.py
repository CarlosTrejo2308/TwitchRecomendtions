import unittest
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

# from test.main_test import TestMain
# from test.testing_integration import TestIntegration
from test_functional_api import TestTwitchApi
from test_channel import TestChannel
from test_functional_bolt import TestBolt



# Unitarios
# TestMain()
TestChannel()
TestTwitchApi()
TestBolt()


# Int
# TestIntegration()

# A change to trigger build on travis
if __name__ == "__main__":
    unittest.main()
