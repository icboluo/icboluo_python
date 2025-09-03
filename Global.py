class Pos:
    win_l = -1
    win_t = -1
    win_w = -1
    win_h = -1
    figure_x = -1
    figure_y = -1

    @staticmethod
    def win_position() -> list[int]:
        return [Pos.win_l, Pos.win_t, Pos.win_w, Pos.win_h]

    @staticmethod
    def update_position(l, t, w, h) -> None:
        Pos.win_l = l
        Pos.win_t = t
        Pos.win_w = w
        Pos.win_h = h

    # 查询怪物区域
    @staticmethod
    def monster_area() -> tuple[int, int, int, int]:
        return Pos.win_l, Pos.win_t, Pos.win_w // 2, Pos.win_h * 9 // 13

    @staticmethod
    def figure_position() -> list[int]:
        return [Pos.figure_x, Pos.figure_y]

    # 跟新人物位置
    @staticmethod
    def update_figure(x, y):
        Pos.figure_x = x
        Pos.figure_y = y
