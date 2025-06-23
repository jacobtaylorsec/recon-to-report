import requests

def get_geolocation(ip):
    """
    Uses the ip-api service to get geolocation data for a given IP.
    Returns a dictionary with city, region, country, and organization.
    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data.get('status') == "success":
            return {
                "city": data.get('city', 'N/A'),
                "region": data.get('regionName', 'N/A'),
                "country": data.get('country', 'N/A'),
                "org": data.get('org', 'N/A')
            }
        else:
            return {"error": "Geolocation lookup failed"}
    except Exception as e:
        return {"error": f"Geolocation lookup failed: {e}"}
