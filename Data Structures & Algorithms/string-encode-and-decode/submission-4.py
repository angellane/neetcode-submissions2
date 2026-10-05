class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'pspsps'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('pspsps')
