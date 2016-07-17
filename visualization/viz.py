# -*- coding: utf-8 -*-
# @Author: shubham.chandel
# @Date:   2016-07-16 18:15:29
# @Last Modified by:   shubham.chandel
# @Last Modified time: 2016-07-16 18:30:03

from flask import Flask, render_template, redirect, request

# from binascii import hexlify, unhexlify
# from markdown2 import markdown

# from helpers import get_entries_raw, get_entries, get_entry_mdata, societies

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return render_template("d3.html")


if __name__ == '__main__':
	app.run()

