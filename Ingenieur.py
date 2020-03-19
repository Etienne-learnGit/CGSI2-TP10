from Employe import *

class ingenieur(employe):

    def __init__(self, nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail, nbhProjet, nbhGestion):
        employe.__init__(self, nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail)
        self._nbhProjet = nbhProjet
        self._nbhGestion = nbhGestion

    def afficher(self):
        pass
