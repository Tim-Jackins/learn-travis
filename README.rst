# learn-travis
How do you use travis with python?

.. image:: https://travis-ci.org/Tim-Jackins/learn-travis.svg?branch=master
   :target: https://travis-ci.org/Tim-Jackins/learn-travis
   :alt: Travis CI Status
   
sudo: false

language: python

python:
	- 3.4
	- 3.5
	- 3.6
#install: pip3 install --trusted-host pypi.python.org -r requirements.txt
install: pip3 install --trusted-host pypi.python.org -r requirements.txt

script: python3 print_rank.py #&& autopep8 print_rank.py --in-place

deploy:
  skip-cleanup: true
  github-token: $GITHUB_TOKEN  # Set in travis-ci.org dashboard, marked secure
  keep-history: true
  on:
    branch: master
change