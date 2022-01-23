str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for letter in str:
    ord_ = ord(letter)+2

    if ord_ == 34:
        print(' ', end="")
        continue

    if  122 < ord_ or ord_ < 96 :
        print(chr(ord_-26), end="")
        continue
    print(chr(ord_), end="")

print('\n')

