def sousTableau(tableau, index_debut, index_fin):
    if index_debut < 0 or index_fin >= len(tableau) or index_debut > index_fin:
        return None 
    sous_tableau = tableau[index_debut:index_fin + 1]
    return sous_tableau
resultat = sousTableau(mon_tableau, index_debut, index_fin)
print(resultat)  
