import psutil

def get_system_usage():
    print("CPU Usage:", psutil.cpu_percent(), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")

if __name__ == "__main__":
    get_system_usage()
