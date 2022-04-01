import os
import subprocess
import sys

import sequana_pipelines.depletion.main as m

from . import test_dir

def test_standalone_subprocess(tmpdir):
    input_dir = os.sep.join((test_dir, 'data'))
    cmd = ["test", "--input-directory", input_dir, "--working-directory", str(tmpdir), "--force"]
    subprocess.call(cmd)


def test_standalone_script(tmpdir):
    input_dir = os.sep.join((test_dir, 'data'))
    sys.argv = ["test", "--input-directory", input_dir, "--working-directory", str(tmpdir), "--force", "--mode",
"selection", "--reference", "{input_dir}/measles.fa"]
    m.main()


def test_version():
    cmd = ["sequana_depletion", "--version"]
    subprocess.call(cmd)

