from promptflow import tool
import json

@tool
def prevadec(data):
    lines = data.split('\n')
    serial_number = ""
    hostname = ""
    ip_address = ""

    for line in lines:
        if "Serial Number:" in line:
            serial_number = line.split("Serial Number:")[1].strip()
        elif "Hostname:" in line:
            hostname = line.split("Hostname:")[1].strip()
        elif "IP Adresa:" in line:
            ip_address = line.split("IP Adresa:")[1].strip()

    return {
        "serial_number": serial_number,
        "hostname": hostname,
        "ip_address": ip_address
    }
