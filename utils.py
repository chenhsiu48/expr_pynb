#!/usr/bin/python

import os
import time


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def join_path(*dirs):
    if len(dirs) == 0:
        return ''
    path = dirs[0]
    for d in dirs[1:]:
        path = os.path.join(path, d)
    return path


def make_filepath(fpath, dir_name=None, ext_name=None, tag=None):
    if dir_name is None:
        dir_name = os.path.dirname(fpath)
        if dir_name == '':
            dir_name = '.'
    fname = os.path.basename(fpath)
    base, ext = os.path.splitext(fname)
    if ext_name is None:
        ext_name = ext
    elif ext_name != '' and ext_name[0] != '.':
        ext_name = '.' + ext_name
    name = base
    if tag == '':
        name = name.split('-')[0]
    elif tag is not None:
        name = '%s-%s' % (name, tag)
    if ext_name != '':
        name = '%s%s' % (name, ext_name)
    return join_path(dir_name, name)


def rm_files(*files):
    for f in files:
        if os.path.exists(f):
            os.remove(f)


def run_cmd(cmd):
    print(cmd)
    os.system(cmd)
