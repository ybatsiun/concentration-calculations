__author__ = "Бредихин І.В."

from services.loggerService import log
import re
import random
from config import *

def getEquations(rea):
    n = len(rea)

    if not all(rea):  # удаляем пустые элементы списка
        k = 0
        flag = 0
        while k < n - flag:
            if rea[k] == "":
                del rea[k]
                flag += 1
                k -= 1
            k += 1

    rea2 = []
    direct = re.compile(" *-> *")
    reversible = re.compile(" *= *")
    for s in rea:  # разбиваем элементы списка на подсписки по знакам "=" и "->"
        if "->" in s:
            rea2.append(direct.split(s))
        elif "=" in s:
            k = reversible.split(s)
            rea2.append(k)
            rea2.append(k[::-1])
        else:
            log(
                'Упс. Что-то пошлО не так... Как минимум одно уравнение не содержит знака "=" или "->". \
    Я, конечно, отработаю, но результат удовлетворит ваши ожидания едва ли.'
            )

    for s in rea2:  # разбиваем элементы подсписков на подподсписки по знаку "+"
        j = 0
        for t in s:
            s[j] = re.split(" *\+ *", t)
            j += 1
    i = 0

    agg = set()  # множество со списком реагентов
    for s in rea2:  # разбиваем ещё и коэффициенты с реагентами
        j = 0
        for t in s:
            k = 0
            for u in t:
                d = re.match("[0-9]+[A-Z]", u)
                if d == None:
                    agg.add(rea2[i][j][k])
                    rea2[i][j][k] = ["1", rea2[i][j][k]]

                else:
                    d = d.end(0)
                    agg.add(rea2[i][j][k][d - 1:])
                    rea2[i][j][k] = [rea2[i][j][k]
                                     [: d - 1], rea2[i][j][k][d - 1:]]
                k += 1
            j += 1
        i += 1

    equa = []  # список со слагаемыми уравнений
    equa_html = []
    concentrationsSigns = []
    i = 0
    for s in rea2:  # собираем эти слагаемые
        k = "k" + str((i + 1)) + "*"
        k_html = 'k<sub>' + str((i + 1)) +'</sub>'
        for t in s[0]:
            if t[0] == "1":
                # the one for python operations
                k = k + "C_{}*".format(t[1])
                # the one for html represantation
                k_html = k_html + 'C<sub>{}</sub>'.format(t[1])
            else:
                # the one for python operations
                k = k + "C_{}**{}".format(t[1], t[0])
                # the one for html represantation
                k_html = k_html + 'C<sub>{}</sub><sup>{}</sup>'.format(t[1], t[0])


        # remove the last '*' if it exists
        kf = k.rfind("*")
        if(kf != -1 and (len(k)-1)==kf):
            new_string = k[:kf] + k[kf+1:]
            equa.append(new_string)
        else:
            equa.append(k)
        equa_html.append(k_html)
        i += 1

    equations = []
    reagentsList = []
    equationDataArray = []
    for s in agg:  # собираем конечные уравнения
        equationData = {}
        k = "dC_{}/dt = ".format(s)
        k_html = '   <p>dC<sub>{}</sub>/dt = '.format(s)
        equationData['reagent'] = s
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
                                l = "-"
                            else:
                                l = "+"
                            if v[0] == "1":
                                n = ""
                            else:
                                n = v[0]
                            if flag:
                                k = k + "{}{}*{}".format(
                                    l if l == "-" else "",
                                    "1" if n == "" else n,
                                    equa[i],
                                )
                                k_html = k_html + '{}{}{}'.format(l if l == '-' else '', n, equa_html[i])
                                flag = False
                            else:
                                k = k + " {} {}*{}".format(
                                    l, "1" if n == "" else n, equa[i]
                                )
                                k_html = k_html + ' {} {}{}'.format(l, n, equa_html[i])

        equationData['equation'] = k
        equationData['html'] = k_html
        equationDataArray.append(equationData)

    return equationDataArray


def _convertEquationToExpression(equation, concentrationsSigns):
    functions = []

    functionName = f"equationFunc_{random.randint(1,101)}"
    functionString = _getFunctionString(
        equation, functionName, concentrationsSigns)
    exec(functionString)

    return locals()[functionName]


def _getFunctionString(equationString, functionName, concentrationsSigns):
    
    nstring = equationString.replace("**", "^")
    splitted = re.split("(\-|\+|\*|\^|\n)", nstring)
    newSplitted = []
    for val in splitted:
        newSplitted.append(val.strip().replace("^", "**"))

    # generate an array of variables  to replace
    varKeys = []
    for i in range(0, len(SPEED_CONSTANTS)):
        varKeys.append("k"+str(i + 1))
    varKeys = varKeys + concentrationsSigns
    finalSplitted = []
    for val in newSplitted:

        index = [i for i, item in enumerate(varKeys) if item in val]
        if len(index) != 0:
            finalSplitted.append('args["' + val + '"]')
        else:
            finalSplitted.append(val)

    template = f"def {functionName}(args): return "

    for s in finalSplitted:
        template = template + s

    return template


def convertEquations(equationDataArray):
    """
    Parameters:
    equationDataArray (Array): objects each containig 'equation' - string for differential equation and 'reagentName'
    Returns:
    equationDataArray (Array): objects each containing equationDataArray data and 'function' - function to calculate concentration
                               for reagent at a time
    """
    concentrationsSigns = []
    for equationData in equationDataArray:
        concentrationsSigns.append("C_{}".format(equationData['reagent']))

    for equationData in equationDataArray:
        secondEquationPart = equationData['equation'].split(" = ")[1]
        equationData['function'] = _convertEquationToExpression(
            secondEquationPart, concentrationsSigns)

    return sorted(equationDataArray, key=lambda k: k['reagent'])
