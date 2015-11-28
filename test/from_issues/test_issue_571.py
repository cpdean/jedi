from __future__ import print_function


def test_use_case():
    import jedi
    code = 'foo = 10;print(foo)'
    assignments = jedi.Script(code, column=len(code) - 2).goto_assignments()
    assert len(assignments) == 1
