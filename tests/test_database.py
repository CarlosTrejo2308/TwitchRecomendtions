from abs.absDataBase import AbstactClassDB


class mockBD(AbstactClassDB):
    def __init__(self, conection):
        super().__init__()
        self.conection = conection
        self.list_of_channels = []

    def save_list(self, lschannels):
        self.list_of_channels = lschannels

    def get_list(self):
        return self.list_of_channels


if __name__ == '__main__':
    lo = mockBD("conection")
