__author__ = "Бредихин І.В."

import re
from config import *
import re


def getEquations():
    rea = calculation['equations']
    n = len(rea)

    if not all(rea):  # удаляем пустые элементы списка
        k = 0
        flag = 0
        while k < n - flag:
            if rea[k] == '':
                del rea[k]
                flag += 1
                k -= 1
            k += 1

    rea2 = []
    direct = re.compile(' *-> *')
    reversible = re.compile(' *= *')
    for s in rea:  # разбиваем элементы списка на подсписки по знакам "=" и "->"
        if '->' in s:
            rea2.append(direct.split(s))
        elif '=' in s:
            k = reversible.split(s)
            rea2.append(k)
            rea2.append(k[::-1])
        else:
            print('Упс. Что-то пошлО не так... Как минимум одно уравнение не содержит знака "=" или "->". \
    Я, конечно, отработаю, но результат удовлетворит ваши ожидания едва ли.')

    for s in rea2:  # разбиваем элементы подсписков на подподсписки по знаку "+"
        j = 0
        for t in s:
            s[j] = re.split(' *\+ *', t)
            j += 1
    i = 0

    agg = set()  # множество со списком реагентов
    for s in rea2:  # разбиваем ещё и коэффициенты с реагентами
        j = 0
        for t in s:
            k = 0
            for u in t:
                d = re.match('[0-9]+[A-Z]', u)
                if d == None:
                    agg.add(rea2[i][j][k])
                    rea2[i][j][k] = ['1', rea2[i][j][k]]

                else:
                    d = d.end(0)
                    agg.add(rea2[i][j][k][d-1:])
                    rea2[i][j][k] = [rea2[i][j][k][:d-1], rea2[i][j][k][d-1:]]
                k += 1
            j += 1
        i += 1

    equa = []  # список со слагаемыми уравнений
    concentrationsSigns = []
    i = 0
    for s in rea2:  # собираем эти слагаемые
        k = 'k' + str((i + 1)) + '*'
        for t in s[0]:
            concentrationsSigns.append('C_{}'.format(t[1]))
            if t[0] == '1':
                k = k + 'C_{}*'.format(t[1])

            else:
                k = k + 'C_{}**{}'.format(t[1], t[0])
        equa.append(k)
        i += 1
    equations = []
    for s in agg:  # собираем конечные уравнения
        k = 'dC({})/dt = '.format(s)
        i = -1
        flag = True
        for t in rea2:
            i += 1
            j = -1
            for u in t:
                j += 1
                for v in u:
                    for w in v:
                        if w == s:
                            if j == 0:
                                l = '-'
                            else:
                                l = '+'
                            if v[0] == '1':
                                n = ''
                            else:
                                n = v[0]
                            if flag:
                                k = k + \
                                    '{}{}*{}'.format(
                                        l if l == '-' else '',
                                        '1' if n == '' else n, equa[i])
                                flag = False
                            else:
                                k = k + ' {} {}*{}'.format(l, '1' if n == '' else n, equa[i])

        secondPartEquation = k.split(' = ')[1]
        # copy string
        equations.append(secondPartEquation.encode().decode())

    return {
        'system': equations,
        'reagentsList': agg,
        'concentrationsSigns': concentrationsSigns
    }
