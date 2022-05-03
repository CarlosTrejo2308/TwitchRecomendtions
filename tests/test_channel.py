from src.imp.channel import Channel
import unittest


class TestChannel(unittest.TestCase):

    # Create channels to test
    def setUp(self):
        self.test_cases = [
            (Channel(id="83232866", name="ibai", priority=120),
             {"user_id": "83232866", "username": "ibai", "priority": 120}),
            (Channel(id="459331509", name="auronplay"),
             {"user_id": "459331509", "username": "auronplay", "priority": 0}),
            (Channel(id="197855687"),
             {"user_id": "197855687", "username": "", "priority": 0}),
            (Channel(id="121510236", name="juansguarnizo", priority=90),
             {"user_id": "121510236", "username": "juansguarnizo", "priority": 90}),
            (Channel(id="76385901", priority=85),
             {"user_id": "76385901", "username": "", "priority": 85}),
        ]

    def test_create_channel(self):
        for test_case in self.test_cases:
            channel, parameters = test_case
            user_id_expected = parameters["user_id"]
            username_expected = parameters["username"]
            priority_expected = parameters["priority"]

            user_id = channel._id
            username = channel._name
            priority = channel._priority

            with self.subTest("The user_id obtained wasn't the expected one",
                              user_id_expected=user_id_expected):
                self.assertEqual(user_id, user_id_expected)

            with self.subTest("The username obtained wasn't the expected one",
                              username_expected=username_expected):
                self.assertEqual(username, username_expected)

            with self.subTest("The user priority obtained wasn't the expected one",
                              priority_expected=priority_expected):
                self.assertEqual(priority, priority_expected)

            with self.subTest("The _is_blocked boolean wasn't the expected one",
                              _is_blocked=channel._is_blocked):
                self.assertFalse(channel._is_blocked)

    def test_increase_priority(self):
        adders = [24, 22, 17, 10, 25]

        for test_case, adder in zip(self.test_cases, adders):
            channel, parameters = test_case
            priority_expected = parameters["priority"]
            priority_expected += adder

            priority = channel._priority
            priority += adder

            with self.subTest("The priority of the user wasn't increased appropriately",
                              priority_expected=priority_expected):
                self.assertEqual(priority, priority_expected)

    def test_reset_priority(self):
        for test_case in self.test_cases:
            channel, _ = test_case
            channel.reset_priority()
            priority_expected = 0
            priority = channel._priority

            with self.subTest("The priority of the user wasn't resetted appropriately",
                              priority_expected=priority_expected):
                self.assertEqual(priority, priority_expected)

    def test_blocked(self):
        blockeds = [True, False, True, False, False]

        for test_case, blocked in zip(self.test_cases, blockeds):
            channel, parameters = test_case
            channel.block(blocked)

            blocked_expected = blocked
            is_blocked = channel._is_blocked
            priority = channel._priority

            if is_blocked:
                priority_expected = 0
            else:
                priority_expected = parameters["priority"]

            with self.subTest("The user wasn't blocked appropriately"):
                self.assertEqual(is_blocked, blocked_expected)

            with self.subTest("The priority of the user wasn't resetted appropriately",
                              priority_expected=priority_expected):
                self.assertEqual(priority, priority_expected)

            extra_priority = 10
            channel.increase_priority(extra_priority)
            priority = channel._priority

            if is_blocked:
                priority_expected = 0
            else:
                priority_expected = parameters["priority"] + extra_priority

            with self.subTest("The priority assigned to the user is not correct",
                              priority_expected=priority_expected):
                self.assertEqual(priority, priority_expected)

    def tearDown(self):
        del self.test_cases


# if __name__ == '__main__':
#     unittest.main()
