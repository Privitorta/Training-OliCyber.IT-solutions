import requests
import re

url = "http://vuoto.challs.olicyber.it/"

# ovviamente le ho trovate a mano però voglio fare script non rompetemi

def priviSitoVuoto():
    session = requests.Session()
    
    # <!-- E invece no, ecco la prima parte della flag: flag{you_ -->
    html = session.get(url).text
    html_comments = re.findall(r'<!--(.*?)-->', html, re.DOTALL)
    part1 = None
    for comment in html_comments:
        if 'flag{' in comment and 'prima parte' in comment:
            match = re.search(r'"([^"]*flag\{[^"]*)"', comment)
            if match:
                part1 = match.group(1)
                break
    print(f"HTML: {part1}")

    # <!-- Ecco la seconda parte della flag: can_t_see_me_ -->
    css = session.get(f"{url}css/style.css").text
    css_comments = re.findall(r'/\*(.*?)\*/', css, re.DOTALL)
    part2 = None
    for comment in css_comments:
        if 'flag' in comment and 'seconda parte' in comment:
            match = re.search(r'"([^"]*)"', comment)
            if match:
                part2 = match.group(1)
                break
    print(f"CSS: {part2}")

    # /* Ecco la terza parte della flag: in_the_browser} */
    js = session.get(f"{url}js/script.js").text
    js_comments = re.findall(r'/\*(.*?)\*/', js, re.DOTALL)
    part3 = None
    for comment in js_comments:
        if 'flag' in comment and 'terza parte' in comment:
            match = re.search(r'"([^"]*)"', comment)
            if match:
                part3 = match.group(1)
                break
    print(f"JS: {part3}")
    
    if all([part1, part2, part3]):
        clean1 = part1.replace('flag{', '')
        clean3 = part3.replace('}', '')
        flag = f"flag{{{clean1}{part2}{clean3}}}"
        print(f"\nFlag: {flag}")
        return flag
    else:
        print("Mancano parti della flag")
        return None

if __name__ == "__main__":
    priviSitoVuoto()