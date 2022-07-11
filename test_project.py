from project import get_order_quantity
from project import validate_quantity

def main():
    test_order_quantity()
    test_quantity_format()

def test_order_quantity():
    assert get_order_quantity(23,7) == 4
    assert get_order_quantity(21,7) == 3

def test_quantity_format():
    file1 = '/Users/zuneemtamrakar/Desktop/combine_csv/incorrect_quantity.csv'
    file2 = '/Users/zuneemtamrakar/Desktop/combine_csv/both_correct.csv'
    assert validate_quantity(file2) == True
    assert validate_quantity(file1) == 'incorrect quantity format'
   



if __name__ == '__main__':
    main()