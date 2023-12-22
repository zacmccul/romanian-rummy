"""
File to subclass from for tests to grab env variables. VS Code when it runs
grabs these as normal, but our pre-commit hook just runs tests as normal and
needs this.
"""
import sys

from dotenv import dotenv_values

config = dotenv_values("../.env")
for path in (
    config["PYTHONPATH"].split(":")
    if "PYTHONPATH" in config and config["PYTHONPATH"] is not None
    else []
):
    sys.path.append(path)


def init():
    pass
