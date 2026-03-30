#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] hər zaman proqramın adıdır, ona görə onu saymırıq
    argv = sys.argv[1:]
    count = len(argv)

    # Birinci sətir: Arqumentlərin sayını və sonundakı işarəni təyin edirik
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # İkinci hissə: Hər bir arqumenti öz mövqeyi ilə çap edirik
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
