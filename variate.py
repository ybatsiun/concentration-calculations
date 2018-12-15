from config import *

# result = []

# for key in constants[0]:
#     value = constants[0][key]
#     for key1 in constants[1]:
#         value1 = constants[1][key1]
#         # check length
#         result.append([value, value1])

# print("FIRST")
# print(result)


def globalFunc(constants):
        def work(index,arr):
                for key in constants[index]:
                        #breakpoint()
                        value = constants[index][key]
                        arr.append(value)
                        if(index+1 >= constantsLength):
                                #breakpoint()
                                result.append(arr.copy())
                                arr.pop()
                        else:
                                #breakpoint()
                                work(index+1,arr)
                                arr.pop()

        result = []
        constantsLength = len(constants)

        work(0,[])
        return result

    

s = globalFunc(constants)
print("SECOND")
print(s)
print(len(s))
