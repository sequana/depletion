import os
import subprocess
import tempfile

from sequana_pipelines.depletion.main import main

from click.testing import CliRunner



from . import test_dir
input_dir = os.sep.join((test_dir, 'data'))

def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = ["test", "--input-directory", input_dir, "--working-directory", directory.name, "--force"]
    subprocess.call(cmd)


def test_standalone_script():

    directory = tempfile.TemporaryDirectory()
    args = ["--input-directory", input_dir, "--working-directory", directory.name, "--force", "--mode", 
"selection", "--reference-file", f"{input_dir}/measles.fa"]
    runner = CliRunner()
    results = runner.invoke(main, args)
    assert results.exit_code == 0


def test_version():
    cmd = ["sequana_depletion", "--version"]
    subprocess.call(cmd)

