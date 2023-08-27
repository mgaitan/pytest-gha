"""
A pytest plugin to fold verbose pytest outputs, enhancing readability in 
GitHub Actions logs by grouping sections of information.
"""
import pytest


__version__ = "0.1"


def pytest_addoption(parser):
    parser.addoption("--gha-logs-fold", action="store_true", default=False,
                     help="Fold output for GitHub Actions")


def pytest_report_header(config):
    if not config.getoption("--gha-logs-fold"):
        return

    return "::group::Pytest Header Information"


def pytest_sessionstart(session):
    if not session.config.getoption("--gha-logs-fold"):
        return

    print("::group::Test Collection")


def pytest_sessionfinish(session, exitstatus):
    if not session.config.getoption("--gha-logs-fold"):
        return

    print("\n::endgroup::")
    if exitstatus == 1:  # if there are failures
        print("::group::Failures")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if not config.getoption("--gha-logs-fold"):
        return

    if exitstatus == 1:  # if there are failures
        print("::endgroup::")
    print("::endgroup::")  # Finaliza el grupo de "Pytest Header Information"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()
    report.config = item.session.config


def pytest_runtest_logreport(report):
    if not report.config.getoption("--gha-logs-fold"):
        return

    if report.failed:
        print("::endgroup::")
        print("::group::Failed Test Details")
