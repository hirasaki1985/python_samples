# coding: utf-8
import os, sys
import argparse

from logging import getLogger, StreamHandler, INFO, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)

def main(args):
  pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument("-train_path", "-p", help="", default="./train_images")

  args = parser.parse_args()
  main(args)
