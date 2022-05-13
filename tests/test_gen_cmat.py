"""Test gen_cmat."""
from pathlib import Path
from json_de2zh.gen_cmat import gen_cmat

text1 = Path("data/sternstunden04-de.txt").read_text('utf8').splitlines()
text1 = [elm.strip() for elm in text1 if elm.strip()]

text2 = Path("data/sternstunden04-zh.txt").read_text('utf8').splitlines()
text2 = [elm.strip() for elm in text2 if elm.strip()][:-1]


def test_gen_cmat():
    """Test gencmat."""
    cmat = gen_cmat(text1, text2)

    assert cmat.shape == (29, 30)

    assert cmat.max() > 0.5  # .53

    # assert divmod(cmat.argmax(), cmat.shape[1]) == (13, 13)
    assert cmat.mean() > 0.15  # 0.18
