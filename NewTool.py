import time

from Tool import write
from ai4 import count_people_status
from 战斗 import attack_in_success


def attack1():
    # attack_in_success(1, 4)
    # write()
    is_match = aliveAndDeadIsMatch(6, 2)
    print(is_match)


def aliveAndDeadIsMatch(total, alive):
    ad_dict = count_people_status('picture/temp1.png')
    a = ad_dict['alive']
    d = ad_dict['dead']
    return a == alive and d >= total - alive

if __name__ == '__main__':
    attack1()