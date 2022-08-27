from pprint import pprint

class Configurator:
    
    _config = None
    day = None
    event = None
    segments = []
    
    def __init__(self, config = None):
        if config:
            self._config = config
        else:
            # self._loadConfig()
            pass
        
        self._parseConfig()
        if self._checkConfig():
            pprint(self._config)
        
    def _parseConfig(self):
        if not self._config:
            raise Exception(f'Config file is required')
        
        # self.day = self._config['day']
        self.event = '/_imports' + self._config['event'].strip()
        # self.segments = self._config['segments']
        
        self.segments = []
        for segment in self._config['segments']:
            tempSegment = segment
            tempSegment['name'] = segment['name'].replace("[\"']/g", '')
            self.segments.append(tempSegment)
        
        return True
        
    def _checkConfig(self):
        # Check config file
        if not self._config:
            raise Exception("Config file does not exist")
        
        # Check event file
        
        # if not self._fileLoader.fileExist(self.event):
        #     raise Exception(f'Event file with name `{self.event}` does not exist')
        
        # Check fields
        if not self.event or not self.segments:
            raise Exception(f'Config fields `event` & `segments are required`')
        
        if not isinstance(self.segments, list):
            raise Exception(f'Config segments field must be array')
        return True
        