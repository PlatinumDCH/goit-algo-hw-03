from random import randint
from typing import Generator

G = Generator[int, None, None]
def gen_random_num(min: int = 1,max: int = 100)->G:
    while True:
        yield randint(min, max)


def get_numbers_ticket(quantity: int = 10):
    set_num:set = set()
    flag = True
    while flag:
        if len(set_num) == quantity:
            flag = False
        else:
            num = next(gen_random_num())
            set_num.add(num)
    return set_num

print(get_numbers_ticket())