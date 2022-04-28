import pytest
import total_charge

shop = [total_charge.ItemRecord('cereal', 10.00, 'wic')]

shop2 = [total_charge.ItemRecord('shoes', 165.00, 'wic')]

# happy path
def test_total_charge():
    result = total_charge.calculate_total('Massachusetts', shop)
    assert result == 10.00


def test_total_charge2():
    result = total_charge.calculate_total('New Hampshire', shop)
    assert result == 10.00


def test_total_charge3():
    result = total_charge.calculate_total('Maine', shop)
    assert result == 10.00

# testing clothes MA and ME
def test_total_clothes():
    result = total_charge.calculate_total('Maine',)

