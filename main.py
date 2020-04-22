import utils
import object_generator
import test_object_generator, test_utils


def integration_test(size, limit):
    """
    This method test the project with a given params and prints the results
    :param size: give size array, number of objects
    :param limit: given reference range
    """
    assert type(size) is int, "Invalid given size, size must be type of int."
    assert type(limit) is int, "Invalid given limit, limit must be type of int."

    array = object_generator.generate_array(size, limit)
    print("Given Array:")
    [print(vars(a)) for a in array]
    print("Sorted Array:")
    [print(vars(a)) for a in utils.compare_sort_array(array)]


if __name__ == "__main__":
    integration_test(10, 50)
