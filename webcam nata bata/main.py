from flask import Flask, render_template

app = Flask(__name__)
app = app  # <--- TAMBAHKAN BARIS INI

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bagian ini hanya jalan di laptopmu (PyCharm), Vercel akan mengabaikannya
    print("--- LEON SANDBOX RUNNING ---")
    app.run(debug=True, port=5000)