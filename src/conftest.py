# import os,pytest
# import Framework
#
#
# @pytest.fixture
# def browser(request):
#     "pytest fixture for browser"
#     return request.config.getoption("-B")
#
# @pytest.fixture
# def browser_version(request):
#     "pytest fixture for browser version"
#     return request.config.getoption("-V")
#
# @pytest.fixture
# def os_name(request):
#     "pytest fixture for os_name"
#     return request.config.getoption("-P")
#
# @pytest.fixture
# def os_version(request):
#     "pytest fixture for os version"
#     return request.config.getoption("-O")
#
# # def pytest_terminal_summary(terminalreporter, exitstatus):
# #     "add additional section in terminal summary reporting."
#
# def pytest_addoption(parser):
#    Framework.OptionParser().set_standard_options()