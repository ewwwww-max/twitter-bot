# Automated Twitter Complaint & Network Monitoring Bot

A Python automation bot that continuously monitors internet speed and automatically posts complaint tweets to the ISP when performance drops below a defined threshold.

## What it does
- Runs a speed test every 5 minutes using the Speedtest API
- Compares download/upload speeds against a configurable baseline
- Automatically posts a complaint tweet when speeds drop below 70% of the promised rate
- Logs all speed readings to a CSV file for historical analysis
- Logs all complaints to a text file as a local record

## Tech Stack
- **Python 3** — core language
- **Tweepy** — Twitter/X REST API integration
- **speedtest-cli** — real-time network performance measurement
- **python-dotenv** — secure credential management via environment variables

## Project Structure
twitter_bot/
├── main.py          # Entry point, runs the monitoring loop
├── monitor.py       # Speed test logic
├── complaint.py     # Threshold checking, complaint formatting, logging
├── config.py        # Configurable settings (baseline speed, thresholds, intervals)
├── speed_log.csv    # Auto-generated speed history
└── complaints.txt   # Auto-generated complaint log

## Setup
1. Clone the repository
2. Install dependencies: `pip install speedtest-cli tweepy python-dotenv`
3. Create a `.env` file with your Twitter API credentials:

API_KEY=your_api_key
API_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret

4. Configure your baseline speed in `config.py`
5. Run: `python main.py`

## Note on Twitter API
Tweet posting requires Twitter/X API write access credentials. The bot includes full Tweepy integration — to enable live tweeting, uncomment `client.create_tweet()` in `main.py` and add valid API credentials to `.env`.