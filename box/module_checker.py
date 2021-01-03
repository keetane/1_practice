import sys
import subprocess

if "subprocess" in sys.modules:
    print("module already imported")
else:
    pring("module not imported")