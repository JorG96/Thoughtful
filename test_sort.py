import pytest
from challenge import sort

def test_standard_package():
    """Test packages that should be classified as STANDARD"""

    assert sort(12, 14, 10, 3) == "STANDARD"
    

def test_special_package_by_volume():
    """Test packages that should be SPECIAL due to volume"""
    
    assert sort(100, 100, 100, 15) == "SPECIAL"


def test_special_package_by_dimension():
    """Test packages that should be SPECIAL due to single dimension"""
  
    assert sort(150, 10, 10, 15) == "SPECIAL"
    assert sort(160, 10, 10, 15) == "SPECIAL"

def test_special_package_by_mass():
    """Test packages that should be SPECIAL due to mass"""

    assert sort(10, 10, 10, 20) == "SPECIAL"
    assert sort(10, 10, 10, 25) == "SPECIAL"

def test_rejected_package():
    """Test packages that should be REJECTED"""

    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(150, 10, 10, 20) == "REJECTED"
    assert sort(200, 200, 200, 25) == "REJECTED"

