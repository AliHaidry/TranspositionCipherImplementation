import random

# Transposition Cipher
def trans_codec(message,keylen,seed,cipher):
    random.seed(seed)
    msglen = len(message)
    assert keylen <= msglen

    excess = msglen % keylen
    if excess != 0:
        padlen = keylen - excess
        message += padlen * 'Z' # pad with z cos its least common english alphabet
        msglen = len(message)
    st = ''
    key_0 = [x for x in range(keylen)]
    key_1 = random.sample(key_0, keylen)

    if cipher:
        for i in range(0,msglen,keylen):
            msgblock = message[i:i+keylen]
            msgaray = list(msgblock)
            for i in range(keylen):
                msgaray[key_1[i]] = msgblock[i]
            st += ''.join(msgaray)
    else:
        for i in range(0,msglen,keylen):
            msgblock = message[i:i+keylen]
            msgaray = list(msgblock)
            for i in range(keylen):
                msgaray[i] = msgblock[key_1[i]]
            st += ''.join(msgaray)
    return st

# example test
seed = 35
keylen = 7
message = 'HELLOWORLD'

ciphered_msg = trans_codec(message,keylen,seed,True)
print(ciphered_msg)
print(trans_codec(ciphered_msg,keylen,seed,False))

message = 'THISISASECRETMESSAGE'
ciphered_msg = trans_codec(message,keylen,seed,True)
print(ciphered_msg)
print(trans_codec(ciphered_msg,keylen,seed,False))