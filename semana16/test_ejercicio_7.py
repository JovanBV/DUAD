from ejercicio_funciones_7 import delete_even_numbers, verify_even_number, verify_if_prime

def test_delete_even_numbers_mixed():
    # Arrange
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Act
    result = delete_even_numbers(input_list)
    # Assert
    assert result == [1, 2, 3, 5, 7, 9]

def test_delete_even_numbers_all_even():
    # Arrange
    input_list = [2, 4, 6, 8, 10]
    # Act
    result = delete_even_numbers(input_list)
    # Assert
    assert result == [2]

def test_delete_even_numbers_no_evens():
    # Arrange
    input_list = [1, 3, 5, 7, 9]
    # Act
    result = delete_even_numbers(input_list)
    # Assert
    assert result == [1, 3, 5, 7, 9]

def test_verify_even_number_even_above_two():
    # Act & Assert
    assert verify_even_number(4) is True

def test_verify_even_number_even_below_or_equal_two():
    # Act & Assert
    assert verify_even_number(2) is False

def test_verify_even_number_odd_number():
    # Act & Assert
    assert verify_even_number(3) is False

def test_verify_if_prime_mixed():
    # Arrange
    input_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Act
    result = verify_if_prime(input_list)
    # Assert
    assert result == [2, 3, 5, 7]

def test_verify_if_prime_all_primes():
    # Arrange
    input_list = [2, 3, 5, 7, 11, 13]
    # Act
    result = verify_if_prime(input_list)
    # Assert
    assert result == [2, 3, 5, 7, 11, 13]

def test_verify_if_prime_no_primes():
    # Arrange
    input_list = [4, 6, 8, 9, 10]
    # Act
    result = verify_if_prime(input_list)
    # Assert
    assert result == []
