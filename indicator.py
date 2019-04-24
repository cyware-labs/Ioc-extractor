import urllib
from bs4 import BeautifulSoup
import ioc_finder


defang_mappings = {
    "urls" :
        {
            'find': 'http',
            'replace': 'hxxp'
        },
    "email_addresses_complete":
        {
            'find': '@',
            'replace': '[@]'
        },
    "email_addresses":
        {
            'find': '@',
            'replace': '[@]'
        },
    "ipv4_cidrs":
        {
            "find": ".",
            'replace': '[.]'
        },
    "ipv4s":
        {
            "find": ".",
            'replace': '[.]'
        },
    "domains":
        {
            "find": ".",
            'replace': '[.]'
        },
    "ipv6s":
        {
            "find": "::",
            'replace': '[::]'
        }
}

def defang(data):
    for key in data:
        if key in defang_mappings.keys():
            new_data = data[key]
            data[key] = [d.replace(defang_mappings[key]['find'], defang_mappings[key]['replace']) for d in new_data]
    return data

def remove_html_data(text):
    soup = BeautifulSoup(text, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text


def find_iocs(text):
    iocs = ioc_finder.find_iocs(text)
    return iocs

def parse_indicators_url(link, fang=True):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(link, headers={'User-Agent': user_agent})
    f = urllib.request.urlopen(request)
    content = f.read().decode().lower()
    plain_text = remove_html_data(content)
    data = find_iocs(plain_text)
    data.pop('phone_numbers')
    if fang:
        print(data)
    else:
        defang_data = defang(data)
        print(defang_data)
    return


def parse_indicators_file(text, fang=True):
    content = text.lower()
    plain_text = remove_html_data(content)
    data = find_iocs(plain_text)
    data.pop('phone_numbers')
    if fang:
        print(data)
    else:
        defang_data = defang(data)
        print(defang_data)
    return