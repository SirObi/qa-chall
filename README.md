# What's the purpose of this repo?

This repository contains a solution to a QA challenge.

# What kind of tests does this repo include?

Given the time constraints of the challenge, the repo contains only several  
regression tests for critical functionality of the 2 websites under test.

# Main design choices

**Python** - Python is a mature, stable language, with a large community and regularly  
updated software testing libraries. This makes it a good choice in terms of stability  
and scalability.

**Selenium WebDriver** - this open-source suit of tools is the usual choice  
for Test Automation teams due to its popularity and compatibility with multiple  
languages

**Page Object pattern** - since the challenge concentrates on two Web  
applications, the natural design choice for the framework is to follow the Page  
Object pattern.  
It espouses separation of concerns and code reuse, by keeping the test  
cases separate from the implementation details and HTML page structure.  
The latter two are neatly organized into classes containing page-specific element  
locators and functions. Whenever a test involves a particular page, it simply  
has to import the corresponding class.

**Gherkin** - as the first step in attempting this challenge, the author tried  
to understand the business purpose behind the required tests and capture it in  
the form of Gherkin specs. This informed the organization of the test framework.  

# How to run it?

Please note: due to the time constraints of the challenge,
this manual is for Mac users only.

## Clone this repository

`git clone obioiboibobiboibobiboib`

## Install Python and virtualenv

Your Mac should come with Python pre-installed.

However, you'll need the Python package manager, called `pip`

`sudo easy_install pip`

For stability purposes, it's generally a good idea to create a virtual  
environment for a new Python project.

`cd` to the directory you've cloned.

Install virtualenv:

`sudo pip install virtualenv`

Create and launch a new virtual environment:

`virtualenv env`  
`source env/bin/activate`

## Install selenium in the virtual environment

`pip install selenium`

## Download chromedriver and add its location to PATH
This project uses Chrome for presentation purposes.

In order to drive Chrome, you need the latest version of `chromedriver`
on your PATH.

The most stable way to install chromedriver is via Homebrew:

`brew install chromedriver`  

If you do not have Homebrew installed, first run:  
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## Make sure chromedriver can be found by Python:
Launch Python in the Terminal:
`python`  

Type:  

`from selenium import webdriver`  

`browser = webdriver.Chrome()`

## Run the regression suite for given app
The two applications under test are Wikipedia and Travelex.

You can launch the test suite for Wikipedia like so:
`sdsd`  

And the test suit for Travelex like so:
`djsdskj`
