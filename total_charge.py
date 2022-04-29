from dataclasses import dataclass


@dataclass
class ItemRecord:
    name: str
    price: float
    item_type: str


def calculate_total(state: str, currentItemRecord: list[ItemRecord]):
    total_to_charge = 0.0
    tax = 0.0
    if state == 'Massachusetts':
        for item in currentItemRecord:
            if item.price <= 0:
                raise ValueError("Price should be greater than zero ")
            tax = item.price * 0.0625
            if item.item_type == 'wic':
                total_to_charge = item.price
            elif item.item_type == 'clothes' and item.price > 175.00:
                total_to_charge = round(item.price + tax, 2)
            elif item.item_type == 'clothes':
                total_to_charge = round(item.price, 2)
            else:
                total_to_charge = round(item.price + tax, 2)
    elif state == 'New Hampshire':
        for item in currentItemRecord:
            if item.price <= 0:
                raise ValueError("Price should be greater than zero ")
            total_to_charge = item.price
    elif state == 'Maine':
        for item in currentItemRecord:
            if item.price <= 0:
                raise ValueError("Price should be greater than zero ")
            if item.item_type == 'wic':
                total_to_charge = item.price
            else:
                tax_maine = round(item.price * 0.055, 2)
                total_to_charge = round(item.price + tax_maine, 2)

    total_to_charge = round(total_to_charge, 2)
    return total_to_charge


#shop2 = [ItemRecord('shoes', 00.00, 'clothes')]

#print("Your Total charge is: $ {} ".format(calculate_total('Maine', shop2)))
