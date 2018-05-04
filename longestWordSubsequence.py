import time
S = "abppple"

D = ["able", "ale", "apple", "bale", "kangaroo"]
with open('words_alpha.txt') as file:
    D = file.read().splitlines()
file.close()


def find_longest_word_subsequence_of_string(string, word_dict):
    # Hint 1: check each word one at a time just to see if it's a subsequence
    longest_word_length = 0
    longest_word = ""
    
    # This solution isn't optimal because it goes through the whole dictionary
    for word in word_dict:
        valid_subsequence_length = return_valid_subsequence_length(word, string)
        if valid_subsequence_length > longest_word_length:
            longest_word_length = valid_subsequence_length
            longest_word = word
    
    return longest_word

    

def word_letter_frequency(word):
    # for each letter in apple, count how many occurrences
    # for each letter in abppple, count how mant occurences
    
    word_letter_count = {}
    for c in word:
        if c not in word_letter_count:
            word_letter_count[c] = 1
        else:
            word_letter_count[c] += 1

    return word_letter_count


assert word_letter_frequency("apple") == {
        "a": 1, 
        "p": 2,
        "l": 1,
        "e": 1
}

def check_subsequence_exists(word_freq_dict, string_freq_dict):
    # if the word doesn't have enough letters, e.g. kangaroo has a k but abppple doesn't
    # just return false immediately.
    for key, val in word_freq_dict.items():
        if key not in string_freq_dict:
            return False
        if string_freq_dict[key] < word_freq_dict[key]:
            return False

    return True

assert check_subsequence_exists(word_letter_frequency("kangaroo"), word_letter_frequency("abppple")) == False
assert check_subsequence_exists(word_letter_frequency("able"), word_letter_frequency("abppple")) == True
assert check_subsequence_exists(word_letter_frequency("bale"), word_letter_frequency("abppple")) == True # need to check sequence order
assert check_subsequence_exists(word_letter_frequency("apple"), word_letter_frequency("abppple")) == True


def check_subsequence_order(word, string):
    # greedily map word onto string, if all the letters can be mapped,
    # e.g. for "able" in "abppple"
    # a = 1, b = 2, l = 6, e = 7 and a < b < l < e means that the subsequence appears in order
    
    # keep track of which character each index is pointing at
    word_pointer = 0
    string_pointer = 0

    for i in range(0, len(word)):
        while word[i] != string[string_pointer]:
            # print(word[i], string[string_pointer])
            string_pointer += 1
            if string_pointer == len(string):
                return False
        # print(i, word[i], string_pointer, string[string_pointer])

    return True

assert check_subsequence_order("able", "abppple") == True
assert check_subsequence_order("bale", "abppple") == False


def return_valid_subsequence_length(word, string):
    # to get the longest word, we need a function to return the letters if valid
    # else return 0
    
    string_freq_dict = word_letter_frequency(string)
    word_freq_dict = word_letter_frequency(word)
    if check_subsequence_exists(word_freq_dict, string_freq_dict) and check_subsequence_order(word, string):
        return len(word)

    return 0

assert return_valid_subsequence_length("able", "abppple") == 4
assert return_valid_subsequence_length("bale", "abppple") == 0
assert return_valid_subsequence_length("ale", "abppple") == 3



start = time.time()
assert find_longest_word_subsequence_of_string(S, D) == "apple"
end = time.time()
print(end-start)

start = time.time()
print(find_longest_word_subsequence_of_string("wasdtearamelon", D))
end = time.time()
print(end-start)

