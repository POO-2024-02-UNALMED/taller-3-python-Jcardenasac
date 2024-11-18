class TV:
    _canal = 1
    _volumen = 1
    _precio = 500
    _numTV = 0
    _control = None

    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado

    def getMarca(self):
        return self._marca

    def setMarca(self,marca):
        self._nombre = marca

    def getCanal(self):
        return self._canal

    def setCanal(self,canal):
        self._canal = canal
    
    def getPrecio(self):
        return self._precio

    def setPrecio(self,precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self,volumen):
        self._volumen = volumen

    def getControl(self):
        return self._control

    def setControl(self,control):
        self._nombre = control

    @classmethod
    def getNumTV(self):
        return self._numTV
    
    @classmethod
    def setNumTV(self, numTV):
        self._numTV = numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._canal != 120 and self._estado == True : 
            self._canal += 1

    def canalDown(self):
        if self._canal != 1 and self._estado == True :
            self._canal -= 1

    def volumenUp(self):
        if self._volumen != 7 and self._estado == True :
            self._volumen += 1

    def volumenDown(self):
        if self._volumen != 0 and self._estado == True :
            self._volumen -= 1