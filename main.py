def counting_top_words_in_xml(file_name):
    import json
    from collections import Counter
    with open(file_name, encoding='utf-8') as sorting_words:
        json_data = json.load(sorting_words)

    sorted_list = []
    all_news = json_data['rss']['channel']['items']
    for description in all_news:
        words = description['description'].split(' ')

    for word in words:
        if len(word) >= 6:
            sorted_list.append(word)
            sorted_words = Counter(sorted_list).most_common(10)
    print(sorted_words)

    frequency = {}

    for words in sorted_list:
        if words in frequency:
            frequency[words] += 1
        else:
            frequency[words] = 1
    inverse = [(value, key) for key, value in frequency.items()]
    reverse_inverse = sorted(inverse, reverse=True)
    sorted_list_1 = []
    for word in reverse_inverse[0:10]:
        qwe = (word[1], word[0])
        sorted_list_1.append(qwe)
    print(sorted_list_1)


counting_top_words_in_xml('newsafr.json')
