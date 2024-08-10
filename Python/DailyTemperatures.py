# pylint: disable:missing-module-docstring,invalid-name
class DailyTemperatures:
    """2232"""
    def solution1(self, temperatures: list[int]) -> list[int]:
        """ O(n^2) solution"""
        res = [0] * len(temperatures)

        # pylint: disable=consider-using-enumerate
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res

    def solution2(self, temperatures: list[int]) -> list[int]:
        """_summary_

        Args:
            temperatures (list[int]): _description_

        Returns:
            list[int]: _description_
        """
        res = [0] * len(temperatures)
        stack: list[list[int]] = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_t
            stack.append([t, i])
        return res