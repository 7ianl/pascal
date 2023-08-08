class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        m = 0
        c = keysPressed[0]
        t = 0
        for i, v in enumerate(releaseTimes):
            if v-t > m:
                m = v-t
                c = keysPressed[i]
            elif v-t == m and ord(keysPressed[i]) > ord(c):
                c = keysPressed[i]
            t = v
        return c