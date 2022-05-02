from src.imp.base.api import TwitchAPIBuilder
from src.imp.exceptions import UserIDNotFoundError
from src.imp.exceptions import UserNotFoundError
from src.imp.exceptions import InvalidInputTypeError
from sre_compile import isstring
import requests


class FunctionalTwitch:
    def __init__(self):
        __api = TwitchAPIBuilder()
        __api.set_client_id("0yb8krhzd429df6ovknk5ax54cv4oj")
        __api.set_oauth_token("d6z0n30q8kkgokv96dn6jsjxj55xzi")
        __api.add_headers()
        self._twitch_api = __api.generate_api()

    def __check_username(self, request, username):
        if not isstring(username):
            raise InvalidInputTypeError(username)

        check_status_code = (request.status_code == 400)
        if check_status_code:
            raise UserNotFoundError(username)

        is_list_empty = request.json()["data"]
        if not is_list_empty:
            raise UserNotFoundError(username)

    def get_user_id(self, username):
        URL = f"https://api.twitch.tv/helix/users?login={username}"
        request = requests.get(url=URL, headers=self._twitch_api.headers)
        self.__check_username(request, username)
        user_data = request.json()['data']
        user_id = user_data[0]['id']
        return user_id

    def __check_user_id(self, request, user_id):
        if not isstring(user_id):
            raise InvalidInputTypeError(user_id)

        check_status_code = (request.status_code == 400)
        if check_status_code:
            raise UserIDNotFoundError(user_id)

        is_list_empty = request.json()["data"]
        if not is_list_empty:
            raise UserIDNotFoundError(user_id)

    def get_username(self, user_id):
        URL = f"https://api.twitch.tv/helix/users?id={user_id}"
        request = requests.get(url=URL, headers=self._twitch_api.headers)
        self.__check_user_id(request, user_id)
        user_data = request.json()['data']
        user_id = user_data[0]['login']
        return user_id

    def get_total_followers(self, username):
        user_id = self.get_user_id(username)
        URL = f'https://api.twitch.tv/helix/users/follows?to_id={user_id}'
        request = requests.get(url=URL, headers=self._twitch_api.headers)
        user_data = request.json()
        total_followers = user_data['total']
        return total_followers

    def get_total_following(self, username):
        user_id = self.get_user_id(username)
        URL = f'https://api.twitch.tv/helix/users/follows?from_id={user_id}'
        request = requests.get(url=URL, headers=self._twitch_api.headers)
        user_data = request.json()
        total_followings = user_data['total']
        return total_followings

    def get_following_names(self, username, first_names=3):
        user_id = self.get_user_id(username)
        # URL = f'https://api.twitch.tv/helix/users/follows?from_id={user_id}'
        query = f'follows?from_id={user_id}&first={first_names}'
        URL = f'https://api.twitch.tv/helix/users/' + query
        request = requests.get(url=URL, headers=self._twitch_api.headers)
        followers_data = request.json()['data']
        followers_user = []

        for follower in followers_data:
            follower_user = follower["to_name"]
            followers_user.append(follower_user)

        return followers_user
