# -*- coding: utf-8 -*-
import csv
import cv2


class TUMRGBImageFileLoader(object):
    def __init__(self, dataset_dir_path: str):
        f = open(f'{dataset_dir_path}/rgb.txt', 'r', newline='')
        self._dataset_dir_path = dataset_dir_path
        self._db = csv.reader(f, delimiter=' ')

    def next(self):
        try:
            while True:
                out = next(self._db)
                if out[0] != '#':
                    break
        except StopIteration:
            return None

        return cv2.imread(f'{self._dataset_dir_path}/{out[1]}')
