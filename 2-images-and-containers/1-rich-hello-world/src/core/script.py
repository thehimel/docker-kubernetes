from src.core.utilities.console import console


def script(text: str, style: str = "green") -> None:
    console.print(text, style=style)
