from group_anagrams import group_anagrams


def normalise(groups):
    return sorted(sorted(group) for group in groups)


def test_example():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert normalise(result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_empty_list():
    assert group_anagrams([]) == []


def test_empty_string():
    assert normalise(group_anagrams([""])) == [[""]]


def test_no_anagrams():
    result = group_anagrams(["a", "b", "c"])
    assert normalise(result) == [["a"], ["b"], ["c"]]
