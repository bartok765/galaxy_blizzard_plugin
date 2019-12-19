import os
import sys
import json
import tempfile
from shutil import rmtree, copy, copytree

from invoke import task
from galaxy.tools import zip_folder_to_file

from src.version import __version__


@task
def build(c, target="build"):
    if os.path.exists(target):
        rmtree(target)

    # firstly flat dependencies pip-compile as pip requires --no-deps for foreign platform dependencies
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        c.run(f'pip-compile requirements/app.txt --output-file=-', out_stream=tmp)

    # then install all stuff with pip to target folder
    args = [
        'pip', 'install',
        '-r', tmp.name,
        '--python-version', '37',
        '--platform', sys.platform,
        '--target', target,
        '--no-compile',
        '--no-deps'
    ]
    c.run(" ".join(args), echo=True)
    os.unlink(tmp.name)

    # copy source files
    copytree("src", target)
