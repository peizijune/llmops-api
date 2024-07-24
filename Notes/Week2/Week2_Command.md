### 1-5 项目目录结构、依赖注入

1 设置test目录 <br>
> Settings | Project | Project Structure：标记为Tests <br>

2 $ pip install injector <br>

### 1-6 依赖库安装

1 $ pip install flask <br>
2 internal.handler包中创建app_handler.py，__init__.py中导出 <br>
3 internal.router包中创建router.py，__init__.py中导出 <br>
> @inject：通过构造函数实现注入 <br>
> @dataclass：自动生成构造函数 <br>
> @inject一定要写在@dataclass前面！！！（先注入，再调用构造函数） <br>

4 internal.server包中创建http.py，__init__.py中导出 <br>
5 app包中创建http包，在http包中创建app.py <br>
6 运行：Edit Configurations... | Flask server | script | 选中app/http/app.py <br>
> Environment variables: FLASK_DEBUG = 1 // 热加载（修改任何代码都会自动重新加载）

7 在浏览器中访问 <http://127.0.0.1:5000/ping> <br>
8 打包项目后，如果其他人需要运行，则要知道需要安装哪些包
> $ pip freeze // 查看当前项目安装了哪些包（不管有没有使用过） <br>
> $ pip freeze > requirements.txt // 写入requirements.txt <br>
>
> Reference: <https://pypi.org/project/pipreqs/> <br>
> $ pip install --no-deps pipreqs // pipreqs只统计当前项目使用过哪些包 <br>
> $ pip install yarg==0.1.9 docopt==0.6.2 <br>
> $ pipreqs --ignore venv --force // --ignore venv 忽略venv目录，--force 重写当前的requirements.txt <br>
> 可以在Edit Configurations... | Shell Script | Script
> text中添加该命令，之后直接运行（每次push代码到Git仓库之前都可以运行该命令更新requirements.txt） <br>
>
> $ pip install -r requirements.txt // 安装requirements.txt中列出的所有包 <br>

### 1-8 PostgreSQL (RDBMS) <br>

> $ brew install postgresql@15 <br>
>
> $ open ~/.bash_profile <br>
> export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH" <br>
> export LDFLAGS="-L/opt/homebrew/opt/postgresql@15/lib" <br>
> export CPPFLAGS="-I/opt/homebrew/opt/postgresql@15/include" <br>
> export PKG_CONFIG_PATH="/opt/homebrew/opt/postgresql@15/lib/pkgconfig" <br>
> $ source ~/.bash_profile <br>
> $ brew services start postgresql@15
> $ brew services stop postgresql@15