
import numpy as np
import time
import sys
import os
import matplotlib.pyplot as plt


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.top10freq = []
        self.top10words= []
        self.top10sz = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1

        top10 = False
        for i in range(len(self.top10words)):
            if self.top10words[i] == word:
                self.top10freq[i] +=1
                top10 = True

        if self.top10sz <10 and not top10:
            self.top10words.append(word)
            self.top10freq.append(node.frequency)
            self.top10sz += 1

        minval = min(self.top10freq)
        minidx = np.argmin(self.top10freq)
        if not top10 and node.frequency > minval and self.top10sz >= 10 :
            
            self.top10words[minidx] = word
            self.top10freq[minidx] = node.frequency
    def search(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                print(word, " : not in the Trie")
                return 0 
            
        return node.frequency
    
    def displaytop10(self):
        for i in range (len(self.top10freq)):
            print(self.top10words[i], " : ", self.top10freq[i])


if __name__ == '__main__':
    start = time.time()
    
    path = "Task1/datasetCNNSTORIES"
    files = []
    
    for f in os.listdir(path):
        files.append(f)
    
    if len(files) <= 0:
        sys.exit()

    
trie = Trie()

for file in files:
    wordslist = [open(os.path.join(path, file), "r", encoding="utf-8").read().split()]
    for words in wordslist:
        for items in words:
            trie.insert(items)

trie.displaytop10()
end = time.time()
print("time taken : ", end- start)

plt.pie(trie.top10freq, labels=trie.top10words)
plt.title("TOp 10 words")
plt.show()

    


    
