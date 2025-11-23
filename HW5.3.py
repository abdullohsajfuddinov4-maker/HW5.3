#1
'''
def manfi_son(f):
    def w(a):
        n = [i for i in a if i < 0]
        return f(n)
    return w 

@manfi_son
def son (n):
    return n

print(son ([1,3,5,5,-500,54,-5]))
'''
#2
'''

def matin(f):
    def w(a):
        s = []
        for i in a:
            try:
                if i.isalpha():
                    s.append(i)
            except AttributeError:
                pass
        return f(s)
    return w


@matin
def str_func(s):
    return s


print(str_func([5, 4, 1, 'dhgh', 656, 'dh']))
'''
#3
'''
def len_soz(f):
    def w(a):
        l = [ i for i in a if len(i) >= 3 ]
        return f(l)
    return w

@len_soz
def soz(s):
    return s
 
print(soz(['anor','gilos','nok','it']))
'''
#4
'''
def son_2_kara(f):
    def w(a):
        s = [i*2 for i in a]
        return f(s)
    return w

@son_2_kara
def son(a):
    return(a)

print(son([5,8,6,3,4,5]))
'''
#5
'''
import time
def taymer(f):
    def w(*args, **kwargs):
        s = time.time()
        a = f(*args, **kwargs)
        e = time.time()
        print(f'ishlagan vaqti {e-s}')
        return a
    return w

@taymer
def a ():
    for i in range(100000):
        print(i*2)

a()
'''
#6
'''
def upper(f):
    def w(a):
        a = [i.upper() for i in a]
        return f(a)
    return w

@upper
def matin(a):
    return a

print(matin(['oaurga oighag','aoieghegag frgfa ']))
'''
#7
'''
def index_son(f):
    def w(a):
        a = [a[i] for i in range(len(a)) if i % 2 ==0]
        return f(a)
    return w

@index_son
def son(a):
    return a

print(son([1,2,3,4,5,6,7]))
'''
#8
'''
def k_y(func):
    def wrapper(years):
        a = []
        for i in years:
            if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
                a.append(i)
 
               return func(a)
    return wrapper


@k_y
def yil (lst):
    return lst


print(yil([1999, 2000, 2001, 2004, 1800,2024, 2020, 2100]))

'''
#9
'''
def islist(f):
    def w(arg):
        if not isinstance(arg, list):
            print((f"{arg} : Argument list bo'lishi kerak!"))
        else:
            print(f'{arg} : list')
        return f(arg)
    return w


@islist
def a(data):
    return data


a([1, 2, 3])
a("abc")
'''
#10
'''
def file(funk):
    def w(*args, **kwargs):
        a = funk(*args, **kwargs)
        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(str(a) + "\n")
        return a
    return w


@file
def text():
    return "Bu biror natija"


print(text())
'''
