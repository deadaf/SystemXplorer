from tkinter import Frame, Label, Tk

import psutil

mem_total = psutil.virtual_memory()[0] / 1073741824


def mem_available():
    mem_available = psutil.virtual_memory()[1] / 1000000000
    mem_free = psutil.virtual_memory()[4] / 1000000000

    mem_free_top = mem_available + mem_free

    return mem_free_top


def mem_use():
    mem_use = psutil.virtual_memory()[3] / 1000000000

    return mem_use


swap_mem_total = psutil.swap_memory()[0] / 1073741824

swap_mem_used = psutil.swap_memory()[1] / 1000000000

swap_mem_free = psutil.swap_memory()[2] / 1000000000

swap_mem_percent = psutil.swap_memory()[3]


MEM_PERCENT = psutil.virtual_memory()[2]


def populate_mem_info_tab(mem_tab: Frame, root: Tk):
    x = 10
    s = 5
    g = 50

    Label(mem_tab, text="Memory: ", font="Helvetica 23").place(x=5, y=12)

    total_ram = Label(
        mem_tab,
        text="Total RAM:         " + str(round(mem_total, 1)) + " GB",
    )
    total_ram.place(x=x, y=0 + s + g)

    use_ram_text = Label(mem_tab, text="Used Ram:                GB ")
    use_ram_text.place(x=x, y=21 + g + s * 2)
    use_ram = Label(mem_tab, text=str(round(mem_use(), 1)))
    use_ram.place(x=(x * 10) + 20, y=21 + g + s * 2)

    available_ram_text = Label(mem_tab, text="Available Ram:         GB ")
    available_ram_text.place(x=x, y=42 + g + s * 3)
    available_ram = Label(mem_tab, text=str(round(mem_available(), 1)))
    available_ram.place(x=x * 12, y=42 + g + s * 3)

    mem_percent_text = Label(mem_tab, text="RAM Use:            %")
    mem_percent_text.place(x=x, y=63 + g + s * 4)
    mem_percent = Label(mem_tab, text=str(round(MEM_PERCENT, 1)), fg="black")
    mem_percent.place(x=(x * 13) + 5, y=63 + g + s * 4)

    Label(mem_tab, text="Swap: ", font="Helvetica 23").place(x=5, y=200)

    total_swap = Label(
        mem_tab,
        text="Total Swap Area:      " + str(round(swap_mem_total, 1)) + " GB",
    )
    total_swap.place(x=x, y=245)

    total_swap_use = Label(
        mem_tab,
        text="Used Swap Area:      " + str(round(swap_mem_used, 1)) + " GB",
    )
    total_swap_use.place(x=x, y=266 + s)

    total_swap_free = Label(
        mem_tab,
        text="Free Swap Area:      " + str(round(swap_mem_free, 1)) + " GB",
    )
    total_swap_free.place(x=x, y=286 + (s * 2))

    total_swap_percent = Label(
        mem_tab,
        text="Swap Area Percent:  %" + str(round(swap_mem_percent, 1)),
    )
    total_swap_percent.place(x=x, y=307 + (s * 3))

    def update():
        use_ram["text"] = round(mem_use(), 1)
        available_ram["text"] = round(mem_available(), 1)
        mem_percent["text"] = round(MEM_PERCENT, 1) - 5
        if round(MEM_PERCENT, 1) - 5 > 50:
            mem_percent["fg"] = "red"
        elif round(MEM_PERCENT, 1) - 5 <= 50:
            mem_percent["fg"] = "green"

        root.after(1000, update)  # run itself again after 1000 ms

    update()
