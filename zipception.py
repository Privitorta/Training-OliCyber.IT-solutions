import zipfile
import os

contatore = 3000
directory = r"C:\Users\Emma\Downloads\CTF\olimpiadi"

while contatore > 0:
    zip_file = f"flag{contatore}.zip"
    zip_path = os.path.join(directory, zip_file)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            print(f"Estraendo {zip_file}...")
            zip_ref.extractall(directory)
    except Exception as e:
        print(f"Errore durante l'estrazione di {zip_file}: {e}")

    contatore -= 1