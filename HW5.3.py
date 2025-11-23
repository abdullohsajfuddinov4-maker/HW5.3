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
def son_2_kara(f):
    def w(a):
        s = [i*2 for i in a]
        return f(s)
    return w

@son_2_kara
def son(a):
    return(a)

print(son([5,8,6,3,4,5]))

