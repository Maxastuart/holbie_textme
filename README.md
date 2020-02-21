# holbie_textme

Holberton School Hack Day Project to use intranet's API &amp; receive an email or text (SMS) when the checker is out for your current projects

## setup

### install python 3.7

mac:

```bash
brew install python
```

linux (ubuntu):

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7
```

### use venv, a virtual environment to get the right dependencies for our project

This, and the rest, should be done in the folder you cloned this repo into ( /foo/bar/holbie_textme )

```bash
python3.7 -m pip venv venv   # creates a venv folder in your current directory
source venv/bin/activate        # activates this virtual environment
```

### install dependencies

```bash
python3.7 -m pip install -r requirements.txt
```

### Get our secret environment variables from Slack

put them in a file called ```.env```

### develop away
