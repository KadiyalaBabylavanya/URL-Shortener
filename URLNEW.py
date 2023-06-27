import pyperclip
import pyshorteners
from tkinter import *
import sqlite3

root = Tk()
root.title("URL SHORTENER")
root.configure(bg="#49A")
url = StringVar()
url_address = StringVar()

# Connect to SQLite database
conn = sqlite3.connect('url_pairs.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS urls (short_url text, long_url text)''')
conn.commit()

def urlshortener():
    url_address_input = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address_input)
    url_address.set(url_short)
    store_url_pair(url_short, url_address_input)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

def store_url_pair(short_url, long_url):
    cursor.execute("INSERT INTO urls VALUES (?, ?)", (short_url, long_url))
    conn.commit()

Label(root, text="   MY URLShortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()

# Close the database connection when the application exits
conn.close()
