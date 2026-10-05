class Solution:

    def encode(self, strs: List[str]) -> str:
        return '1'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('1')
