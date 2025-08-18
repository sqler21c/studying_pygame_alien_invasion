import sys, os

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# 상위 폴더 경로 가져오기
parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 상위 폴더 경로를 sys.path에 추가
sys.path.append(parent_folder)


# print("os.path.name : ", os.path.dirname(__file__))
# print("os.path.dirname(os.path.abspath(os.path.dirname(__file__))) : ", os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from alien_invasion import AlienInvasion

"""
def test_alien_invasion():
    ai = AlienInvasion()
    assert ai.screen_width == 1200
    assert ai.screen_height == 800
    assert ai.bg_color == (230, 230, 230)

"""