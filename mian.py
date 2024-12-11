import subprocess
import os
from datetime import datetime


def backup_database(host, port, user, password, database, backup_dir):
    # D:\phpstudy_pro\Extensions\MySQL5.7.26\bin
    mysqldump_path = r"D:\phpstudy_pro\Extensions\MySQL5.7.26\bin\mysqldump.exe"
    # 获取当前日期时间，用于生成备份文件名
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = os.path.join(backup_dir, f'{database}_{timestamp}.sql')

    # 构造 mysqldump 命令，包含 --no-create-db 参数
    mysqldump_cmd = [
        mysqldump_path,
        '--no-create-db',  # 添加此参数
        '-h', host,
        '-P', port,
        '-u', user,
        '-p' + password,  # 注意：这里没有空格，直接跟上密码（出于安全考虑，建议使用更安全的方式处理密码）
        database
    ]

    # 执行命令并将输出重定向到备份文件
    try:
        with open(backup_file, 'wb') as f:
            result = subprocess.run(mysqldump_cmd, stdout=f, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"备份失败: {result.stderr}")
            return False
        else:
            print(f"备份成功: {backup_file}")
            return True

    except Exception as e:
        print(f"发生错误: {e}")
        return False


# 示例调用
if __name__ == "__main__":
    host = '127.0.0.1'
    user = 'test'
    password = '123456'  # 出于安全考虑，请不要在代码中硬编码密码
    database = 'api_ddf_web'
    backup_dir = 'D:\\mysql\\db'
    port = '3306'

    # 确保备份目录存在
    os.makedirs(backup_dir, exist_ok=True)

    backup_database(host, port, user, password, database, backup_dir)
