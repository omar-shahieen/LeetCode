class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        childs = defaultdict(dict)

        for s in strs:
            node = childs
            for c in s:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = {}  # end of word marker

        pref = ""
        node = childs
        for c in strs[0]:
            if "#" in node:       # a shorter word ended here
                return pref
            if c not in node:     # character not shared
                return pref
            if len(node) > 1:  # branch point (or end marker counts as branch)
                return pref 
            pref += c
            node = node[c]

        return pref