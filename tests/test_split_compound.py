"""Test split_compound lemma_split."""
from json_de2zh.split_compound import split_compound

sent = """Der palästinensische Schriftsteller Emil Habibi ist
der einzige Autor im Nahen Osten, dessen Werk von allen
Seiten größte und offizielle Anerkennung zuteil geworden ist."""
sent_de = """Bei russischen Angriffen im Osten der Ukraine sind
    nach ukrainischen
    Behördenangaben acht Zivilisten getötet worden. In der Stadt Lyman in der Region Donezk
    seien vier Zivilisten durch russischen Beschuss getötet und elf weitere verletzt worden, erklärte Regionalgouverneur Pawlo Kyrylenko am Sonntag bei Telegram."""


def test_split_compound_s():
    """Test split_compound."""
    res = split_compound(sent)  # e.g., res = [["sein", "Angabe"]]

    word = "sein"
    word = "ist"  # not lemmatized yet
    assert any(map(lambda x: word in x, res))

    word = "Seite"
    word = "Seiten"  # ditto
    assert any(map(lambda x: word in x, res))


def test_split_compound_combined_words():
    """Test split_compound."""
    res = split_compound(sent_de)

    word = "Angabe"
    word = "Angaben"  # ditto
    assert any(map(lambda x: word in x, res))

    word = "Behörde"
    word = "Behörden"  # ditto
    assert any(map(lambda x: word in x, res))
