from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length
from  apps.forms import BaseForm
class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='邮箱格式错误'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,20, message='密码长度为6-20位')])
    remember = IntegerField()  #这个值不用验证，这里只是接收

    # 添加获取错误信息的方法
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message