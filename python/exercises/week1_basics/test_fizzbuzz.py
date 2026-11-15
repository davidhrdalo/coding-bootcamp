from fizzbuzz import fizzbuzz


def test_first_five():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_multiples_up_to_fifteen():
    result = fizzbuzz(15)
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[9] == "Buzz"
    assert result[14] == "FizzBuzz"


def test_zero_gives_empty_list():
    assert fizzbuzz(0) == []


def test_length_matches_n():
    assert len(fizzbuzz(100)) == 100
