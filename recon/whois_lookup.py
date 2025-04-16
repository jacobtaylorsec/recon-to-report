import whois

def getwho_whois(domain):
    """
    
    Retrieves WHOIS data for a given domain.
    Returns the WHOIS information or an error message
    
    """
    try:
        return whois.whois(domain)
    except Exception as e:
        return f"WHOIS lookup failed: {e}"
    
    