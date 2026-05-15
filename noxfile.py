from __future__ import annotations

import nox


@nox.session
def spelling(session: nox.Session):
    """
    Spell check documentation
    """
    session.install("-r", "requirements/spelling.in", "-c", "requirements/spelling.txt")
    session.run(
        "codespell",
        "docs",
        *session.posargs,
    )


@nox.session
def build(session: nox.Session):
    """
    Build the docsite with mkdocs
    """
    session.install("-r", "requirements/requirements.in", "-c", "requirements/requirements.txt")
    session.run(
        "mkdocs",
        "build",
        "--strict",
        *session.posargs,
    )
