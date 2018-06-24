import numpy


class Distribution:
    def __init__(self, mean, stddev):
        self._mean = mean
        self._stddev = stddev
        self._min = self._mean - self._stddev  # not actual minimum, one standard deviation min
        self._max = self._mean + self._stddev  # not actual maximum, one standard deviation max

    def __repr__(self):
        return "Distribution(mean={}, stddev={}, min={}, max={})".format(self.mean, self.stddev, self.min, self.max)

    @staticmethod
    def of(array):
        return Distribution(float(numpy.mean(array)), float(numpy.std(array)))

    @property
    def mean(self):
        return self._mean

    @property
    def stddev(self):
        return self._stddev

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    def interval_overlap_with(self, distribution):
        """
        TODO: Returns True if the interval [min, max] of two distributions are overlapping otherwise return False.
        The implementation of this method must be commutative, meaning that a.range_overlap_with(b) == b.range_overlap_with(a)

        example:
            if a.min == 1 and a.max == 5, b.min == 3 and b.max == 6,
            then a.range_overlap_with(b) == True == b.range_overlap_with(a)

        :param distribution: another Distribution object
        :return: a boolean value
        """
        
        largest_min = self.min if self.min > distribution.min else distribution.min
        smallest_max = self.max if self.max < distribution.max else distribution.max
        
        return largest_min <= smallest_max

    @staticmethod
    def overlap_proportion(distribution1, distribution2):
        """
        TODO: Find the degree of overlap between the interval [min, max] of two distributions in terms of proportion.
        The return value must fall within the range between 0 and 1.

        :param distribution1: Distribution object
        :param distribution2: Distribution object
        :return: a numeric value (between 0 and 1)
        """
        
        if distribution1.min > distribution2.min:
            larger_min = distribution1.min
            smaller_min = distribution2.min
        else:
            larger_min = distribution2.min
            smaller_min = distribution1.min
        
        if distribution1.max > distribution2.max:
            larger_max = distribution1.max
            smaller_max = distribution2.max
        else:
            larger_max = distribution2.max
            smaller_max = distribution1.max
        
        if larger_min > smaller_max: # no overlap
            return 0
        
        overlap = smaller_max - larger_min
        total_interval = larger_max - smaller_min 
        
        return overlap/total_interval
