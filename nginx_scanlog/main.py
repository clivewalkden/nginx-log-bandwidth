__author__ = "Clive Walkden"
__email__ = "scripts.clive@mailsanitizr.com"

import click
import mmap
import re
from tqdm import tqdm


@click.command()
@click.argument('filename')
def init(filename):
    if not filename:
        filename = 'access.log'

    # process the log file and return a data dictionary
    print('## Loading File')
    bandwidth = process_log(filename)

    print("\n## Log file recorded:")
    print(' - Total lines: ' + str(bandwidth['total_records']))
    print(' - ' + str(bandwidth['counted']) + ' rows included, ' + str(bandwidth['skipped']) + ' rows skipped.')
    print('-----------------------------------')
    print(' - ' + bandwidth['total_bandwidth'] + ' of bandwidth usage.')
    print('-----------------------------------')


def process_log(log):
    print('## Reading file')
    log_file = open(log, 'r')

    total_records = get_num_lines(log)
    counted = 0
    skipped = 0
    total_bandwidth = 0

    print('## Calculating Bandwidth')
    for line in tqdm(log_file, desc='Scanning rows', total=total_records):
        data = find(line)
        if data:
            counted += 1
            total_bandwidth += int(data[0][5])
        else:
            skipped += 1

    log_file.close()
    result = {
        'total_records': total_records,
        'counted': counted,
        'skipped': skipped,
        'total_bandwidth': sizeof_fmt(total_bandwidth)
    }

    return result


def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    fp.close()
    return lines


def find(text):
    pat = (r''
           '(.+)\s-\s-\s'  # IP Address
           '\[(.+)\]\s'  # Date Time
           '"(DELETE|HEAD|GET|OPTIONS|POST|PUT)\s(.+)\s\w+/.+"\s'  # Requested File
           '(\d+)\s'  # Status
           '(\d+)\s'  # Bandwidth
           '"(.+)"\s'  # Referrer
           '"(.+)"'  # User Agent
           )
    match = re.findall(pat, text)

    if match:
        return match
    else:
        log = open('skipped.log', 'a')
        log.write(text)
        log.close()

    return False


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


if __name__ == '__main__':
    init()
