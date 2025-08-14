import sys

import pygame

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""
    
    def __init__(self):
        """ Initialize game and make game's resource """
        pygame.init() # pygame 초기화
        
        self.screen = pygame.display.set_mode((1200, 800)) # 게임 화면 크기 설정
        pygame.display.set_caption("Alien Invasion") # 게임 제목 설정

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            """ keyboard and mouse event 처리 """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # 가장 최근 그린 화면을 표시
            pygame.display.flip() # 화면 업데이트
            
if __name__ == '__main__':
    # make intance of AlienInvasion
    ai = AlienInvasion()
    ai.run_game()