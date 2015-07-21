import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import *
from xml.dom import minidom
import nltk
from nltk.corpus import WordNetCorpusReader

path = os.getcwd()
os.chdir(path)
corpus = path + "../resources/wn-affect-1.1/a-synsets.xml"

def load_asynsets(corpus):
    tree = ET.parse(corpus)
    root = tree.getroot()

    asynsets = {}
    for pos in ["noun", "adj", "verb", "adv"]:
        asynsets[pos] = {}
        for elem in root.findall(".//%s-syn-list//%s-syn" % (pos, pos)):
            # n#05588321 -> (n, 05588321)
            (p, offset) = elem.get("id").split("#")
            if not offset: continue

            asynsets[pos][offset] = { "offset16": offset, "pos": pos };
            if elem.get("categ"):
                asynsets[pos][offset]["categ"] = elem.get("categ")
            
            if elem.get("noun-id"):
                # n#05588321 -> 05588321
                noun_offset = elem.get("noun-id").replace("n#", "", 1)
                asynsets[pos][offset]["noun-offset"] = noun_offset
                asynsets[pos][offset]["categ"] = asynsets["noun"][noun_offset]["categ"]

            if elem.get("caus-stat"):
                asynsets[pos][offset]["caus-stat"] = elem.get("caus-stat")

    return asynsets
    

def merge_asynsets_with_wn(asynsets):
    pos_map = { "noun": "n", "adj": "a", "verb": "v", "adv": "r" }
    # start from "noun" because other pos use noun-synset
    for pos in ["noun", "adj", "verb", "adv"]:
        for offset in asynsets[pos].keys():
            # Get WordNet-2.0 domain/synset?




if __name__ == '__main__':
    asynsets_16 = load_asynsets("../resources/wn-affect-1.1/a-synsets.xml")
    asynset_30 = merge_asynsets_with_wn(aynsets_16)

