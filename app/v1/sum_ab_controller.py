from flask import Blueprint
from app.src.demo import sum_a_b

demo_sum = Blueprint('demo_sum', __name__)


@demo_sum.route('/<a>/<b>')
def sum_ab(a, b):
    """
       API接口文档 演示接口
       调用这个接口，将A数和B数相加
       ---
       tags:
         - 演示Swagger API ：两数相加
       parameters:
         - name: a
           in: path
           type: integer
           required: true
           description: 输入a 数字 1
           value: 1
         - name: b
           in: path
           type: integer
           description:  输入b 数字 2
           value: 2
       responses:
         500:
           description: 服务器报错
         200:
           description: 200 OK
    """
    c = sum_a_b(a, b)
    return str(c)

