class GameStats:
    """게임의 통계 정보를 저장하는 클래스"""
    def __init__(self, ai_game):
        """게임이 시작될 때 통계 정보를 초기화"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """게임 도중에 변경되는 통계 정보를 초기화"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
