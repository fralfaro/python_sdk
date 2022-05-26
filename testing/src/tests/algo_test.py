import utils.algo
import pytest

@pytest.mark.parametrize(
    "data",
    [
        [3, 2, 1, 5, -3, 2, 0, -2, 11, 9],
        (3, 2, 1, 5, -3, 2, 0, -2, 11, 9)
    ]
)
def test_sel_sort(data):
    sorted_vals = utils.algo.sel_sort(data)
    assert sorted_vals == sorted(data)

@pytest.fixture
def values():
    return (2, 3, 1, 4, 6)

def test_min(values):
    val = utils.algo.min(values)
    assert val == 1

def test_max(values):
    val = utils.algo.max(values)
    assert val == 6
