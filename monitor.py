# monitor.py
# One job: measure internet speed and return the results.

import speedtest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_speed():
    try:
        logging.info("Running speed test...")
        st = speedtest.Speedtest()
        st.get_best_server()
        
        download_mbps = st.download() / 1_000_000   # Convert bits to megabits
        upload_mbps = st.upload() / 1_000_000
        ping = st.results.ping
        
        logging.info(f"Download: {download_mbps:.2f} Mbps | Upload: {upload_mbps:.2f} Mbps | Ping: {ping}ms")
        
        return {
            "download": round(download_mbps, 2),
            "upload": round(upload_mbps, 2),
            "ping": round(ping, 2)
        }
    
    except Exception as e:
        logging.error(f"Speed test failed: {e}")
        return None