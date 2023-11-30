from tkinter import Label, Frame
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

        # print(i[0], i[1], i[2], result[0], result[1], result[2], result[3])

        disks.append(
            [
                i[0],
                i[1],
                i[2],
                str(round(result[0] / 1000000000, 1)),
                str(round(result[1] / 1000000000, 1)),
                str(round(result[2] / 1000000000, 1)),
                result[3],
            ]
        )

    return disks


def populate_disk_info_tab(disk_tab: Frame):
    disk_use = disk_usage()

    for i in disk_use:
        index = disk_use.index(i)
        temp_disk = disk_use[index]

        disk_frame = Frame(
            disk_tab,
            highlightbackground="grey",
            highlightthickness=2,
            bg="white",
            width=480,
            height=100,
            borderwidth="2",
        )
        disk_frame.pack(pady=10)

        disk_fr = Label(disk_frame, bg="white", text="Device: " + temp_disk[0])
        disk_fr.place(x=10, y=5)

        disk_type = Label(disk_frame, bg="white", text="File Type: " + temp_disk[2])
        disk_type.place(x=10, y=30)

        disk_path = Label(disk_frame, bg="white", text="Path: " + temp_disk[1])
        disk_path.place(x=10, y=55)

        disk_capacity = Label(
            disk_frame,
            bg="white",
            text="Storage Capacity: " + temp_disk[3] + "GB",
        )
        disk_capacity.place(x=200, y=5)

        disk_free = Label(disk_frame, bg="white", text="Free: " + temp_disk[5] + "GB")
        disk_free.place(x=200, y=30)

        disk_free = Label(
            disk_frame,
            bg="white",
            text="Storage Percent: %" + str(temp_disk[6]),
        )
        disk_free.place(x=310, y=30)
