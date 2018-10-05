import binascii

def XorWord(src, cipher):
    out = ''.join(chr(ord(s)^ord(c)) for s,c in zip(src,cipher*100))
    return out;

def BFDecrypt():
    iSrc = "\x20\x2a\x27\x21\x3d\x31\x75\x2a\x25\x76\x2b\x75\x19\x32\x76\x19\x32\x2e\x75\x19\x31\x76\x28\x22\x75\x34\x20\x33\x2a\x19\x31\x76\x34\x2a\x22\x19\x76\x20\x19\x25\x34\x3f\x36\x32\x76\x67\x3b";
    for i in range(0x00, 0xFF):
        print(XorWord(iSrc, chr(i)));
        print("\n - - - - - \n")

def OffsetFlag():
    msg = "FLAG[WLCMTTHWNDRFULWRLDFCRYPT]";
    nMsg = "";
    for i in range(0, len(msg)):
        nMsg += chr(ord(msg[i]) + 0x20);

    print(nMsg);

def main():
    BFDecrypt();

main();


#DECRYPTED: FLAG[WLCMTTHWNDRFULWRLDFCRYPT]
