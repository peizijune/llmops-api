### 1-5 依赖注入

1 $ pip install injector <br>

### 1-6 依赖库安装

1 $ pip install flask <br>
2 internal.handler包中创建app_handler.py，__init__.py中导出 <br>
3 internal.router包中创建router.py，__init__.py中导出 <br>
> @inject：通过构造函数实现注入 <br>
> @dataclass：自动生成构造函数 <br>
> @inject一定要写在@dataclass前面！！！（先注入，再调用构造函数） <br>

4 internal.server包中创建http.py，__init__.py中导出 <br>
5 app包中创建http包，在http包中创建app.py <br>
6 运行：Edit Configurations... | Flask | 选中app/http/app.py <br>
> FLASK_DEBUG = 1：由任何代码修改时，自动重新加载