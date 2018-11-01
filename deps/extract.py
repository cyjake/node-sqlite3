import sys
import tarfile
from os import path
import subprocess

tarball = path.abspath(sys.argv[1])
dirname = path.abspath(sys.argv[2])
tfile = tarfile.open(tarball,'r:gz')
tfile.extractall(dirname)

patchfile = path.join(path.dirname(tarball), "sqlite3.patch")
cwd = path.join(dirname, path.basename(tarball).replace(".tar.gz", ""))
subprocess.Popen(["patch", "-p1", "--input", patchfile], cwd=cwd)
