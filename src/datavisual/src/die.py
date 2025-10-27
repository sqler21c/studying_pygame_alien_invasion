from random import randint

class Die:
    """주사위 하나를 나타내는 클래서스
    """

    def __init__(self, num_sides=6):
        """6면채 주사위를 초기화합니다."""
        self.num_sides = num_sides

    def roll(self):
        """주사위를 굴립니다."""
        return randint(1, self.num_sides)
