__author__ = "Clive Walkden"
__email__ = "scripts.clive@mailsanitizr.com"

import re
from tqdm import tqdm


def process_log(log):
    print('## Processing file')
    requests = get_requests(log)

    print('## Calculating Bandwidth')
    bandwidth = get_bandwidth(requests)
    # files = get_files(requests)
    # totals = file_occur(files)

    return bandwidth


def get_requests(f):
    print('## Reading file')
    log_line = f.read()
    pat = (r''
           '(.+)\s-\s-\s'  # IP Address
           '\[(.+)\]\s'  # Date Time
           '"GET\s(.+)\s\w+/.+"\s'  # Requested File
           '(\d+)\s'  # Status
           '(\d+)\s'  # Bandwidth
           '"(.+)"\s'  # Referrer
           '"(.+)"'  # User Agent
           )
    print('## Finding matches')
    requests = find(pat, log_line)
    return requests


def find(pat, text):
    match = re.findall(pat, text)
    if match:
        return match
    return False


def get_files(requests):
    requested_files = []
    for req in tqdm(requests, desc="Counting Requests"):
        requested_files.append(req[2])
    return requested_files


def get_bandwidth(requests):
    total = 0
    for req in tqdm(requests, desc="Calculating Bandwidth"):
        total += int(req[4])
    return total


def file_occur(files):
    d = {}
    for file in tqdm(files, desc="Counting file Occurences"):
        d[file] = d.get(file, 0) + 1
    return d


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


if __name__ == '__main__':
    log_file = open('test-access.log', 'r')

    # process the log file and return a data dictionary
    print('## Loading File')
    data = process_log(log_file)

    # result = calculate_bandwidth(data)
    result = sizeof_fmt(data)

    print('## Log file recorded:')
    print(' - ' + result + ' of bandwidth usage.')
