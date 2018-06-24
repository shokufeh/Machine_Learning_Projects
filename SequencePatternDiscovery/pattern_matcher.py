import sys
from math import sqrt
from distribution import Distribution


def main(argv):
    pattern_sequence_path = argv[0]
    long_sequence_path = argv[1]

    pattern_sequence = []
    long_sequence = []

    # load defined pattern sequence
    with open(pattern_sequence_path) as f:
        for line in f:
            pattern_sequence.append(float(line.strip()))

    # load long sequence
    with open(long_sequence_path) as f:
        for line in f:
            long_sequence.append(float(line.strip()))

    pattern_seq_dist = Distribution.of(pattern_sequence)
    pattern_seq_len = len(pattern_sequence)

    subsequences = sliding(long_sequence, window_size=pattern_seq_len)
    similarity_scores = []

    for subsequence in subsequences:
        # skip if length of the subsequence isn't equal to pattern sequence's
        if len(subsequence) != pattern_seq_len:
            continue

        subsequence_dist = Distribution.of(subsequence)

        # it is not necessary to compute similarity score for a subsequence with
        # a distribution that is very different from pattern sequence's.
        if not pattern_seq_dist.interval_overlap_with(subsequence_dist):
            continue

        if Distribution.overlap_proportion(pattern_seq_dist, subsequence_dist) < 0.5:
            continue

        similarity_scores.append(similarity_score(pattern_sequence, subsequence))

    sorted_subsequences = sorted(zip(subsequences, similarity_scores), key=lambda triple: triple[1], reverse=True)

    # show top three subsequences
    top_subsequences = sorted_subsequences[:3]
    for subsequence, _ in top_subsequences:
        print(subsequence)


def sliding(array, window_size, step=1):
    """
    TODO: Group elements of array in fixed size windows by running a sliding window over them.

    Example:
        when window_size = 2, step = 1, array = [1, 3, 6, 2, 1, 6]
        result should be [[1, 3], [3, 6], [6, 2], [2, 1], [1, 6], [6]]
    :param array: array
    :param window_size: number of elements per group
    :param step: the distance between the first elements of successive groups
    :return: an array of grouped elements
    """
    
    subseqs = []
    for i in range(0, len(array), step):
        subseqs.append(array[i:i+window_size])
    
    return subseqs


def similarity_score(array1, array2):
    """
    TODO: Finds out how similar two array of values are in terms of scores. The similarity score doesn't have to be
    interpolated into a value within range between 0 and 1, it is just a numeric value that can help you to rank and
    get the top N similar subsequences to the given pattern sequence. The higher the score, the better matched the two
    sequences.

    Example: Similarity based on Euclidean distance.

    :param array1: an array of numeric values
    :param array2: an array of numeric values
    :return: a score
    """
    
    # using Euclidean distance
    total = sum(pow(a - b, 2) for a, b in zip(array1, array2))
    distance = sqrt(total)
    
    return 1/(distance+1)


if __name__ == "__main__":
    main(sys.argv[1:])
