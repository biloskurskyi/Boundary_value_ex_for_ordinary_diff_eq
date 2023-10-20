import sympy
from sympy import Symbol
import matplotlib.pyplot as plt

_ = ('lab number 6')
print(_.center(40))
f = sympy.sympify(input('Enter your function: '))


def func(x):
    k = Symbol('x')
    return f.subs(k, x)


xs = Symbol('x')
p = 1
q = 1
a = 0
b = 6.28
a0 = 1
a1 = 0
b0 = 1
b1 = 0
A = 0
B = 0
n = 100
h = (b - a) / n
xi = []
for i in range(n):
    xi.append(a + i * h)
print('xi:', *xi)
fi = []
for i in xi:
    fi.append(func(i))
print('fi:', *fi)
pi = []
for i in xi:
    pi.append(p)
print('pi:', *pi)
qi = []
for i in xi:
    qi.append(q)
print('qi:', *qi)


def mi(n_, h_, qi_, pi_):
    arr = []
    for i in range(n_):
        arr.append(((h_ ** 2) * qi_[i] - 2) / (1 + ((h_ / 2) * pi_[i])))
    return arr


def ki(n_, h_, pi_):
    arr = []
    for i in range(n_):
        arr.append((1 - ((h_ / 2) * pi_[i])) / (1 + ((h_ / 2) * pi_[i])))
    return arr


def Fi(n_, h_, pi_, fi_):
    arr = []
    for i in range(n_):
        arr.append(fi_[i] / (1 + ((h_ / 2) * pi_[i])))
    return arr


def ci(n_, mi_, ki_, h_, a0_, a1_):
    arr = []
    for i in range(n_):
        if i == 0:
            arr.append(a1_ / (h_ * a0_ - a1_))
        else:
            arr.append(1 / (mi_[i] - ki_[i] * arr[i - 1]))
    return arr


def di(n_, ki_, h_, a0_, a1_, Fi_, A_, ci_):
    arr = []
    for i in range(n_):
        if i == 0:
            arr.append((A_ * h_) / (h_ * a0_ - a1_))
        else:
            arr.append(ci_[i] * (h_ ** 2 * Fi_[i] - ki_[i] * arr[i - 1]))
    return arr


def yi(n_, h_, B_, b0_, b1_, di_, ci_):
    arr = []
    for i in range(n_ + 1):
        arr.append(0)
    arr[n_] = ((B_ * h_ + b1_ * di_[n - 1]) / (b0_ * h_ + b1_ * (ci_[n - 1] + 1)))
    for i in range(n_ - 1, -1, -1):
        arr[i] = di_[i] - (ci_[i] * arr[i + 1])
    return arr


_mi = mi(n, h, qi, pi)
print('mi:', *mi(n, h, qi, pi))
_ki = ki(n, h, pi)
print('ki:', *ki(n, h, pi))
_Fi = Fi(n, h, pi, fi)
print('Fi:', *Fi(n, h, pi, fi))
_ci = ci(n, _mi, _ki, h, a0, a1)
print('ci:', *ci(n, _mi, _ki, h, a0, a1))
_di = di(n, _ki, h, a0, a1, _Fi, A, _ci)
print('di:', *di(n, _ki, h, a0, a1, _Fi, A, _ci))
_yi = yi(n, h, B, b0, b1, _di, _ci)
print('yi:', *yi(n, h, B, b0, b1, _di, _ci))

_2 = 'lab number 6'
plt.title(_2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.plot(_yi, color='red')
plt.grid()
plt.show()
