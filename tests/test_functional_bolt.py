from matplotlib import testing
import load_path
from src.imp.functional_api import FunctionalTwitch
from src.imp.functional_bolt import FunctionalBolt
from src.imp.channel import Channel

import unittest
from unittest.mock import patch


class TestBolt(unittest.TestCase):

    def setUp(self):
        functional_api = FunctionalTwitch()
        self.testing_bolt = FunctionalBolt(functional_api)

    @patch("builtins.print")
    @patch.object(FunctionalTwitch, "get_user_id")
    def test_add_channel(self, mock_get_user_id, mock_print):
        test_cases = [
            Channel("83232866", "ibai"),
            Channel("459331509", "auronplay"),
            Channel("197855687", "fernanfloo"),
            Channel("121510236", "juansguarnizo"),
            Channel("76385901", "elded"),
        ]

        for expected_channel in test_cases:
            expected_name = expected_channel.name
            expected_user_id = expected_channel.id
            mock_get_user_id.return_value = expected_user_id

            self.testing_bolt.add_channel(expected_name)
            channel = self.testing_bolt._channels[expected_name]

            with self.subTest(expected_user_id=expected_user_id):
                self.assertEqual(channel._id, expected_user_id)

            with self.subTest(expected_name=expected_name):
                self.assertEqual(channel._name, expected_name)

            mock_get_user_id.assert_called_once_with(expected_name)
            mock_get_user_id.reset_mock()

    @patch("builtins.print")
    def test_remove_channel(self, mock_print):
        self.testing_bolt.add_channel("ibai")
        self.testing_bolt.add_channel("auronplay")
        self.testing_bolt.add_channel("fernanfloo")
        self.testing_bolt.add_channel("elded")

        test_cases = [
            "ibai",
            "fernanfloo",
            "ibai",
            "auronplay"
        ]

        for username in test_cases:
            if username in self.testing_bolt._channels.keys():
                msg = f"-- channel {username} was removed successfully."
            else:
                msg = f"!! channel {username} wasn't found in the channel list!"

            self.testing_bolt.remove_channel(username)
            with self.subTest(expected_msg=msg):
                mock_print.assert_called_with(msg)

            self.assertNotIn(username, self.testing_bolt._channels.keys())

    @patch("builtins.print")
    def test_block_channel(self, mock_print):
        self.testing_bolt.add_channel("auronplay")
        self.testing_bolt.add_channel("juansguarnizo")
        self.testing_bolt.add_channel("elded")

        self.testing_bolt.block_channel("juansguarnizo")
        self.testing_bolt.block_channel("elded")

        test_cases = [
            ("auronplay", False),
            ("juansguarnizo", True),
            ("elded", True),
        ]

        for username, block_expected in test_cases:
            is_blocked = self.testing_bolt._channels[username].is_blocked

            with self.subTest(block_expected=block_expected):
                self.assertEqual(is_blocked, block_expected)


# if __name__ == '__main__':
#     unittest.main()
