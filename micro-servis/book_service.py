from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Belajar Flask", "stock": 5}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['PUT'])
def decrease_stock(book_id):

    for book in books:

        if book['id'] == book_id:

            if book['stock'] > 0:

                book['stock'] -= 1

                return jsonify(book), 200

            return jsonify({
                "error": "Stok buku habis"
            }), 400

    return jsonify({
        "error": "Buku tidak ditemukan"
    }), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)