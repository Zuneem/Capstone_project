import glob
import os
import pandas as pd
import csv 


def main():
    x =find_files()
    combine_files(x)
    new_file = 'order.csv'
    total_units(new_file)

# go to the Directory and take seven most recent sales reports 

def find_files():
    files_path = "/Users/zuneemtamrakar/Desktop/daily_sales/*.csv"
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True) 
    needed_files = files[0:7]
    return needed_files
    
# combine those seven sales reports and combine them into one csv and save it in the local directory

def combine_files(needed_files):
    for file in needed_files:
        if file.endswith('.csv'):
            master_df = pd.concat(map(pd.read_csv, needed_files))
    master_df.to_csv('order.CSV', index=False)


# update the created csv file with only the sizes for a column and the total quantity for each size on second column

def total_units(new_file):
    sales=pd.read_csv(new_file)
    sales = sales.groupby(['size'])[['quantity']].sum()
    sales.to_csv('sales.CSV')

# assign variable to each size's quantity
        
def get_var(sales):
    new_dict = {}
    with open(sales) as f:
        reader = csv.DictReader(f)
        for line in reader:
            if line['size'] not in new_dict:
                new_dict[line['size']] = int(line['quantity'].replace('.0', ''))

    return new_dict

# different sizes are sold a pack. For example, 11x14 is sold in a pack of 7; while 
# 16x20 is sold in a pack of 5. So, we need to calculate the number of packs we need
# to order

def get_order_quantity(quantity,pack):
    if quantity % pack == 0:
        return quantity // pack
    else :
        return (quantity // pack ) +1

if __name__ == '__main__':
    main()