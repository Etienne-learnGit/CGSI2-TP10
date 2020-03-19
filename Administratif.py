from Employe import *

class administratif(employe):

    def __init__(self,  nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail, serviceDeT):
        employe.__init__(self, nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail)
        self.__serviceDeT = serviceDeT

    def afficher(self):
        print("* [id = ",self._id,"] Nom et Prenom : ",self._nom, self._prenom," , Salaire : ",self._echelonSal," , Statue : Administartif , Annee d'embauche : ",self._anneeEmbauche," , Nombre de jours de tarvail : ",self._nbJoursTravail," , Service : ",self.__serviceDeT)
