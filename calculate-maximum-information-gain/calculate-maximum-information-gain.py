class Solution:
    def calculateEntropy(self, input: List[str]) -> float:
        counter = collections.Counter(input)
        ans = 0
        for count in counter.values():
            p = count / len(input)
            ans += -1 * p * math.log2(p)
        return ans
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        if not petal_length or not species:
            return 0
        length_species_list = sorted(zip(petal_length, species))
        # Unpack to two lists
        petal_length, species = zip(*length_species_list)

        # To maximize information gain, minimize subgroup weighted entropy sum
        subgroup_weighted_entropy_sum = float('inf')
        n = len(petal_length)
        
        # Try all the splitting position
        for i in range(1, n):
            h_1 = self.calculateEntropy(species[:i])
            h_2 = self.calculateEntropy(species[i:])
            subgroup_weighted_entropy_sum = min(subgroup_weighted_entropy_sum, h_1 * (i / n) + h_2 * ((n - i) / n))

        original_group_entropy = self.calculateEntropy(species)

        return original_group_entropy - subgroup_weighted_entropy_sum