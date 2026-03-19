from address import extract_city, extract_state, extract_zipcode

def test_extract_city():
    address = "525 S Center St, Rexburg, ID 83460"
    assert extract_city(address) == "Rexburg"

def test_extract_state():
    address = "525 S Center St, Rexburg, ID 83460"
    assert extract_state(address) == "ID"

def test_extract_zipcode():
    address = "525 S Center St, Rexburg, ID 83460"
    assert extract_zipcode(address) == "83460"

def test_extract_city_long():
    address = "123 Main Street, Los Angeles, CA 90001"
    assert extract_city(address) == "Los Angeles"