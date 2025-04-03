
def word_count(text):
    count = text.split()
    return len(count)

def char_counts(text):
    lowercased = text.lower()
    character_count = {}
    
    for n in lowercased:
        if n not in character_count:
            character_count[n] = 1
        else:
            character_count[n] += 1
    return character_count

def char_srtd(char_frequency):
    char_list = [{"char": char, "count": count} for char, count in char_frequency.items()]

    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list