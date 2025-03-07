from ejercicio_funciones_3 import sum_all_list

def test_sum_all_list_with_float_parameter():
    # Arrange
    input_list = [1.5,1.5,3,4]
    # Act
    result = sum_all_list(input_list)
    # Assert
    assert result == 10

def test_sum_all_list_with_big_list():
    # Arrange
    input_list = [847, 392, 15, 764, 921, 104, 550, 832, 307, 691, 248, 965, 186, 742, 588, 633, 456, 378, 111, 799, 203, 975, 26, 847, 512, 924, 314, 680, 157, 834, 721, 569, 495, 133, 740, 21, 901, 230, 665, 815, 350, 487, 783, 241, 92, 608, 456, 177, 312, 999]
    # Act
    result = sum_all_list(input_list)
    # Assert
    assert result == 25796

def test_sum_all_list_with_negative_integers():
    # Arrange
    input_list = [-8, -78, -2]
    # Act
    result = sum_all_list(input_list)
    # Assert
    assert result == -88
