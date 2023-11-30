from tkinter import Frame, ttk
import psutil


def get_running_processes():
    processes = []
    for proc in psutil.process_iter(
        [
            "pid",
            "name",
            "status",
            "cpu_percent",
            "memory_info",
            "create_time",
            "username",
        ]
    ):
        try:
            info = proc.info
            processes.append(
                {
                    "pid": info["pid"],
                    "name": info["name"],
                    "status": info["status"],
                    "cpu_percent": info["cpu_percent"],
                    "memory_info": info["memory_info"],
                    "create_time": info["create_time"],
                    "username": info["username"],
                }
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes


def populate_processes_info_tab(process_tab: Frame):
    processes_use = get_running_processes()

    # Create a Treeview widget to display the process information
    process_tree = ttk.Treeview(
        process_tab,
        columns=(
            "pid",
            "name",
            "status",
            "cpu_percent",
            "memory_info",
            "create_time",
            "username",
        ),
    )
    process_tree.heading("#1", text="PID")
    process_tree.heading("#2", text="Name")
    process_tree.heading("#3", text="Status")
    process_tree.heading("#4", text="CPU %")
    process_tree.heading("#5", text="Memory Info")
    process_tree.heading("#6", text="Create Time")
    process_tree.heading("#7", text="Username")
    process_tree.column("#1", width=50)
    process_tree.column("#2", width=150)
    process_tree.column("#3", width=80)
    process_tree.column("#4", width=70)
    process_tree.column("#5", width=100)
    process_tree.column("#6", width=120)
    process_tree.column("#7", width=100)

    for process in processes_use:
        process_tree.insert(
            "",
            "end",
            values=(
                process["pid"],
                process["name"],
                process["status"],
                process["cpu_percent"],
                process["memory_info"],
                process["create_time"],
                process["username"],
            ),
        )

    process_tree.pack(fill="both", expand=True)
