from nose.tools import *
from ex49 import ex49



def test_sentence():
    result = ex49.parse_sentence([('verb','go'),('direction','north')])
    assert_equal((result.subject, result.verb, result.object), ('player','go','north'))
    result = ex49.parse_sentence([('stop', 'in'),('verb','go'),('stop', 'at'),('direction','north'),('stop', 'behind')])
    assert_equal((result.subject, result.verb, result.object), ('player','go','north'))
    result = ex49.parse_sentence([('noun', 'bear'),('stop', 'up'),('verb','hit'),('noun','tree')])
    assert_equal((result.subject, result.verb, result.object), ('bear','hit','tree'))
    


    
    
