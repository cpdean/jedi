import jedi


def test_use_case():
    s = jedi.Script(source="map(lambda", line=1, column=10)
    assert len(s.completions()) > 0


def test_map_in_a_lambda_multiline():
    src = (
        "\n"
        "map(lambda\n"
        "\n"
    )
    s = jedi.Script(source=src, line=2, column=10)
    assert len(s.completions()) > 0


def test_just_lambda():
    """
    maybe this is the intended behavior. it works
    """
    s = jedi.Script(source="lambda", line=1, column=6)
    assert len(s.completions()) == 1
