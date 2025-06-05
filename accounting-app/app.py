import argparse
import csv
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'records.csv')

def add_record(args):
    date = args.date or datetime.now().strftime('%Y-%m-%d')
    is_new = not os.path.exists(DATA_FILE)
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(['date', 'category', 'amount', 'description'])
        writer.writerow([date, args.category, args.amount, args.description])
    print('Record added.')

def list_records(args):
    if not os.path.exists(DATA_FILE):
        print('No records found.')
        return
    with open(DATA_FILE, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print('\t'.join(row))

def main():
    parser = argparse.ArgumentParser(description='简单记账工具')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='添加记录')
    add_parser.add_argument('amount', type=float, help='金额')
    add_parser.add_argument('-c', '--category', default='misc', help='分类')
    add_parser.add_argument('-d', '--description', default='', help='描述')
    add_parser.add_argument('--date', help='日期 YYYY-MM-DD')
    add_parser.set_defaults(func=add_record)

    list_parser = subparsers.add_parser('list', help='列出所有记录')
    list_parser.set_defaults(func=list_records)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
