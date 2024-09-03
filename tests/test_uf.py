# test_uf.py

import sys
import os
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from uf import UF

def test_initialization():
    """
    Test the initialization of the UF class.
    """
    print("Test: Initialization of UF class")
    print("Expected: UF instance should not be None.")
    uf = UF(10)
    assert uf is not None, "Initialization failed: UF instance is None."

def test_union():
    """
    Test the union operation.
    """
    print("Test: Union operation")
    print("Expected: After union(1, 2), find(1, 2) should return True.")
    uf = UF(10)
    uf.union(1, 2)
    assert uf.find(1, 2) == True, "Union operation failed: find(1, 2) did not return True."

def test_find():
    """
    Test the find operation.
    """
    print("Test: Find operation")
    print("Expected: Initially, find(1, 2) should return False. After union(1, 2), find(1, 2) should return True.")
    uf = UF(10)
    assert uf.find(1, 2) == False, "Find operation failed: find(1, 2) did not return False initially."
    uf.union(1, 2)
    assert uf.find(1, 2) == True, "Find operation failed: find(1, 2) did not return True after union."

def test_multiple_unions():
    """
    Test multiple union operations.
    """
    print("Test: Multiple union operations")
    print("Expected: After union(1, 2) and union(2, 3), find(1, 3) should return True.")
    uf = UF(10)
    uf.union(1, 2)
    uf.union(2, 3)
    assert uf.find(1, 3) == True, "Multiple union operations failed: find(1, 3) did not return True aft."

def test_no_connection():
    """
    Test no connection between elements.
    """
    print("Test: No connection between elements")
    print("Expected: After union(1, 2), find(1, 3) should return False.")
    uf = UF(10)
    uf.union(1, 2)
    assert uf.find(1, 3) == False, "No connection test failed: find(1, 3) did not return False."

def test_union_with_self():
    """
    Test union with self.
    """
    print("Test: Union with self")
    print("Expected: Each element should be connected to itself.")
    uf = UF(10)
    for i in range(10):
        assert uf.find(i, i) == True, f"Union with self failed: find({i}, {i}) did not return True."

def test_random_chain():
    """
    Test a random chain of unions.
    """
    print("Test: Chain of random unions")
    uf = UF(100)

    random_first_node = random.randint(0, 99)
    current_node = random_first_node
    for i in range(1, 20):
        new_node = random.randint(0, 99)
        uf.union(current_node, new_node)
        current_node = new_node

    assert uf.find(random_first_node, current_node) == True, "Random chain of unions failed: find did not return True."