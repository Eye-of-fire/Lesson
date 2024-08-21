a = 0
def say_hello(name):
    global a
    a += 1
    print("Hello World", name)
say_hello('vadim')
say_hello('maks')
say_hello('anton')
print(f'________{a}_______')
import random
def lottery():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win = random.choice(tickets)
    return win
win =lottery()
print(win)
print('________----------_______')
def lottery(*args,**kwargs):
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = (random.choice(tickets))
    print(*args)
    return win1, win2
win1, win2  = lottery('basa')
print(win1,win2)
print('______________________')
def test(a =2 ,b = True):
    print(a,b)
test()
test(False, 'ok')
test([1,2])
test(*[1,2])
