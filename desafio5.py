from math import *
from builtins import staticmethod
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque
import functools
import heapq
import hashlib
from datetime import datetime, timedelta
import json
import re
from itertools import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)

    k = int(input())
    a.sort(key=lambda row: row[k])
    for row in a:
        print(*row)