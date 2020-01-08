from flasgger import Swagger
from flask import Flask
from app.v1.sum_ab_controller import demo_sum

app = Flask(__name__)

# API 文档的配置
template = {
  "swagger": "2.0",
  "info": {
    "title": "XXX 在线API",
    "description": "在线API 调用测试",
    "contact": {
      "responsibleOrganization": "AturX",
      "responsibleDeveloper": "AturX",
      "email": "pywizard6261@gmail.com",
      "url": "www.me.com",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.0.1"
  },
  "host": "localhost:5000",  # overrides localhost:5000
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}
Swagger(app, template=template)



# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(demo_sum, url_prefix="/sumAB")


if __name__ == '__main__':
    # 访问API 接口地址 ：  http://localhost:5000/apidocs/
   app.run(host='0.0.0.0', port='5000')