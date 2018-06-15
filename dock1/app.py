#tst1

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello! here is flsk app ' + __name__

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'flask User %s' % username

@app.route('/page/<pageon>')
def forurl(pageon):
    # show the static page URL
    u = request.cookies.get('username')
    
    return 'Page %s' % Flask.static_url_path + pageon

@app.route('/args')
def show_args():
    m = request.method
    return 'method:' + repr(m) + '. args:' + repr(request.args)

@app.route('/favicon.ico')
def redir_static():
	return redirect('static' +  request.path)

if __name__ == '__main__':
    app.run('0.0.0.0',3002)
