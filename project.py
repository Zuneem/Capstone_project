import glob
import os
import pandas as pd
import csv 
import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random


def main():
    x =find_files()
    combine_files(x)
    new_file = 'order.csv'
    total_units(new_file)
    sales = 'sales.csv'
    place_order(get_var(sales))

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

# once we have the quantity that we need to order, we can how automate the
# order process using selenium

def place_order(new_dict):
    
    eleven_x_fourteen = get_order_quantity(new_dict['11x14'],7)
    eight_x_ten = get_order_quantity(new_dict['8x10'],10)
    sixteen_x_twenty = get_order_quantity(new_dict['16x20'],5)
    twelve_x_twentyfour = get_order_quantity(new_dict['12x24'],3)
    eighteen_x_twentyfour = get_order_quantity(new_dict['18x24'],3)
    twentyfour_x_thirtysix = get_order_quantity(new_dict['24x36'],1)
    
    # print(eleven_x_fourteen)
    # print(eight_x_ten)
    # print(sixteen_x_twenty)
    # print(twelve_x_twentyfour)
    # print(eighteen_x_twentyfour)
    # print(twentyfour_x_thirtysix)
    
    t = random.randint(1,3)
    browser = wd.Chrome('/Users/zuneemtamrakar/bin/chromedriver')
    browser.implicitly_wait(20)

    try:
        browser.get('https://www.hobbylobby.com/Art-Supplies/Painting-Canvas-Art-Surfaces/Blank-Canvas/Super-Value-Blank-Canvas-Set---11%22-x-14%22/p/80872879')
        browser.implicitly_wait(25)
        quan_11x14 = browser.find_element(By.XPATH, '//*[@id="qty"]')
        quan_11x14.clear()
        time.sleep(t)
        type(quan_11x14)
        quan_11x14.send_keys(eleven_x_fourteen)
        time.sleep(t)
        add1 = browser.find_element(By.XPATH, '//*[@id="addToCartButton"]/span')
        add1.click()
        time.sleep(t)
    except NoSuchElementException:
        print('11x14 is out of stock')
        pass

    try: 
        browser.get('https://www.hobbylobby.com/Art-Supplies/Painting-Canvas-Art-Surfaces/Blank-Canvas/Super-Value-Blank-Canvas-Set---8%22-x-10%22/p/80872876')
        quan_8x10 = browser.find_element(By.XPATH, '//*[@id="qty"]')
        quan_8x10.clear()
        time.sleep(t)
        type(quan_8x10)
        quan_8x10.send_keys(eight_x_ten)
        time.sleep(t)
        add2 = browser.find_element(By.XPATH, '//*[@id="addToCartButton"]/span')
        add2.click()
        time.sleep(t)
    except NoSuchElementException:
        print('8x10 is out of stock')
        pass

    try:
        browser.get('https://www.hobbylobby.com/Art-Supplies/Painting-Canvas-Art-Surfaces/Blank-Canvas/Super-Value-Blank-Canvas-Set---16%22-x-20%22/p/80872705')
        quan_16x20 = browser.find_element(By.XPATH, '//*[@id="qty"]')
        quan_16x20.clear()
        time.sleep(t)
        type(quan_16x20)
        quan_16x20.send_keys(sixteen_x_twenty)
        time.sleep(t)
        add3 = browser.find_element(By.XPATH, '//*[@id="addToCartButton"]/span')
        add3.click()
        time.sleep(t)
    except NoSuchElementException:
        print('16x20 is out of stock')
        pass

    try:
        browser.get("https://www.hobbylobby.com/Art-Supplies/Painting-Canvas-Art-Surfaces/Blank-Canvas/Master's-Touch-Blank-Canvas-Panel-Set---12%22-x-24%22/p/80790634")
        quan_12x24 = browser.find_element(By.XPATH, '//*[@id="qty"]')
        quan_12x24.clear()
        time.sleep(t)
        type(quan_12x24)
        quan_12x24.send_keys(twelve_x_twentyfour)
        time.sleep(t)
        add4 = browser.find_element(By.XPATH, '//*[@id="addToCartButton"]/span')
        add4.click()
        time.sleep(t)
    except NoSuchElementException:
        print('12x24 is out of stock')
        pass

    try:
        browser.get("https://www.hobbylobby.com/Art-Supplies/Painting-Canvas-Art-Surfaces/Blank-Canvas/Master's-Touch-Blank-Canvas-Panel-Set---18%22-x-24%22/p/7729")
        quan_18x24 = browser.find_element(By.XPATH, '//*[@id="qty"]')
        quan_18x24.clear()
        time.sleep(t)
        type(quan_18x24)
        quan_18x24.send_keys(eighteen_x_twentyfour)
        time.sleep(t)
        add5 = browser.find_element(By.XPATH, '//*[@id="addToCartButton"]/span')
        add5.click()
        time.sleep(t)
    except NoSuchElementException:
        print('18x24 is out of stock')
        pass

    try:
        browser.get("https://www.hobbylobby.com/Art-Supplies/Painting-Canvas-Art-Surfaces/Blank-Canvas/Master's-Touch-Grandeur-Collection-Blank-Canvas---24%22-x-36%22/p/80936695")
        quan_24x36 = browser.find_element(By.XPATH, '//*[@id="qty"]')
        quan_24x36.clear()
        time.sleep(t)
        type(quan_24x36)
        quan_24x36.send_keys(twentyfour_x_thirtysix)
        time.sleep(t)
        add6 = browser.find_element(By.XPATH, '//*[@id="addToCartButton"]/span')
        add6.click()
        time.sleep(8)
    except NoSuchElementException:
        print('24x36 is out of stock')
        pass

    cart = browser.find_element(By.XPATH, '//*[@id="page"]/div/div[1]/div[3]/ul/li[5]/a[1]')
    cart.click()
    time.sleep(25)

    
    browser.close()



if __name__ == '__main__':
    main()