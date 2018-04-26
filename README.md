# learn-travis
How do you use travis with python?

sudo: false

#notifications:
#  email:
#    recipients:
#     - timmins.jack595@gmail.com
#    on_success: never # default: change
#    on_failure: always # default: always

language: python

python:
	- 3.4
	- 3.5
	- 3.6

install: pip3 install --trusted-host pypi.python.org -r requirements.txt

script: python3 print_rank.py #&& autopep8 print_rank.py --in-place

deploy:
  skip-cleanup: true
  github-token: $GITHUB_TOKEN  # Set in travis-ci.org dashboard, marked secure
  keep-history: true
  on:
    branch: master