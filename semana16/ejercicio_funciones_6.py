def convert_to_list(text):
    split_list = text.split('-')
    return split_list


def sort_list(text):
    text.sort()
    return text


def combine_list(text):
    all_text = "".join(text)
    print(all_text)
    return all_text


def main():
    text = "python-variable-function-computer-monitor"
    text = convert_to_list(text)
    text = sort_list(text)
    text = combine_list(text)

main()