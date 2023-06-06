## K Most Popular Words
### Goal:
Design and Implement an efficient java/python/scala code (or any language you prefer) to determine Top K most frequent/repeated words in a given dataset (example: K = 10). The objective here is to obtain the result with the least possible execution Time (or with the best performance on your computer).

### How to run the code:
```
python main.py --file data/small_50MB_dataset.txt --topk 10
```
- file: choose the file to analyze
- topk: the topk most frequent words (default=10)

### Results:

|       |         ets |     memory | cpu |
|------:|------------:|-----------:|----:|
|  50MB |    3.913952 |  13.796875 | 1.8 |
| 300MB |   19.547053 |  17.406250 | 2.3 |
|  2.5G |  176.376642 | 168.125000 | 2.4 |
|  16GB | 1102.085003 | 239.703125 | 2.4 |