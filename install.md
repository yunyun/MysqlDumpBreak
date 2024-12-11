
python -m venv venv

在Windows系统中，使用以下命令：


venv\Scripts\activate.bat

在Mac或Linux系统中，使用以下命令：


source venv/bin/activate



关于导出包，如果您想要导出您已安装的包列表，可以使用以下命令：


pip freeze > requirements.txt

安装包：
在venv环境激活后，您可以使用以下命令来安装requirements.txt中列出的所有包：


pip install -r requirements.txt

这将根据requirements.txt文件中指定的版本安装所有所需的包。




验证安装：
安装完成后，您可以运行以下命令来验证安装的包列表：


pip list

这将列出venv环境中已安装的所有包。



apt install python3-venv

python.exe -m pip install --upgrade pip




