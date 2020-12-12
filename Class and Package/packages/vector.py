class Vector:
    def __init__(self, _deg):
        self.deg = _deg
        self.elem = {}
        self.__current = [0 for i in range(_deg)]
        
    def add(self, _name, _li):
        if len(_li) == self.deg:
            self.elem[_name] = _li
        else:
            raise Exception('Given list does not have proper degree!') 
    
    def delete(self, _name):
        if self.elem.get(_name):
            del self.elem[_name]
        else:
            raise Exception(f'No element with name {_name} exists!')
    
    def showlist(self):
        print(self.elem)
    
    showelem = showlist 
    
    def showcurrent(self,_name):
        if self.elem.get(_name): 
            self.__current = self.elem[_name]
            print(self.__current)
        else:
            raise Exception(f'No element with name {_name} exists!')
            
        