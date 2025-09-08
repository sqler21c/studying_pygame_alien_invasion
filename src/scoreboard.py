import pygame.font

class Scoreboard:
    """점수를 기록할 클래스
    """

    def __init__(self, ai_game):
        """점수 기록에 필요한 속성 초기하

        Args:
            ai_game (_type_): 실행중인 현재 클래스
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 점수 정보에 쓸 폰트 설정
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 초기 점수 이미지 
        self.prep_score()

    def prep_score(self):
        """점수를 이미지로 렌더링
        """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, 
                                            True, 
                                            self.text_color, 
                                            self.settings.bg_color)
        #화면 우측 상단에 점수 표시
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """점수를 화면에 그린다
        """
        self.screen.blit(self.score_image, self.score_rect)