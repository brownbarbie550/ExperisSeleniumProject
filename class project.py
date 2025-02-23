import os
import requests
from bs4 import BeautifulSoup
from scapy.all import IP, TCP, sr1
from urllib.parse import urlparse


def check_all_ports(ip):
    open_ports = []
    for port_number in range(1, 65536):
        tcp_scan = IP(dst=ip) / TCP(dport=port_number, flags="S")
        tcp_resp = sr1(tcp_scan, verbose=0, timeout=0.1)
        if tcp_resp and tcp_resp.haslayer(TCP) and tcp_resp(TCP).flags == 0x12:
            open_ports.append(port_number)
            print(f"Port {port_number} is open")
    return open_ports


def web_scan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            bsoup = BeautifulSoup(response.text, "html.parser")
            found_links = bsoup.find_all("a")
            for link in found_links:
                print(f"mission accomplished link: {link.get('href')}")
            download_path = "C:\\Users\\dagi2\\Downloads\\New folder"
        else:
            print(f"mission failed, couldn't retrieve content from {url}. status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")



def download_pic_pdf_or_link(url, download_path):
    try:
        reponse = requests.get(url, stream=True)
        if response.status_code == 200:
            content_type = response.headers.get("Content-Type")
            if "pdf" in content_type.lower():
                download_path = os.path.join(download_path, "pdf")
            elif "image" in content_type.lower():
                download_path = os.path.join(download_path, "image")
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            file = os.path.join(download_path, os.path.basename(urlparse(url).path))
            with open(file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                print(f"Successfully Downloaded: {file}")
    except Exception as e:
        print(f"something went wrong in the process of downloading {url:} {e}")



if __name__ == "__main__":
    url_to_scan = input("what URL would you like to scan?:")
    ip_to_scan = input("what IP would you like to scan?:")
    web_scan(url_to_scan)
    open_ports = check_all_ports(ip_to_scan)
    print("Open ports:", open_ports)
    download_path = r"C:\\Users\\dagi2\\Downloads\\New folder"
    url = url_to_scan
    download_pic_pdf_or_link(url, download_path)



