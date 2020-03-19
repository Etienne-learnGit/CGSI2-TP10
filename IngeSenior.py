from Ingenieur import *

class ingeSenior(ingenieur):

    def __init__(self, nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail, nbhProjet, nbhGestion, responsabilite):
        ingenieur.__init__(self, nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail, nbhProjet, nbhGestion)
        self.__responsabilite = responsabilite

    def afficher(self):
        print("* [id = ",self._id,"] Nom et Prenom : ",self._nom, self._prenom," , Salaire : ",self._echelonSal," , Statue : ingenieur-Senior, Annee d'embauche : ",self._anneeEmbauche," , Nombre de jours de tarvail : ",self._nbJoursTravail," , Nombre d'heure de projet : ",self._nbhProjet," , Nombre d'heure de gestion : ",self._nbhGestion," , Responsabilite : ",self.__responsabilite)
