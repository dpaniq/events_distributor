import csv
# import yaml
import json

from os.path import exists


class FileLoader:
    
    pwd = None
    
    def __init__(self, work_directory):
        self.pwd = work_directory
    
    def fileExist(self, filePath) -> bool:
        return exists(f'{self.pwd}/{filePath}')
    

    def load(self, fileName, openAs = 'json'):
        return self.__loadFile(fileName, openAs)
    
    def mkOutputDir(self, output):
        pass
        
        # try:
        #     # os.removedirs(f'{self._fileLoader.pwd}/distanation/')
        #     os.mkdir(f'{self._fileLoader.pwd}/day{self._config.day}')
        # except FileNotFoundError or FileExistsError:
        #     print('ok :)')
        # return
    
    def __loadFile(self, filePath, openAs = None):
        path = f'{self.pwd}{filePath}'
        
        print(f'path: {path}')
        file = None
        if exists(path):
            if openAs == 'csv':
                return self.__loadAsCSV(path)
                    # elif openAs == 'csv':
                    #     print('here')
                    #     return self.__loadAsCSV(path)
            # try:
            #     with open(path, newline='') as _file:
            #         if openAs == 'json':
            #             file = json.load(_file)
            #         elif openAs == 'csv':
            #             print('here')
            #             return self.__loadAsCSV(path)
                        
            #         elif openAs == yaml:
            #             file = yaml.load(_file)
            #         else:
            #             print(f'The file {path} (opened as {openAs}) does not exist')
            #             raise Exception('The extension of file is not supported')
            # except FileNotFoundError or FileExistsError:    
            #     print(f'Some file in file loader')
            # finally:
            #     return file
            #     _file.close()
        print(f'The file {path} not exist')
        return None
    
    def __loadAsYAML(self, path):
        pass
    
    def __loadAsJSON(self, path):
        pass
    
    def __loadAsCSV(self, path):
        file = []
        try:
            with open(path, newline='') as csvfile:
                spamreader = csv.reader(csvfile) #  delimiter=' ', quotechar='|'
                for row in spamreader:
                    file.append(row)
        except FileNotFoundError or FileExistsError:
            print(f'Some error in load csv')
        finally:
            print('File loaded successfuly')
            return file
    
    def saveAsCSV(self, fileName, data):
        file = open(f'{fileName}', 'w', newline = '')
        with file:   
            write = csv.writer(file)
            write.writerows(data)
            # write.writerows([[1,2], [3,4]])