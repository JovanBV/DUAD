from ejercicio_funciones_6 import convert_to_list, sort_list, combine_list

def test_convert_to_list_with_hyphenated_string():
    # Arrange
    input_value = "apple-banana-cherry"
    # Act
    result = convert_to_list(input_value)
    # Assert
    assert result == ["apple", "banana", "cherry"]


def test_convert_to_list_with_empty_string():
    # Arrange
    input_value = ""
    # Act
    result = convert_to_list(input_value)
    # Assert
    assert result == [""]  


def test_convert_to_list_with_no_hyphens():
    # Arrange
    input_value = "singleword"
    # Act
    result = convert_to_list(input_value)
    # Assert
    assert result == ["singleword"]


def test_sort_list_with_mixed_strings():
    # Arrange
    input_value = ["banana", "apple", "cherry"]
    # Act
    result = sort_list(input_value)
    # Assert
    assert result == ["apple", "banana", "cherry"]


def test_sort_list_with_numbers_as_strings():
    # Arrange
    input_value = ["3", "1", "2"]
    # Act
    result = sort_list(input_value)
    # Assert
    assert result == ["1", "2", "3"]


def test_sort_list_with_identical_elements():
    # Arrange
    input_value = ["same", "same", "same"]
    # Act
    result = sort_list(input_value)
    # Assert
    assert result == ["same", "same", "same"]  


def test_combine_list_with_words():
    # Arrange
    input_value = ["hello", "world"]
    # Act
    result = combine_list(input_value)
    # Assert
    assert result == "helloworld"


def test_combine_list_with_empty_strings():
    # Arrange
    input_value = ["", "", ""]
    # Act
    result = combine_list(input_value)
    # Assert
    assert result == ""


def test_combine_list_with_numbers_as_strings():
    # Arrange
    input_value = ["1", "2", "3"]
    # Act
    result = combine_list(input_value)
    # Assert
    assert result == "123"
