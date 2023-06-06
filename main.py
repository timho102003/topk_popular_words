import argparse
import heapq
import os
import re
import time
from collections import Counter

import nltk
import psutil
from memory_profiler import memory_usage
from nltk.corpus import stopwords

from config import *

logger = myLogger()


def read_file_in_chunks(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


def find_top_k_words(file_path, k):
    word_count = Counter()

    # Read and process the file line by line
    for line in read_file_in_chunks(file_path):
        # Clean the dataset
        line = line.lower()
        words = re.findall(r"\b[a-z]+\b", line)

        # Remove stop words
        filtered_words = [word for word in words if word not in stopwords]

        # Update the frequency count of each word
        word_count.update(filtered_words)

    # Find the top k words
    top_k_words = heapq.nlargest(k, word_count.keys(), key=word_count.get)

    word_count_sort = sorted(word_count.items(), key=lambda i: i[1] * -1)
    logger.info(word_count_sort[:k], bold=True)

    return top_k_words


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--topk", type=int, required=False, default=10)
    args = parser.parse_args()

    assert os.path.isfile(args.file)

    logger.header(f"Dataset: {args.file}")
    logger.header(f"TopK: {args.topk}")

    start_time = time.time()
    mem_usage_before = memory_usage(-1, interval=0.1, timeout=1)[0]
    current_process = psutil.Process()
    cpu_usage_before = current_process.cpu_percent(interval=None)

    top_k_words = find_top_k_words(args.file, args.topk)

    end_time = time.time()
    mem_usage_after = memory_usage(-1, interval=0.1, timeout=1)[0]
    cpu_usage_after = current_process.cpu_percent(interval=None)

    logger.header(f"Top {args.topk} words: {top_k_words}")
    logger.header(f"Execution time: {end_time - start_time} seconds")
    logger.header(f"Memory used: {mem_usage_after - mem_usage_before} MiB")
    logger.header(f"CPU usage: {cpu_usage_after - cpu_usage_before} %")
