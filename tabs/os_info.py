from tkinter import Label, Frame
import platform

ARCHITECTURE = platform.architecture()[0]

MACHINE = platform.machine()

NODE = platform.node()

SYSTEM = platform.system()

OS_PLATFORM = platform.platform(aliased=0, terse=0)

OS_VERSION = platform.version()

OS_NAME = platform.freedesktop_os_release()["PRETTY_NAME"]

OS_VERSION_LOCAL = platform.freedesktop_os_release()["VERSION"]

OS_BASE = platform.freedesktop_os_release()["ID_LIKE"]

OS_SUPPORT = platform.freedesktop_os_release()["SUPPORT_URL"]


def populate_os_info_tab(os_tab: Frame):
    s = 5
    x = 10

    os_name = Label(os_tab, text="OS Name:        " + OS_NAME)
    os_name.place(x=x, y=0 + s)

    system1 = Label(os_tab, text="System:           " + SYSTEM)
    system1.place(x=x, y=21 + s * 2)

    node = Label(os_tab, text="Node:               " + NODE)
    node.place(x=x, y=42 + s * 3)

    machine = Label(os_tab, text="Machine:          " + MACHINE)
    machine.place(x=x, y=63 + s * 4)

    os_platform = Label(os_tab, text="Platform:          " + OS_PLATFORM)
    os_platform.place(x=x, y=84 + s * 5)

    os_version = Label(os_tab, text="Version Time:  " + OS_VERSION)
    os_version.place(x=x, y=105 + s * 6)

    architecture = Label(os_tab, text="Architecture:    " + ARCHITECTURE)
    architecture.place(x=x, y=126 + s * 7)

    os_version_local = Label(os_tab, text="OS Version:      " + OS_VERSION_LOCAL)
    os_version_local.place(x=x, y=147 + s * 8)

    os_base = Label(os_tab, text="OS BASE:         " + OS_BASE)
    os_base.place(x=x, y=168 + s * 9)

    os_support = Label(os_tab, text="Support:           " + OS_SUPPORT)
    os_support.place(x=x, y=189 + s * 10)
