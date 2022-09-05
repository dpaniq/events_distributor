import os
from pprint import pprint

from .Importer import Importer
from .File import File
from .Error import Error

class Configurator(File):
    event = None
    
    def __init__(self):
        # self.__cwd = os.getcwd()
        self.load()
        self.check()
        print('asdasdasd')
     
    def load(self):
        self.event = Importer.loadJSON(f"config.json")
        print(self.event)
        print('^^^^')
        
    def check(self):
        # if not self.data['events']:
        #     return Error.throw(1, 'The `events` must be inside config', name=Configurator.__name__)
            
        
        # if not isinstance(self.data['events'], list):
        #     return Error.throw(2, 'The type of `events` must be array', name=Configurator.__name__)
        
        return True if not all([
                Configurator.checkEvent(self.event), 
                Configurator.checkSegments(self.event['segments'])
            ]) else False
        
        # for event in self.data['events']:
        #     if not all([
        #         Configurator.checkEvent(event), 
        #         Configurator.checkSegments(event['segments'])
        #     ]):
        #         return False
            
        # return True
    
    @staticmethod
    def checkEvent(event):
        if not event['name']:
            return Error.throw(10, 'The event `name` is required', name=Configurator.__name__)
        
     
    @staticmethod
    def checkSegments(segments):
        if not segments:
            return Error.throw(100, 'The `segments` must be inside events.event', name=Configurator.__name__)
        if not isinstance(segments, list):
            return Error.throw(101, 'The `segments` must be array', name=Configurator.__name__)
        
        for segment in segments:
            if not segment['name']:
                return Error.throw(102, 'The segment `name` is required', name=Configurator.__name__)
            
            if not segment['columns']:
                return Error.throw(103, 'The segment `columns` is required', name=Configurator.__name__)
            if not isinstance(segment['columns'], int):
                return Error.throw(104, 'The type `columns` must be int', name=Configurator.__name__)
            
            if not segment['rows']:
                return Error.throw(105, 'The segment `rows` is required', name=Configurator.__name__)
            if not isinstance(segment['rows'], int):
                return Error.throw(106, 'The type `rows` must be int', name=Configurator.__name__)
        return True