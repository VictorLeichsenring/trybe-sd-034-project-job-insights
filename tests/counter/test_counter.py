from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'

    # Teste para a palavra "Python"
    python_result = count_ocurrences(path, 'Python')
    assert python_result == 1639

    # Teste para "Python" em lowercase
    python_result_lowercase = count_ocurrences(path, 'python')
    assert python_result_lowercase == 1639

    # Teste para "Python" em uppercase
    python_result_uppercase = count_ocurrences(path, 'PYTHON')
    assert python_result_uppercase == 1639

    # Teste para a palavra "JavaScript"
    javascript_result = count_ocurrences(path, 'JavaScript')
    assert javascript_result == 122

    # Teste para "JavaScript" em lowercase
    javascript_result_lowercase = count_ocurrences(path, 'javascript')
    assert javascript_result_lowercase == 122

    # Teste para "JavaScript" em uppercase
    javascript_result_uppercase = count_ocurrences(path, 'JAVASCRIPT')
    assert javascript_result_uppercase == 122


if __name__ == "__main__":
    test_counter()
