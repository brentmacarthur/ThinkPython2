'''
Think Python, 2nd - Exercise 3-2
'''

def do_twice(f, v):
    f(v)
    f(v)

def do_four(func, val):
    do_twice(func, val)
    do_twice(func, val)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')
do_four(print_twice, 'spam')
