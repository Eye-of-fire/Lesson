calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    str = len(string)
    str1 = string.upper()
    str2 = string.lower()
    return str,str1, str2
    print(str,str1, str2)




def  is_contains(string,list_to_search):   # string = str , list_to_search = list
    count_calls()
    for i in list_to_search:
        if i in string:
            return True
        return False

def is_contains(string, list_to_search):
  count_calls()
  return string.upper() in [a.upper() for a in list_to_search]









print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)