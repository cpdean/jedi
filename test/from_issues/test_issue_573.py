from __future__ import print_function
import jedi


def test_usecase():
    """
    for whatever reason the actual bug comes
    from when you try to call repr on
    the call signatures
    """
    src = "\n".join(
        ("import threading",
         "threading.Thread(foo()")
    )
    s = jedi.Script(source=src, line=2, column=22)
    signatures = s.call_signatures()
    assert len(signatures) > 0
    # and fails...
    print(signatures)
