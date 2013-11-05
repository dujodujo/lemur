#import string
#primer = """Napiši funkcijo skritopis(s), ki (kar predobro) skrije besedilo tako,
#da vsako besedo zamenja z njeno prvo črko."""
#
#s = primer[0]
#for i in range(1,len(primer)):
#    if not (str.isalpha(primer[i]) and str.isalpha(primer[i-1])):
#        s += primer[i]
#print(s)
#
#s = "Tule    je samo en preveč."
#s = "Tule ni nobenega preveč."
#s = "Ta    je res    pretiran."
#
#import re
#print(len(re.findall("\s\s+", s)) / (len(re.findall("\s+", s)) or 1))
#print(len(re.findall("\s+", s)))
