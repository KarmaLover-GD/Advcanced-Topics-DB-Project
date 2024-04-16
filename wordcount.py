from pyspark import SparkContext, SparkConf
import os
import numpy as np
import time
import matplotlib.pyplot as plt

start = time.time()
# Initialize SparkContext
conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

# Function to read a file and return its content as an RDD of lines
def read_file(file_path):
    return sc.textFile(file_path)

# Directory containing all the text files
input_dir = "Task1/datasetCNNSTORIES"

# Get a list of all files in the directory
files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

# Read all files into an RDD of lines
lines_rdd = sc.union([read_file(file) for file in files[0:2]])

# Tokenize the lines into words
words_rdd = lines_rdd.flatMap(lambda line: line.split())

# Count the occurrences of each word
word_counts_rdd = words_rdd.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Display or save the results
word_counts = word_counts_rdd.collect()
print("time taken for word counting : ", time.time() - start)
start = time.time()
top10words = []
top10freq = []
for word, count in word_counts:
    if(len(top10words) < 10):
        top10words.append(word)
        top10freq.append(count)
    else:
        if count > min(top10freq):
            top10words[np.argmin(top10freq)] = word
            top10freq[np.argmin(top10freq)] = count

print("------------------ top10words------------------")
for i in range(10):
    print( top10words[i], ": ", top10freq[i])
            
print("time taken to display top 10 words ", time.time() - start)           


plt.pie(top10freq, labels=top10words)
plt.title("TOp 10 words")
plt.show()

# Stop SparkContext
sc.stop()
