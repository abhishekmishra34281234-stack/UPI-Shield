import sys
import os

# Root directory ko path me add karein taaki app import ho sake
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app