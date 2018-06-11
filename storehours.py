#!/usr/bin/env python
"""Storehours assignment"""
import argparse
import csv
from datetime import datetime


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
        store = list(filter(lambda el: el['dealerlocator_id'] == args.storeid, hours))
        if store:
            #Sort stores by time to get the newest time for store
            store = sorted(store, key=lambda el: datetime.strptime(el.get('update_time'),\
                             "%Y-%m-%d %H:%M:%S"))[::-1][0]
            #Store store hours in dictionary to be displayed later
            store_hours = {
                "Monday":store.get('mon_start', "NaN") +" - "+store.get('mon_end', "NaN"),
                "Tuesday":store.get('tue_start', "NaN") +" - "+store.get('tue_end', "NaN"),
                "Wednsday":store.get("wed_start", "NaN") +" - "+store.get("wed_end", "NaN"),
                "Thursday":store.get("thus_start", "NaN") + " - "+store.get("thus_end", "NaN"),
                "Friday":store.get("fri_start", "NaN") + " - "+store.get("fri_end", "NaN"),
                "Saturday":store.get("sat_start", "NaN") + " - " +store.get("sat_end", "NaN"),
                "Sunday":store.get("sun_start", "NaN") + " - "+store.get("sun_end", "NaN")
            }
            #Store weekday numbers to be used to find whether store is open today or not
            day_week_map = {
                "6":"sun_start_openclose",
                "0":"mon_start_openclose",
                "1":"tue_start_openclose",
                "2":"wed_start_openclose",
                "3":"thu_start_openclose",
                "4":"fri_start_openclose",
                "5":"sat_start_openclose"
            }
            #Print store hours 
            print(store_hours)
            #Check if isopen is present 
            if args.isopen:
                #Its open so we get todays date weekday
                now = datetime.now().weekday()
                #Get status by weekday number 
                status = day_week_map.get(str(now))
                print("Store is %s"%store.get(status, " "))
    else:
        print(parser.print_help())
        parser.exit(2)
