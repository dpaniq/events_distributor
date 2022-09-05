from pprint import pprint

class Error:
    code = None
    message = ''
    data = None
    
    def __init__(self, name = 'unknown'):
        self.name = name
    
    @staticmethod
    def throw(code, message, data = None, name="unknown"):
        print(f"\n[{name}-error]:")
        
        
        error = {}
        if code:
            error['code'] = code
        if message:
            error['message'] = message
        if data:
            error['data'] = data
        pprint(error, indent=2, width=80)
        return False
    
    # def throw(self):
    #     print(f"\n[{self.name}-error]:")
    #     pprint(self.get(), indent=2, width=80)
    
    def get(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data,
        }
    
    def set(self, code, message = '', data = {}):
        self.code = code
        self.message = message
        self.data = data
        return self
    
        
