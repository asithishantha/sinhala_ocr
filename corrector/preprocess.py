__author__ = 'Amali Rathnapriya'

import codecs
import sys
import os
import StringIO
import glob

from collections import Counter


package_directory = os.path.dirname(os.path.abspath(__file__))
# def create_outfile():
corpus_root = 'D:/Corpus/Corpus/SINHALACORPUS/NEWSPAPERS'


def preprocess():



    oldstdout = sys.stdout
    # joined=open('outfile.txt','w')
    # for root, dirs, files in os.walk(corpus_root):
    #     for file in files:
    #         if file.endswith(".TXT"):
    #             # print(os.path.join(root, file))
    #             # files=glob.glob(corpus_root)
    #             # for file in files:
    #                 f=open(file, 'r')
    #                 f.readlines()
    #                 f.close()



   #create a unique words dictionary from the corpus

    text=codecs.open('outfile.txt',encoding='utf-8')
    text2 = text.read()

    f = open('dictionary.txt', 'w')
    print ("dictionary of unique words creation started")


    dic = {}

    Counter(text2.split()).items()

    for item in text2.replace(',',' ').replace('.',' ').replace('?',' ').split():
        if dic.has_key(item):
            dic[item] += 1
            #print repr(item)
            #print "\n"
            f.write(item.encode('utf-8'))
            f.write(" - ")
            f.write(str(dic[item]))
            f.write("\n")
        else:
            dic[item] = 1

    # print dic
    # print len(dic)

    f.close()
    print ("dictionary created")

def main():
    preprocess()

main()