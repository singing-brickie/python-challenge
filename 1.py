def translate(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    x = list(alpha)
    y = list(message)
    str = ''
    for i in range(0, len(y)):
        if y[i] in x:
            pos = (x.index(y[i]) + 2) % 26
            str += x[pos]
        else:
            str += y[i]
    return str

code="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(translate(code))
print(translate("map"))


