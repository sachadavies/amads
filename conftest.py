from pathlib import Path


def pytest_ignore_collect(path):
    """
    Tells pytest which files to ignore when collecting and running tests.
    Returns True if the file should be ignored.
    """
    # Always skip .venv directories, because they likely correspond to virtual environments
    if ".venv" in str(path):
        return True

    # target_dirs are the directories we want to test (note we don't let pytest
    # try and collect tests directly from the demos directory)
    target_dirs = ["amads", "tests"]

    path = Path(path).resolve()
    target_dirs = [Path(dir).resolve() for dir in target_dirs]

    # Return True if the path is not a subdirectory of any of the target dirs
    return not any(path.is_relative_to(dir) for dir in target_dirs)
