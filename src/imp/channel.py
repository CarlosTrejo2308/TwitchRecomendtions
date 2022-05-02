class Channel:
    def __init__(self, id, name="", priority=0):
        self._id = id
        self._name = name
        self._priority = priority
        self._is_blocked = False

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def is_blocked(self):
        return self._is_blocked

    def increase_priority(self, num):
        if not self._is_blocked:
            self._priority += num

    def reset_priority(self):
        self._priority = 0

    def block(self, blocked):
        self._is_blocked = blocked
        if self._is_blocked:
            self.reset_priority()

    def __str__(self):
        msg = f"\nid: {self._id}"
        msg += f"\nname: {self._name}"
        msg += f"\npriority: {self._priority}"
        msg += f"\nblocked: {self._is_blocked}"
        return msg
