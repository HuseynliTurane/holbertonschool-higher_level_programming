#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """İki siyahının elementlərini bir-birinə bölür."""
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            # Bölməni yerinə yetirməyə çalışırıq
            res = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            # Element integer və ya float deyilsə
            print("wrong type")
        except ZeroDivisionError:
            # Sıfıra bölmə halı
            print("division by 0")
        except IndexError:
            # Siyahılardan biri x indeksindən qısadırsa
            print("out of range")
        finally:
            # Xəta olub-olmamasından asılı olmayaraq nəticəni əlavə edirik
            # (Xəta olubsa res = 0 olaraq qalır)
            new_list.append(res)
    return new_list
