import glob
import os
import pandas as pd 


def main():
    x =find_files()
    combine_files(x)

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


if __name__ == '__main__':
    main()