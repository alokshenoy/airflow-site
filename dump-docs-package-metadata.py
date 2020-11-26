import json
import sys

import os
from typing import List
import semver


ROOT_DIR = os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))
APACHE_AIRFLOW_ARCHIVE = os.path.join(ROOT_DIR, "docs-archive")
PACKAGE_ARCHIVE = os.path.join(ROOT_DIR, "docs-packages-archive")


def get_all_versions(directory: str) -> List[str]:
    return sorted(
        (f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))),
        key=lambda d: semver.VersionInfo.parse(d),
    )


def get_stable_version(directory: str):
    with open(os.path.join(directory, "stable.txt")) as f:
        return f.read().strip()


def dump_docs_package_metadata():
    all_packages_infos = [
        {
            "package-name": "apache-airflow",
            "stable-version": get_stable_version(APACHE_AIRFLOW_ARCHIVE),
            "all-versions": get_all_versions(APACHE_AIRFLOW_ARCHIVE),
        }
    ]

    all_packages_infos.extend(
        {
            "package-name": f,
            "stable-version": get_stable_version(os.path.join(PACKAGE_ARCHIVE, f)),
            "all-versions": get_all_versions(os.path.join(PACKAGE_ARCHIVE, f)),
        }
        for f in os.listdir(PACKAGE_ARCHIVE)
        if os.path.exists(os.path.join(PACKAGE_ARCHIVE, f, "stable.txt"))
    )

    json.dump(all_packages_infos, sys.stdout, indent=2)


dump_docs_package_metadata()
