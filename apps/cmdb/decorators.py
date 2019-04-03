from flask import session, redirect, url_for
from functools import wraps
import  config
def login_required(func):
    @wraps(func) # 保留func的属性
    def inner(*args, **kwargs):
        if config.CMDB_USER_ID  in session:
            return func(*args, **kwargs)
        else:
            #session中没有user_id表示没有登录，则跳转到登录页面
            return redirect(url_for('cmdb.login'))
    return inner