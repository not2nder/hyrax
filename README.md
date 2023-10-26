## HYRAX - CLI Password Manager

![menu image](./img/menu.png)

### How to install:
Clone the repo
```
$ git clone https://github.com/not2nder/hyrax
```
Install the dependencies
```
$ cd hyrax
$ pip install -r requirements.txt
```
Now, you can run the file `main.py`

### How to use? 

**First, you will have to register a new user**

```
$ python3 main.py --register
```
or 
```
$ python3 main.py --register -u username
```
**To add a new password, you will need to run this command:**
```
$ python3 main.py -u user -p password --new -s service -l login
```
**To show your stored passwords, run this command: **

```
$ python3 main.py -u user -p password --show
```

And your output will be like this
```
+------------+-----------+----------+-----------+
| Password   | Service   | User     |   Pass_id |
+============+===========+==========+===========+
| password   | service   | login    |         1 |
+------------+-----------+----------+-----------+
```
