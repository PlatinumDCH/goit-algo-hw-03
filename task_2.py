from random import randint
from typing import Generator

G = Generator[int, None, None]
def gen_random_num(min:int,max:int)->G:
    while True:
        yield randint(min, max)


def check_para(mn,mx,qt)->bool:
    if not isinstance(mn, int) or mn<1:
        return False
    if not isinstance(mx, int) or mx<1 or mx>1000:
        return False
    if not isinstance(qt, int) or qt<=0:
        return False
    if mn>mx:
        return False
    if qt > (mx - mn + 1):
        return False
    return True

def get_numbers_ticket(min:int, max:int, quantity:int)->list[int]:
    if not check_para(min,max,quantity):
        return []
    
    set_num:set[int] = set()

    while len(set_num)< quantity:
        num = next(gen_random_num(min,max))
        set_num.add(num)
    return sorted(list(set_num))
