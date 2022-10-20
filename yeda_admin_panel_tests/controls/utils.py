from selene import have, command
from selene.support.shared import browser


def resource(relative_path):
    import yeda_admin_panel_tests
    from pathlib import Path
    return (
        Path(yeda_admin_panel_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )

