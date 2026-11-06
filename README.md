# My Python DSA Project - KK


Now you have two ways of invoking your runner:
python -m dsa run arrays.two_sum

dsa run arrays.two_sum

# Executuin flow of the program

Terminal command : python -m dsa run arrays.two_sum

1. dsa/main.py
-----
from dsa.cli import main
main()
-----


dsa/cli.py
argparse parses the arguments
Builds module name:
dsa.problems.arrays.two_sum


Python import mechanism
importlib.import_module()
Loads the requested module


dsa/problems/arrays/two_sum.py
module.main()


Input parsing
Read numbers and target


two_sum(nums, target)
Execute the actual algorithm



# Different Execution Entrypoints
--------
Execution	                Starting point
python -m dsa	            dsa/__main__.py
dsa	                        dsa.cli:main
python two_sum.py	        two_sum.py itself
--------
First two reach the same cli function through different entry points.


# How to Run ?
Install your project in editable mode.
From your project root:
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

This is important:
pip install -e . installs your project in editable mode. Any changes you make to the Python source files are immediately reflected without reinstalling the package.
You can now invoke:
dsa run arrays.two_sum
The dsa command is a console-script entry point installed into your virtual environment. It isn't a standalone compiled binary, but it provides the same convenient command-line invocation.




# Read more about the project structure here and running flow:
 - https://chatgpt.com/s/t_6ae9e05233688191afaabbee48df3020 