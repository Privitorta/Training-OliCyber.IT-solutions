from PIL import Image

def main():
    filename = "bits.bmp"
    raw = Image.open(open(filename, "rb")).tobytes()
    bin_str = bytes([(x&1)+48 for x in raw]).decode()
    decoded = bytes(int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8))
    with open("output", "wb") as f:
        f.write(decoded)
    print("Output scritto in 'output'")
if __name__ == "__main__":
    main()