# flask

网页处理分为服务器端和客户端。服务器端处理客户端请求是程序实例(app).
程序实例需要知道url和对应python函数执行，对应关系称为路由(route)。

视图函数(view)，基于route不同，返回不同的html文件或html字符串。
###服务器启动
flask.exe位于 C:\Program Files\Python36\Scripts\路径
服务器启动后，会进入轮询，等待并处理请求。轮询会一直运行，直到程序停止，比如按
Ctrl-C键。可以随时更改服务器端所有文件，flask会稍后更新网页端
####脚本调用
hello.py:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```
通过变量传递启动参数
run.bat:   
```bash
set FLASK_APP=hello.py
set FLASK_ENV=development
flask run 
```


####python调用

```python
 # coding=utf-8
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000)
```
现在打开Web浏览器，在地址栏中输入http://127.0.0.1:5000/，即可打开网页

###动态路由
```python
@app.route('/user/<name>')
    def user(name):
    return '<h1>Hello, %s!</h1>' %name
```
动态路由使用@app.route修饰，后接路径参数
尖括号中的内容是动态的，凡是匹配到/item/前缀的URL都会被映射到这个路由上，在内部把id作为参数而获得。

它使用了特殊的字段标记<variable_name>，默认类型是字符串。如果需要指定参数类型需要标记成<converter:variable_name>这样的格式，converter有下面几种。

string：接受任何没有斜杠“/”的文本（默认）。
int：接受整数。
float：同int，但是接受浮点数。
path：和默认的相似，但也接受斜杠。
uuid：只接受uuid字符串。
any：可以指定多种路径，但是需要传入参数。
    @app.route('/<any(a, b):page_name>/')
访问/a/和访问/b/都符合这个规则，/a/对应的page_name就是a。
###misc
1. 请求
    * 上下文
    * 调度
    * 钩子
    * 响应
2. 命令行扩展
3. 自定义错误页面
4. 链接，redirect
5. 静态文件
6. 可变url

pip install flask-bootstrap
pip install flask-moment
pip install flask-wtf
pip install flask-sqlalchemy

文件上传，
网页跳转：重定向。

登陆 or注册，注册成功 ，登陆，登陆成功，其他操作。<验证码>

可以把变量存放到会话中，会话中不存在的键，会返回成None。
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```
    

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
```
###模板
模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请
求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，这一过程
称为渲染。为了渲染模板，Flask使用了一个名为Jinja2的强大模板引擎。
 <lazy -evaluation>

###填表
通过flask_wtf动态生成表格，通过点击submit按钮触发POST事件，通过判断validate_on_submit()，改变视图。

如何区分不同按钮提交的多态，添加不同判断。

###数据库
* SQL
* NO-SQL

MySQL、Postgres、SQLite、
Redis、MongoDB或者CouchDB。

关系型数据库存储数据很高效，而且避免了重复。将这个数据库中
的用户角色重命名也很简单，因为角色名只出现在一个地方。一旦在roles表中修改完角
色名，所有通过role_id引用这个角色的用户都能立即看到更新。
但从另一方面来看，把数据分别存放在多个表中还是很复杂的。生成一个包含角色的用户
列表会遇到一个小问题，因为在此之前要分别从两个表中读取用户和用户角色，再将其联
结起来。
NoSQL数据库当然也有好处。数据重复可以提升查询速度。列出用户及其角色的操
作很简单，因为无需联结。

还有一些数据库抽象层代码包供选择，例如SQLAlchemy和
MongoEngine。你可以使用这些抽象包直接处理高等级的Python对象，而不用处理如表、
文档或查询语言此类的数据库实体。

Peewee是一个简单小巧的Python ORM