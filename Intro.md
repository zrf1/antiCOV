# 用turtle画图

## 文件说明

### Helper.py

用importlib.reload重新加载画图过程，减少人工调试，调用`python helper.py`

### Doctor.py

画医生，增加定位功能，调用`python doctor.py`

### Nurse.py

画护士，增加定位功能，调用`python nurse.py`

### main.py

画doctor和nurse，然后调用背景

## 打包发布

pyinstaller -F -i img\favicon.ico main.py

### 图片资源打包

### 方法1：修改`.spec`文件，打包资源，再使用`sys._MEIPASS`获取路径

修改`main.spec`中的
`datas=[('img\\background.gif','img')]`
进行打包

调用时，用`if getattr(sys, 'frozen', False)`判断，再生成路径`bgpic(os.path.join(path, "img","background.gif"))`

### 方法2：使用pic2py以base64方式把图片写入py文件，使用时新建图片

写入py，`write_data.append('%s = "%s"\n' % (filename, b64str.decode()))`

调用前新建，`image.write(base64.b64decode(pic_code))`
