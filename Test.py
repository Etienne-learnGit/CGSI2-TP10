from Filiale import *
from EntrepriseMulti import *
from IngeJunior import *
from IngeSenior import *
from Administratif import *
from DirecteurFiliale import *

ENT = entreprise("RCAT", "France")
F1 = filiale("RCTA-Belgique", "Belgique", 2000)
F2 = filiale("RCTA-Maroc", "Maroc", 2010)
F3 = filiale("RCTA-Tunisie", "Tunisie", 1950)
F4 = filiale("RCTA-Angleterre", "Angleterre", 2005)
ENT.ajoutFiliale(F1)
ENT.ajoutFiliale(F2)
ENT.ajoutFiliale(F3)
ENT.ajoutFiliale(F4)
D1 = directeurF("Jambon", "Beur", 8, 210, 1960)
F3.ajoutSalarie(D1)
A1 = administratif("Jean", "Michel", 2, 300, 2003, 562, "RH")
IJ1 = ingeJunior("Will", "Fred", 7, 230, 2005, 809, 64, 50, 4)
F1.ajoutSalarie(A1)
F1.ajoutSalarie(IJ1)
IS1 = ingeSenior("Jean", "Hugue", 9, 126, 2000, 9004, 6050, 800, "responsable prod" )
F2.ajoutSalarie(IS1)

ENT.afficherEnt()
