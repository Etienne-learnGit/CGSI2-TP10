from Salarie import *

class employe(salarie):

    def __init__(self, nom, prenom, echelonSal, id, anneeEmbauche, nbJoursTravail):
        salarie.__init__(self, nom, prenom, echelonSal, id)
        self._anneeEmbauche = anneeEmbauche
        self._nbJoursTravail = nbJoursTravail

    def afficher(self):
        pass
