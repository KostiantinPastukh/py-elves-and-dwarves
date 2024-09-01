from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self.__musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} "
            f"is playing a song on the "
            f"{self.__musical_instrument}"
        )