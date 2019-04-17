import re
from string import Template

def testEval(s):
    print('evaluating...')
    eval(s)

# def f():
#     return globals()["a"] * globals()["b"]
# #v = eval('globals()["a"]**3')
# a = 'test'
# lol = f'some{a}'
# a = 2
# print(lol)

#teststing = ['globals()["a"]','*','globals()["b"]']

# def generate(teststing):
#    def subf():
#      for w in teststing:



string = "2*k1*C_A**3 + 2*k2*C_B**2 - 1*k3*C_B*C_C**2"
string = '2*k1*C_A**3'
nstring = string.replace("**", "^")
splitted = re.split("(\-|\+|\*|\n)", nstring)
newSplitted = []
for val in splitted:
    newSplitted.append(val.strip().replace("^", "**"))

varKeys = ["C_A", "C_B", "C_C", "k1", "k2"]

finalSplitted = []
for val in newSplitted:

    index = [i for i, item in enumerate(varKeys) if item in val]
    if len(index) != 0:
      finalSplitted.append('globals()["' + val + '"]')
    else:
      finalSplitted.append(val)

print(finalSplitted)


# fruit_list = ['raspberry', 'apple', 'strawberry']
# berry_idx = [i for i, item in enumerate(fruit_list) if 'ras' in item]
# print(berry_idx)
