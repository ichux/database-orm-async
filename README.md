# database-orm-async
Examples were adapted from https://www.encode.io/databases/ and https://www.encode.io/orm/

# run without issues
1. create a virtual env and ensure you are inside the directory that contains these codes
2. activate and install libraries found in this project
3. run:
```shell
array=(orm_async.py database_async.py sqlite_async.py)
rm -f *.sqlite && for i in ${array[@]}; do python src/$i; echo; done
```