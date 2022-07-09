from project import get_order_quantity

def main():
    test_order_quantity()

def test_order_quantity():
    assert get_order_quantity(23,7) == 4
    assert get_order_quantity(21,7) == 3


if __name__ == '__main__':
    main()