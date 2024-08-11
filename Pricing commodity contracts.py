from datetime import date
import math

# Function to price any contract
def price_contract(in_dates, out_dates, in_prices, out_prices, rate, storage_cost_rate, maximum_storage, injection_withdrawal_cost_rate):
    price = 0
    volume = 0
    
    # Sort dates
    all_dates = sorted(set(in_dates + out_dates))
    
    for date in all_dates:
        # Withdrawal date
        if date in out_dates:
            if volume >= rate: 
                volume -= rate
                # Profit from selling gas
                price += rate * out_prices[out_dates.index(date)]
                # Withdrawal cost
                price -= rate * injection_withdrawal_cost_rate
            else:
                # We cannot withdraw more gas than is actually stored
                price += volume * out_prices[out_dates.index(date)]
                # Withdrawal cost
                price -= volume * injection_withdrawal_cost_rate
                print('Extraction of only %s on date %s as there is insufficient volume of gas stored'%(volume, date))
            print('Extracted gas on %s at a price of %s'%(date, out_prices[out_dates.index(date)]))
                
        # Injection date
        if date in in_dates:
            if volume <= maximum_storage - rate: 
                volume += rate
                # Cost to purchase gas
                price -= rate * in_prices[in_dates.index(date)]
                # Injection cost
                price -= rate * injection_withdrawal_cost_rate
            else:
                # We cannot inject more than can be stored
                price -= (maximum_storage - volume) * in_prices[in_dates.index(date)]
                # Injection cost
                price -= (maximum_storage - volume) * injection_withdrawal_cost_rate
                print('Injection of only %s on date %s as there is insufficient space in the storage facility'%((maximum_storage - volume),date))
            print('Injected gas on %s at a price of %s'%(date, in_prices[in_dates.index(date)]))
    
    # Storage cost
    price -= math.ceil((max(out_dates) - min(in_dates)).days // 30) * storage_cost_rate 
    return price

# Example usage of price_contract()
in_dates = [date(2022, 1, 1), date(2022, 2, 1), date(2022, 2, 21), date(2022, 4, 1)] #injection dates
in_prices = [20, 21, 20.5, 22] #prices on the injection days
out_dates = [date(2022, 1, 27), date(2022, 2, 15), date(2022, 3, 20), date(2022, 6, 1)] # extraction dates
out_prices = [23, 19, 21, 25] # prices on the extraction days
rate = 100000  # rate of gas in cubic feet per day
storage_cost_rate = 10000  # total volume in cubic feet
injection_withdrawal_cost_rate = 0.0005  # $/cf
max_storage_volume = 500000 # maximum storage capacity of the storage facility
result = price_contract(in_dates, out_dates, in_prices, out_prices, rate, storage_cost_rate, max_storage_volume, injection_withdrawal_cost_rate)
print()
print(f"The value of the contract is: ${result}")
