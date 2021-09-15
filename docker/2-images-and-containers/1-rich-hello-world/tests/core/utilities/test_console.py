from rich.console import Console
from src.core.utilities.console import console


def test_console():
    assert isinstance(console, Console)
