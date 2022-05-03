from src.imp.functional_api import FunctionalTwitch
import requests

from unittest.mock import patch
import unittest


class TestTwitchApi(unittest.TestCase):
    def setUp(self):
        self.functional_api = FunctionalTwitch()
        self.functional_headers = self.functional_api._twitch_api.headers

    @patch.object(requests, "get")
    def test_get_user_id(self, mock_requests_get):
        test_cases = {
            "ibai": "232866",
            "auronplay": "459331509",
            "fernanfloo": "197855687",
            "juansguarnizo": "121510236",
            "elded": "76385901"
        }

        for username, expected_user_id in test_cases.items():
            URL = f"https://api.twitch.tv/helix/users?login={username}"
            json_return = {"data": [{"id": expected_user_id}]}
            # Mocking .get(), changing the return value of .get().json()
            mock_requests_get.return_value.json.return_value = json_return
            user_id = self.functional_api.get_user_id(username)

            # Test Assertions
            with self.subTest(expected_user_id=expected_user_id):
                self.assertEqual(user_id, expected_user_id)

            mock_requests_get.assert_called_once_with(
                url=URL,
                headers=self.functional_headers)
            mock_requests_get.return_value.json.assert_called()
            mock_requests_get.reset_mock()

    @patch.object(requests, "get")
    def test_get_username(self, mock_requests_get):
        test_cases = {
            "ibai": "83232866",
            "auronplay": "459331509",
            "fernanfloo": "197855687",
            "juansguarnizo": "121510236",
            "elded": "76385901"
        }

        for expected_username, user_id in test_cases.items():
            URL = f"https://api.twitch.tv/helix/users?id={user_id}"
            # Mocking .get(), changing the return value of .get().json()
            json_return = {"data": [{"login": expected_username}]}
            mock_requests_get.return_value.json.return_value = json_return
            username = self.functional_api.get_username(user_id)

            # Test Assertions
            with self.subTest(expected_username=expected_username):
                self.assertEqual(username, expected_username)

            mock_requests_get.assert_called_once_with(
                url=URL,
                headers=self.functional_headers)
            mock_requests_get.return_value.json.assert_called()
            mock_requests_get.reset_mock()

    @patch.object(requests, "get")
    @patch.object(FunctionalTwitch, "get_user_id")
    def test_get_total_followers(self,
                                 mock_get_user_id,
                                 mock_requests_get):
        # ~ Date: 04/10/2022, Time: 01:34 AM ~
        test_cases = {
            "ibai": "9841415",
            "auronplay": "12330451",
            "fernanfloo": "2716858",
            "juansguarnizo": "7698178",
            "elded": "4984070"
        }

        for username, expected_total in test_cases.items():
            json_return = {"total": expected_total}
            mock_get_user_id.return_value = username
            mock_requests_get.return_value.json.return_value = json_return

            total_followers = self.functional_api.get_total_followers(username)
            user_id = self.functional_api.get_user_id(username)
            URL = f'https://api.twitch.tv/helix/users/follows?to_id={user_id}'

            # Test Assertions
            with self.subTest(expected_total=expected_total):
                self.assertEqual(total_followers, expected_total)

            mock_get_user_id.assert_called_with(username)
            mock_requests_get.assert_called_once_with(
                url=URL,
                headers=self.functional_headers)
            mock_requests_get.return_value.json.assert_called()

            mock_get_user_id.reset_mock()
            mock_requests_get.reset_mock()

    @patch.object(requests, "get")
    @patch.object(FunctionalTwitch, "get_user_id")
    def test_get_total_following(self,
                                 mock_get_user_id,
                                 mock_requests_get):
        # ~ Date: 04/11/2022, Time: 04:43 PM ~
        test_cases = {
            "ibai": "165",
            "auronplay": "50",
            "fernanfloo": "56",
            "juansguarnizo": "348",
            "elded": "446"
        }

        for username, expected_total in test_cases.items():
            json_return = {"total": expected_total}
            mock_get_user_id.return_value = username
            mock_requests_get.return_value.json.return_value = json_return

            total_followings = self.functional_api.get_total_following(
                username)
            user_id = self.functional_api.get_user_id(username)
            URL = f'https://api.twitch.tv/helix/users/follows?from_id={user_id}'

            # Test Assertions
            with self.subTest(expected_total=expected_total):
                self.assertEqual(total_followings, expected_total)

            mock_get_user_id.assert_called_with(username)
            mock_requests_get.assert_called_once_with(
                url=URL,
                headers=self.functional_headers)
            mock_requests_get.return_value.json.assert_called()

            mock_get_user_id.reset_mock()
            mock_requests_get.reset_mock()

    @patch.object(requests, "get")
    @patch.object(FunctionalTwitch, "get_user_id")
    def test_get_following_names(self,
                                 mock_get_user_id,
                                 mock_requests_get):
        # ~ Date: 04/11/2022, Time: 08:13 PM ~
        test_cases = {
            "ibai": ["rivers_gg", "Koldo_lol", "Rickyexp"],
            "auronplay": ["xCry", "ernesBarbeQ", "ElSpreen"],
            "fernanfloo": ["heyobii", "auronplay", "ZilverK"],
            "juansguarnizo": ["facubanzas", "Carreraaa", "Rickyexp"],
            "elded": ["eLaLiga", "MrFerruzca", "Kamet0"]
        }

        for username, expected_names in test_cases.items():
            json_data_return = [dict(to_name=name) for name in expected_names]
            json_return = {"data": json_data_return}
            mock_requests_get.return_value.json.return_value = json_return

            following_names = self.functional_api.get_following_names(username)
            user_id = self.functional_api.get_user_id(username)
            query = f'follows?from_id={user_id}&first=3'
            URL = f'https://api.twitch.tv/helix/users/' + query

            # Test Assertions
            with self.subTest(expected_names=expected_names):
                self.assertEqual(following_names, expected_names)

            mock_get_user_id.assert_called_with(username)
            mock_requests_get.assert_called_once_with(
                url=URL,
                headers=self.functional_headers)
            mock_requests_get.return_value.json.assert_called()

            mock_get_user_id.reset_mock()
            mock_requests_get.reset_mock()

    def tearDown(self):
        del self.functional_api
        del self.functional_headers


# if __name__ == "__main__":
    # unittest.main()
