import re
from src.core.script import script


def test_script(capsys):
    text = "hello"
    script(text)
    captured = capsys.readouterr()

    # Strip ANSI
    captured = re.sub(r'\033\[(\d|;)+?m', '', captured.out)
    assert text == captured.rstrip()
