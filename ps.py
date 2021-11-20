import psutil

print("PID     NAME            CPU%")
print('-----------------------------')
for proc in psutil.process_iter():
    procs_info = proc.as_dict(attrs = ['pid','name','cpu_percent'])
    print("{}     {}              {}".format(procs_info['pid'],procs_info['name'],procs_info['cpu_percent']))
