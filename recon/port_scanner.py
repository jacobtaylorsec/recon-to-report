import socket

def grab_banner(ip,port):
    """
    
    Attempts to connect to the given IP and port to retrieve a banner.
    Returns the banner as a string, or "no banner" if unsuccessful
    
    """
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except Exception:
        return "NO banner"
    
def scan_ports(ip, ports=None):
    """
    
    Scans common ports on the target IP.
    Returns a list of touples (port, banner) for ports that are open.
    
    """
    if ports is None:
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

        open_ports = []
        for port in ports:
            try:
                s = socket.socket()
                s.settimeout(0.5)
                s.connect((ip, port))
                banner = grab_banner(ip, port)
                open_ports.append((port, banner))
                s.close()
            except Exception:
                pass
            return open_ports
