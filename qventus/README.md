# URL MATCHER

This tool can match URL for you.
This tool use trie tree for matching url.
The setup time is O(M\*N) for N is the length of key and M is the number of keys.
The search time is O(N) for N is the length of key.

## Getting Started

Just unzip this and you are good to go.

## Usage

There are two ways of input. One is from console, another is from file.

### Input from console
```shell
python url_query_trie.py
backload_urls:http://www.example.com,https://www.hello.com,http://www.siliconvalley.com
how many queries:3
record 1 http://www.example.com
record 2 http://www.pinterest.com
record 3 http://www.siliconworld.com
FULL URL FOUND
NO URL FOUND
PARTIAL URL FOUND
```

### Input from file
First, create a file or you can use input.txt in the zip.
The file format comes as bellow.
```
backload_urls
number of queries
query
query
query
query
query
......
```

Second, use the file as input with '-f' for this tool, we use "input.txt" as the example.
```shell
python url_query_trie.py -f input.txt
```
