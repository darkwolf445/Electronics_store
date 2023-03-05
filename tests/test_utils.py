
from utils import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price()

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.apply_discount()