from ejercicio_funciones_5 import find_lower, find_upper

def test_find_upper_with_numbers_and_letters():
    # Arrange
    input_value = 'There are 45 Oscars in the South Park.'
    # Act
    result = find_upper(input_value)
    # Assert
    assert result == 4

def test_find_upper_with_special_characters():
    # Arrange
    input_value = '#$%^#@@!%#'
    # Act
    result = find_upper(input_value)
    # Assert
    assert result == 0

def test_find_upper_with_all_uppercase():
    # Arrange
    input_value = 'HELLO WORLD'
    # Act
    result = find_upper(input_value)
    # Assert
    assert result == 10

def test_find_lower_with_mixed_case():
    # Arrange
    input_value = "Hello World"
    # Act
    result = find_lower(input_value)
    # Assert
    assert result == 8  
def test_find_lower_with_no_lowercase():
    # Arrange
    input_value = "HELLO WORLD!"
    # Act
    result = find_lower(input_value)
    # Assert
    assert result == 0  

def test_find_lower_with_only_lowercase():
    # Arrange
    input_value = "hello world"
    # Act
    result = find_lower(input_value)
    # Assert
    assert result == 10  
