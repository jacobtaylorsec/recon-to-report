import requests

def get_geolocation(ip):
    """

    Uses the ip-api service to get geolocation data for a given IP.
    Returns a formatted string with city, region, country, organization.

    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == "success":
            return f"{data.get('city')}, {data.get('regionName')}, {data.get('country')}, {data.get('org')})"
        else:
            return "Geolocation lookup failed"
    except Exception:
        return "Geolocation lookup failed"