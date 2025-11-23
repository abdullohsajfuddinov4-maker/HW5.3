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


