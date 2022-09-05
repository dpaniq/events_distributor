import os


import pathlib
pathlib.Path(__file__).parent.resolve()

# For the current working directory:

import pathlib



os.getcwd()

from src.classes.Distributor import Distributor

if __name__ == '__main__':
  os.system('cls' if os.name == 'nt' else 'clear')
  mainPath = pathlib.Path(__file__).parent.resolve()
  print(pathlib.Path(__file__).parent.resolve())
  print(pathlib.Path().resolve())
  os.chdir(mainPath)
  print(os.getcwd())
  """
    Start application
  """
  Distributor().start()