import psutil

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_info', 'create_time', 'username']):
        try:
            info = proc.info
            processes.append({
                'pid': info['pid'],
                'name': info['name'],
                'status': info['status'],
                'cpu_percent': info['cpu_percent'],
                'memory_info': info['memory_info'],
                'create_time': info['create_time'],
                'username': info['username'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes
