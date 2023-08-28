from exercice import calculer_somme

def test_calculer_somme_positifs():
    assert calculer_somme([1, 2, 3]) == 6
    assert calculer_somme([10, 20, 30, 40, 50]) == 150

def test_calculer_somme_negatifs():
    assert calculer_somme([-1, -2, -3]) == -6
    assert calculer_somme([-10, -20, -30, -40, -50]) == -150

def test_calculer_somme_melange():
    assert calculer_somme([-10, 5, 15, -20, 30]) == 20
    assert calculer_somme([0, 0, 0, 0, 0, 0]) == 0

def test_calculer_somme_liste_vide():
    assert calculer_somme([]) == 0

def test_calculer_somme_un_element():
    assert calculer_somme([42]) == 42
    assert calculer_somme([-100]) == -100

def test_calculer_somme_grands_nombres():
    assert calculer_somme([10**6, 2*10**6, 3*10**6]) == 6*10**6
    assert calculer_somme([-5*10**5, 0, 5*10**5]) == 0

def test_calculer_somme_decimaux():
    assert calculer_somme([0.1, 0.2, 0.3]) == 0.6
    assert calculer_somme([-0.1, 0.1, -0.1, 0.1]) == 0.0
