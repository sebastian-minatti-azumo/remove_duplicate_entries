import argparse
import csv
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def remove_duplicate_entries(csv_path):
    """
    Remove old entries from csv file.

    For instance:
      ZNGA_2018-12-06,2018-12-06,-1,True,ZNGA,-1,-0.55
      ZNGA_2018-12-06,2018-12-07,-1,True,ZNGA,-2,-0.55
      ZNGA_2018-12-06,2018-12-08,-1,True,ZNGA,-1,-0.55

    The algorithm will keep the last row, in this case
      ZNGA_2018-12-06,2018-12-08,-1,True,ZNGA,-1,-0.55
    :param csv_path: The path to the csv file.
    """
    entries = {}
    with open(csv_path) as csv_file:
        with open('output.csv', 'w', newline='') as out:
            reader = csv.DictReader(csv_file)
            writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
            for row in reader:
                key = row['id']
                if key in entries:
                    logger.error('removing old entry for {}'.format(key))
                entries[key] = row
            writer.writeheader()
            writer.writerows(entries.values())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv-path')
    args = parser.parse_args()

    remove_duplicate_entries(args.csv_path)
