#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Elementi çap edirik, end="" vasitəsilə hamısını eyni sətirdə saxlayırıq
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            # Əgər i siyahının ölçüsündən böyükdürsə, döngəni dayandırırıq
            break
    print("")  # Sonda yeni sətirə keçid
    return count
