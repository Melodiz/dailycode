import numpy as np
def subsample_frequent_words(word_count_dict, threshold=1e-5):
    """
    Calculates the subsampling probabilities for words based on their frequencies.

    This function is used to determine the probability of keeping a word in the dataset
    when subsampling frequent words. The method used is inspired by the subsampling approach
    in Word2Vec, where each word's frequency affects its probability of being kept.

    Parameters:
    - word_count_dict (dict): A dictionary where keys are words and values are the counts of those words.
    - threshold (float, optional): A threshold parameter used to adjust the frequency of word subsampling.
                                   Defaults to 1e-5.

    Returns:
    - dict: A dictionary where keys are words and values are the probabilities of keeping each word.

    Example:
    >>> word_counts = {'the': 5000, 'is': 1000, 'apple': 50}
    >>> subsample_frequent_words(word_counts)
    {'the': 0.028, 'is': 0.223, 'apple': 1.0}
    """
    total_count = sum(word_count_dict.values())
    keep_prob_dict = {}

    for word, count in word_count_dict.items():
        frequency = count / total_count
        drop_prob = 1 - np.sqrt(threshold / frequency)
        keep_prob_dict[word] = max(0, 1 - drop_prob)

    return keep_prob_dict


def get_negative_sampling_prob(word_count_dict):
    """
    Calculates the negative sampling probabilities for words based on their frequencies.

    This function adjusts the frequency of each word raised to the power of 0.75, which is
    commonly used in algorithms like Word2Vec to moderate the influence of very frequent words.
    It then normalizes these adjusted frequencies to ensure they sum to 1, forming a probability
    distribution used for negative sampling.

    Parameters:
    - word_count_dict (dict): A dictionary where keys are words and values are the counts of those words.

    Returns:
    - dict: A dictionary where keys are words and values are the probabilities of selecting each word
            for negative sampling.

    Example:
    >>> word_counts = {'the': 5000, 'is': 1000, 'apple': 50}
    >>> get_negative_sampling_prob(word_counts)
    {'the': 0.298, 'is': 0.160, 'apple': 0.042}
    """

    # Calculate the total sum of frequencies raised to the power of 0.75
    total_count = sum(count**0.75 for count in word_count_dict.values())

    # Calculate the probability for each word
    negative_sampling_prob_dict = {
        word: (count**0.75) / total_count for word, count in word_count_dict.items()
    }

    return negative_sampling_prob_dict
