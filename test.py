arr = [2, 3, 4, 5]  # [0,0,0,0] [1,0,0,0]
step = 0.5
workArray = [0, 0, 0, 0]
collector = []

while(workArray[0] <= arr[0]):

    while(workArray[1] <= arr[1]):

        while(workArray[2] <= arr[2]):

            while(workArray[3] <= arr[3]):
                collector.append(workArray)
                print(workArray)
                workArray[3] += step
            workArray[3] = 0
            workArray[2] += step

        workArray[2] = 0
        workArray[1] += step

    workArray[1] = 0
    workArray[0] += step

