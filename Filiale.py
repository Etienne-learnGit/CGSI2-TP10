from abc import ABC, abstractmethod

class filiale(ABC) :

    def __init__(self, nom, pays, dateCrea):
        self.__nom = nom
        self.__pays = pays
        self.__dateCrea = dateCrea
        self.__lstSalarie = []

    def getPays(self):
        return self.__pays

    def getDate(self):
        return self.__dateCrea

    def getNom(self):
        return self.__nom

    def getNBsal(self):
        return len(self.__lstSalarie)

    def getLSTsal(self):
        return self.__lstSalarie

    def ajoutSalarie(self, Salarie):
        self.__lstSalarie.append(Salarie)

    def supSalarie(self, Salarie):
        self.__lstSalarie.remove(Salarie)

    def afficherF(self):
        print(" Site : ", self.__pays)
