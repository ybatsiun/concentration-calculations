arr = [1, 1, 2, 5]  
step = 1
workArray = [0, 0, 0, 0]
collector = []

while(workArray[0] <= arr[0]):

    while(workArray[1] <= arr[1]):

        while(workArray[2] <= arr[2]):

            while(workArray[3] <= arr[3]):
                collector.append(workArray.copy())
                workArray[3] += step
            workArray[3] = 0
            workArray[2] += step

        workArray[2] = 0
        workArray[1] += step

    workArray[1] = 0
    workArray[0] += step


# def do(arr, step, index):

#     while(workArray[index] <= arr[index]):
#         #breakpoint()
#         print(index)
#         print(index+1 >= len(workArray))
#         if(index+1 >= len(workArray)):
#             #breakpoint()
#             collector.append(workArray)
#             #workArray[index] += step
#         else:
#             #breakpoint()
#             do(workArray, step, index+1)
#             workArray[index+1] = 0
#             workArray[index] += step


#do(arr, step, 0)
print(collector)
