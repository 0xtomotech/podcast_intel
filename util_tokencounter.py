# Purpose: Count the number of tokens in a text file

from transformers import GPT2Tokenizer


def count_tokens_in_file(file_path):
    # Initialize the tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text and count the tokens
    tokens = tokenizer.encode(text, add_special_tokens=False)
    return len(tokens)


file_path = 'text_library/ThinkingBasketball_202306-202401.txt'
token_count = count_tokens_in_file(file_path)
print(f"Number of tokens in the file: {token_count}")
