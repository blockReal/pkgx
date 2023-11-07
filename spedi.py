import time
import sys

def blink_text(text, delay):
    while True:
        sys.stdout.write("\r" + " " * len(text))  # Hapus teks sebelumnya
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r" + text)  # Tampilkan teks
        sys.stdout.flush()
        time.sleep(delay)

try:
    text_to_blink = "Hello, TEA Protocol"  # Ganti teks sesuai keinginan Anda
    blink_delay = 0.5  # Ganti kecepatan berkedip sesuai keinginan Anda
    blink_text(text_to_blink, blink_delay)
except KeyboardInterrupt:
    pass
