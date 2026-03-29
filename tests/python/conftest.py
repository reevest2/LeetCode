import sys
import os

# Add the problems directory to the Python path so tests can import solutions.
# This allows: from solution import Solution
# when the test adds the specific problem's python/ directory to sys.path.
PROBLEMS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'problems')
