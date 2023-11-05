import platform

architecture = (platform.architecture()[0])

machine = (platform.machine())

node = (platform.node())

system = (platform.system())

os_platform = (platform.platform(aliased=0, terse=0))

os_version = (platform.version())

os_name = (platform.freedesktop_os_release()["PRETTY_NAME"])

os_version_local = (platform.freedesktop_os_release()["VERSION"])

os_base = (platform.freedesktop_os_release()["ID_LIKE"])

os_support = (platform.freedesktop_os_release()["SUPPORT_URL"])