import time

def simulate_c2():
    time.sleep(1)
    return {
        "event": "C2 beacon simulated",
        "technique": "T1071",
        "destination": "c2.fake-server.local"
    }
