import sys
import os
from pathlib import Path

# Add the parent directory to sys.path
module_path = str(Path(__file__).parent.parent)
if module_path not in sys.path:
    sys.path.insert(0, module_path)
    print(f"Added {module_path} to Python path")