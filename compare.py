import csv
import time
from algorithms import linear_search, binary_search, interpolation_search
from binary_tree import (
    BinarySearchTree,
    tree_linear_search,
    tree_binary_search,
    tree_interpolation_search,
)


def compare_search(left_border, right_border, step):
    data = []

    for n in range(left_border, right_border, step):
        linear_search_time, binary_search_time, interpolation_search_time = (
            get_arr_time(n)
        )
        (
            tree_linear_search_time,
            tree_binary_search_time,
            tree_interpolation_search_time,
        ) = get_tree_time(n)
        data.append(
            [
                n,
                linear_search_time,
                binary_search_time,
                interpolation_search_time,
                tree_linear_search_time,
                tree_binary_search_time,
                tree_interpolation_search_time,
            ]
        )

    return data


def get_arr_time(n):
    arr = list(range(n))
    target = n + 1

    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    linear_search_time = "{:e}".format(end_time - start_time)

    start_time = time.time()
    binary_search(arr, target)
    end_time = time.time()
    binary_search_time = "{:e}".format(end_time - start_time)

    start_time = time.time()
    interpolation_search(arr, target)
    end_time = time.time()
    interpolation_search_time = "{:e}".format(end_time - start_time)

    return linear_search_time, binary_search_time, interpolation_search_time


def get_tree_time(n):
    bst = BinarySearchTree()
    root = bst.root

    mid = n // 2
    for i in range(mid):
        bst.insert(i)
    for i in range(mid, n):
        bst.insert(i)
    target = n - 1

    start_time = time.time()
    tree_linear_search(root, target)
    end_time = time.time()
    tree_linear_search_time = "{:e}".format(end_time - start_time)

    start_time = time.time()
    tree_binary_search(root, target)
    end_time = time.time()
    tree_binary_search_time = "{:e}".format(end_time - start_time)

    start_time = time.time()
    tree_interpolation_search(root, target)
    end_time = time.time()
    tree_interpolation_search_time = "{:e}".format(end_time - start_time)

    return (
        tree_linear_search_time,
        tree_binary_search_time,
        tree_interpolation_search_time,
    )


def write_csv_data(left_border, right_border, step):
    data = compare_search(left_border, right_border, step)

    with open("search_comparison.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Number of Elements",
                "Linear Search Time",
                "Binary Search Time",
                "Interpolation Search Time",
                "Tree Linear Search Time",
                "Tree Binary Search Time",
                "Tree Interpolation Search Time",
            ]
        )
        writer.writerows(data)
        print("Comparison data saved to search_comparison.csv")


# write_csv_data(200, 1000, 200)
