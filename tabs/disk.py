import psutil


def disk_partitions():
    result = psutil.disk_partitions(all=False)

    disk_list = []

    for i in result:
        door = i[0].find("loop")
        
        if door == -1:
            disk_list.append([i[0], i[1], i[2]])
    
    return disk_list

def disk_usage():
    disk = disk_partitions()
    disks = []
    
    for i in disk:
        result = psutil.disk_usage(i[1])

        #print(i[0], i[1], i[2], result[0], result[1], result[2], result[3])
        
        disks.append([i[0], i[1], i[2], str(round(result[0]/1000000000, 1)), str(round(result[1]/1000000000,1)), str(round(result[2]/1000000000, 1)), result[3]])

    return disks

