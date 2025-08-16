def get_num_words(text):
	return len(text.split())


def get_chars_dict(text):
	chars = {}
	for char in text:
		lowered_char = char.lower()
		if lowered_char in chars:
			chars[lowered_char] += 1
		else:
			chars[lowered_char] = 1
	return chars


def sort_on(data):
	return data["num"]


def get_sorted_char_list(chars_dict):
	result_list = []
	for char, count in chars_dict.items():
		char_dict = {"char": char, "num": count}
		result_list.append(char_dict)
	result_list.sort(reverse=True, key=sort_on)	
	return result_list
