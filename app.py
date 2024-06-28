from flask import Flask, request, render_template, send_file
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    admn = request.form['admn']
    resp = requests.post("https://parent.iitism.ac.in/index.php/parent_portal/grade_sheet/print_grade_report/0/B.TECH",
                         data={"admn_no": admn})
    file_path = f'gradesheet{admn}.pdf'
    with open(file_path, 'wb') as f:
        f.write(resp.content)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
