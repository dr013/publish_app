from flask import Flask, request, render_template
import settings
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('info.html')
    else:
        print 1
        custom = None
        module_name = None
        project = request.form["project"]
        product = request.form['product']
        version = request.form['version']
        build_type = request.form["build_type"]
        if "module" in request.form:
            module_name = request.form["module"]
        if 'custom' in request.form:
            custom = request.form["custom"]
        path = mk_dir(project, product, version, build_type, module_name, custom)
        f = request.files['artifact']
        filepath = '{path}{filename}'.format(path=path, filename=secure_filename(f.filename))
        f.save(filepath)
        return filepath


def mk_dir(project, product, version, build_type, module_name, custom):

    path = '{base}{sep}{project}{sep}{product}{sep}'

    if build_type != 'stable':
        pattern = '{type}-builds{sep}'.format(type=build_type, sep=os.sep)
        path += pattern

    path += '{version}{sep}'

    if module_name:
        path += module_name
        path += os.sep

    if custom:
        path += custom
        path += os.sep

    path = path.format(base=settings.SAVE_PATH, sep=os.sep, project=project, product=product, version=version)

    if not os.path.isdir(path):
        os.makedirs(path)

    return path
