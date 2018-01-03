# -*- coding: utf-8 -*-

class SimpleGPIO():  
    def __init__(self,gpio=None): 
        self._base_path= "/sys/class/gpio/"
        self._gpio = gpio
        #self._direction = None
        #self._edge = None
        #self._last_value = None
    def setGPIO(self,gpio):
        self._gpio = gpio
    def getGPIO(self):
        return self._gpio
    def _writeFile(self,file_name,value): 
        fo = open(file_name, "w")
        fo.write(value)
        fo.close()
    def _readFile(self,file_name): 
        fo = open(file_name, "r")
        value = fo.read(7)
        fo.close()
        return value
    def _isOne(self,strValue): 
        return False if len(strValue)<=0 else strValue[0]=='1'
    def export(self):
        self._writeFile( self._base_path+"export" , str(self._gpio) )
    def unexport(self):  
        self._writeFile( self._base_path+"unexport" , str(self._gpio) )
    # direction should be"in" or "out", write tofile as "low" or "high".
    def _setDirection(self,direction): 
        self._writeFile(  self._base_path+"gpio"+str(self._gpio)+"/direction" , direction)
    def getDirection(self):
        return self._readFile( self._base_path+"gpio"+str(self._gpio)+"/direction")
    # edge should be "none" or "rising" or "falling" or "both"
    def _setEdge(self,edge):
        self._writeFile(  self._base_path+"gpio"+str(self._gpio)+"/edge" , edge)
    def getEdge(self):
        return self._readFile( self._base_path+"gpio"+str(self._gpio)+"/edge" )
    #setup gpio
    def setGPIOoutHIGH(self):
        self._setDirection("high")
    def setGPIOoutLOW(self):
        self._setDirection("out")#self._setDirection("low")
    def setGPIOin(self):
        self._setDirection("in")
        self._setEdge( "none")
    def setGPIOinRaising(self):
        self._setDirection("in")
        self._setEdge("rising")
    def setGPIOinFalling(self):
        self._setDirection("in")
        self._setEdge("falling")
    def setGPIOinBoth(self):
        self._setDirection("in")
        self._setEdge("both")
    # 1 , 0
    def _setValue(self,value): 
        self._writeFile( self._base_path+"gpio"+str(self._gpio)+"/value" , value )
    def setValueHigh(self): 
        self._setValue(self,'1')
    def setValueLow(self): 
        self._setValue(self,'0')
    def getValue(self):
        return self._readFile( self._base_path+"gpio"+str(self._gpio)+"/value" )
    def getIsHigh(self):
        return self._isOne(self.getValue() )

