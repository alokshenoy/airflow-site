import glob
import json
import sys

import yaml
import os

ROOT_DIR = os.path.dirname(os.path.join(os.path.abspath(__file__), os.path.pardir))

def load_yaml(filepath: str):
    with open(filepath) as f:
        return yaml.safe_load(f)


def dump_docs_package_metadata():
    to_load_paths = [
        'docs-archive/metadata.yaml'
    ]

    to_load_paths.extend(
        glob.glob("docs-packages-archive/*/metadata.yaml")
    )

    all_packages_infos = [load_yaml(f) for f in to_load_paths]
    json.dump(all_packages_infos, sys.stdout, indent=2)

dump_docs_package_metadata()
