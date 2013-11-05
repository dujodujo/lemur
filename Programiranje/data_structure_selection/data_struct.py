import string
import collections

title1 = "The Adventures of Tom Sawyer.txt"
start_file1 = "*** START OF THIS PROJECT GUTENBERG EBOOK TOM SAWYER ***"
end_file1 = "*** END OF THIS PROJECT GUTENBERG EBOOK TOM SAWYER ***"

title2 = "The Adventures of Huckleberry Finn.txt"
start_file2 = "*** START OF THIS PROJECT GUTENBERG EBOOK HUCKLEBERRY FINN ***"
end_file2 = "*** END OF THIS PROJECT GUTENBERG EBOOK HUCKLEBERRY FINN ***"

def cut_header_footer(title,start_file,end_file):
    for i,line in enumerate(open(title,"rt")):
        line = line.strip()
        if line == start_file:
            start = i+1
        if line == end_file:
            end = i

    t1,t2 = title.split(".")
    title_test = t1 + "-test." + t2

    open(title_test, "w").write("".join(open(title, "r").readlines()[start:end]))
    return title_test

def get_words(title):
    histogram = collections.defaultdict(set)
    fp = open(title,"rt")
    for line in fp:
        cut_chars(line,histogram)
    return histogram

def cut_chars(line,h):
    line = line.replace("-"," ")

    for word in line.split():
        word = word.strip(string.punctuation + string.punctuation)
        word = word.lower()
        h[word] = h.get(word, 0) + 1

def total_words(histogram):
    return sum(histogram.values())

def different_words(histogram):
    return len(histogram)

def most_common_words(histogram):
    t = []
    for key,vaue in histogram.items():
        t.append((vaue,key))
    t.sort(reverse = True)
    return t

def write_most_common_words(mcw,title,tw):
    t1,t2 = title.split("-")
    t1 = t1 + t2.lstrip("test")

    print("Total words:",tw)
    print("The most common words in")
    print(t1)
    print("+"*32)

    for i,(frequency,words) in enumerate(mcw[:10]):
        print("{0}. {1:<24} {2:>4}".format(i,words,frequency))

title2 = cut_header_footer(title2,start_file2,end_file2)
title1 = cut_header_footer(title1,start_file1,end_file1)

histogram2 = get_words(title2)
histogram1 = get_words(title1)

c2 = collections.Counter(histogram2)
c1 = collections.Counter(histogram1)

tw2 = total_words(histogram2)
tw1 = total_words(histogram1)

dw2 = different_words(histogram2)
dw1 = different_words(histogram1)

mcw2 = most_common_words(histogram2)
mcw1 = most_common_words(histogram1)

write_most_common_words(mcw2,title2,tw2)
print()
write_most_common_words(mcw1,title1,tw1)

print(c2)
print(c1)
