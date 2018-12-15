from config import *

result = []
# 1st lap
for key in constants[0]:
        value = constants[0][key]
        for key1 in constants[1]:
                value1 = constants[1][key1]
                # check length
                result.append([value,value1])


print(result)


