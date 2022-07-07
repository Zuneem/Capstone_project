import glob
import os
import pandas as pd 


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


if __name__ == '__main__':
    main()