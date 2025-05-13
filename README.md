# Django File Upload Platform by knde55

一个基于 Django + Bootstrap + Docker 的文件上传平台，支持用户上传 PDF、Markdown、TeX 文件，管理员审核后展示，支持评论、评分和排行榜功能。

## 🧰 功能特性

- 登录用户或 IP 白名单用户上传文件
- 文件需管理员审核后展示
- 用户可查看文件、评论、评分
- 排行榜显示上传数量和平均评分

## 🛠️ 技术栈

- Django 4.2
- Bootstrap 5
- PostgreSQL
- Docker + Docker Compose
- Gunicorn + Nginx

## 🚀 快速部署

### 1. 克隆仓库

```bash
git clone https://github.com/knde55/django-file-upload-template.git
cd django-file-upload-template
