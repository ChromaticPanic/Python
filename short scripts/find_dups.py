
import sqlite3
import os
import sys
import hashlib
import argparse
import subprocess
import multiprocessing

if getattr(sys, 'frozen', False):
    dname = os.path.abspath(os.path.dirname(sys.executable))
else:
    dname = os.path.abspath(os.path.dirname(__file__))

os.chdir(dname)
db = "tmk_db.sqlite"

class CONNECTION():
    def __init__(self):
        self.con = sqlite3.connect(os.path.join(dname, db))
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def send(self, query):
        result = []
        try:
            self.cur.execute(query)
            self.con.commit()
            result.extend(self.cur.fetchall())
            return result
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def sendonly(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
            return

        except Exception as ex:
            print(ex)
            sys.exit(1)

    def cur(self):
        return self.cur

video_path = os.path.join(dname, "videos")
tmk_path = os.path.join(dname, "tmk_files")
exact_match_file = os.path.join(dname, "sha-exact-match.txt")
log_file = os.path.join(dname, "tmk_log.txt")

def main():
    global tmk_path
    parser = argparse.ArgumentParser(description='Python tmk pdq wrapper for finding video duplicates')
    parser.add_argument('-p', metavar='--path', type=str, nargs='?', default=video_path, action='store', help='full path to video folder')
    parser.add_argument('-t', metavar='--tmkpath', type=str, nargs='?', default=tmk_path, action='store', help='full path to tmk folder')

    args = parser.parse_args()
    if args.t:
        tmk_path = os.path.abspath(args.t)
    if not os.path.exists(tmk_path):
        os.makedirs(tmk_path)

    pool = multiprocessing.Pool(processes=1)

    os.path.abspath(args.p)
    if os.path.exists(args.p):
        for file in os.scandir(args.p):
            if file.is_file() and file.path.endswith(".mp4"):
                pool.apply(add_to_db, [file.path, file.name, file.stat().st_size])
    else:
        print("Path does not exist: {}".format(args.p))
        input("Press Any key to exit")
        sys.exit(1)

    pool.close()
    pool.join()

    input("Press Any key to exit")

def add_to_db(path, name, size):
    global tmk_path
    global exact_match_file
    global log_file
    with open(path, 'rb') as f:
        con = CONNECTION()
        print("Calculating hash for {}".format(path))
        h = hashlib.sha256(f.read()).hexdigest()
        print(h)
        found = con.send("SELECT * FROM tmk WHERE id like '{}'".format(h))
        if not found:
            try:
                con.sendonly("INSERT INTO tmk (id, fullpath, filename, filesize, tmkpath) VALUES ('{}','{}','{}','{}','{}')".format(h, path, name, size, tmk_path))
                with open(log_file, 'a') as f:
                    f.write("INSERT INTO tmk '{}','{}','{}','{}','{}' ".format(h, path, name, size, tmk_path))
            except:
                print("Error adding to database")
                sys.exit(1)
            generate_tmk(path, h)
        elif path in found:
            return
        else:
            with open(exact_match_file, 'a') as f:
                f.write(path + " " + h + "\n")
            

def generate_tmk(file, h):
    global tmk_path
    global log_file

    print("Generating TMK for {}    ".format(file), end='')
    hashalgo = os.path.join(dname, "tmk/cpp/tmk-hash-video")

    p = subprocess.Popen([hashalgo, "-f", "/usr/bin/ffmpeg", "-i", file, "-d", tmk_path], stdout=sys.stdout, stderr=sys.stdout)
    p.wait()

    if p.returncode == 1:
        print("Error generating TMK for {}".format(file))
        sys.exit(1)
    else:
        os.rename(os.path.join(tmk_path, os.path.basename(file)[:-4] + ".tmk"), os.path.join(tmk_path, h + ".tmk"))
    
    with open(log_file, 'a') as f:
        f.write("...tmk generated \n")

    print("...Done\n\n")

# def get_col_names():
#     # con.cur.execute(query + " limit 1;")
#     return [member[0] for member in con.cur.description]


if __name__ == "__main__":
    main()
