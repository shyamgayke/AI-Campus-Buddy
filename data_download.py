import os
import requests
import zipfile
import kaggle
import pandas as pd
from datasets import load_dataset

# Create data directory
os.makedirs('data', exist_ok=True)

def download_kaggle_dataset(dataset_slug, output_path):
    """Download dataset from Kaggle."""
    kaggle.api.dataset_download_files(dataset_slug, path=output_path, unzip=True)

def download_file(url, output_path):
    """Download file from URL."""
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)

def download_simple_wikipedia():
    """Download Simple Wikipedia dump."""
    url = 'https://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-pages-articles.xml.bz2'
    output_path = 'data/simplewiki.xml.bz2'
    download_file(url, output_path)

if __name__ == '__main__':
    # Download ASAP AES from Kaggle
    try:
        download_kaggle_dataset('c/asap-aes', 'data/asap_aes')
    except:
        print("ASAP AES download failed. Manual download required.")

    # Download CommonLit Readability from Kaggle
    try:
        download_kaggle_dataset('competitions/commonlitreadabilityprize', 'data/commonlit')
    except:
        print("CommonLit download failed. Manual download required.")

    # Download BEA 2019 from Hugging Face
    try:
        bea_dataset = load_dataset('bea2019', 'wi+locness')
        bea_dataset.save_to_disk('data/bea2019')
    except:
        print("BEA 2019 download failed.")

    # Cambridge Learner Corpus - manual
    print("Cambridge Learner Corpus: Manual download required from https://www.cambridgeenglish.org/research-and-validation/learner-corpus/")

    # Simple Wikipedia
    download_simple_wikipedia()

    # AG News from Hugging Face
    try:
        ag_dataset = load_dataset('ag_news')
        ag_dataset.save_to_disk('data/ag_news')
    except:
        print("AG News download failed.")

    print("Data download complete.")
