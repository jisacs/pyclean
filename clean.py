import sys
import os
import argparse


def list_files(path):
    for path, dirs, files in os.walk(path):
      print (path)
      for f in files:
        print ('\t'+f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove dupplicate files.')
    parser.add_argument('--path',dest='path', help='source directory',required=True)
    args = parser.parse_args()
    list_files(args.path)
