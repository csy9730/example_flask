import urllib
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter):
    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = urllib.request.unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(value)
                                   for value in values)


app.url_map.converters['list'] = ListConverter


@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'Separator:{}{}'.format('+', page_names)


@app.route('/list2/<list(separator=u"|"):page_names>/')
def list2(page_names):
    return 'Separator:{}{}'.format('|', page_names)
#这样我们访问“/list1/a+b/”和“/list2/a|b/”就能实现同样的功能了。自定义转换器需要继承至BaseConverter，要设置to_python和to_url两个方法。

if __name__=='__main__':
    #app.run(host='0.0.0.0', port=9000)
    app.run(host='127.0.0.1', port=9000)