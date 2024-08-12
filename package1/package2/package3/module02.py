#from package1.module01 import hello

#from .module01 import hello #относительный импорт

def good_word(name):
    #hello(name)
    print("Ты лучщий", name)


if __name__ == '__main__':
    good_word('Урбан')
