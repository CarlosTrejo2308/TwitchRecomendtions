from src.imp.base.bolt import APIBolt
from src.imp.channel import Channel

from src.imp.exceptions import UserNotFoundError
from tqdm import tqdm


class FunctionalBolt(APIBolt):
    def __init__(self, api):
        self._api = api
        self._recommended = {}
        self._channels = {}

    def add_channel(self, username):
        try:
            user_id = self._api.get_user_id(username)
            if username not in self._channels.keys():
                channel = Channel(user_id, username)
                self._channels[username] = channel
                msg = f"++ channel {username} was added successfully."
            else:
                msg = f">> channel {username} is already in the channel list."

            print(msg)
        except UserNotFoundError:
            print(f"!! There's no possible to add an nonexistent channel")

    def remove_channel(self, username):
        if username in self._channels.keys():
            del self._channels[username]
            msg = f"-- channel {username} was removed successfully."
        else:
            msg = f"!! channel {username} wasn't found in the channel list!"

        print(msg)
        # except:
        #     print("Oh no!, Something went wrong while trying to remove the channel")

    def block_channel(self, user_name):
        if user_name in self._channels.keys():
            self._channels[user_name].block(True)
            msg = f"++ channel {user_name} was blocked successfully."
        else:
            msg = f"!! channel {user_name} wasn't found in the channel list!"

        print(msg)
        # except:
        #     print("Oh no!, Something went wrong while trying to block the channel")

    def show_recommendations(self):
        self.generate_recommendations()

        print("Recommendations:")
        channels_sorted = sorted(self._recommended.values(),
                                 key=lambda x: x._priority, reverse=True)
        for channel in channels_sorted:
            print(f"-> channel {channel._name}, priority: {channel._priority}")

################################################################################

    def show_channels(self):
        for channel in self._channels.values():
            print(channel)

    def __add_to_recommendations(self, username, priority):
        subchannel_id = self._api.get_user_id(username)
        subchannel = Channel(subchannel_id, username, priority)

        is_followed = username in self._channels.keys()
        is_recommended = username in self._recommended.keys()

        if is_recommended:
            self._recommended[username].increase_priority(priority)

        if (not is_followed) and (not is_recommended):
            self._recommended[username] = subchannel

    def generate_recommendations(self):
        for channel in tqdm(self._channels.values(), colour="green"):
            if channel._is_blocked == True:
                continue

            total_followers = self._api.get_total_followers(channel._name)
            total_followings = self._api.get_total_following(channel._name)
            channel_priority = total_followers / total_followings

            subchannels_names = self._api.get_following_names(channel._name)

            # print(f"\nFrom channel: {channel._name}")
            # print(f"With total followers: {total_followers}")
            # print(f"With total followings: {total_followings}")
            # print(f"Channel priority: {channel_priority}")
            for subchannel_name in subchannels_names:
                # print(f"- add subchannel: {subchannel_name}")

                self.__add_to_recommendations(
                    subchannel_name, channel_priority)
            # print()
