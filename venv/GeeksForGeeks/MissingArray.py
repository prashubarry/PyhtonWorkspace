import re
from typing import List, TypeVar, Tuple, Any, Generator
from random import randrange, randint
Num = TypeVar('Num', int, float)
def missing_array(data: List[int]) -> int:
    n = len(data)
    total = (n+1) * (n+2) // 2
    sum_of_data = sum(data)
    return total - sum_of_data

if __name__=='__main__':
    l1 = list(map(int, input("Enter the list: \n").strip().split()))
    print(missing_array(l1))

