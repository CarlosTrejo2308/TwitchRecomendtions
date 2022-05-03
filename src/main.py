# Main program - User Interface
import load_path
from imp.functional_bolt import FunctionalBolt
from imp.functional_api import FunctionalTwitch

working_api = FunctionalTwitch()
functional_bolt = FunctionalBolt(working_api)


def get_options():
    msg = "\n0. Exit\n"
    msg += "1. Add Channel\n"
    msg += "2. Remove Channel\n"
    msg += "3. Block Channel\n"
    msg += "4. View Channels\n"
    msg += "5. Get Recommendations\n"
    return msg


def channel_input():
    print("\nEnter the channel name:")
    option = input(">> ")
    return option


def get_channel():
    print("Enter the channel name: ")
    channel = input(">> ")
    try:
        channel = working_api.get_user_id(channel)
    except:
        print("!! Hay un problema con este canal, o no hay internet")
        channel = None

    return channel


def do_action(comand):
    if comand == 0:
        print("Goodbye!")
        return -1

    elif comand == 1:
        channel = channel_input()
        functional_bolt.add_channel(channel)

    elif comand == 2:
        channel = channel_input()
        functional_bolt.remove_channel(channel)

    elif comand == 3:
        channel = channel_input()
        functional_bolt.block_channel(channel)

    elif comand == 4:
        functional_bolt.show_channels()

    elif comand == 5:
        functional_bolt.show_recommendations()

    else:
        print("Out of Bounds!\n")


def main():
    while(True):
        print(get_options())

        try:
            option = int(input(">> "))
            do_action(option)
        except:
            print("Please only numbers!")


if __name__ == '__main__':
    main()
