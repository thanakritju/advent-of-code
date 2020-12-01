from area import biggest_area


def test_biggest_area():
    test_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]

    actual = biggest_area(test_input)

    assert actual == 17
