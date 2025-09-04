import requests, re

url = "http://infinite.challs.olicyber.it/"
session = requests.session()

# math test
def privisolvemath(challenge):
    numbers = re.findall(r'\d+', challenge)
    return str(sum(map(int, numbers)))
# art test
def privisolveart(challenge):
    color = re.findall(r'colore ([a-zA-Z]+)\?', challenge)[0].lower()
    return color.capitalize()
# grammar test
def privisolvegrammar(challenge):
    match = re.search(r'Quante "(.+?)" ci sono nella parola "(.+)"\?', challenge)
    letter, word = match.groups()
    for var in (letter, word):
        # fix caratteri strani visto che porco il cane mi si era fermato il cagnaccio del dio
        if 'Ã' in var:
            letter = letter.encode('latin1').decode('utf-8')
            word = word.encode('latin1').decode('utf-8')
            break
    return str(word.lower().count(letter.lower()))

def privisolver():
    test_count = 0
    response = session.get(url)
    page_text = response.text
    while True:
        test_count += 1
        print(f"sfida {test_count}")
        if test_count > 505:
            break
        challenge_match = re.findall(r'<p>(.+)</p>', page_text)
        challenge = challenge_match[0]
        type_match = re.findall(r'<h2>(.+)</h2>', page_text)
        challenge_type = type_match[0]
        print(f"tipo: {challenge_type}")
        print(f"domanda: {challenge}")
        hidden_inputs = {}
        form_match = re.findall(r'<input type="hidden" name="([^"]+)" value="([^"]+)"', page_text)
        for name, value in form_match:
            hidden_inputs[name] = value
        if "MATH TEST" in challenge_type:
            solution = privisolvemath(challenge)
        elif "ART TEST" in challenge_type:
            solution = privisolveart(challenge)
        elif "GRAMMAR TEST" in challenge_type:
            solution = privisolvegrammar(challenge)
        else:
            break
        print(f"risposta: {solution}")
        data = {'answer': solution}
        data.update(hidden_inputs)
        response = session.post(url, data=data)
        page_text = response.text
        if "WRONG!" in page_text:
            break
        elif "flag" in page_text.lower():
            print("flag:")
            print(page_text)
            flag_match = re.search(r'flag\{[^}]+\}', page_text)
            if flag_match:
                print(f"Flag: {flag_match.group(0)}")
            break
        else:
            print(f"sfida {test_count} risolta")
            if test_count > 500:
                print(page_text)
        print("\n")

if __name__ == "__main__":
    privisolver()