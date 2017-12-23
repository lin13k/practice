class Movie_Rating:
    """docstring for Movie_Rating"""

    def rate(self, rates):
        return self.dp(rates, False)

    def dp(self, rates, skipFlag):
        if(len(rates) == 0):
            return 0

        pickSum = rates[0] + self.dp(rates[1:], False)
        if skipFlag is False:
            # can skip
            skipSum = self.dp(rates[1:], True)
            return max(pickSum, skipSum)
        else:
            # cannot skip
            return pickSum


if __name__ == "__main__":
    print(Movie_Rating().rate([9,-1,-3,4,5]))
    print(Movie_Rating().rate([-1,-2,-3,-4,-5]))
