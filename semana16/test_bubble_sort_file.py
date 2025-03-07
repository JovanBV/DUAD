from bubble_sort import bubble_sort
import pytest

def test_bubble_sort_with_small_lists():
    #Arrange
    input_list = [15, 1, 2]
    expected_result = [1, 2, 15]
    #Act
    bubble_sort(input_list)
    #Assert
    assert input_list == expected_result


def test_bubble_sort_with_big_lists():
    #Arrange
    input_list = [134, 57, 99, 121, 20, 182, 46, 72, 15, 161, 89, 5, 198, 191, 140, 106, 125, 38, 65, 174, 180, 108, 196, 24, 8, 86, 184, 48, 114, 143, 33, 149, 178, 164, 26, 104, 41, 93, 156, 151, 83, 35, 132, 60, 112, 9, 127, 193, 144, 100, 76, 70, 190, 56, 77, 102, 154, 116, 96, 172, 136, 118, 34, 167, 97, 52, 146, 17, 12, 71, 92, 45, 29, 81, 1, 110, 139, 55, 101, 113, 66, 122, 186, 88, 109, 78, 4, 47, 30, 115, 187, 123, 169, 107, 160, 22, 37, 91, 173, 79]
    expected_result = [1, 4, 5, 8, 9, 12, 15, 17, 20, 22, 24, 26, 29, 30, 33, 34, 35, 37, 38, 41, 45, 46, 47, 48, 52, 55, 56, 57, 60, 65, 66, 70, 71, 72, 76, 77, 78, 79, 81, 83, 86, 88, 89, 91, 92, 93, 96, 97, 99, 100, 101, 102, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 121, 122, 123, 125, 127, 132, 134, 136, 139, 140, 143, 144, 146, 149, 151, 154, 156, 160, 161, 164, 167, 169, 172, 173, 174, 178, 180, 182, 184, 186, 187, 190, 191, 193, 196, 198]
    #Act
    bubble_sort(input_list)
    #Assert
    assert input_list == expected_result

def test_bubble_sort_with_empty_list():
    # Arrange
    input_list = []
    # Act
    bubble_sort(input_list)
    # Assert
    assert input_list == []

def test_bubble_sort_with_string_parameter():
    #Arrange
    string_input = 'Hola'
    #Act and Assert
    with pytest.raises(TypeError):
        bubble_sort(string_input)


