from ejercicio_funciones_4 import turn_string

def test_turn_string_with_no_values():
    # Arrange
    input_value = ''
    # Act
    result = turn_string(input_value)
    # Assert
    assert result == ''


def test_turn_string_with_spaces():
    # Arrange
    input_value = 'Hello world'
    # Act
    result = turn_string(input_value)
    # Assert
    assert result == 'dlrow olleH'


def test_turn_string_with_single_character():
    # Arrange
    input_value = 'A'
    # Act
    result = turn_string(input_value)
    # Assert
    assert result == 'A'