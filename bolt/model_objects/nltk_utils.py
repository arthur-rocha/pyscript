from pathlib import Path
from zipfile import ZipFile
from shutil import copy

def extract_zip(zip_package):
    copy(zip_package, 'nltk_data')
    ZipFile(f'nltk_data/{zip_package}').extractall(
                path='nltk_data/'
            )

def extract_nltk_packages():
    d = Path('nltk_data/')
    d.mkdir(parents=True, exist_ok=True)
    extract_zip('corpora.zip')
    extract_zip('tokenizers.zip')
