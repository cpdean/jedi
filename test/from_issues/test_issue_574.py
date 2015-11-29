import jedi


def test_use_case():
    # smoketest it, crashes in report
    s = 'import zipfile; z = zipfile.ZipFile("foo"); z.read(n).'
    jedi.Script(s, 1, len(s), ".").completions()
