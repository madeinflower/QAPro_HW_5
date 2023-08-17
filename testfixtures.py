import pytest

# Фикстура с scope='function'
@pytest.fixture(scope='function')
def sample_list():
    return [1, 2, 3]

@pytest.fixture(scope='function')
def sample_dict():
    return {'a': 1, 'b': 2, 'c': 3}

@pytest.fixture(scope='module')
def module_fixture():
    print("\nModule fixture setup")
    yield
    print("\nModule fixture teardown")

# Тестовые функции, использующие фикстуры
def test_list_sum(sample_list):
    assert sum(sample_list) == 6

def test_dict_keys(sample_dict):
    assert 'a' in sample_dict
    assert 'b' in sample_dict
    assert 'c' in sample_dict

def test_list_length(sample_list):
    assert len(sample_list) == 3

def test_module_fixture_usage(module_fixture):
    print("\nTest using module fixture")

def test_another_module_fixture_usage(module_fixture):
    print("\nAnother test using module fixture")
