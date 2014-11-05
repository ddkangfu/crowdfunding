
###开发环境说明
  1. Django 1.7.1
  2. MySql 5.5
  
###开发环境设置
  1. 安装virtualenvwrapper；
  2. 建立虚拟环境，如下例将建立一个名为django171的虚拟环境：
        mkvirtualenv django171
  3. 使用git clone项目到本地文件夹：
        git clone git@coding.net:ddkangfu/crowdfunding.git
  4. 使用git flow init初始化项目：
        cd crowdfunding
        git checkout master
        git flow init -d
  5. 安装相关的python包：
        pip install -r requirements.txt