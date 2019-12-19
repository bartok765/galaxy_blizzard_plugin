import os
import sys
import json
import tempfile
from shutil import rmtree
from distutils.dir_util import copy_tree

from invoke import task
from galaxy.tools import zip_folder_to_file

from src.version import __version__


@task
def build(c, target="build"):
    if os.path.exists(target):
        print('--> Removing {} directory'.format(target))
        rmtree(target)

    # Firstly dependencies needs to be "flatten" with pip-compile as pip requires --no-deps if --platform is used
    print('--> Flattening dependencies to temporary requirements file')
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        c.run(f'pip-compile requirements/app.txt --output-file=-', out_stream=tmp)

    # Then install all stuff with pip to target folder
    print('--> Installing with pip for specific version')
    args = [
        'pip', 'install',
        '-r', tmp.name,
        '--python-version', '37',
        '--platform', sys.platform,
        '--target', target,
        '--no-compile'
        '--no-deps'
    ]
    c.run(" ".join(args), echo=True)
    os.unlink(tmp.name)

    print('--> Copying source files')
    copy_tree("src", target)
