import socket

def grab_banner(sock):
    """
    Attempts to retrieve a banner from an open socket.
    Returns the banner as a string or 'NO banner' if none found.
    """
    try:
        sock.settimeout(2)
        banner = sock.recv(1024).decode(errors='ignore').strip()
        return banner if banner else "NO banner"
    except Exception:
        return "NO banner"

def scan_ports(ip, ports=None):
    """
    Scans common ports on the target IP.
    Returns a list of tuples (port, banner) for ports that are open.
    """
    if ports is None:
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

    open_ports = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((ip, port))
            banner = grab_banner(sock)
            open_ports.append((port, banner))
            sock.close()
        except Exception:
            pass
    return open_ports

