# 🔍 Recon-to-Report: Python Recon Automation Tool

**Recon-to-Report** is a lightweight Python tool that performs automated reconnaissance on a target domain and generates a structured, easy-to-read Markdown report. It combines core recon techniques into one cohesive workflow — ideal for cybersecurity students, ethical hackers, or anyone building out their red team toolkit.

## ✨ Features

- ✅ **WHOIS Lookup** — Retrieves domain registration and ownership details  
- ✅ **DNS Enumeration** — Collects A, MX, NS, and TXT records  
- ✅ **IP Geolocation** — Locates the IP using public geolocation APIs  
- ✅ **Port Scanning** — Scans common TCP ports  
- ✅ **Banner Grabbing** — Attempts to identify services on open ports  
- ✅ **Markdown Reporting** — Outputs a clean, human-readable report  

This tool is intended **for educational and authorized security testing purposes only**.

Unauthorized scanning, probing, or information gathering on systems you do not own or have explicit permission to test is **illegal** and strictly discouraged.

By using this tool, you agree to take full responsibility for your actions and comply with all applicable laws and regulations.

The developer assumes **no liability** for any misuse or damage caused by this software.

---

## 📋 Prerequisites

- Python 3.10 or higher  
- Required Python packages (install via `requirements.txt`)

---

## 🛠️ How to Use

1. **Clone or download the project:**

   ```bash
   git clone https://github.com/jacobtaylorsec/recon-to-report.git
   cd recon-to-report
Install required dependencies:

bash
pip install -r requirements.txt
Run the tool:

bash
python recon.py
Follow the prompt to enter the target domain:

yaml
Enter target domain: example.com
After completion, open report.md to see the generated report.

⚠️ Legal and Ethical Notice
Please use this tool only on domains and systems for which you have explicit permission to test. Unauthorized scanning or probing is illegal and can have serious consequences.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Contribution
Contributions, issues, and feature requests are welcome! Feel free to open a pull request or issue on GitHub.

📫 Contact
Developed by Jacob Taylor — GitHub Profile
