MIN_VOLUME = 0
MAX_VOLUME = 2
MIN_CHANNEL = 0
MAX_CHANNEL = 3

class Television:
    def __init__(self):
        self.is_powered = False
        self.channel = 0
        self.volume = 0
        self.is_muted = False

    def power(self):
        self.is_powered = not self.is_powered
        if not self.is_powered:
            self.is_muted = False

    def channel_up(self):
        if self.is_powered:
            self.channel = (self.channel + 1) % (MAX_CHANNEL + 1)

    def channel_down(self):
        if self.is_powered:
            self.channel = (self.channel - 1) % (MAX_CHANNEL + 1)

    def volume_up(self):
        if self.is_powered:
            if self.is_muted:
                self.is_muted = False
                self.volume = self.stored_volume
            if self.volume < MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        if self.is_powered:
            if self.is_muted:
                self.is_muted = False
                self.volume = self.stored_volume
            if self.volume > MIN_VOLUME:
                self.volume -= 1

    def mute(self):
        if self.is_powered:
            if self.is_muted:
                self.is_muted = False
                self.volume = self.stored_volume
            else:
                self.stored_volume = self.volume
                self.volume = 0
                self.is_muted = True

    def __str__(self):
        return f"Power = {'on' if self.is_powered else 'off'}, TV channel = {self.channel},TV Volume =  {self.volume}"





                                          #Almukhtar Alghafri#



