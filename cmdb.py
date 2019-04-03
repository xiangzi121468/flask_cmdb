from flask import Flask
import config
from apps.cmdb import bp as cmdb_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from flask_wtf import CSRFProtect #开启token 认证
app = Flask(__name__)
app.config.from_object(config) #引入配置文件
CSRFProtect(app)
app.register_blueprint(cmdb_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
from exts import db
db.init_app(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=888)