def count_letters(words: dict[str, int]) -> dict[str, int]:
	letter_count = {}
	for word in words:
    	for letter in word:
        	if letter in letter_count:
            	letter_count[letter] += 1
        	else:
            	letter_count[letter] = 1
	return letter_count