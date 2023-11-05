import psutil

mem_total = psutil.virtual_memory()[0]/1073741824 

def mem_available():
    mem_available = psutil.virtual_memory()[1]/1000000000 
    mem_free = psutil.virtual_memory()[4]/1000000000 

    mem_free_top = mem_available+mem_free
    
    return mem_free_top

def mem_percent():
    mem_percent = psutil.virtual_memory()[2] 

    return mem_percent

def mem_use():
    mem_use = psutil.virtual_memory()[3]/1000000000 

    return mem_use
    

swap_mem_total = psutil.swap_memory()[0]/1073741824 

swap_mem_used = psutil.swap_memory()[1]/1000000000 
 
swap_mem_free = psutil.swap_memory()[2]/1000000000 

swap_mem_percent = psutil.swap_memory()[3] 