import nmap
import os
import time

def start():
    #welcome message
    GREEN   = "\033[92m"
    CYAN    = "\033[96m"
    YELLOW  = "\033[93m"
    WHITE   = "\033[97m"
    RESET   = "\033[0m"
    BOLD    = "\033[1m"

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def banner():
        ascii_art = (
            GREEN + BOLD +
            "\n"
            "     ____.             .__        \n"
            "    |    |____ __  _  _|__|______ \n"
            "    |    \\__  \\\\ \\/ \\/ /  \\_  __ \\\n"
            "/\\__|    |/ __ \\\\     /|  ||  | \\/\n"
            "\\________(____  /\\/\\_/ |__||__|   \n"
            "              \\/                  \n"
            + RESET
        )

        border  = CYAN + BOLD + "╔══════════════════════════════════════════════════════════════╗" + RESET
        title   = CYAN + BOLD + "║" + RESET + "     " + YELLOW + BOLD + "SELAMAT DATANG DI  J A W I R - S C A N N E R" + RESET + "         " + CYAN + BOLD + "║" + RESET
        sub     = CYAN + BOLD + "║" + RESET + "              " + WHITE + "[ Network Recon Tool v1.0 ]" + RESET + "                   " + CYAN + BOLD + "║" + RESET
        border2 = CYAN + BOLD + "╚══════════════════════════════════════════════════════════════╝" + RESET

        info = [
            f" {GREEN}Author   :{RESET} NasibakarIsiAyam",
            f" {GREEN}Platform :{RESET} Linux / Windows / macOS",
            f" {GREEN}Status   :{RESET} {YELLOW}[ READY ]{RESET}",
            f" {GREEN}Github   :{RESET} github.com/NasibakarisiAyam/jawir-scanner",
        ]

        print(ascii_art)
        print(border)
        print(title)
        print(sub)
        print(border2)
        print()
        for line in info:
            print(line)
            time.sleep(0.08)
        print()

    if __name__ == "__main__":
        clear()
        banner()

    scanner = nmap.PortScanner()

    #define the target ip address
    target = input("Enter the target IP address: ")

    print("""
          Choose the type of scan you want to perform:
          1) SYN Scan (Stealth Scan)
          2) UDP Scan
          3) Comprehensive Scan (TCP Connect + SYN + UDP)
          4) Os Detection Scan + Version Detection
    """)
#buat fungsi untuk setiap jenis scan
    def syn(): scanner.scan(target, arguments = '-sS -p 1-1024 -v')
    def UDP(): scanner.scan(target, arguments = '-sU -p 1-1024 -v')
    def Comprehensive(): scanner.scan(target, arguments = '-A -p 1-1024 -v')
    def Os_Version(): scanner.scan(target, arguments = '-O -sV -p 1-1024 -v')

    scan_type = int(input("Enter the scan type (1-4): "))

    if scan_type == 1:
        print(f"Performing SYN Scan on {target}...")
        syn()
    elif scan_type == 2:
        print(f"Performing UDP Scan on {target}...")
        UDP()
    elif scan_type == 3:
        print(f"Performing Comprehensive Scan on {target}...")
        Comprehensive()
    elif scan_type == 4:
        print(f"Performing OS Detection + Version Detection Scan on {target}...")
        Os_Version()
    else:
        print("Invalid scan type selected. Please choose a number between 1 and 4.")
        start()

    #display the results
    print(scanner.scaninfo())

    hosts = scanner.all_hosts()
    if not hosts:
        print("No hosts found. Please check the target IP address and try again.")
        exit()
    
    host = hosts[0]
    print(f"Host: {host} ({scanner[host].hostname()})")
    print(scanner[host].state())

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in ports:
            print(f"port: {port}\tstate: {scanner[host][proto][port]['state']}")
   

start()