from src.pre_built.counter import count_ocurrences

def test_counter():
    path = 'data/jobs.csv'
    
    # Teste para a palavra "Python"
    python_result = count_ocurrences(path, 'Python')
    assert python_result == 1639, f"Teste falhou para a palavra 'Python'. Esperado: 1639, Obtido: {python_result}"
    
    # Teste para "Python" em lowercase (insensibilidade a maiúsculas e minúsculas)
    python_result_lowercase = count_ocurrences(path, 'python')
    assert python_result_lowercase == 1639, f"Teste falhou para 'python' (lowercase). Esperado: 1639, Obtido: {python_result_lowercase}"
    
    # Teste para "Python" em uppercase
    python_result_uppercase = count_ocurrences(path, 'PYTHON')
    assert python_result_uppercase == 1639, f"Teste falhou para 'PYTHON' (uppercase). Esperado: 1639, Obtido: {python_result_uppercase}"
    
    # Teste para a palavra "JavaScript"
    javascript_result = count_ocurrences(path, 'JavaScript')
    assert javascript_result == 122, f"Teste falhou para a palavra 'JavaScript'. Esperado: 122, Obtido: {javascript_result}"
    
    # Teste para "JavaScript" em lowercase (insensibilidade a maiúsculas e minúsculas)
    javascript_result_lowercase = count_ocurrences(path, 'javascript')
    assert javascript_result_lowercase == 122, f"Teste falhou para 'javascript' (lowercase). Esperado: 122, Obtido: {javascript_result_lowercase}"
    
    # Teste para "JavaScript" em uppercase
    javascript_result_uppercase = count_ocurrences(path, 'JAVASCRIPT')
    assert javascript_result_uppercase == 122, f"Teste falhou para 'JAVASCRIPT' (uppercase). Esperado: 122, Obtido: {javascript_result_uppercase}"
    
    print("Todos os testes passaram.")

if __name__ == "__main__":
    test_counter()
    