import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from main import hello


def test_hello():
    assert hello() == "Hello, World!"
