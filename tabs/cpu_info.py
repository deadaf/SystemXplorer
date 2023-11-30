from tkinter import Frame, Label, Listbox, Tk

import psutil


def cpu_time():
    cpu_time = psutil.cpu_times()[0]

    return cpu_time


cpu_use = psutil.cpu_percent(interval=0.5, percpu=True)


def cpu_use_top():
    cpu_use_top = psutil.cpu_percent(interval=0.5, percpu=False)

    return cpu_use_top


cpu_info_core = psutil.cpu_count(logical=False)

cpu_info_thread = psutil.cpu_count(logical=True)

cpu_core_freq = psutil.cpu_freq(percpu=True)


def cpu_core_freq_top():
    cpu_core_freq_top = psutil.cpu_freq(percpu=False)

    return cpu_core_freq_top


def cpu_name():  # [0] => cpuname, [1] => all cpu
    cpu_name_top = []

    # Processors:
    with open("/proc/cpuinfo", "r") as f:
        info = f.readlines()

    cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
    for index, item in enumerate(cpuinfo):
        result = ("    " + str(index) + ": " + item).strip()
        cpu_name_top += [[str(result)] + [str(cpu_core_freq[index][0]) + " Mhz"]]

    return cpuinfo[0].strip(), cpu_name_top


CPU_NAME = cpu_name()


def populate_cpu_info_tab(cpu_tab: Frame, root: Tk):
    x = 10
    s = 5

    cpu_name = Label(cpu_tab, text="CPU:                        " + CPU_NAME[0])
    cpu_name.place(x=x, y=0 + s)

    cpu_use_text = Label(cpu_tab, text="CPU Use:                 %")
    cpu_use_text.place(x=x, y=21 + s * 2)
    cpu_use = Label(cpu_tab, text=int(cpu_use_top()), fg="black")
    cpu_use.place(x=(x * 9) + 62, y=21 + s * 2)

    cpu_core = Label(cpu_tab, text="CPU Core:                " + str(cpu_info_core))
    cpu_core.place(x=x, y=42 + s * 3)

    cpu_thread = Label(cpu_tab, text="CPU Thread:            " + str(cpu_info_thread))
    cpu_thread.place(x=x, y=63 + s * 4)

    cpu_freq_top_text = Label(cpu_tab, text="CPU Freq(Mhz): ")
    cpu_freq_top_text.place(x=x, y=84 + s * 5)
    cpu_freq_top = Label(cpu_tab, text=int(cpu_core_freq_top()[0]))
    cpu_freq_top.place(x=(x * 11) + 30, y=84 + s * 5)

    cpu_max_freq = Label(
        cpu_tab, text="CPU max. Freq:       " + str(cpu_core_freq_top()[2])
    )
    cpu_max_freq.place(x=x, y=105 + s * 6)

    cpu_max_freq = Label(
        cpu_tab, text="CPU min. Freq:        " + str(cpu_core_freq_top()[1])
    )
    cpu_max_freq.place(x=x, y=126 + s * 7)

    cpu_clock_text = Label(cpu_tab, text="CPU Clock(Second): ")
    cpu_clock_text.place(x=x, y=147 + s * 8)
    cpu_clock = Label(cpu_tab, text=int(cpu_time()))
    cpu_clock.place(x=(x * 14), y=147 + s * 8)

    core = Label(cpu_tab, text="Cores: ", font="Helvetica 17")
    core.place(x=x, y=230)

    cpu_list = CPU_NAME[1]
    list = Listbox(cpu_tab, width=53, height=18, font="Helvetica 12")
    for i in cpu_list:
        index = cpu_list.index(i)
        list.insert(index, i[0] + " @ " + i[1])

    list.place(x=x, y=260)

    def update():
        cpu_use["text"] = cpu_use_top()
        if cpu_use_top() < 50:
            cpu_use["fg"] = "green"
        elif cpu_use_top() >= 50:
            cpu_use["fg"] = "red"

        cpu_freq_top["text"] = int(cpu_core_freq_top()[0])

        cpu_clock["text"] = cpu_time()
        root.after(1000, update)  # run itself again after 1000 ms

    update()
