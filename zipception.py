import zipfile
import os

contatore = 3000
directory = r"C:\Users\Emma\CTF"

while contatore > 0:
    zip_file = f"flag{contatore}.zip"
    zip_path = os.path.join(directory, zip_file)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            print(f"sto estraendo {zip_file}...")
            zip_ref.extractall(directory)
    except Exception as e:
        print(f"l'estrazione di {zip_file} non è andata a buon fine: {e}")

    contatore -= 1