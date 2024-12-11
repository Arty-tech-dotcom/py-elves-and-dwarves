from players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level):
        super().__init__(nickname, musical_instrument)
        self.__bow_level = bow_level

    def get_rating(self):
        return self.__bow_level * 3

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.__bow_level} level"
