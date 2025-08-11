# 📡 Daily Alert Monitoring Script

This project is a **daily monitoring system** that compares financial transaction data from two different sources:

1. **Payment Database** (requires login)  
2. **Bank Statement Website** (requires login)  

The main goal is to ensure data consistency between both systems by comparing the **remarks** column.  
Any mismatches are recorded in a `.txt` report and sent to a **Telegram bot** for daily monitoring.

---

## 📅 Schedule & Automation

The script runs **once daily at 07:00 AM** server time via a scheduled job.

Example for Linux `cron` job:
```bash
0 7 * * * /usr/bin/python3 /path/to/alert_monitoring.py


📂 Workflow Diagram
flowchart TD
    A[Start - 07:00 AM] --> B[Login to Payment Database]
    B --> C[Fetch Payment Data]
    C --> D[Login to Bank Statement Website]
    D --> E[Fetch Bank Statement Data]
    E --> F[Clean & Normalize Data]
    F --> G[Compare Remarks Column]
    G --> H[Generate TXT Report of Differences]
    H --> I[Send Report to Telegram Bot]
    I --> J[End]


🛠 Tools & Libraries Used
Python (>= 3.8) – Main programming language

pandas – Data cleaning, merging, and comparison

requests – Sending reports to Telegram Bot

Telegram Bot API – Notification delivery

Cron Job / Task Scheduler – For automation


📊 Features
Automated daily execution at 07:00 AM

Compares two datasets using remarks column

Generates a clear .txt report with mismatched records

Sends results to Telegram bot for quick monitoring

Can be adapted to run manually when needed


📂 Project Structure
bash
Copy
Edit
alert-monitoring/
│
├── data/
│   ├── payment_data.csv          # Dummy payment dataset (for testing)
│   ├── bank_data.csv             # Dummy bank statement dataset (for testing)
│
├── images/
│   └── flow_diagram.png          # Workflow diagram (optional)
│
├── alert_monitoring.py           # Main Python script
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation


⚙️ Installation
Clone this repository

bash
Copy
Edit
git clone https://github.com/yourusername/alert-monitoring.git
cd alert-monitoring
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up your environment variables

Replace YOUR_TELEGRAM_BOT_TOKEN and YOUR_CHAT_ID in alert_monitoring.py with your credentials.

▶️ Usage
Run Manually
bash
Copy
Edit
python alert_monitoring.py
Run Automatically (Linux)
Add this line to crontab:

bash
Copy
Edit
0 7 * * * /usr/bin/python3 /path/to/alert_monitoring.py
📌 Future Improvements
Automate login to bank statement website using API or secure web scraping

Store results in a database for historical tracking

Add email notifications as a backup alert method

Implement real-time monitoring instead of daily batch

Author: Intan Puspita Pribadi
Category: Data Monitoring & Automation
Tags: Python, Data Monitoring, Telegram Bot, Automation
