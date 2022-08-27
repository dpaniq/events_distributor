from importlib.metadata import distribution
import os
import pathlib

from src.classes.config import Config
from src.classes.file_loader import FileLoader
from src.classes.distributor import Distributor

os.system('cls\n\n' if os.name == 'nt' else 'clear\n\n')

print(pathlib.Path(__file__).parent.resolve())

if __name__ == '__main__':
  config = {
    "output": '/output',
    "event": "/events1.csv", 
    "segments": [
      {
          "name": "1. Проекты в сфере онлайн-образования",
          "columns": 3,
          "rows": 33
      },
      {
          "name": "2. Медицина",
          "columns": 5,
          "rows": 5
      },
      {
          "name": "3. Логистика и строительство",
          "columns": 1,
          "rows": 1
      }
    ]
  }    

  distributor = Distributor(
    Config(config),
    FileLoader(pathlib.Path(__file__).parent.resolve())
  )
  distributor.start()
