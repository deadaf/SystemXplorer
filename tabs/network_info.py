from tkinter import Frame, Label, Tk
import psutil


def populate_network_info_tab(network_tab: Frame, root: Tk):
    # Get network usage statistics
    network_stats = psutil.net_io_counters()

    Label(network_tab, text="Network Usage Statistics").pack()
    Label(network_tab, text=f"Bytes Sent: {network_stats.bytes_sent} bytes").pack()
    Label(network_tab, text=f"Bytes Received: {network_stats.bytes_recv} bytes").pack()
    Label(network_tab, text=f"Packets Sent: {network_stats.packets_sent}").pack()
    Label(network_tab, text=f"Packets Received: {network_stats.packets_recv}").pack()
