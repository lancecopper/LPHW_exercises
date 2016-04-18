from web import format
urls = (
    '/', 'Index',
    '/test', 'Tesst'
    '/login', 'Login',
    '/logout', 'logout',
)

render = web.template.render("/opt/py/login")
allowed = (
    ('admin', '123123'),
    )
    
web.config.debug = False
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sesssions'))

class Index:
    def GET(self):
        return render.login()
    def POST(self):
        i = web.input()
        username = i.get('username')
        passwd = i.get('passwd')
        if (username,passwd) in allowed:
            sesssion.logged_in = True
            web.setcookie('system_management', ,60)
            raise web.seeother('/')
        else:
            return '<h1>Login Error!!!<h1>Login'
            
class Logout:
    def GET(self):
        session.logged_in = False
        raise web.seeother("/login")
            
class Test:
    def Get(self):
        if session.get('logged_in', False):
            return '<h1>logout now</h1>Login'
            
if  __name__ == '__main__':
    app.run()