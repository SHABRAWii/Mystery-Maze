from Gui.Gui import run
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

run(10, 10)