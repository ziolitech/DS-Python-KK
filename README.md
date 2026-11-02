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
pip install -e ".[dev]"
dsa run arrays.two_sum



# Read more about the project structure here and running flow:
 - https://chatgpt.com/s/t_6ae9e05233688191afaabbee48df3020 