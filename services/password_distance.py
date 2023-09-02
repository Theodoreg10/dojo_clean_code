
def compute_levenshtein_distance(string1, string2):
    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    elif string1[0] == string2[0]:
        return compute_levenshtein_distance(tail(string1), tail(string2)
                                            )
    else:
        value_a = compute_levenshtein_distance(tail(string1), string2)
        value_b = compute_levenshtein_distance(string1, tail(string2))
        value_c = compute_levenshtein_distance(tail(string1),
                                               tail(string2))
        return 1 + min(value_a, value_b, value_c)


def tail(string):
    return string[1:]


if __name__ == "__main__":
    assert (compute_levenshtein_distance("Python", "Peithen") == 3)
    assert (compute_levenshtein_distance("Azerty12", "Azerty14") == 1)
    assert (compute_levenshtein_distance("Toto", "toto13") == 3)
    assert (compute_levenshtein_distance("JohnDoe2001", "Johndoe2002") == 2)
