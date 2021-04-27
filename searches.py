class SearchAlgorithms:

    def __init__(self):
        pass

    def linear(self, s_list, n):

        for i in range(len(s_list)):
            if s_list[i] == n:
                return i

        return -1

    def binary(self, s_list, n, min_at, max_at):

        """
        :param s_list: Sorted List which is to be searched from
        :param n: Element to be searched
        :param min_at: Zero
        :param max_at: Length of the list
        :return: Index at which the element was found / -1 If element absent
        """

        mid = (min_at + max_at) // 2
        if s_list[mid] == n:
            return mid
        elif s_list[mid] > n:
            return self.binary(s_list, n, min_at, mid - 1)
        else:
            return self.binary(s_list, n, mid + 1, max_at)

        return -1

    def exponential(self, s_list, n, e):
        
        """
        :param s_list: List to be searched from
        :param n: Element to be searched
        :param e: Raise function to the power e
        :return: Index at which the element was found / -1 If element absent
        """

        if s_list[0] == n:
            return 0

        at = 1
        while at < len(s_list) and s_list[at] <= n:
            at = at * e

        if at > len(s_list):
            l = len(s_list)
        else:
            l = at

        return self.binary(s_list[:l], n, 0, len(s_list[:l]))

    def interpolation(self, s_list, n):

        low, high = 0, (len(s_list) - 1)
        while low <= high and s_list[low] <= n <= s_list[high]:
            try:
                at = low + int(((float(high - low) / (s_list[high] - s_list[low])) * (n - s_list[low])))
                if s_list[at] == n:
                    return at
                if s_list[at] < n:
                    low = at + 1;
                else:
                    high = at - 1;
            except ZeroDivisionError:
                break

        return -1

    def hop(self, s_list, n, jump):
        
        """
        :param s_list: List to be searched from
        :param n: Element to be searched
        :param jump: Make hops of how many elements?
        :return: Index at which the element was found / -1 If element absent
        """
        low, high = 0, 0
        l = len(s_list)

        while s_list[low] <= n and low < l:

            if l - 1 > low + jump:
                high = low + jump
            else:
                high = l - 1

            if s_list[low] <= n <= s_list[high]:
                break

            low += jump;

        if low >= l or s_list[low] > n:
            return -1

        if l - 1 > low + jump:
            pass
        else:
            high = l - 1

        i = low

        while i <= high and s_list[i] <= n:

            if s_list[i] == n:
                return i

            i += 1

        return -1

    def fibonacci(self, s_list, n):

        neg_one, neg_two = 1, 0
        fib = neg_one + neg_two

        while fib < len(s_list):
            neg_two, neg_one = neg_one, fib
            fib += neg_two

        at = -1

        while fib > 1:
            i = min(at + neg_two, (len(s_list) - 1))

            if s_list[i] < n:

                fib, neg_one = neg_one, neg_two
                neg_two, at = fib - neg_one, i

            elif s_list[i] > n:

                fib = neg_two
                neg_one -= neg_two
                neg_two = fib - neg_one

            else:
                return i

        if neg_one and at < (len(s_list) - 1) and s_list[at + 1] == n:
            return at + 1;
        return -1
