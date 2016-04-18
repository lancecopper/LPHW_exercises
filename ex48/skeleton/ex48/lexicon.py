vocabulary = {'north': 'direction', 'south': 'direction',
    'east': 'direction', 'down': 'direction', 'up': 'direction', 
    'left': 'direction', 'right': 'direction', 'back': 'direction',
    'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb', 
    'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop', 
    'at': 'stop', 'it': 'stop', 'door': 'noun', 'bear': 'noun', 
    'princess': 'noun', 'cabinet': 'noun' 
    }

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
        
def isnum(s):
    numflag = True
    for i in s:
        if ord(i) not in range(48,58):
            numflag = False
    return numflag


def scan_alt(phrase):    
    sig_word = []
    words = phrase.split()
    for w in words:
        if w in vocabulary:
            sig_word.append((vocabulary[w], w))        
        elif type(convert_number(w)) is int:
            sig_word.append(('number', int(w)))
        else:
            sig_word.append(('error', w))
    return sig_word
    
def scan(phrase):    
    sig_word = []
    words = phrase.split()
    for w in words:
        if w.lower() in vocabulary:
            sig_word.append((vocabulary[w.lower()], w))     
        elif isnum(w):
            sig_word.append(('number', int(w)))
        else:
            sig_word.append(('error', w))
    return sig_word
    