class Settings:
    """외계인 침공의 설정을 저장하는 클래스"""
    
    def __init__(self):
        """게임 설정초기화"""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 밝은 회색
        self.ship_speed = 1.5 # 우주선 속도 설정
        
        #탄환 설정
        self.bullet_speed = 3.0 # 탄환 속도
        self.bullet_width = 3 # 탄환 너비
        self.bullet_height = 15 # 탄환 높이
        self.bullet_color = (60, 60, 60) # 탄환 색상
        self.bullets_allowed = 3 # 화면에 존재할 수 있는 탄환 수