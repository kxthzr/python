import pytest
from television import Television

def test_init():
    # Initialize the television
    tv = Television()
    # Test default values
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    # Power on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    # Power off
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Muted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Unmuted
    tv.power()  # Turn off the TV
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up():
    tv = Television()
    tv.channel_up()  # TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()  # Turn on the TV
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Wrap-around to min channel
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.channel_down()  # TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()  # Turn on the TV
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Wrap-around to max channel

def test_volume_up():
    tv = Television()
    tv.volume_up()  # TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()  # Turn on the TV
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_up()  # Unmute and increase volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()  # Volume at max
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv = Television()
    tv.volume_down()  # TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()  # Turn on the TV
    tv.volume_up()
    tv.volume_up()  # Set volume to max
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()  # Unmute and decrease volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()  # Volume at min
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
