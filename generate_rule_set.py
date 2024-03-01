import math
import re
import maxminddb
import requests
import json
import os
from aggregate6 import aggregate

dnsmasq_china_list = [
    "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf",
    "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf",
    "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/google.china.conf"
]

chnroutes2 = [
    "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
]

apnic = [
    "https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"
]

maxmind = [
    "https://raw.githubusercontent.com/Dreamacro/maxmind-geoip/release/Country.mmdb"
]

adguard = [
    "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
]

output_dir = "./rule-set"


def convert_dnsmasq(url: str) -> str:
    r = requests.get(url)
    domain_suffix_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                domain = re.match(r"server=\/(.*)\/(.*)", line)
                if domain:
                    domain_suffix_list.append(domain.group(1))
    result = {
        "version": 1,
        "rules": [
            {
                "domain_suffix": []
            }
        ]
    }
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filepath = os.path.join(output_dir, url.split("/")[-1] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_chnroutes2(url: str) -> str:
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                ip_cidr_list.append(line)
    result = {
        "version": 1,
        "rules": [
            {
                "ip_cidr": []
            }
        ]
    }
    result["rules"][0]["ip_cidr"] = ip_cidr_list
    filepath = os.path.join(output_dir, url.split("/")[-1] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_apnic(url: str, country_code: str, ip_version: str) -> str:
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                if line.split("|")[1] == country_code and line.split("|")[2] == ip_version:
                    if ip_version == "ipv4":
                        ip_cidr_list.append(line.split(
                            "|")[3] + "/" + str(32 - int(math.log2(int(line.split("|")[4])))))
                    else:
                        ip_cidr_list.append(line.split(
                            "|")[3] + "/" + line.split("|")[4])
    result = {
        "version": 1,
        "rules": [
            {
                "ip_cidr": []
            }
        ]
    }
    result["rules"][0]["ip_cidr"] = aggregate(ip_cidr_list)
    filepath = os.path.join(output_dir, "apnic-" +
                            country_code.lower() + "-" + ip_version + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_maxmind(url: str, country_code: str, ip_version: str) -> str:
    r = requests.get(url)
    with open("Country.mmdb", "wb") as f:
        f.write(r.content)
    f.close()
    reader = maxminddb.open_database("Country.mmdb")
    ip_cidr_list = []
    for cidr, info in reader.__iter__():
        if info.get("country") is not None:
            if info["country"]["iso_code"] == country_code:
                if ip_version == "ipv4" and cidr.version == 4:
                    ip_cidr_list.append(str(cidr))
                elif ip_version == "ipv6" and cidr.version == 6:
                    ip_cidr_list.append(str(cidr))
        elif info.get("registered_country") is not None:
            if info["registered_country"]["iso_code"] == country_code:
                if ip_version == "ipv4" and cidr.version == 4:
                    ip_cidr_list.append(str(cidr))
                elif ip_version == "ipv6" and cidr.version == 6:
                    ip_cidr_list.append(str(cidr))
    reader.close()
    result = {
        "version": 1,
        "rules": [
            {
                "ip_cidr": []
            }
        ]
    }
    result["rules"][0]["ip_cidr"] = aggregate(ip_cidr_list)
    filepath = os.path.join(output_dir, "maxmind-" +
                            country_code.lower() + "-" + ip_version + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_adguard(url: str) -> str:
    r = requests.get(url)
    domain_list = []
    domain_suffix_list = []
    domain_keyword_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if line.strip() == "":
                continue

            if line.startswith("!"):
                continue
            if line.startswith("#"):
                continue

            if line.startswith("@@"):
                continue

            if "*" in line:
                continue
            if "?" in line:
                continue

            if line.endswith("$important"):
                line = line[:-10]

            if line.startswith("://"):
                if line.endswith("^"):
                    domain_list.append(line[3:-1])
                else:
                    print("Warning: " + line)
            elif line.startswith("||"):
                if line.endswith("^"):
                    domain_suffix_list.append(line[2:-1])
                else:
                    domain_keyword_list.append(line[2:])
            elif line.startswith("|"):
                if line.endswith("^"):
                    domain_list.append(line[1:-1])
                else:
                    domain_keyword_list.append(line[1:])
            else:
                if line.endswith("^"):
                    domain_suffix_list.append(line)
    result = {
        "version": 1,
        "rules": [
            {
                "domain": [],
                "domain_keyword": [],
                "domain_suffix": []
            }
        ]
    }
    result["rules"][0]["domain"] = domain_list
    result["rules"][0]["domain_keyword"] = domain_keyword_list
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filepath = os.path.join(output_dir, url.split("/")[-1] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_adguard_unblock(url: str) -> str:
    r = requests.get(url)
    domain_suffix_list = []
    domain_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        print("\n")
        for line in lines:
            if line.strip() == "":
                continue

            if line.startswith("!"):
                continue
            if line.startswith("#"):
                continue

            if "*" in line:
                continue
            if "?" in line:
                continue

            if line.endswith("$important"):
                line = line[:-10]

            if line.startswith("@@||"):
                if line.endswith("^|"):
                    domain_suffix_list.append(line[4:-2])
                elif line.endswith("^"):
                    domain_suffix_list.append(line[4:-1])
                else:
                    print("Warning: " + line)
            elif line.startswith("@@|"):
                if line.endswith("^|"):
                    domain_list.append(line[3:-2])
                elif line.endswith("^"):
                    domain_list.append(line[3:-1])
                else:
                    print("Warning: " + line)
            elif line.startswith("@@"):
                if line.endswith("^|"):
                    domain_suffix_list.append(line[2:-2])
                elif line.endswith("^"):
                    domain_suffix_list.append(line[2:-1])
                else:
                    print("Warning: " + line)
    result = {
        "version": 1,
        "rules": [
            {
                "domain": [],
                "domain_suffix": []
            }
        ]
    }
    result["rules"][0]["domain"] = domain_list
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filepath = os.path.join(output_dir, url.split("/")[-1] + ".unblock.json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def main():
    files = []
    os.mkdir(output_dir)
    for url in dnsmasq_china_list:
        filepath = convert_dnsmasq(url)
        files.append(filepath)
    for url in chnroutes2:
        filepath = convert_chnroutes2(url)
        files.append(filepath)
    for url in apnic:
        filepath = convert_apnic(url, "CN", "ipv4")
        files.append(filepath)
        filepath = convert_apnic(url, "CN", "ipv6")
        files.append(filepath)
    for url in maxmind:
        filepath = convert_maxmind(url, "CN", "ipv4")
        files.append(filepath)
        filepath = convert_maxmind(url, "CN", "ipv6")
        files.append(filepath)
    for url in adguard:
        filepath = convert_adguard(url)
        files.append(filepath)
        filepath = convert_adguard_unblock(url)
        files.append(filepath)
    print("rule-set source generated:")
    for filepath in files:
        print(filepath)
    for filepath in files:
        srs_path = filepath.replace(".json", ".srs")
        os.system("sing-box rule-set compile --output " +
                  srs_path + " " + filepath)


if __name__ == "__main__":
    main()
