from Salarie import *

class directeurF(salarie):

    def __init__(self, nom, prenom, echelonSal, id, anneeNomination):
        salarie.__init__(self, nom, prenom, echelonSal, id)
        self.__anneeNomination = anneeNomination

    def afficher(self):
        print("* [id = ",self._id,"] Nom et Prenom : ",self._nom, self._prenom," , Salaire : ",self._echelonSal, " , Statue : Directeur , Annee Nomination : ",self.__anneeNomination,".")

