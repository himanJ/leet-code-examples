from typing import List


# Recursion is breaking down the problem into similar smaller problem.
# recursive function here needs to track:
#   1. current response array - current_arr
#   2. next_position in the remaining list - next_position
#   3. target.(final_target - sum of current_arr).
#Finding sub-list in candidates= [1, 2, 2, 2, 5] with target(final) = 5 breaks down as:
#   current_arr=[1], target(remaining)=4, next_position=1 (index in candidates[])
#       current_arr=[1, 2], target= 5-(1+2) = 2, next_position=2
#           current_arr=[1,2,2], target=0, next_position=3 . Notice when target=0, a result is available to add to the final result. Add current_arr to final_result
#               current_arr=[1,2,2,2], target=-2, next_position=4. When target < 0, array sum has exceeded the target value, this array can be ignored.
#           current_arr=[1,2,5(skipped remaining 2s here. 2 is already used at 3rd position in step above)], target = -3, next_position=N/A. target < 0, stop further recursion.
#       current_arr=[1,5(skipped all 2s, since 2 is used at second position in the step above)], target = -6, next_position=N/A. target < 0, stop further recursion.
#   current_arr=[2], target = 3, next_position=2
#       current_arr=[2,2], target = 1, next_position=3
#           current_arr=[2,2,2], target = -1, next_position=4. target < 0, stop further recursion.
#           current_arr=[2,2,5], target = -4, next_position=N/A. target < 0, stop.
#       current_arr=[2,5(skipped remaining 2s)], target = -2, next_position=N/A. target <0, stop.
#   current_arr=[5(skipped remaining 2s, already used at 1st position above)], target=5, next_position=N/A. target=0. Add to result
# Notice, We added 2 current_arr to result above(wherever, target=0).
# result=[[1,2,2], [5]]

def backtrack():

def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    result = List[List[int]]

    # Sort the list so that "Each element in candidates may only be used once in the combination."
    # You can skip the same number as you iterate through the list ( see prev in the backtrack function)
    candidates.sort()
    print(f"{candidates=}") # [1, 2, 2, 2, 5]






def main():
    candidates = [2, 5, 2, 1, 2]
    target = 5
    combination_sum2(candidates, target)


if __name__ == "__main__":
    main()
