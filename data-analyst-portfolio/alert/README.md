# Daily Alert Monitoring Script

This project is a **daily monitoring system** that compares financial transaction data from two different sources:
1. **Payment Database** (requires login)  
2. **Bank Statement Website** (requires login)  

The main goal is to ensure data consistency between both systems by comparing the **remarks** column.  
Any mismatches are recorded in a .txt report and sent to a **Telegram bot** for daily monitoring.

---

## Schedule & Automation
The script runs **once daily at 07:00 AM** server time via a scheduled job.

---

## Workflow Diagram
![Flow Process](https://raw.githubusercontent.com/<Pribadiintan>/data-analyst-portfolio/main/alert/Flow%20Process.png)

---

## Tools & Libraries Used

- **Python (>= 3.8)** – Main programming language
- **pandas – Data cleaning**, merging, and comparison
- **requests – Sending reports** to Telegram Bot
- **Telegram Bot API** – Notification delivery
- **Cron Job / Task Scheduler** – For automation

---

## Features

- **Automated daily execution at 07:00 AM**
- **Compares two datasets using remarks column**
- **Generates a clear .txt report with mismatched records**
- **Sends results to Telegram bot for quick monitoring**
- **Can be adapted to run manually when needed**

---

## Future Improvements

- **CAutomate login to bank statement website using API or secure web scraping**
- **CStore results in a database for historical tracking**
- **CAdd email notifications as a backup alert method**
- **CImplement real-time monitoring instead of daily batch**

---

Author: Intan Puspita Pribadi
Category: Data Monitoring & Automation
Tags: Python, Data Monitoring, Telegram Bot, Automation








