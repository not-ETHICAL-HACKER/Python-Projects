class TypeManager:
    def __init__(self,obj):
        self.obj = obj 
        self.type = None
    def __repr__(self):
        return f"<class '{self.type}'>"
    def find_type(self):
        new_token = type(self.obj).__name__
        type_map = {
            int: 'int',
            float: 'real',
            str: 'txt',
            bool: 'bits'
        }
        return type_map.get(type(new_token), 'unknown')