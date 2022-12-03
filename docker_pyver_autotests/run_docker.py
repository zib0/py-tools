import concurrent.futures as cf
import os
import shlex
import subprocess as sp
import sys

IMAGES = [
    "python:3.6.15-slim-bullseye",
    "python:3.7.15-slim-bullseye",
    "python:3.8.15-slim-bullseye",
    "python:3.9.15-slim-bullseye",
    "python:3.10.8-slim-bullseye",
]


def install(package):
    sp.check_call(
        [sys.executable, "-m", "pip", "install", package],
        stdout=sp.DEVNULL,
        stderr=sp.DEVNULL,
    )


def pull_docker_image(image):
    print(f"Pulling {image}")
    sp.check_call(
        shlex.split(f"docker pull {image}"),
        stdout=sp.DEVNULL,
        stderr=sp.DEVNULL,
    )
    return f"Pulled {image}"


def test_py_version(image):
    result = sp.check_output(
        shlex.split(
            f"docker run --rm -it {image} python -c 'import sys; print(sys.version_info)'"
        ),
        stderr=sp.DEVNULL,
    )
    return result.decode("utf-8").replace("\n", "")


def run_in_docker(image):
    print("Running in {}".format(image))
    result = sp.Popen(
        shlex.split(
            f"docker run --rm -it -w /opt -v {os.getcwd()}:/opt {image} python autotests.py"
        ),
        stdout=sp.PIPE,
        stderr=sp.PIPE,
    )
    return result.stdout.read().decode("utf-8") + result.stderr.read().decode(
        "utf-8"
    )


def run():
    n_cores = os.cpu_count()
    with cf.ProcessPoolExecutor(n_cores) as executor:
        for result in executor.map(pull_docker_image, IMAGES):
            print(result)
    with cf.ProcessPoolExecutor(n_cores) as executor:
        for result in executor.map(test_py_version, IMAGES):
            print(result)
    with cf.ProcessPoolExecutor(n_cores) as executor:
        for result in executor.map(run_in_docker, IMAGES):
            print(result)


if __name__ == "__main__":
    run()
