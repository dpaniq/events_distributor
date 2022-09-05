import csv
# import yaml
import json

from os.path import exists
from .File import File

class Exporter:
    @staticmethod
    def saveCSV(path, data):
        if File.exist(path):
            file = open(path, 'w', newline = '')
            with file:   
                write = csv.writer(file)
                write.writerows(data)
        return None