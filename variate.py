def getVariants(constants):
        def work(index,arr):
                for key in constants[index]:
                        value = constants[index][key]
                        arr.append(value)
                        if(index+1 >= constantsLength):
                                result.append(arr.copy())
                                arr.pop()
                        else:
                                work(index+1,arr)
                                arr.pop()

        result = []
        constantsLength = len(constants)
        work(0,[])
        return result