class Global:
    win_l = -1
    win_t = -1
    win_w = -1
    win_h = -1
    glo_ren_wu_x = 1
    glo_ren_wu_y = 1

    @staticmethod
    def find_zuo_biao() -> list[int]:
        return [Global.win_l, Global.win_t, Global.win_w, Global.win_h]

    @staticmethod
    def find_position() -> list[int]:
        return [Global.win_l, Global.win_t, Global.win_w, Global.win_h]

    @staticmethod
    def update_position(l, t, w, h) -> None:
        Global.win_l = l
        Global.win_t = t
        Global.win_w = w
        Global.win_h = h
