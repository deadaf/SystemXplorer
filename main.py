import time
from tkinter import Frame, Tk, ttk

from tabs import (
    cpu_info,
    disk_info,
    mem_info,
    os_info,
    processes_info,
    network_info,
    battery_info,
)


class SystemXplorer:
    def __init__(self, root: Tk):
        self.root: Tk = root
        self.root.title("System-Xplorer")
        self.root.geometry("600x730")
        self.root.resizable(width=True, height=True)

    def system_info_interface(self):
        notebook = ttk.Notebook(self.root)

        os_tab = Frame(notebook)
        cpu_tab = Frame(notebook)
        mem_tab = Frame(notebook)
        disk_tab = Frame(notebook)
        processes_tab = Frame(notebook)
        network_tab = Frame(notebook)
        battery_tab = Frame(notebook)

        notebook.add(os_tab, text="OS Info")
        notebook.add(cpu_tab, text="CPU Info")
        notebook.add(mem_tab, text="Mem Info")
        notebook.add(disk_tab, text="Disk Info")

        notebook.add(processes_tab, text="Processes")
        notebook.add(network_tab, text="Network Info")
        notebook.add(battery_tab, text="Battery Info")

        notebook.pack(expand=True, fill="both")

        os_info.populate_os_info_tab(os_tab)
        cpu_info.populate_cpu_info_tab(cpu_tab, self.root)
        mem_info.populate_mem_info_tab(mem_tab, self.root)
        disk_info.populate_disk_info_tab(disk_tab)
        processes_info.populate_processes_info_tab(processes_tab)
        network_info.populate_network_info_tab(network_tab, self.root)
        battery_info.populate_battery_info_tab(battery_tab, self.root)


def print_authors_info():
    info = """
	System Xplorer - a comprehensive system information summary tool.
			
        Rohit Kumar
        - https://github.com/deadaf

        Vishwakant
        - https://github.com/vishwakant1602

        Lakshay Garg
        - https://github.com/lgarg12

        Vaibhav Bansal
        - https://github.com/Vaibhavbansal15


	"""
    print(info)


def main():
    print_authors_info()
    time.sleep(0.1)

    root = Tk()
    SystemXplorer(root).system_info_interface()
    root.mainloop()


if __name__ == "__main__":
    main()
