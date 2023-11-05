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

def cpu_name(): # [0] => cpuname, [1] => all cpu
    cpu_name_top = []
    
    # Processors:
    with open("/proc/cpuinfo", "r")  as f:
        info = f.readlines()

    cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
    for index, item in enumerate(cpuinfo):
        result = ("    " + str(index) + ": " + item).strip()
        cpu_name_top += [[str(result)] + [str(cpu_core_freq[index][0])+" Mhz"]]

    return cpuinfo[0].strip(), cpu_name_top


cpu_name()