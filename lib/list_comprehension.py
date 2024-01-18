#!/usr/bin/env python3

def return_evens(num_list):
    evens = [ n % 2 == 0 for n in num_list]
    # return num_list([n])
    print(evens)
    return evens


return_evens([0, 1, 4, 5, 6, 8, 9])


pass

def make_exclamation(sentence_list):
    exclamation = [k + '!' for k in sentence_list]
    print(exclamation)
    return exclamation
# make_exclamation(['Hi', 'To','ui'])
make_exclamation(["Hello", "I'm doing great", "Python is fun"])
pass