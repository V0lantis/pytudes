import os
from os.path import join
import re
from typing import Optional


def get_ipynb_files(file: os.DirEntry, dirPath: str = "./ipynb") -> Optional[str]:
    ipynb_matching_regex = re.compile("^.*?\.ipynb$")
    m = ipynb_matching_regex.match(file.name)
    if m:
        return join(dirPath, m.group())

# (def .*?",\n)(\s{4}"\s{4}\\".+?\n)?(\s{4}".+?,\n)+?(\s{4}"\w)

def clean_ipynb(file_path):
    with open(file_path, "r+") as f:
        data = f.read()
        f.seek(0)
        f.write(
            re.sub(
                r'(def .*?",\n)(\s{4}"\s{4}\\"?\w.+?\n)?(\s{4}".+?,\n)+?(\s{4}"\w)',
                r'\1\2    "    pass\\n",\n\4',
                data,
            )
        )
        f.truncate()


if __name__ == "__main__":
    gen = os.scandir("./ipynb")
    ipynb_files = []
    files = list(filter(None, map(get_ipynb_files, gen)))
    for f in files:
        clean_ipynb(f)
    # clean_ipynb("./ipynb/Advent 2017.ipyn")
