class Television:
    """
    A class to represent a Television with basic functionalities like power,
    volume control, muting, and channel control.
    """

    # Class variables (constants)
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize the Television instance with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmute the television when it's powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by 1, looping back to the minimum channel if the
        maximum is exceeded, but only if the television is powered on.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by 1, looping back to the maximum channel if the
        minimum is exceeded, but only if the television is powered on.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by 1 if it's below the maximum, unmuting the television
        if it is muted, but only if the television is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1 if it's above the minimum, unmuting the television
        if it is muted, but only if the television is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Provide a string representation of the television's current state.

        Returns:
            str: A string showing the power status, channel, and volume.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else 0}"
