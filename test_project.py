from project import get_order_quantity
from project import validate_quantity
from project import validate_size

def main():
    test_order_quantity()
    test_correct_quantity_format()

def test_order_quantity():
    assert get_order_quantity(23,7) == 4
    assert get_order_quantity(21,7) == 3


def test_correct_quantity_format():
    file2 = '/Users/zuneemtamrakar/Desktop/combine_csv/both_correct.csv'
    file1 = '/Users/zuneemtamrakar/Desktop/combine_csv/incorrect_quantity.csv'
    assert validate_quantity(file2) == True
    assert validate_quantity(file1) == False

def test_correct_size_format():
    file_a = '/Users/zuneemtamrakar/Desktop/combine_csv/both_correct.csv'
    file_b = '/Users/zuneemtamrakar/Desktop/combine_csv/incorrect_size.csv'
    assert validate_size(file_a) == True
    assert validate_size(file_b) == False
    


if __name__ == '__main__':
    main()