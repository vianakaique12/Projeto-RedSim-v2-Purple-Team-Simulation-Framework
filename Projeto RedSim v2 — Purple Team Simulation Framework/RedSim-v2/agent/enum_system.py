import platform
import socket
import getpass

def collect_system_info():
    return {
        "os": platform.system(),
        "hostname": socket.gethostname(),
        "user": getpass.getuser(),
        "architecture": platform.machine()
    }
