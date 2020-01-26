import re
from typing import List, TypeVar, Tuple, Any, Generator
from random import randrange, randint
def missing_array(data:List[int]) ->int:
    total = 1
    n = len(data)
    for i in range(2, n+2):
        total+=i
        total-=data[i-2]
    return total
if __name__=='__main__':
    l1 = list(map(int, input("Enter the list: \n").strip().split()))
    print(missing_array(l1))
