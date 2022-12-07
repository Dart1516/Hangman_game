from my_project import  pick_secret_word
import pytest

def test_pick_secret_word():
    list_of_words = []
    with open("Lista_de_palabras_largas.txt", "rt") as file:
        for a_word in file:
            a_word = a_word.strip()
            list_of_words.append(a_word.upper())
    for _ in range(15):
        word = pick_secret_word()
        assert word in list_of_words

pytest.main(["-v", "--tb=line", "-rN", __file__])