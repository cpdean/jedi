import jedi


def test_specific_use_case():
    """
    smoketest to see if this crashes
    """
    src = "\n".join((
        "class C(object):",
        "  def m(self):",
        "    self.x = lambda self:"
    ))
    s = jedi.Script(source=src, line=3, column=24)
    s.completions()


def test_general_use_case():
    """
    smoketest to see if this crashes
    """
    source = "\n".join((
        "max(hash_table., key=lambda)",
        ""
    ))
    script = jedi.Script(column=15, source=source, line=1)
    script.completions()
