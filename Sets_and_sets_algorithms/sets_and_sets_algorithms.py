def set_algorithms_demo():
    """
    Demonstrates basic set algorithms: union, intersection, difference, symmetric difference,
    subset, superset, and membership testing.
    """
    # Create two sets with some overlapping elements
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    # Union: all unique elements from both sets
    union_set = set_a | set_b  # or set_a.union(set_b)
    print("Union:", union_set)

    # Intersection: elements common to both sets
    intersection_set = set_a & set_b  # or set_a.intersection(set_b)
    print("Intersection:", intersection_set)

    # Difference: elements in set_a but not in set_b
    difference_set = set_a - set_b  # or set_a.difference(set_b)
    print("Difference (A - B):", difference_set)

    # Symmetric Difference: elements in either set, but not both
    sym_diff_set = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
    print("Symmetric Difference:", sym_diff_set)

    # Subset and Superset checks
    print("Is set_a a subset of union_set?", set_a.issubset(union_set))
    print("Is union_set a superset of set_b?", union_set.issuperset(set_b))

    # Membership test
    print("Is 3 in set_b?", 3 in set_b)
    print("Is 6 in set_b?", 6 in set_b)

    # Removing duplicates from a list using set
    list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
    unique_list = list(set(list_with_duplicates))
    print("Unique elements from list:", unique_list)


# Example usage:
if __name__ == "__main__":
    set_algorithms_demo()
