class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}
        for name in self.file_names:
            word = ''
            with open(name, encoding='utf-8') as file:
                for line in file:
                    for char in line:
                        if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            word += ''
                        else:
                            word += char
                words = word.lower().split()
                all_words[name] = words
        return all_words

    def find(self, word) -> dict:
        word = word.lower()
        find_dict = {}
        for name, words in self.get_all_words().items():
            if word in words:
                find_dict[name] = words.index(word) + 1
        return find_dict

    def count(self, word) -> dict:
        word = word.lower()
        count_dict = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if word == i:
                    count += 1
            count_dict[name] = count
        return count_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
