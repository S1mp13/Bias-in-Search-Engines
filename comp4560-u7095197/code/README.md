# Bias in Search Engines

## Hardware and software requirements

- Python Version: 3.9
- Memory: >= 32GiB

## Dependencies

numpy

tqdm

matplotlib

## Data Preparation

We Need to Download MS_MARCO.tsv

- Download file from `https://msmarco.blob.core.windows.net/msmarcoranking/collection.tar.gz`, then get `collection.tar.gz`.
- Extract the file from `collection.tar.gz` and get `collection.tsv`.
- Rename `collection.tsv` to `ms_marco.tsv`.
- Move `ms_marco.tsv` to `/data/ms_marco.tsv`


## Run

We use `python3 main.py` to run it.

It takes about 1-2 hours to complete the analysis。

