import sys
from collections import deque, Counter, defaultdict
import heapq, bisect, math

def main():
    MOD = 10**9 + 7
    try: sys.stdin = open('in.txt')
    except: pass
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    ns = lambda: next(it).decode()



    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
