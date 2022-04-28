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
            tax = item.price * 0.0625
            if item.item_type == 'wic':
                total_to_charge = item.price
            elif item.item_type == 'clothes' and item.price > 175.00:
                total_to_charge = item.price + tax
            elif item.item_type == 'clothes':
                total_to_charge = item.price
            else:
                total_to_charge = item.price + tax
    elif state == 'New Hampshire':
        for item in currentItemRecord:
            total_to_charge = item.price
    elif state == 'Maine':
        for item in currentItemRecord:
            if item.item_type == 'wic':
                total_to_charge = item.price
            else:
                tax_maine = item.price * 0.055
                total_to_charge = item.price + tax_maine

    return total_to_charge


shop = [ItemRecord('shoes', 200.00, 'clothes')]

print("Your Total charge is: $ {} ".format(calculate_total('Maine', shop)))
