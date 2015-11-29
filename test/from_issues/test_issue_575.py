import jedi


def test_use_case():
    s = jedi.Script("from .. import foo", line=1, column=18, path="foo.py")
    s.usages()
