class Television:
    # Class variables (constants)
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        # Toggle the power status
        self.__status = not self.__status

    def mute(self):
        # Mute or unmute the TV only when it's on
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        # Change the channel upward when the TV is on
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        # Change the channel downward when the TV is on
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        # Increase the volume and unmute if muted
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        # Decrease the volume and unmute if muted
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        # Return the string representation of the Television object
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else 0}"
