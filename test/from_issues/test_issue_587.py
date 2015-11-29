# -*- coding: utf-8 -*-
import jedi

import sys
_vers = sys.version_info[:3]
_major, _, _ = _vers

PY3 = _major == 3


def test_use_case():
    """
    smoketest to see if this crashes.

    the need to version check is because python3.2 doesn't
    support unicode literals as built-in syntax
    """
    if not PY3:
        src = "¹".decode("utf-8")
    else:
        src = "¹"
    s = jedi.Script(source=src, line=1, column=len(src))
    s.completions()
