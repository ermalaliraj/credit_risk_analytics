import os, os.path, sys, shutil, re, itertools
from collections import namedtuple
from distutils.command.build_ext import build_ext as _build_ext
from distutils.command.build import build as _build

from distutils.core import setup
from distutils.core import Extension

pack_name = 'rpy2'
pack_version = __import__('rpy').__version__

# hmeq <- read.csv("c:/temp/hmeq.csv")

