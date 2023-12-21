tbd

## Installation Instructions
1. [Install VS Code & Python](https://code.visualstudio.com/docs/python/python-tutorial)
   1. Install Python3.10+ (newer the better!)
   2. Install Python extension
2. git clone https://github.com/zacmccul/unknown.git in VS Code
3. `python -m venv .venv`
4. `.venv/Scripts/activate` depending on the system may need .bat, .ps1, orjust activate
5. `pip install -r requirements.txt`
6. `pre-commit install`  (prefix with python -m if pre-commit isn't found)
7. `pre-commit run --all-files`
