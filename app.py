from flask import Flask, render_template,url_for,redirect,request
from user_agents import parse

app = Flask(__name__)


@app.route('/compraRealizada/<id>')
def compraRealizada(id):
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile  
    return render_template("compraRealizada.html", is_mobile=is_mobile, id=id)


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True)