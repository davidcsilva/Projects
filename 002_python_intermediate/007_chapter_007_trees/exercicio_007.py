'''
Prefix Tree
'''


class TrieNode:
    def __init__(self):
        self.children = {}      # Maps character -> TrieNode
        self.is_end = False     # True if a complete word ends at this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the Trie in O(m) time, where m = len(word)."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        """Returns True only if the exact complete word exists in the Trie."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Returns True if any word in the Trie starts with the given prefix."""
        return self._find_node(prefix) is not None

    def autocomplete(self, prefix):
        """Returns all complete words in the Trie starting with 'prefix'."""
        node = self._find_node(prefix)
        if not node:
            return []

        results = []
        self._dfs_collect(node, prefix, results)
        return results

    def delete(self, word):
        """Deletes a word from the Trie and cleans up unused nodes."""
        def _delete_helper(current, word, depth):
            if depth == len(word):
                if not current.is_end:
                    return False  # Word does not exist
                current.is_end = False
                # Node can be deleted only if it has no other children
                return len(current.children) == 0

            char = word[depth]
            if char not in current.children:
                return False

            should_delete_child = _delete_helper(
                current.children[char], word, depth + 1)

            if should_delete_child:
                del current.children[char]
                return len(current.children) == 0 and not current.is_end

            return False

        _delete_helper(self.root, word, 0)

    def _find_node(self, text):
        current = self.root
        for char in text:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def _dfs_collect(self, node, path, results):
        if node.is_end:
            results.append(path)
        for char, child_node in node.children.items():
            self._dfs_collect(child_node, path + char, results)


# --- Example Usage ---
trie = Trie()
words = ["apple", "app", "application", "apt", "bat", "batch", "bath"]
for w in words:
    trie.insert(w)

print("Search 'app':        ", trie.search("app"))         # True
print("Search 'appl':       ", trie.search(
    "appl"))        # False (prefix only)
print("Starts with 'appl':  ", trie.starts_with("appl"))   # True
print("Autocomplete 'app':  ", trie.autocomplete(
    "app"))   # ['app', 'apple', 'application']
print("Autocomplete 'bat':  ", trie.autocomplete(
    "bat"))   # ['bat', 'batch', 'bath']

trie.delete("app")
print("After deleting 'app':", trie.autocomplete(
    "app"))   # ['apple', 'application']
