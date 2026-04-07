#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary: # Əgər açar lüğətdə varsa
        del a_dictionary[key] # Onu sil
    return a_dictionary # Hər iki halda lüğəti geri qaytar
#111
