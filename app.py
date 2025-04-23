from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # ✅ Gọi đúng file bạn đã sửa

@app.route('/about')
def about():
    return render_template('about.html')

from flask import request  # thêm dòng này ở đầu file

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Ghi vào file CSV
        with open('contacts.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email, message])

        # Ghi thêm vào contacts.txt (nếu bạn muốn)
        with open('contacts.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name} | {email} | {message}\n")


        # Hiển thị lại trang kết quả
        return render_template('contact_result.html', name=name, email=email, message=message)

    # Nếu là GET thì hiển thị form liên hệ
    return render_template('contact.html')

@app.route('/contacts')
def view_contacts():
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = "Chưa có ai liên hệ."

    return render_template('contacts.html', content=content)

    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
