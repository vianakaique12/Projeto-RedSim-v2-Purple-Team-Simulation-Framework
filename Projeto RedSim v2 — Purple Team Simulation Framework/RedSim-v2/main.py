from agent.enum_system import collect_system_info
from agent.persistence_sim import simulate_persistence
from agent.c2_beacon_sim import simulate_c2
from blue_team.detection_engine import analyze_event
from datetime import datetime
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "events.log")

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

def main():
    log("RedSim v2 started")

    system_info = collect_system_info()
    log(f"Discovery: {system_info}")

    persistence_event = simulate_persistence()
    log(f"Red Team: {persistence_event}")

    c2_event = simulate_c2()
    log(f"Red Team: {c2_event}")

    for event in [persistence_event, c2_event]:
        alerts = analyze_event(event)
        for alert in alerts:
            log(f"ALERT: {alert}")

    log("RedSim v2 finished")

if __name__ == "__main__":
    main()
    print("Simulation completed. Check logs/events.log")
    