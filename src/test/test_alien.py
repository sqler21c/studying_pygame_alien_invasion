import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

print("os.path.name : ", os.path.dirname(__file__))
print("os.path.dirname(os.path.abspath(os.path.dirname(__file__))) : ", os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from alien_invasion import AlienInvasion

def test_alien_invasion():
    ai = AlienInvasion()
    assert ai.screen_width == 1200
    assert ai.screen_height == 800
    assert ai.bg_color == (230, 230, 230)
