from Salarie import *

class entreprise :

    def __init__(self, nom, paysO):
        self.__nom = nom
        self.__paysO = paysO
        self.__lstFiliale = []

    def ajoutFiliale(self, F):
        self.__lstFiliale.append(F)

    def afficherEnt(self):

        print("- La multinationale ",self.__nom," est compose de ",len(self.__lstFiliale)," filiales. Son siege est en ",self.__paysO)

        for i in range(0, len(self.__lstFiliale)):
            d = self.__lstFiliale[0]
            date = d.getDate()
            c = self.__lstFiliale[i]
            date1 = self.__lstFiliale[i].getDate()
            if date1 < date:
                self.__lstFiliale[0] = c
                self.__lstFiliale[i] = d
        FA = self.__lstFiliale[0].getNom()
        nbSal = self.__lstFiliale[0].getNBsal()
        print("- La filiale la plus ancienne de cette multinationale est : ",FA,". Elle est composée de ",nbSal," salaries")


        nbSalar = 0
        for i in range(0, len(self.__lstFiliale)):
            nbSalar += self.__lstFiliale[i].getNBsal()
        print(self.__nom," est composé de ",nbSalar," salaries : ")


        for i in self.__lstFiliale :
            liste = i.getLSTsal()
            for y in liste :
                y.afficher()
            i.afficherF()
