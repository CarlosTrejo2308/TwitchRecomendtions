class UserIDNotFoundError(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"User-id \"{self.user_id}\" doesn't exist"


class UserNotFoundError(Exception):
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f"Username \"{self.user}\" doesn't exist"


class InvalidInputTypeError(Exception):
    def __init__(self, user_data):
        self.user_data = user_data

    def __str__(self):
        msg = f"The input data must be a string type "
        msg += f"variable, not {type(self.user_data).__name__} type."
        return msg
