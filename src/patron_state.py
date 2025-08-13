from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def click_lock(self):
        pass

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_next(self, doubleclick=False):
        pass

    @abstractmethod
    def click_previous(self, doubleclick=False):
        pass


class LockedState(State):
    def click_lock(self):
        if self.player.playing:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self):
        print("[LockedState] Bloqueado. No se puede reproducir.")

    def click_next(self, doubleclick=False):
        print("[LockedState] Bloqueado. No se puede avanzar.")

    def click_previous(self, doubleclick=False):
        print("[LockedState] Bloqueado. No se puede retroceder.")


class ReadyState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self, doubleclick=False):
        self.player.next_song()

    def click_previous(self, doubleclick=False):
        self.player.previous_song()


class PlayingState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    def click_next(self, doubleclick=False):
        if doubleclick:
            self.player.next_song()
        else:
            self.player.fast_forward(5)

    def click_previous(self, doubleclick=False):
        if doubleclick:
            self.player.previous_song()
        else:
            self.player.rewind(5)


class AudioPlayer:
    def __init__(self):
        self.state = ReadyState(self)
        self.playing = False
        self.current_song = "Canción 1"

    def change_state(self, state: State):
        self.state = state
        print(f"[AudioPlayer] Estado cambiado a: {state.__class__.__name__}")

    def click_lock(self):
        self.state.click_lock()

    def click_play(self):
        self.state.click_play()

    def click_next(self, doubleclick=False):
        self.state.click_next(doubleclick)

    def click_previous(self, doubleclick=False):
        self.state.click_previous(doubleclick)

    def start_playback(self):
        self.playing = True
        print(f"[AudioPlayer] Reproduciendo {self.current_song}")

    def stop_playback(self):
        self.playing = False
        print("[AudioPlayer] Reproducción detenida")

    def next_song(self):
        self.current_song = "Siguiente canción"
        print(f"[AudioPlayer] Reproduciendo {self.current_song}")

    def previous_song(self):
        self.current_song = "Canción anterior"
        print(f"[AudioPlayer] Reproduciendo {self.current_song}")

    def fast_forward(self, time):
        print(f"[AudioPlayer] Avanzando {time} segundos...")

    def rewind(self, time):
        print(f"[AudioPlayer] Retrocediendo {time} segundos...")


if __name__ == "__main__":
    player = AudioPlayer()

    player.click_play()
    player.click_next()
    player.click_next(doubleclick=True)
    player.click_lock()
    player.click_play()
    player.click_lock()
    player.click_play()