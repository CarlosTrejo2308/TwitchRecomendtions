from abc import ABC, abstractmethod


# Abstract Builder class
class APIBuilder(ABC):
    @abstractmethod
    def set_client_id(self, id):
        pass

    @abstractmethod
    def set_oauth_token(self, token):
        pass

    @abstractmethod
    def add_headers(self):
        pass

    @abstractmethod
    def generate_api(self):
        pass


# Product class
class TwitchAPI:
    def __init__(self):
        self.__client_id = ""
        self.__oauth_token = ""
        self.__authorization = ""
        self.__HEADERS = {}

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, id):
        self.__client_id = id

    @property
    def oauth_token(self):
        return self.__oauth_token

    @oauth_token.setter
    def oauth_token(self, token):
        self.__oauth_token = token

    @property
    def authorization(self):
        return self.__authorization

    @authorization.setter
    def authorization(self, authorization):
        self.__authorization = authorization

    @property
    def headers(self):
        return self.__HEADERS

    @headers.setter
    def headers(self, headers):
        self.__HEADERS = headers


# Concrete Builder class
class TwitchAPIBuilder(APIBuilder):
    def __init__(self):
        self.__api = TwitchAPI()

    def set_client_id(self, id):
        self.__api.client_id = id
        return self

    def set_oauth_token(self, token):
        self.__api.oauth_token = token
        return self

    def add_headers(self):
        autorization = 'Bearer ' + self.__api.oauth_token
        self.__api.authorization = autorization
        headers = {
            'client-id': self.__api.client_id,
            'Authorization': self.__api.authorization
        }
        self.__api.headers = headers
        return self

    def generate_api(self):
        return self.__api
