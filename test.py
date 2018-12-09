#TODO if last item in result array doesnt fit with initial array add it into the result array .
# this is for cases with fractional numbers

def getVariants(arr, step):
    index = 0
    collector = []
    workArray = [0]*len(arr)

    def fillCollectorArray(workArray, step, index):
        while(workArray[index] <= arr[index]):
            if(index+1 >= len(workArray)):
                collector.append(workArray.copy())
                workArray[index] += step
            else:
                fillCollectorArray(workArray, step, index+1)
                workArray[index+1] = 0
                workArray[index] += step

    fillCollectorArray(workArray, step, index)
    return collector

arr = [9, 9, 9, 89]
g = getVariants(arr, 9)


    



