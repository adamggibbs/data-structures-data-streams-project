import sys
import os
from collections import defaultdict


def exact_algorithm(thres, file_path):
    """Run exact frequent items algorithm"""
    M = defaultdict(int)
    dataset_size = 0
    output = list()

    with open(file_path, "r") as dataset:
        # Process the transactions as we get them
        for transaction in dataset:
            dataset_size += 1
            # Get the transaction as list of ints
            transaction = [
                int(item) for item in transaction.split() if item.isnumeric()
            ]
            # Using defaultdict properties of initializing the value for a
            # non-existing key to 0
            for item in transaction:
                M[item] += 1

    # filtering step
    for key in M:
            output.append((key, M[key]))

    return output
