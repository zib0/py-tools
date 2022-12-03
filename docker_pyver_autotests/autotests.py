import os
import subprocess as sp
import sys
from pathlib import Path


def install(package):
    sp.check_call(
        [sys.executable, "-m", "pip", "install", package],
        stdout=sp.DEVNULL,
        stderr=sp.DEVNULL,
    )


CWD = Path(__file__).parent
OUTPUT_DIR = Path(CWD / "output")
PY_VERSION = (
    f"{sys.version_info.major}_{sys.version_info.minor}_{sys.version_info.micro}"
)


def sample_output():
    with open(f"{OUTPUT_DIR}/{SAMPLE_FILE.stem}_{PY_VERSION}.txt", "w") as f:
        result = sp.Popen(["python", SAMPLE_FILE], stdout=sp.PIPE)
        f.write(result.stdout.read().decode("utf-8"))


def run_tests():
    for s in .iterdir():
        if s.is_file():
            continue
        try:
            pyfile = Path(list(s.rglob("*.py"))[0])
        except IndexError:
            continue
        out_path = Path(OUTPUT_DIR / f"{}/{Path().name}")
        out_path.mkdir(parents=True) if not out_path.exists() else None
        print(f"Running {pyfile}")
        with open(f"{out_path}/{pyfile.stem}_{PY_VERSION}.txt", "w") as f:
            result = sp.Popen(["python", pyfile], stdout=sp.PIPE, stderr=sp.PIPE)
            try:
                result.wait(timeout=30)
            except sp.TimeoutExpired:
                print(f"Timeout for {pyfile}")
                f.write("TIMEOUT")
                result.terminate()
                continue
            f.write(result.stdout.read().decode("utf-8"))
            f.write(result.stderr.read().decode("utf-8"))
            print(f"Wrote {out_path}/{pyfile.stem}_{PY_VERSION}.txt")


def run():
    print(f"Python Version: {PY_VERSION.replace('_', '.')}")
    install("isort")
    install("matplotlib")
    install("networkx")
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)
    print("Running sample output")
    sample_output()
    print("Running student output")
    run_tests()
    print("Done")


if __name__ == "__main__":
    run()
