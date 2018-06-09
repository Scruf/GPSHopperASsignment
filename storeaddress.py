#!/usr/bin/env python
import sys
import argparse
import csv
from pprint import pprint


parser = argparse.ArgumentParser()
parser.add_argument('--storeid')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.storeid:
        stores = []
        with open('acm_dealerlocator.csv') as csvfile:
            stores += [line for line in csv.DictReader(csvfile)]
        store = list(filter(lambda el: el.get('dealerlocator_id') == args.storeid, stores))
        if not store:
            print("Could not find store with %s id"%args.storeid)
        else:
            store_address = store[0].get('dealer_address1', " ") + " "+\
                            store[0].get('dealer_address2', " ") + " "+\
                            store[0].get('dealer_city', " ")
            store_status = store[0].get('dealer_store_status', " ")
            print(store_address , store_status) 
        
        
            
        # code goes here
        # print the store address and fix any broken info
        # address must inclue the full address (1 & 2 (if available)) and the city/state.
        # also show if the store status...eg. is open or opening soon
    else:
        print(parser.print_help())
        parser.exit(2)
