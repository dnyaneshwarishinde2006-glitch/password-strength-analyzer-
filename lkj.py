import socket

target = input("Enter IP address or hostname: ")

print(f"\nScanning {target}...\n")

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

open_ports = []

for port in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} ({common_ports[port]}) is OPEN")
        open_ports.append(port)

    s.close()

print("\n----- Vulnerability Report -----")

if open_ports:
    print("Open Ports Found:")
    for port in open_ports:
        print(f"- Port {port} ({common_ports[port]})")

    if 23 in open_ports:
        print("\nWarning: Telnet is insecure and may be vulnerable.")
else:
    print("No open common ports found.")

print("\nScan Completed.")