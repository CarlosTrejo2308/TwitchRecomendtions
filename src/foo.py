import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

from imp.functional_bolt import FunctionalBolt
from imp.functional_api import FunctionalTwitch

api_functional = FunctionalTwitch()
bolt = FunctionalBolt(api_functional, "database")

# Channels that I follow
# bolt.add_channel("ibai!@#!@")
# bolt.add_channel("auronplay")
# bolt.add_channel("fernanfloo")
# bolt.add_channel("elded")

# bolt.remove_channel("auronplay")
# bolt.block_channel("fernanfloo")

# bolt.calculate()
# bolt.show_recommendations()

# print(api_functional.get_user_id("CyPSTestTwitchAPI"))
# print(api_functional.get_total_followers("CyPSTestTwitchAPI"))
# print(api_functional.get_total_following("CyPSTestTwitchAPI"))
