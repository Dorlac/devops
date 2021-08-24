# Pytest naming convention
# Test functions should be in the form
# def test_should_{expected_outcome}():
# 
# Classes should be in the form
# Test{class_name}
# and should not have an __init__ method.
# Place files next to module under test with
# the name {module_name}_test.py so they are placed
# next to each other.

# Fixtures and Setup
# XUnit Style Setup and Teardown
# allow setup before Modules, Functions,
# Classes, and Methods
# 
# Add fixtures to parameter of tests 
# to run before tests. Or use @pytest.mark.usefuxtures()
# 
# Test fixture Teardown
# yield keyword or add finalizer method

# TDD
# list functionality that you intead to implement
# begin with the simplest test case
# create a failing test
# make the test pass in th simplest way possible
# refractor
# repeat for the remaining test cases
# this is known as the red, green, refactor process and is the essence of TDD
# 
# Best practices
# Do the next simplest test case
# Use descriptive test names
# Keep tests fast with minimum console output and mock out slow collaberaters
# Use Code coverage analysis tools
# Run tests multiple times and in a random order
# use pytest-random-order and pytest-repeat plugins
# use a static code analysis tool
# Use a static code analysis (pylint)
# note code repetition features and UML diagram capabilities
# Test Driven Development: By Example
# Clean Code: A Handbook of Agile Software Craftmanship
# Working Effectively with Legacy Code
# Also, Robert Martin's "Clean Code" videos: https://cleancoders.com


# Happy path (positive case) and sad path (negative case) testing
# Happy path testing handles the expected input
# Sad path testing handles unexpected or incorrect input data
# Write seperate tests for positive and negative cases
# Be sure to not combine these two tests


import pytest
from pytest import approx
from unittest.mock import MagicMock

# Test fixtures
# Use fixtures to remove duplication in setup and teardown.
# The scope of fixtures are as follows.
scopes = {"session", "module", "class", "function"}


@pytest.fixture() # specify scope and autouse as arguments
def name_of_fixture_goes_here():
    pass

# fixture will run for each test
@pytest.fixture(autouse=True)
def auto_use():
    pass

@pytest.fixture()
def teardown_with_yield():
    # do something
    yield
    # executed after the fixture goes out of scope
    # yield is a replacement for return


@pytest.fixture()
def teardown_with_add_finalizer_method(request):
    # Do something
    def teardown_step_one():
        pass
    def teardown_step_two():
        pass
    request.addfinalizer(teardown_step_one)
    request.addfinalizer(teardown_step_two)


def test_using_fixture_as_parameter(setup):
    pass

@pytest.mark.usefixtures("setup")
def test_using_fixture_decorator():
    pass

def test_should_AssertTrue():
    assert True

# use approx to compare floats
def test_float_comparison():
    assert (0.1 + 0.2 ) == approx(0.3)

# use raises to verify that expected exception is raised

# Test Doubles
# learn unittest.mock and monkeypatch
def test_returnsCorrtectStirng(monkeyppatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(retrun_value="some random string")

# Combine similar tests using parametrize decorator
@pytest.mark.parametrize("list","of","parameters","to","be","tested")
def test_multiple_senarios_tested()
    pass

# Look for conftest.py for prewritten fixtures
# don't even have to import to use the fixtures there
# keep directly under the test folder
# use pytest parameters

