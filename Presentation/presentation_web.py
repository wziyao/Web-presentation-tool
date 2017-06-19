import sys
import codecs
import random
import os

import urllib

from flask import Flask, json, jsonify, request
from flask import render_template, url_for, redirect


FILE_NAMES = []
FILE_TO_SHOW = None   

# the calss for a presentation page
class Page():

    def __init__(self, page_lines=None, index=0):

      if page_lines:
        self.header = page_lines[0]
        self.lines = page_lines[1:]
        self.index = index
        self.last_page = False

    def set_last_page():

        self.last_page = True


# the class for the presentation file
class File():

    def __init__(self, name=None):

      if name:

        self.name = name
        self.line_count = 0 # number of total lines
        self.pages = []
        self.page_count = 0 # current viewed page

        file_name = 'txt/' + name + '.txt'
        #inputf = codecs.open(u'lists/b.txt', 'r', encoding='utf-8')
        input_file = codecs.open(file_name, 'r', encoding='utf-8')

        page_index = 0 # starting from 0

        page_lines = []
        for line in input_file:
          #print line

          if line.strip():
            line = line.strip()
            if line == '<':
              page_lines = []
            elif line == '/>':
                self.pages.append(Page(page_lines, page_index))
                page_index += 1
            else:
              page_lines.append(line)
              self.line_count += 1

        self.pages[-1].last_page = True

        input_file.close()

        #print self.name, self.line_count, len(self.pages)

      return  

# serve for the app entrance: show a list of available presentation files in ./txt folder
def get_file_list():

  files = os.listdir('./txt')

  for file in files:
      if file.find('.txt'):
        print file
        names = file.split('.')
        FILE_NAMES.append(names[0])

  return 

app = Flask(__name__)

# main entrance
@app.route('/')
def root():
  return redirect(url_for('list_file_names'))

# test page: static
@app.route('/welcome')
def welcome():
  return redirect(url_for('static', filename='welcome.html'))

# test page: dynamic
@app.route('/hello')
def hello(name=None):

  return render_template('hello.html')


# main entrance. show the cover page with a presentation list according to the files in you ./txt folder
@app.route('/files', methods=['GET', 'POST'])
def list_file_names():

  global FILE_TO_SHOW

  if FILE_TO_SHOW: FILE_TO_SHOW = None

  if FILE_NAMES:
    for file in FILE_NAMES:
      return render_template('files.html', lists=FILE_NAMES)
  else:
    return render_template('hello.html', name='No Files!')

 
 # show a presentation page
@app.route('/page', methods=['GET', 'POST'])
def show_page(name=None, action='current'):

  if len(request.args) > 0:
    name = request.args['name']
    action = request.args['action']

    global FILE_TO_SHOW

    if FILE_TO_SHOW == None:
      FILE_TO_SHOW = File(name)
      FILE_TO_SHOW.page_count = 0
      return render_template('page.html', name=name, page=FILE_TO_SHOW.pages[FILE_TO_SHOW.page_count])

    else:
      if action == 'next' and FILE_TO_SHOW.page_count < len(FILE_TO_SHOW.pages)-1:
          FILE_TO_SHOW.page_count += 1
      elif action == 'previous' and FILE_TO_SHOW.page_count > 0: 
          FILE_TO_SHOW.page_count -= 1
      else: 
        page_count = FILE_TO_SHOW.page_count
        FILE_TO_SHOW = File(name)
        FILE_TO_SHOW.page_count = page_count

      return render_template('page.html', name=name, page=FILE_TO_SHOW.pages[FILE_TO_SHOW.page_count])

  else:
    return render_template('hello.html', name='No File Selected!')

    
if __name__ == '__main__':
  print "initializing in main(): read in FILE_NAMES..."
  get_file_list()

  app.debug = True
  app.run()

