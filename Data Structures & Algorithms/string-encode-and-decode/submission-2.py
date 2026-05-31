class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result = result + i + "-|-"
        return result

    def decode(self, s: str) -> List[str]:
        l = s.split("-|-")
        l.pop(-1)
        return l
