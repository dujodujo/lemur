extensions = [".avi", ".mpg", ".mkv", ".rm", ".mp4"]
not_capital= ["a", "an", "the", "above", "against", "along", "alongside",
"amid", "amidst", "around", "as", "aside", "astride", "at", "athwart", "atop",
"before", "behind", "below", "beneath", "beside", "besides", "between",
"beyond", "but", "by", "down", "during", "for", "from", "in", "inside",
"into", "of", "on", "onto", "out", "outside", "over", "per", "plus", "than",
"through", "throughout", "till", "to", "toward", "towards", "under",
"underneath", "until", "upon", "versus", "via", "with", "within", "without"]

import os

for fname in (os.listdir(".")):
    fname = fname.lower()
    base, ext = os.path.splitext(fname)
    terka = (base,ext)
    if ext not in extensions:
        continue
    base = base.replace(".", " ")
    words = base.split()
    print(words)
    for i in range(len(words)):
        if i == 0 or words[i-1] == "-" or words[i] not in extensions:
            words[i] = words[i].capitalize()
    base = " ".join(words)
    print(base+ext)


