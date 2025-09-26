from random import choice

class RandomWalk:
    """randomwalk class

    """

    def __init__(self, num_points=5000):
        """속성 초기화

        Args:
            num_points (int, optional): Defaults to 5000.
        """
        self.num_points = num_points

        # 이동은 (0, 0)에서 시작
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """랜덤 워크의 각 포인트를 계산
        """
        # 설정한 이동 수에 도달할때  까지 움직임 반복
        while len(self.x_values) < self.num_points:

            # check direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 움직임이 없는 결정은 버림
            if x_step == 0 and y_step == 0:
                continue

            # cal new location
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)