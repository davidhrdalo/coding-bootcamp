from float_compare import are_close


def test_the_classic_example():
    assert (0.1 + 0.2 == 0.3) is False  # this is why the function exists
    assert are_close(0.1 + 0.2, 0.3) is True


def test_clearly_different_numbers():
    assert are_close(1.0, 1.1) is False


def test_identical_and_negative_numbers():
    assert are_close(5, 5) is True
    assert are_close(-0.1 - 0.2, -0.3) is True


def test_relative_tolerance_scales_with_size():
    assert are_close(1e10, 1e10 + 1) is True    # tiny relative difference
    assert are_close(1e10, 1e10 + 100) is False  # larger than 1e-9 of 1e10


def test_near_zero_needs_absolute_tolerance():
    assert are_close(0.0, 1e-12) is False
    assert are_close(0.0, 1e-12, abs_tol=1e-9) is True


def test_custom_relative_tolerance():
    assert are_close(100, 101, rel_tol=0.05) is True
    assert are_close(100, 110, rel_tol=0.05) is False
