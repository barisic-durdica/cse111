from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("A", "B") == "B; A"
    assert make_full_name("Alexander", "Johnson") == "Johnson; Alexander"
    assert make_full_name("Mary-Jane", "Smith-Jones") == "Smith-Jones; Mary-Jane"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("B; A") == "B"
    assert extract_family_name("Johnson; Alexander") == "Johnson"
    assert extract_family_name("Smith-Jones; Mary-Jane") == "Smith-Jones"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("B; A") == "A"
    assert extract_given_name("Johnson; Alexander") == "Alexander"
    assert extract_given_name("Smith-Jones; Mary-Jane") == "Mary-Jane"