import Data.Repository.manufacturers_repo as mr


def get_all_manufacturers():
    return mr.get_all_manufacturers()


def get_manufacturer_by_id(id):
    return mr.get_manufacturer_by_id(id)


def get_manufacturer_by_name(pattern):
    manufacturers = mr.get_manufacturer_by_name(pattern)
    return {i+1: manufacturer for i, manufacturer in enumerate(manufacturers)}


def manufacturer_changes():
    mr.manufacturer_changes()


def store_new_manufacturer_name(manufacturer, new_value):
    mr.store_new_manufacturer_name(manufacturer, new_value)


def store_new_manufacturer_address(manufacturer, new_value):
    mr.store_new_manufacturer_adress(manufacturer, new_value)


def store_new_manufacturer_phone(manufacturer, new_value):
    mr.store_new_manufacturer_phone(manufacturer, new_value)


def store_new_manufacturer(manufacturer):
    mr.store_new_manufacturer(manufacturer)


def delete_manufacturer(manufacturer):
    mr.delete_manufacturer(manufacturer)
