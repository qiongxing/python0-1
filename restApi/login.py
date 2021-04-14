from flask import Flask
from flask import request

from login import Context
from login import NormalLogin

app = Flask(__name__)


@app.route('/cm/api/v1.0/verifyuser', methods=['POST'])
def verifyUser():
    error = None
    if request.method == 'POST':
        login = NormalLogin()
        ctx = Context(login)
        page = ctx.login(request.form['studentId'], request.form['password'])
        if page == "success":
            return "success, 验证成功"

    return "failed, 验证失败"


if __name__ == '__main__':
    app.run(debug=True)
