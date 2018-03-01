#!/usr/bin/env python3
'''
    Copyright (C) 2013  Povilas Kanapickas <povilas@radix.lt>

    This file is part of cppreference-doc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.
'''

import argparse
from index_transform import IndexTransform
import sys

class Index2Search(IndexTransform):
    def __init__(self, out_file):
        super().__init__()
        self.out_file = out_file

    def process_item_hook(self, el, full_name, full_link):

        self.out_file.write(full_name + ' => ' + full_link + '\n')
        IndexTransform.process_item_hook(self, el, full_name, full_link)

def main():
    parser = argparse.ArgumentParser(prog='index2highlight')
    parser.add_argument('index', type=str,
            help='Path to index file to process')
    parser.add_argument('destination', type=str,
            help='Path to destination file to store results to')
    args = parser.parse_args()

    out_f = open(args.destination, 'w', encoding='utf-8')

    tr = Index2Search(out_f)
    tr.transform(args.index)

if __name__ == '__main__':
    main()
