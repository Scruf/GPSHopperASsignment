#!/usr/bin/env python
import sys
import argparse
import csv
from pprint import pprint


parser = argparse.ArgumentParser()
parser.add_argument('--storeid')
parser.add_argument('--isopen', action='store_true', help='test if the store is open now')


if __name__ == "__main__":
    args = parser.parse_args()
    if args.storeid:
        stores = []
        with open('acm_dealerlocator.csv') as csvfile:
            stores += [line for line in csv.DictReader(csvfile)]
        hours = []
        with open('acm_storehours.csv') as csvfile:
            hours += [line for line in csv.DictReader(csvfile)]
        
      
        # code goes here
        # using the storeid, display hours
        # if args.isopen is true check if the store is open now.
    else:
        print(parser.print_help())
        parser.exit(2)
