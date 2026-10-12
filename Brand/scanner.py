print("=== FIKSFC SCANNER v3 - UPGRADED ===")
import socket
target="127.0.0.1"
print(f"Scanning {target} - Safe localhost")
for port in [22,80,443,8000]:
    s=socket.socket(); s.settimeout(0.5)
    try: s.connect((target,port)); print(f"[OPEN] Port {port}")
    except: print(f"[CLOSED] Port {port}")
    s.close()
print("[OK] Scan done - Field secure")
