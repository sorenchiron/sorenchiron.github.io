# author sychen
# copyright 2019

from glob import glob
import os 
import argparse
import time
import re
import torchfun as tf
import shutil

parser = argparse.ArgumentParser('Manager of YAML blog')
parser.add_argument('operation',type=str,help='add,rm')
parser.add_argument('name',type=str,help='name of the blog')
parser.add_argument('date',nargs='?',type=str,default=None,help='format: YYYYMMDD')
parser.add_argument('-d','--dry',action='store_true',default=False,help='do everthing except actuall system calls')
parser.add_argument('-o','--open',action='store_true',default=False,help='open the text markdown after creation')

args = parser.parse_args()



TIME = time.localtime()
NOW = '%d%02d%02d' % (TIME.tm_year,TIME.tm_mon,TIME.tm_mday)
NOW_FORMATTED = time.strftime("%Y-%m-%d")
args.name = args.name.replace(' ','-')


def log(*argv):
    print('--Log:',*argv)

safe_open = tf.safe_open
force_exist = tf.force_exist
omini_open = tf.omini_open

def touch(fpath,date=NOW_FORMATTED):
    log('creating text file',fpath)
    f = open(fpath,'w',encoding='utf-8')
    f.write(f'''---
layout: mypost
title: {args.name}
categories: [文章]
published: true
date: {date}
tags: [文章]
---''')
    f.close()

def add():
    if args.date is None:
        args.date = NOW
    dash_date = f'{args.date[0:4]}-{args.date[4:6]}-{args.date[6:8]}'
    blogfname = f'{args.date[0:4]}-{args.date[4:6]}-{args.date[6:8]}-{args.name}.md'
    blogfpath = os.path.join('_posts',blogfname)
    if os.path.exists(blogfpath):
        log('Abort!',blogfpath,'exists')
        return

    blog_post_folder = os.path.join('posts',args.date[0:4],args.date[4:6],args.date[6:8])

    log('blog markdown file',blogfpath,'to be created')
    log('blog resource folder',blog_post_folder,'to be created')

    if args.dry:
        log('dry run is set, nothing is committed, exiting.')
        return

    touch(blogfpath,date=dash_date)
    force_exist(blog_post_folder)
    if args.open:
        omini_open(blogfpath)
    return

def rm():
    all_blogfpaths = glob('_posts/*.md')
    target_blogname = args.name.lower()
    results=[]
    delete_target = None
    for blogfpath in all_blogfpaths:
        if target_blogname in blogfpath:
            results.append(blogfpath)
    results = sorted(results)
    print(results)
    if len(results)==1:
        delete_target = results[0]
    else:
        delete_target = None

    log('markdown file', delete_target,'to be removed')

    if args.dry:
        log('dry run is set, nothing is committed, exiting.')
        return

    if delete_target:
        os.remove(delete_target)
        log('markdown file', delete_target,'is removed')
    else:
        log('no file is selected for removal')

    pattern = '![测试图片](001.jpeg)'
    log('not fully implemented, my lord.')
    return

def main():
    if args.date and len(args.date)!=8:
        log('date format is incorrect YYYYMMDD',args.date)
        return

    if args.operation == 'add':
        add()
    elif args.operation == 'rm':
        rm()
    else:
        log('operation',args.operation,'not understood')
    return

if __name__ == '__main__':
    main()
