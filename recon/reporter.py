from datetime import datetime

def create_markdown_report(domain, ip, whois_data, geo, dns, ports):
    """
    Generates a Markdown report (report.md) that contains:
    - Target IP and geolocation
    - WHOIS information
    - DNS records
    - Open ports and their banners
    """
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(f"# Recon Report for {domain}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Target IP Address
        f.write("## Target IP Address\n")
        f.write("```\n")
        f.write(f"{ip}\n")
        f.write("```\n\n")

        # Geolocation
        f.write("## Geolocation\n")
        if isinstance(geo, dict):
            if "error" in geo:
                f.write(f"```\n{geo['error']}\n```\n\n")
            else:
                for key, value in geo.items():
                    f.write(f"- **{key.capitalize()}**: {value}\n")
                f.write("\n")
        else:
            f.write("```\n")
            f.write(f"{geo}\n")
            f.write("```\n\n")

        # WHOIS Information
        f.write("## WHOIS Information\n")
        if isinstance(whois_data, dict):
            if "error" in whois_data:
                f.write(f"```\n{whois_data['error']}\n```\n\n")
            else:
                for key, value in whois_data.items():
                    f.write(f"- **{key.replace('_', ' ').capitalize()}**: {value}\n")
                f.write("\n")
        else:
            f.write("```\n")
            f.write(str(whois_data))
            f.write("\n```\n\n")

        # DNS Records
        f.write("## DNS Records\n")
        for record_type, records in dns.items():
            f.write(f"### {record_type} Records\n")
            if isinstance(records, list) and records:
                for record in records:
                    f.write(f"- {record}\n")
            else:
                f.write("- No records found or error occurred.\n")
            f.write("\n")

        # Open Ports and Banners
        f.write("## Open Ports and Banners\n")
        if ports:
            for port, banner in ports:
                f.write(f"- Port {port}: {banner}\n")
        else:
            f.write("No open ports found.\n")

        f.write("\n---\n")
        f.write("Report generated using a custom Python reconnaissance tool.\n")

