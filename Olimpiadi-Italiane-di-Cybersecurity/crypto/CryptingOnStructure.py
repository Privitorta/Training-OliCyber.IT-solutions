# all'autore piace il bacon
def privibacon(message):
    bacon = {
        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
        'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
        'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
        'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
        'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
        'BBAAB': 'Z'
    }
    groups = [message[i:i+5] for i in range(0, len(message), 5)]
    result = ""
    for group in groups:
        if len(group) == 5 and group in bacon:
            result += bacon[group]
    return result

message = "AAAABAAAAAAAABAABBBAABBABABAAABAABABAABAABBBABAABBAAAAABAABABAABBBBAAA"
baconresult = privibacon(message)
print(f"Flag: flag{{{baconresult}}}")