import pytest
from gestionnaire_notes import moyenne, moyenne_ponderee, mention


def test_moyenne():
    assert moyenne([10, 12, 14]) == 12


def test_moyenne_ponderee():
    assert moyenne_ponderee([12, 15], [1, 2]) == 14


def test_mention():
    assert mention(17) == "Très bien"
    assert mention(14) == "Bien"
    assert mention(12) == "Assez bien"
    assert mention(10) == "Passable"
    assert mention(8) == "Ajourné"


def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])


def test_mention_invalide():
    with pytest.raises(ValueError):
        mention(25)
