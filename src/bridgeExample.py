from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, percent):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass



class Tv(Device):
    def __init__(self):
        self._on = False
        self._volume = 50
        self._channel = 1

    def is_enabled(self):
        return self._on

    def enable(self):
        self._on = True
        print("TV encendida")

    def disable(self):
        self._on = False
        print("TV apagada")

    def get_volume(self):
        return self._volume

    def set_volume(self, percent):
        self._volume = max(0, min(100, percent))
        print(f"TV volumen ajustado a {self._volume}")

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = max(1, channel)
        print(f"TV canal cambiado a {self._channel}")


class Radio(Device):
    def __init__(self):
        self._on = False
        self._volume = 30
        self._channel = 101

    def is_enabled(self):
        return self._on

    def enable(self):
        self._on = True
        print("Radio encendida")

    def disable(self):
        self._on = False
        print("Radio apagada")

    def get_volume(self):
        return self._volume

    def set_volume(self, percent):
        self._volume = max(0, min(100, percent))
        print(f"Radio volumen ajustado a {self._volume}")

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = channel
        print(f"Radio frecuencia cambiada a {self._channel} MHz")



class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)



if __name__ == "__main__":
    tv = Tv()
    remote_tv = RemoteControl(tv)
    remote_tv.toggle_power()
    remote_tv.volume_up()
    remote_tv.channel_up()

    print("---")

    radio = Radio()
    remote_radio = AdvancedRemoteControl(radio)
    remote_radio.toggle_power()
    remote_radio.volume_up()
    remote_radio.mute()
