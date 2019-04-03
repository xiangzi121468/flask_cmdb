from flask import Blueprint,request,session
from  flask  import render_template
from flask import Flask,views,url_for,redirect
from .forms import LoginForm
from .models import CMDBUser
import  config
from .decorators import login_required
bp = Blueprint('cmdb', __name__, url_prefix='/cmdb')

@bp.route('/')
@login_required
def index():
    return 'cmdb index'


class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cmdb/cmdb_login.html',message=message)

    def post(self):
        login_form = LoginForm(request.form)
        if login_form.validate():
            email = login_form.email.data
            password = login_form.password.data
            remember = login_form.remember.data
            user = CMDBUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMDB_USER_ID] = user.id
                if remember:
                    # 如果勾选了记住我，则保存session,这样就算浏览器关闭session还是存在的
                    session.permanent = True
                return redirect(url_for('cmdb.index'))  # 因为是蓝图这里必须使用cmdb.index,不能使用index
            else:
                # return render_template('cmdb/cmdb_login.html', message='账号或密码错误')
                # 等同于以下代码
                return self.get(message='账号或密码错误')

        else:
            # login_form.errors是一个字典，如{"email":['邮箱格式错误'], "password":["密码长度为6-20位"]}
            # login_form.errors.popitem() 是取出字典的任意一项，结果是元组，如:("password":["密码长度为6-20位"])
            # 取出该元组的第2个元素：login_form.errors.popitem()[1], 如：["密码长度为6-20位"]
            # 最后取出错误提示语：login_form.errors.popitem()[1][0]
            message = login_form.get_error()
            return self.get(message=message)

bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))