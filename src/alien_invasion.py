import sys
import pygame
from settings import Settings

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""
    
    def __init__(self):
        """ Initialize game and make game's resource """
        pygame.init() # pygame 초기화
        self.clock = pygame.time.Clock() # 게임 속도 조절을 위한 시계 객체 생성
        
        # self.screen = pygame.display.set_mode((1200, 800))을 
        # Settings 사용하여  클래스 인스턴스 생성
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion") # 게임 제목 설정
        
        # self.bg_color = (230, 230, 230)  # 밝은 회색
        # 배경색 설정
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            """ keyboard and mouse event 처리 """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 루프를 반복할때마다 화면을 다시 그립니다. 
            # self.screen.fill(self.bg_color)를 아래와 같이 settings 클래스 사용
            self.screen.fill(self.settings.bg_color)
                    
            # 가장 최근 그린 화면을 표시
            pygame.display.flip() # 화면 업데이트
            
            self.clock.tick(60) # frame 속도

if __name__ == '__main__':
    # make intance of AlienInvasion
    ai = AlienInvasion()
    ai.run_game()