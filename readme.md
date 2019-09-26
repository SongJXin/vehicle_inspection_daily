# 汽车检测线日报系统

功能简介：

* 记录每次审车的情况
* 一个月的每日数量/金额柱状图
* 检索审车记录
* 设置车辆类别
* 汇总每日（自定义时间内）金额

本项目由python django + vue 开发。

## 安装

- python

```shell
pip install -r requriements.txt 
# 生成数据库
python manage.py makemigrations
python manage.py migrate
# 创建超级管理员
python manage.py createsuperuser
```

- vue

```shell
cd frontend
npm install
```