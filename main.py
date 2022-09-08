import os
import pathlib

from src.classes.Distributor import Distributor

if __name__ == '__main__':
  
  # Set directory
  os.chdir(pathlib.Path(__file__).parent.resolve())
  
  # Clear consoles
  os.system('cls' if os.name == 'nt' else 'clear')
  
  # Start application
  Distributor().start()