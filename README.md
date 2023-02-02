# Projetu Devcontainer

This repository contains a script to install a devcontainer for the Projetu project.
This allows you to have a development environment that is identical to the one used by the CI/CD.

## Requirements

This script requires that you edit your project description in VSCode. It also requires that you have Docker installed.

- [Docker](https://docs.docker.com/get-docker/)
- [VSCode](https://code.visualstudio.com/download)

## Installation

Open a terminal in VSCode and run the following command:

```
python3 -c "$(wget -q -O - https://raw.githubusercontent.com/heia-fr/projetu-devcontainer/main/install.py)"
```

At the root directory of your project, add a file named `.env` with the following content:

```
AUTHOR="Your Name"
ACADEMIC_YEAR=2022-2023
TYPE=ps6
```

## Usage

Open the project in a VSCode devcontainer. Then open a terminal and at the root directory of your project, run the following command:

```
serve
```
