class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = len(mat[0])  # Number of columns (assuming all rows have the same length)
        m = len(mat)     # Number of rows

        # Check for an element that appears in each row
        for j in range(n):
            current_element = mat[0][j]
            found_in_all_rows = all(current_element in row for row in mat[1:])

            if found_in_all_rows:
                return current_element

        return -1 