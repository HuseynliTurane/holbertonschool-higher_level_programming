#!/usr/bin/python3
def safe_print_division(a, b):
    """İki tam ədədi bölür və nəticəni 'finally' daxilində çap edir."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        # Sıfıra bölmə xətası baş verərsə, result None olaraq qalır
        pass
    finally:
        # Xəta olsa da, olmasa da bu hissə həmişə işləyəcək
        print("Inside result: {}".format(result))
    return result
