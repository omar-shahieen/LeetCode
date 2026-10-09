class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        window_size = word_len * word_count

        if len(s) < window_size:
            return []

        target = Counter(words)
        res = []
        n = len(s)

        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in target:
                    seen.clear()
                    count = 0
                    left = right + word_len
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > target[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    res.append(left)

                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

        return sorted(res)
