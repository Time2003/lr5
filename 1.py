#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано натуральное число n > 100 . Вывести на экран фразу Мне n лет , учитывая, что при
# некоторых значениях n слово «лет» надо заменить на слово «год» или «года».
import sys
n = int(input("n = "))
if n < 100:
    print("Ошибка!", file=sys.stderr)
    exit(1)
elif n % 10 == 1:
    print("мне", n, "год")
elif n % 10 in (2, 3, 4):
    print("мне", n, "года")
else:
    print("мне", n, "лет")