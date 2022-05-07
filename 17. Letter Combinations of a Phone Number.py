#백트래킹 문제
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dic= {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        result = []

        if digits =="":
            return result
        self.dfs(digits, 0, dic, "", result)

        return result

    def dfs(self, digits, index, dic, item, result):
        if len(digits) == index :
            result.append(item)
            return
        for char in dic[digits[index]]:
            self.dfs(digits, index + 1, dic, item+char, result)
