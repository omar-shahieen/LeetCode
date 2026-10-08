class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        currentLineWords = []
        currentLineLength = 0  # word lengths + one space per gap
        result = []

        for word in words:
            requiredLength = currentLineLength + len(word)

            # Add one space if this is not the first word
            if currentLineWords:
                requiredLength += 1

            if requiredLength <= maxWidth:
                currentLineWords.append(word)
                currentLineLength = requiredLength
            else:
                gaps = len(currentLineWords) - 1

                if gaps == 0:
                    # Single word: left-justify
                    line = currentLineWords[0].ljust(maxWidth)
                else:
                    # Total spaces to distribute = maxWidth - letters only
                    totalSpaces = maxWidth - (currentLineLength - gaps)
                    spacePerGap, extraSpaces = divmod(totalSpaces, gaps)

                    line = ""
                    for i, w in enumerate(currentLineWords[:-1]):
                        # Leftmost gaps get one extra space each
                        line += w + " " * (spacePerGap + (1 if i < extraSpaces else 0))
                    line += currentLineWords[-1]

                result.append(line)
                currentLineWords = [word]
                currentLineLength = len(word)

        # Last line: left-justified, padded on the right
        line = " ".join(currentLineWords)
        line += " " * (maxWidth - len(line))
        result.append(line)
        return result