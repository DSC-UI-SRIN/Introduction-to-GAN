import collections
import os
import subprocess
from multiprocessing.dummy import Pool as ThreadPool
from urllib.parse import urlparse
import json
import numpy as np
import torch
from torch.utils import data
from torch import nn
from tqdm import tqdm
from os import path
from pathlib import Path

def makedir_exist_ok(dirname):
    dirname = Path(dirname)
    if not dirname.is_dir():
        dirname.mkdir(parents=True, exist_ok=False)
        return False
    else:
        return True

class Password(data.Dataset):
    """Dataset class for the CelebA dataset."""
    # CelebA images and attribute labels
    URL = ""
    training_file = 'training.pt'
    test_file = 'test.pt'

    def __init__(self, root="", train=True, transform=None, download=True, input_size=(16,), tokenize=False,
                 max_vocab_size=2048, sample_test=0.2):
        """Initialize and preprocess the CelebA dataset.
        :param sample_test:
        :param tokenize:
        :param max_vocab_size: 
        """

        self.root = root
        self.train = train
        self.transform = transform
        self.input_size = input_size[0]
        self.tokenize = tokenize
        self.max_vocab_size = max_vocab_size
        self.sample_test = sample_test

        if download:
            self.download()

        self.preprocess_data()

        if self.train:
            data_file = self.training_file
        else:
            data_file = self.test_file

        self.data = torch.load(os.path.join(self.processed_folder, data_file))
        self.class_to_idx = json.load(open(self.charmap_file, 'r'))
        self.idx_to_class = json.load(open(self.inv_charmap_file, 'r'))["data"]
        self.num_data = self.data.shape[0]

    def preprocess_data(self):

        if self._check_exists():
            return

        print('Processing for the the first time...')
        makedir_exist_ok(self.processed_folder)

        # filter lines
        lines = []
        with open(self.txt_file, 'r', encoding="latin-1") as f:
            print("Pre-process data..")
            for line in tqdm(f):
                line = line[:-1]
                if self.tokenize:
                    line = self.tokenize_string(line)
                else:
                    line = tuple(list(line))

                if len(line) > self.input_size:
                    line = line[:self.input_size]
                    continue  # don't include this sample, its too long

                # right pad with ` character
                lines.append(line + (("`",) * (self.input_size - len(line))))

        np.random.shuffle(lines)
        counts = collections.Counter(char for line in lines for char in line)
        # Make charmaps
        charmap = {'unk': 0}
        inv_charmap = ['unk']

        print("Make Charmap..")
        for char, count in tqdm(counts.most_common(self.max_vocab_size - 1)):
            if char not in charmap:
                charmap[char] = len(inv_charmap)
                inv_charmap.append(char)

        print("Filter data and convert to discrete")
        data_discrete = []
        filtered_lines = []
        for line in tqdm(lines):
            filtered_line = []
            _data_discrete = []
            for char in line:
                if char in charmap:
                    _data_discrete.append(charmap[char])
                    filtered_line.append(char)
                else:
                    _data_discrete.append(0)
                    filtered_line.append('unk')
            data_discrete.append(tuple(_data_discrete))
            filtered_lines.append(tuple(filtered_line))
        print("loaded {} lines in dataset".format(len(lines)))


        data_discrete = np.array(data_discrete, dtype='int64')
        data_discrete = torch.from_numpy(data_discrete).view(*data_discrete.shape)
        _s = int(len(data_discrete) * self.sample_test)

        with open(os.path.join(self.processed_folder, self.training_file), 'wb') as f:
            torch.save(data_discrete[_s:], f)
        with open(os.path.join(self.processed_folder, self.test_file), 'wb') as f:
            torch.save(data_discrete[:_s], f)

        json.dump(charmap, open(self.charmap_file, 'w'))
        json.dump({"data": inv_charmap}, open(self.inv_charmap_file, 'w'))

    @staticmethod
    def tokenize_string(sample):
        return tuple(list(sample.lower().split(' ')))

    def __getitem__(self, index):
        data = nn.functional.one_hot(self.data[index], num_classes=len(self.class_to_idx))
        return data.type(torch.LongTensor), 0

    def __len__(self):
        """Return the number of images."""
        return self.num_data

    def download(self):
        """Download the CelebA data if it doesn't exist in processed_folder already."""

        if self._check_raw_exists():
            return

        def call_wget(zip_data):
            subprocess.call('wget -N ' + self.URL + " -O " +
                            zip_data, shell=True)

        if not self._check_text_exists():
            pool = ThreadPool(4)
            pool = ThreadPool(4)  # Sets the pool size to 4
            # Open the urls in their own threads
            # and return the results
            pool.map(call_wget, [self.txt_file])
            # close the pool and wait for the work to finish
            pool.close()
            pool.join()

    def _check_raw_exists(self):
        return makedir_exist_ok(self.raw_folder)

    def _check_text_exists(self):
        return os.path.exists(self.txt_file)

    def _check_exists(self):
        return os.path.exists(os.path.join(self.processed_folder, self.training_file)) and \
               os.path.exists(os.path.join(self.processed_folder, self.test_file))

    @property
    def txt_file(self):
        return os.path.join(self.raw_folder, os.path.basename(urlparse(self.URL).path))

    @property
    def raw_folder(self):
        return os.path.join(self.root, self.__class__.__name__, 'raw')

    @property
    def processed_folder(self):
        return os.path.join(self.root, self.__class__.__name__, 'processed')

    @property
    def charmap_file(self):
        return os.path.join(self.processed_folder, "charmap.json")

    @property
    def inv_charmap_file(self):
        return os.path.join(self.processed_folder, "inv_charmap.json")


class Rockyou(Password):
    URL = "https://github.com/brannondorsey/PassGAN/releases/download/data/rockyou-train.txt"
