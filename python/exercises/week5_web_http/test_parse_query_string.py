from parse_query_string import parse_query


def test_simple_pairs():
    assert parse_query("a=1&b=2") == {"a": ["1"], "b": ["2"]}


def test_repeated_keys_collect_in_order():
    assert parse_query("tag=a&tag=b&tag=c") == {"tag": ["a", "b", "c"]}


def test_plus_and_percent_20_are_spaces():
    assert parse_query("q=hello+world&r=hello%20there") == {"q": ["hello world"], "r": ["hello there"]}


def test_utf8_percent_sequences():
    assert parse_query("name=caf%C3%A9") == {"name": ["café"]}


def test_encoded_ampersand_and_equals_do_not_split():
    assert parse_query("x=a%26b%3Dc") == {"x": ["a&b=c"]}


def test_keys_are_decoded_too():
    assert parse_query("first%20name=Ada") == {"first name": ["Ada"]}


def test_key_without_equals_has_empty_value():
    assert parse_query("flag&a=1") == {"flag": [""], "a": ["1"]}


def test_leading_question_mark_and_empty_parts_ignored():
    assert parse_query("?a=1&&b=2&") == {"a": ["1"], "b": ["2"]}


def test_empty_string():
    assert parse_query("") == {}


def test_bad_percent_sequences_stay_literal():
    assert parse_query("p=100%&q=%zz&r=%4") == {"p": ["100%"], "q": ["%zz"], "r": ["%4"]}
