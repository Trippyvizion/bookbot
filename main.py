import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import get_sorted_char_list
def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(sys.argv[1])
	num_words = get_num_words(text)
	chars_dict = get_chars_dict(text)
	sorted_chars = get_sorted_char_list(chars_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char_data in sorted_chars:
    		if char_data['char'].isalpha():
        		print(f"{char_data['char']}: {char_data['num']}")
	print("============= END ===============")
main()
