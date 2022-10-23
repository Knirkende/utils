
class TrieGraph:

    def __init__(self):
        self.root = {}
        self.term = False

    def add_word(self, word):
        if self.root.get(word[0]) is not None:
            self.root[word[0]].add_word(word[1:])
        else:
            self.root[word[0]] = TrieGraph()
            if len(word) == 1:
                self.root[word[0]].term = True
            else:
                self.root[word[0]].add_word(word[1:])

    def get_all_words(self, search_term):
        result_arr = []
        def get_one_word():
            pass

    def search(self, search_term, idx = 0):
        if idx > (len(search_term) - 2):
            return (self.root.get(search_term[idx]) is not None)
        if self.root.get(search_term[idx]) is None:
            return False
        else:
            return self.root[search_term[idx]].search(search_term, idx + 1)


if __name__ == '__main__':
    t = TrieGraph()
    t.add_word('hello')
    t.add_word('holle')
    res = t.search('hello')
    print(res)