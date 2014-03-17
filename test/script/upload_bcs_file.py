#!/usr/bin/env python
#coding:utf8
__author__ = 'windpro'

import os
import logging
from realBlog.lib import pybcs

#设置日志级别
pybcs.init_logging(logging.INFO)


# 请修改这里
AK = "A253f188574249ac454de83ffd54b6c9"           #请改为你的AK
SK = "EAc5f62bfdc8f6c551ef6f389f1f3a5a"         #请改为你的SK
BUCKET='blogcache'



bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK, pybcs.HttplibHTTPC)    #这里可以显式选择使用的HttpClient, 可以是:
                                                                        #HttplibHTTPC
                                                                        #PyCurlHTTPC
lst = bcs.list_buckets()
print '---------------- list of bucket : '
for b in lst:
    print b
print '---------------- list end'

#声明一个bucket
b = bcs.bucket(BUCKET)

#创建bucket (创建后需要在yun.baidu.com 手动调整quota, 否则无法上传下载)
#b.create()

#获取bucket acl, 内容是json
print b.get_acl()['body']

#将bucket 设置为公有可读写
#b.make_public()

#声明一个object
#o = b.object('/CHANGELOG.TXT')
#o.put_file('../../realBlog/editor/CHANGELOG.TXT')
#o.get_to_file('CHANGELOG.TXT')

import os
import os.path
for rootdir_info in [
        #['../../realBlog/themes/', '/themes'],
        ['../../realBlog/editor/', '/editor'],
        #['../../realBlog/admin/style/', '/admin/style'],
        #['../../realBlog/admin/script/', '/admin/script'],
        #['../../realBlog/admin/img/', '/admin/img'],
        #['../../realBlog/admin/image/', '/admin/image'],
    ]:# 指明被遍历的文件夹
    rootdir = rootdir_info[0]
    rootdir_name = rootdir_info[1]
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #for dirname in  dirnames:                       #输出文件夹信息
        #    print "parent is:" + parent
        #    print  "dirname is" + dirname

        for filename in filenames:                        #输出文件信息
            #print "parent is" + parent[len(rootdir):]
            #print "filename is:" + filename
            #print "the full name of the file is:" + os.path.join(parent, filename)[len(rootdir):]
            o = b.object('%s/%s' % (rootdir_name, os.path.join(parent, filename)[len(rootdir):]))
            print "uploading :%s" % os.path.join(parent, filename)
            o.put_file(os.path.join(parent, filename))

#在bcs 上删除.
#o.delete()
