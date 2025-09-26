class Settings:
    """외계인 침공의 설정을 저장하는 클래스"""
    
    def __init__(self):
        """게임 설정초기화"""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 밝은 회색
       
       # 우주선 설정
        self.ship_limit = 1 # 우주선 수
        self.ship_speed = 1.5 # 우주선 속도 설정
        
        #탄환 설정
        self.bullet_speed = 3.0 # 탄환 속도
        self.bullet_width = 600 # 탄환 너비
        self.bullet_height = 15 # 탄환 높이
        self.bullet_color = (60, 60, 60) # 탄환 색상
        self.bullets_allowed = 3 # 화면에 존재할 수 있는 탄환 수

        # 외계인 속도 설정
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1은 오른쪽, -1은 왼쪽
        self.fleet_direction = 1

        # 게임을 빠르게 만드는 속도
        self.speedup_scale = 1.1

        # 외계인 점수가 늘어나는 속도
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """_summary_
        게임을 진행 하는 동안 변하는 설정 초기화
        """
        self.ship_speed = 3.5
        self.bullet_speed = 5.5
        self.alien_speed = 1.0

        # 1은 오른쪽, -1은 왼쪽
        self.fleet_direction = 1

        # 점수 설정
        self.alien_points = 50

    def increase_speed(self):
        """속도를 높인다
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)