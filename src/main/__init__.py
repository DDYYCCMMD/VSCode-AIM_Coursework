from enum import Enum
from typing import Tuple


class Facing(Enum):  # Facing 我们定义为一个枚举类，用于定义方向。如有疑问可以自行 Google / Ask AI
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Grid():
    def __init__(self, width: int, height: int, enemy_pos: tuple):  # DO NOT EDIT THIS METHOD
        self.width: int = width
        self.height: int = height
        self._current_pos: tuple = (0, 0)
        self.current_direction = Facing.UP
        self.enemy_pos: tuple = enemy_pos
        self.position_history: dict = {}  # 用于存储位置历史，键为步数，值为坐标

    @property
    def current_pos(self) -> Tuple[int, int]:

        return self._current_pos

    @current_pos.setter
    def current_pos(self, value: Tuple[int, int]) -> None:

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("传入必须是tuple且长度为2")

        x, y = map(int, value)
        x = min(self.width, max(0, x))
        y = min(self.height, max(0, y))

        self._current_pos = (x, y)

        # TODO: Question 1

    def move_forward(self) -> Tuple[int, int]:  # type: ignore

        x, y = self._current_pos

        if self.current_direction == Facing.RIGHT:
            x = min(self.width, x + 1)
        if self.current_direction == Facing.LEFT:
            x = max(0, x - 1)
        if self.current_direction == Facing.UP:
            y = min(self.height, y + 1)
        if self.current_direction == Facing.DOWN:
            y = max(0, y - 1)

        self.current_pos = (x, y)

        return self._current_pos

        # TODO: Question 2

    def turn_left(self) -> Facing:  # type: ignore

        new_direction = Facing((self.current_direction.value + 1) % 4)
        self.current_direction = new_direction

        return self.current_direction

        # TODO: Question 3a

    def turn_right(self) -> Facing:  # type: ignore

        new_direction = Facing((self.current_direction.value - 1) % 4)
        self.current_direction = new_direction

        return self.current_direction

        # TODO: Question 3b

    def find_enemy(self) -> bool:  # type: ignore

        return self._current_pos == self.enemy_pos

        # TODO: Question 4

    def record_position(self, step: int) -> None:

        if not isinstance(step, int):
            raise TypeError("step 必须是整数")
        self.position_history[step] = self.current_pos

        # TODO: Question 5a

    def get_position_at_step(self, step: int) -> tuple | None:  # type: ignore

        return self.position_history.get(step, None)

        # TODO: Question 5b



class AdvancedGrid(Grid):
    def __init__(self, width: int, height: int, enemy_pos: tuple):
        super().__init__(width, height, enemy_pos)
        self.steps: int = 0

    def move_forward(self) -> Tuple[int, int]:

        new_pos = super().move_forward()
        self.steps += 1

        return new_pos

    def distance_to_enemy(self) -> int:

        x1, y1 = self.current_pos
        x2, y2 = self.enemy_pos

        return abs(x1 - x2) + abs(y1 - y2)

# TODO: Question 6
