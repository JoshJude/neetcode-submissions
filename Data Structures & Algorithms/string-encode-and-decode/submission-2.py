class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded = encoded + (',' if encoded else '') + str(len(s))

        encoded = encoded + '/'

        for s in strs:
            encoded = encoded + s

        # print(encoded)

        return encoded

    def decode(self, s: str) -> List[str]:
        ptr = 0
        strs = []

        parts = s.split('/', 1)
        lengths = [int(l) for l in parts[0].split(',') if l]
        encoded = parts[1]

        for l in lengths:
            strs.append(encoded[ptr:ptr+l])
            ptr = ptr + l
        
        return strs