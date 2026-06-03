# complaint.py
# One job: decide if speeds are bad enough to complain, and format the complaint.

import csv
import os
from datetime import datetime
from config import BASELINE_SPEED_MBPS, DOWNLOAD_THRESHOLD, UPLOAD_THRESHOLD, LOG_FILE, COMPLAINT_LOG

def log_speed(speeds):
    file_exists = os.path.exists(LOG_FILE)
    
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        
        if not file_exists:
            writer.writerow(["timestamp", "download_mbps", "upload_mbps", "ping_ms"])
        
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            speeds["download"],
            speeds["upload"],
            speeds["ping"]
        ])

def should_complain(speeds):
    download_ok = speeds["download"] >= BASELINE_SPEED_MBPS * DOWNLOAD_THRESHOLD
    upload_ok = speeds["upload"] >= BASELINE_SPEED_MBPS * UPLOAD_THRESHOLD
    return not download_ok or not upload_ok

def format_complaint(speeds):
    return (
        f"⚠️ ISP Performance Alert: Getting {speeds['download']}Mbps down / "
        f"{speeds['upload']}Mbps up against a promised {BASELINE_SPEED_MBPS}Mbps. "
        f"Ping: {speeds['ping']}ms. #ISP #InternetSpeed #NetworkMonitoring"
    )

def log_complaint(message):
    with open(COMPLAINT_LOG, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")