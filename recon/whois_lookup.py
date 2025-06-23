import whois

def get_whois(domain):
    """
    Retrieves WHOIS data for a given domain.
    Returns a dictionary with relevant fields or an error message.
    """
    try:
        data = whois.whois(domain)
        return {
            "domain_name": str(data.domain_name),
            "registrar": str(data.registrar),
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "name_servers": data.name_servers,
            "emails": data.emails
        }
    except Exception as e:
        return {"error": f"WHOIS lookup failed: {e}"}
    
    