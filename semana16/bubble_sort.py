def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise TypeError('Input must be a list.')
    for big_index in range(0, len(list_to_sort) - 1):
        for index in range(0, len(list_to_sort)-1 - big_index):
            current_value = list_to_sort[index]
            next_value = list_to_sort[index + 1]
            if current_value > next_value:
                list_to_sort[index] = next_value
                list_to_sort[index + 1] = current_value




list_to_sort = [812, 105, 923, 758, 396, 489, 622, 374, 801, 930, 278, 167, 456, 392, 634, 970, 528, 724, 843, 631, 214, 105, 889, 547, 778, 690, 315, 902, 678, 416, 156, 793, 521, 347, 860, 275, 680, 741, 599, 853, 306, 258, 983, 442, 872, 120, 700, 904, 721, 134, 391, 991, 206, 377, 504, 952, 812, 323, 269, 798, 612, 737, 656, 499, 728, 840, 583, 276, 152, 389, 705, 941, 368, 247, 894, 909, 575, 978, 165, 844, 991, 678, 570, 235, 917, 753, 198, 407, 462, 319, 888, 600, 796, 311, 419, 867, 755, 548, 245, 674]

bubble_sort(list_to_sort)
print(list_to_sort) 