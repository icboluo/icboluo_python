from Tool import find, click_global, click_sleep


def wabao():
    # wait_click_sleep('主界面/main-设施_洛阳.png')
    # wait_click_sleep('设施/战场.png')
    # wait_click_sleep('战场/宝洞.png')
    # wait_click_sleep('战场/宝石矿洞.png')
    # wait_click_sleep('战场/挖宝助手.png')
    for i in range(10000):
        click_sleep('战场/挖宝.png', threshold=0.8)
        if i % 4 == 0:
            x, y = find('战场/购买.png')
            if x != -1:
                click_global(x, y)


if __name__ == "__main__":
    wabao()
