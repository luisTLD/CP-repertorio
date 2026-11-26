import sys
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, product, accumulate
import heapq, bisect, math

# ---------- LISTA ----------
a = [5, 6, 7]
a[1]  # → 6
a[-1]  # → 7
len(a)  # → 3
a.append(8)  # a → [5, 6, 7, 8]
a.extend([9, 10])  # a → [5, 6, 7, 8, 9, 10]
a.pop()  # → 10
a.pop(0)  # → 5
a.insert(0, 5)  # a → [5, 6, 7, 8, 9]
a.remove(9)  # a → [5, 6, 7, 8]
del a[3]  # a → [5, 6, 7]
6 in a  # → True
a.index(6)  # → 1
a[1:3]  # → [6, 7]
a[::-1]  # → [7, 6, 5]
sum(a), min(a), max(a)  # → (18, 5, 7)
sorted(a, reverse=True)  # → [7, 6, 5]
b = a[:]  # b → [5, 6, 7]
[0] * 3  # → [0, 0, 0]
[[0] * 2 for _ in range(3)]  # → [[0, 0], [0, 0], [0, 0]]
list(enumerate(a))  # → [(0, 5), (1, 6), (2, 7)]
list(zip(a, 'xyz'))  # → [(5, 'x'), (6, 'y'), (7, 'z')]

# ---------- STRING ----------
''.join(['ab', 'c', 'd'])  # → 'abcd'
'o rato roeu'.split()  # → ['o', 'rato', 'roeu']
'banana'[1:4]  # → 'ana'
'abc'[::-1]  # → 'cba'
'banana'.count('a')  # → 3
'banana'.find('nan')  # → 2
ord('c') - ord('a')  # → 2
chr(ord('a') + 2)  # → 'c'
'aB'.upper(), 'aB'.lower()  # → ('AB', 'ab')
'7'.isdigit(), 'x'.isalpha()  # → (True, True)
t = list('abc'); t[1] = 'x'
''.join(t)  # → 'axc'
list(map(int, str(305)))  # → [3, 0, 5]

# ---------- SET ----------
s = {1, 2}
s.add(3)  # s → {1, 2, 3}
2 in s  # → True
s.discard(9)  # s → {1, 2, 3}
{1, 2} | {2, 3}  # → {1, 2, 3}
{1, 2} & {2, 3}  # → {2}
{1, 2} - {2, 3}  # → {1}
len(set([3, 1, 3]))  # → 2

# ---------- DICT ----------
d = {'x': 1}
d['x']  # → 1
d.get('y', 0)  # → 0
d['y'] = d.get('y', 0) + 1  # d → {'x': 1, 'y': 1}
'x' in d  # → True
d.pop('x', None)  # → 1
list(d.items())  # → [('y', 1)]
max({'a': 3, 'b': 5}, key={'a': 3, 'b': 5}.get)  # → 'b'
c = Counter("banana")
c['a'], c['z']  # → (3, 0)
c.most_common(1)  # → [('a', 3)]
g = defaultdict(list)
g['a'].append(1)  # g → {'a': [1]}
cnt = defaultdict(int)
cnt['x'] += 1  # cnt → {'x': 1}

# ---------- PILHA E FILA ----------
p = [1, 2]
p.append(3)  # p → [1, 2, 3]
p[-1]  # → 3
p.pop()  # → 3
q = deque([1, 2])
q.append(3)  # q → deque([1, 2, 3])
q[0]  # → 1
q.popleft()  # → 1
q.appendleft(0)  # q → deque([0, 2, 3])
q.pop()  # → 3

# ---------- HEAP (o menor fica em h[0]; não existe key=) ----------
h = [5, 1, 3]
heapq.heapify(h)
h[0]  # → 1
heapq.heappush(h, 0)
heapq.heappop(h)  # → 0
heapq.nsmallest(2, [5, 1, 3])  # → [1, 3]
heapq.nlargest(2, [5, 1, 3])  # → [5, 3]
arestas = [(1, 2, 5), (2, 3, 1)]
h = [(w, u, v) for u, v, w in arestas]
heapq.heapify(h)
heapq.heappop(h)  # → (1, 2, 3)
h = []
heapq.heappush(h, -7); heapq.heappush(h, -9)
-heapq.heappop(h)  # → 9

# ---------- ORDENAÇÃO ----------
sorted([2, 3, 1])  # → [1, 2, 3]
sorted(['ccc', 'a', 'bb'], key=len)  # → ['a', 'bb', 'ccc']
sorted([(1, 9), (2, 3)], key=lambda x: x[1])  # → [(2, 3), (1, 9)]
sorted([(1, 5), (2, 7), (2, 3)], key=lambda x: (-x[0], x[1]))  # → [(2, 3), (2, 7), (1, 5)]
sorted(range(3), key=lambda i: [30, 10, 20][i])  # → [1, 2, 0]

# ---------- BISECT (lista ordenada) ----------
b = [2, 4, 4, 4, 7]
bisect.bisect_left(b, 4)  # → 1
bisect.bisect_right(b, 4)  # → 4
len(b) - bisect.bisect_right(b, 4)  # → 1
bisect.bisect_right(b, 4) - bisect.bisect_left(b, 4)  # → 3
bisect.bisect_right(b, 5) - bisect.bisect_left(b, 3)  # → 3
b[bisect.bisect_left(b, 3)]  # → 4
b[bisect.bisect_right(b, 5) - 1]  # → 4

# ---------- ITERTOOLS ----------
list(permutations([1, 2, 3]))[:2]  # → [(1, 2, 3), (1, 3, 2)]
list(combinations([1, 2, 3], 2))  # → [(1, 2), (1, 3), (2, 3)]
list(product([0, 1], repeat=2))  # → [(0, 0), (0, 1), (1, 0), (1, 1)]
list(accumulate([1, 2, 3], initial=0))  # → [0, 1, 3, 6]

# ---------- MATH E MOD ----------
math.gcd(12, 18), math.lcm(4, 6)  # → (6, 12)
math.isqrt(10)  # → 3
math.comb(5, 2)  # → 10
divmod(7, 2)  # → (3, 1)
-(-7 // 2)  # → 4
-7 // 2  # → -4
(3 - 5) % 7  # → 5
pow(2, 10, 1000)  # → 24
pow(3, 7 - 2, 7)  # → 5
4 * (4 + 1) // 2  # → 10
bin(5)[2:], int('101', 2)  # → ('101', 5)

# ---------- BITS ----------
x = 12
1 << 2  # → 4
x >> 2 & 1  # → 1
x | (1 << 0)  # → 13
x & ~(1 << 2)  # → 8
x ^ (1 << 2)  # → 8
(1 << 4) - 1  # → 15
bin(13).count('1')  # → 3
(13).bit_length() - 1  # → 3
1 << ((13).bit_length() - 1)  # → 8
1 << (6 - 1).bit_length()  # → 8
x & -x  # → 4
(x & -x).bit_length() - 1  # → 2
x & (x - 1)  # → 8
16 > 0 and 16 & (16 - 1) == 0  # → True
format(5, '04b')  # → '0101'

# ---------- BITMASK COMO CONJUNTO (bit i ligado = item i dentro) ----------
n = 4
A = 0b0101
B = 0b0110
(1 << n) - 1  # → 15
A | (1 << 1)  # → 7
A & ~(1 << 0)  # → 4
A >> 2 & 1  # → 1
A | B  # → 7
A & B  # → 4
A & ~B  # → 1
((1 << n) - 1) ^ A  # → 10
A & B == A  # → False
A & B != 0  # → True
bin(A).count('1')  # → 2
[i for i in range(n) if A >> i & 1]  # → [0, 2]
sum(1 << i for i in [0, 2])  # → 5
[m for m in range(1 << n) if bin(m).count('1') == 2]  # → [3, 5, 6, 9, 10, 12]
