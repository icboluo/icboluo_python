from b import wait_click_sleep


def wabao():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/战场.png')
    wait_click_sleep('战场/宝洞.png')
    wait_click_sleep('战场/宝石矿洞.png')
    wait_click_sleep('战场/挖宝助手.png')
    while True:
        wait_click_sleep('战场/挖宝.png')



if __name__ == "__main__":
    wabao()
