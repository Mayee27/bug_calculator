import importlib

import pytest

from calculator import add, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.5, 0.25) == 0.75


def test_divide_normal_numbers():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-9, 3) == -3


def test_divide_by_zero_raises_clear_error():
    # Expected behaviour: a readable ValueError, not a raw ZeroDivisionError.
    with pytest.raises(ValueError, match="zero"):
        divide(10, 0)


def test_importing_calculator_has_no_side_effects(capsys):
    # The module must not run demo code (or crash) when it is imported.
    import calculator
    capsys.readouterr()                # discard anything printed by the first import
    importlib.reload(calculator)
    assert capsys.readouterr().out == ""
