#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # 1. Modulun içindəki bütün adları (funksiya, dəyişən və s.) siyahıya alırıq
    all_names = dir(hidden_4)

    # 2. Siyahını əlifba sırası ilə düzürük
    all_names.sort()

    # 3. Hər bir adı tək-tək yoxlayırıq
    for name in all_names:
        # Şərt: Əgər ad "__" ilə BAŞLAMIRSA, onu çap et
        if not name.startswith("__"):
            print("{}".format(name))
