import time
from datetime import datetime

log_file_path = "/logs/logger.log"

while True:
    with open(log_file_path, "a") as f:
        f.write(f"[{datetime.now()}] Logger is active.\n")
    time.sleep(5)  # Write every 5 seconds
