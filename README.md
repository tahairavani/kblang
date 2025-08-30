# kblang

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version](https://img.shields.io/pypi/v/kblang.svg)](https://pypi.org/project/kblang/)

A Python library to correct spelling errors caused by incorrect keyboard language selection 

## Overview 
With kblang you can change the keyboard language of a text to other languages ​​

It is very common that users do not select the correct language when typing with the keyboard and the text they type is completely meaningless 

For example, they want to write Hello, how are you 

But the keyboard language is Persian and it is typed : 
"عثممخ اخس شقث غخع"

But you can now use kblang to convert user input into what it should be when searching or entering other information. 
## Special features
- Modular support for different keyboards and languages
- Ability to easily add new keyboards
- Text language detection with dedicated language detector module
- Use the keyboard layout however you like. You can use it for your own custom modules.

### Languages ​​and layouts supported in kblang
- persian -> FaLayout class
- english -> EnLayout class

## Installation Guide

To install, you need Python 3.6 or higher, and you can install kblang with pip or manually from this GitHub repository.

install with pip:

~~~shell
pip install kblang
~~~

install from this repository:

~~~shell
pip install git+https://github.com/tahairavani/kblang.git
~~~
