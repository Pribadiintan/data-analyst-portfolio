
---

### **📜 alert_monitoring.py**
```python
import pandas as pd
import requests
import datetime

# ===== CONFIG =====
PAYMENT_DB_FILE = "data/payment_data.csv"   # Dummy file, replace with DB query
BANK_STATEMENT_FILE = "data/bank_data.csv"  # Dummy file, replace with scraping/API
OUTPUT_FILE = "daily_report.txt"
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# ===== FETCH PAYMENT DATA =====
def fetch_payment_data():
    """Fetch payment data from database (dummy example)."""
    df_payment = pd.read_csv(PAYMENT_DB_FILE)
    return df_payment

# ===== FETCH BANK STATEMENT DATA =====
def fetch_bank_statement():
    """Fetch bank statement data from website (dummy example)."""
    df_bank = pd.read_csv(BANK_STATEMENT_FILE)
    return df_bank

# ===== COMPARE DATA =====
def compare_data(df_payment, df_bank):
    """Compare datasets using the remarks column."""
    merged = pd.merge(df_payment, df_bank, on="remarks", how="outer", indicator=True)
    differences = merged[merged["_merge"] != "both"]
    return differences

# ===== GENERATE TXT REPORT =====
def generate_txt_report(differences):
    """Generate TXT report for daily monitoring."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"Daily Monitoring Report - {datetime.date.today()}\n")
        f.write("="*40 + "\n\n")
        if differences.empty:
            f.write("✅ No differences found.\n")
        else:
            f.write("❌ Differences found:\n\n")
            f.write(differences.to_string(index=False))
    return OUTPUT_FILE

# ===== SEND TO TELEGRAM =====
def send_to_telegram(file_path):
    """Send report file to Telegram bot."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    with open(file_path, "rb") as file:
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "caption": f"Daily Monitoring Report - {datetime.date.today()}"
        }
        requests.post(url, data=payload, files={"document": file})

# ===== MAIN =====
if __name__ == "__main__":
    df_payment = fetch_payment_data()
    df_bank = fetch_bank_statement()
    differences = compare_data(df_payment, df_bank)
    report_file = generate_txt_report(differences)
    send_to_telegram(report_file)
    print(f"Report generated and sent to Telegram: {report_file}")
