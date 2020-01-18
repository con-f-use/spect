import spect

def test_Spectclass():
    import re
    sre = spect(re)
    assert '__doc__' in sre.dunder
    assert 'match' in sre.regular
    assert '_MAXCACHE' in sre.const_private
    assert sre.const - sre.regular == {'_MAXCACHE'}
    assert '__getattr__' in spect(sre).magic

