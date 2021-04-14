import sys
import os

def set_syspath(absolute_dependencies: list):

    for directory in absolute_dependencies:
        existe = os.path.exists(directory) and os.path.isdir(directory)
    if not existe:
        raise BaseException(f"[set_syspath] le dossier du Python Path [{directory}] n'existe pas")
    else:
        sys.path.insert(0, directory)