import logging
import subprocess
from multiprocessing import cpu_count
import sys
from os import listdir
from os.path import join, exists
import re
import shutil

from setup_utils import get_vcvarsall, is_win


def call(cmd, **kwargs):
    cwd = f"{kwargs['cwd']}> " if 'cwd' in kwargs else ""
    msg = f"spawning subprocess: {cwd}{cmd}"
    logging.info(msg)
    subprocess.run(cmd, shell=True, check=True, **kwargs)


def main(args):
    bindir = f"{sys.prefix}/bin"
    libdir = f"{sys.prefix}/lib"
    if is_win:
        bindir = f"{sys.prefix}\Scripts"
        libdir = f"{sys.prefix}\libs"
        call(f"\"{get_vcvarsall()}\" amd64")
    if args and args[0] == "--init":
        call(f"bootstrap", cwd="boost_1_66_0")
    call("b2"
         " toolset=msvc"
         " address-model=64"
         " link=shared"
         " variant=release"
         " threading=multi"
         " runtime-link=shared"
         " --with-python"
         f" -j{cpu_count()}"
         " install"
         f" --prefix=\"{sys.prefix}\""
         f" --libdir=\"{libdir}\"",
         cwd="boost_1_66_0")
    if is_win:
        for f in filter(lambda f: re.match('boost_.*\.(dll|exe)$', f), listdir(libdir)):
            p = join(libdir, f)
            if not exists(join(bindir, f)):
                logging.info(f"moving misplaced binary {p} to {bindir}")
                shutil.move(p, bindir)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    main(sys.argv[1:])
