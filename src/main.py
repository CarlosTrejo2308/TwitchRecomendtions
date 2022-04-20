# Main program - User Interface
import load_path
from imp.functional_bolt import FunctionalBolt
from imp.functional_api import FunctionalTwitch
from imp.basedatos import database

working_api = FunctionalTwitch()
db_connection = database()
functional_bolt = FunctionalBolt(working_api, db_connection)


def get_options():
    msg = "\n0. Exit\n"
    msg += "1. Add Channel\n"
    msg += "2. Remove Channel\n"
    msg += "3. Block Channel\n"
    msg += "4. View Channels\n"
    msg += "5. Get Recommendations\n"
    msg += "6. Save Options\n"
    msg += "7. Load Options"
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

    elif comand == 6:
        db_connection.save_list(functional_bolt.ls_channel)

    elif comand == 7:
        functional_bolt.ls_channel = db_connection.get_list()

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
