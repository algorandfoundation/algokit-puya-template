<div align="center">
<a href="https://github.com/algorandfoundation/algokit-puya-template"><img src="https://bafkreihnmpvtrgloxz5exuk2ybfxkeq5b2ka5vxfjejjslswl5ecr7pvpy.ipfs.nftstorage.link/" width=60%></a>
</div>

<p align="center">
    <a target="_blank" href="https://github.com/algorandfoundation/algokit-cli"><img src="https://img.shields.io/badge/docs-repository-00dc94?logo=github&style=flat.svg" /></a>
    <a target="_blank" href="https://developer.algorand.org/algokit/"><img src="https://img.shields.io/badge/learn-AlgoKit-00dc94?logo=algorand&mac=flat.svg" /></a>
    <a target="_blank" href="https://github.com/algorandfoundation/algokit-puya-template"><img src="https://img.shields.io/github/stars/algorandfoundation/algokit-puya-template?color=00dc94&logo=star&style=flat" /></a>
    <a target="_blank" href="https://developer.algorand.org/algokit/"><img  src="https://vbr.wocr.tk/badge?page_id=algorandfoundation%2Falgokit-puya-template&color=%2300dc94&style=flat" /></a>
</p>

---

This template provides a production-ready baseline for developing and deploying [Puya](https://github.com/algorand-devrel/puya) smart contracts.

To use it [install AlgoKit](https://github.com/algorandfoundation/algokit-cli#readme) and then either pass in `-t puya` to `algokit init` or select the `puya` template.

This is one of the official templates used by AlgoKit to initialize an Algorand smart contract project. It's a [Copier template](https://copier.readthedocs.io/en/stable/).

> Please note `Puya` smart contract development language is currently in alpha / developer preview. It is not recommended for production usage yet.

## Features

This template supports the following features:

- Compilation of [multiple Puya contracts](template_content/smart_contracts/config.py) to a [predictable folder location and file layout](template_content/smart_contracts/__main__.py) where they can be deployed
- Deploy-time immutability and permanence control
- [Poetry](https://python-poetry.org/) for Python dependency management and virtual environment management
- Linting via [Ruff](https://github.com/charliermarsh/ruff) or [Flake8](https://flake8.pycqa.org/en/latest/)
- Formatting via [Black](https://github.com/psf/black)
- Type checking via [mypy](https://mypy-lang.org/)
- Testing via pytest (not yet used)
- Dependency vulnerability scanning via pip-audit (not yet used)
- VS Code configuration (linting, formatting, breakpoint debugging)
- dotenv (.env) file for configuration
- Automated testing of the compiled smart contracts
- [Output stability](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/articles/output_stability.md) tests of the TEAL output
- CI/CD pipeline using GitHub Actions:
- - Optionally pick deployments to Netlify or Vercel

# Getting started

Once the template is instantiated you can follow the [README.md](template_content/README.md.jinja) file to see instructions for how to use the template.
