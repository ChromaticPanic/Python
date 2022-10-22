'''
TMK+PDQF, a video-hashing algorithm for general-purpose use. It uses PDQ minus the final
binary-quantization step (hence PDQF, for floating-point), and then uses the TMK algorithm
per se to collect timewise information about the frames. Hashes are 256KB but the first 1KB
serve to differentiate almost all videos. Hash-computation time is a high multiple of videoplayback 
time: perhaps 30x depending on storage density.

PDQ, a photo-hashing algorithm for general-purpose use. Hashes are 256 bits with hamming
distance, accompanied by a 0-100 quality metric which quantifies level of detail, e.g. for
identifying blurry/featureless images. Hash-computation time is on the same order of
magnitude as disk-read of image files

TMK (for Temporal Match Kernel) is a video-similarity-detection algorithm produced in conjunction with Facebook
AI Research (FAIR). It produces fixed-length video hashes (on the order of 256KB), so that results are bounded in
size.



'''
import sqlite3
import os
import sys
import hashlib
import argparse
import subprocess
import multiprocessing
import datetime


class CONNECTION():
    def __init__(self):
        self.db = ""
        self.con = ""
        self.cur = ""

    def __del__(self):
        self.con.close()

    def connect(self,db):
        self.db = db
        self.con = sqlite3.connect(os.path.abspath(self.db))
        self.cur = self.con.cursor()

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


class VideoDedup():
    def __init__(self, dname):
        self.exact_match_file = os.path.abspath(
            os.path.join(dname, "sha-exact-match.txt"))
        self.tmk_path = os.path.abspath(os.path.join(dname, "tmk/"))
        self.log_file = os.path.abspath(os.path.join(dname, "log.txt"))
        self.processcnt = 1
        self.db = os.path.abspath(
            "/home/p4r0d1m3pxz/server_tools/video_dedup/tmk_db.sqlite")
        self.tmk_hash_path = os.path.abspath(
            '/home/p4r0d1m3pxz/server_tools/video_dedup/tmk/cpp/tmk-hash-video')
        self.ffmpeg_path = os.path.abspath('/usr/bin/ffmpeg')
        self.dname = os.path.abspath(dname)
        self.runlog = []
        initlog = []
        initlog.append("tmkpdq.py started at: " + str(datetime.datetime.now()))
        initlog.append("tmkpdq.py args: " + str(sys.argv))
        initlog.append("tmkpdq.py dname: " + str(self.dname))
        initlog.append("tmkpdq.py db: " + str(self.db))
        initlog.append("tmkpdq.py exactmatchfile: " + str(self.exact_match_file))
        initlog.append("tmkpdq.py tmkpath: " + str(self.tmk_path))
        initlog.append("tmkpdq.py logfile: " + str(self.log_file))
        initlog.append("tmkpdq.py processcnt: " + str(self.processcnt))
        for line in initlog:
            print(line)

        if not os.path.exists(self.tmk_hash_path) or not os.path.isfile(self.tmk_hash_path):
            initlog.append(
                "tmkpdq.py tmk_hash_path does not exist... {}".format(self.tmk_hash_path))
            with open(self.log_file, "a", encoding='utf-8') as f:
                for line in initlog:
                    f.write(line + "\n")
            raise Exception(
                "TMK hash program does not exist: {}".format(self.tmk_hash_path))
        else:
            print("TMK hash program found: {}".format(self.tmk_hash_path))
            initlog.append(
                "TMK hash program found: {}".format(self.tmk_hash_path))

        if not os.path.exists(self.ffmpeg_path) or not os.path.isfile(self.ffmpeg_path):
            initlog.append(
                "tmkpdq.py ffmpeg_path does not exist... {}".format(self.ffmpeg_path))
            with open(self.log_file, "a", encoding='utf-8') as f:
                for line in initlog:
                    f.write(line + "\n")
            raise Exception(
                "Stored FFMPEG path does not exist: {}".format(self.ffmpeg_path))
        else:
            print("FFMPEG path found: {}".format(self.ffmpeg_path))
            initlog.append("FFMPEG path found: {}".format(self.ffmpeg_path))

        if not os.path.exists(self.dname):
            initlog.append("Directory does not exist... {}".format(self.dname))
            with open(self.log_file, "a", encoding='utf-8') as f:
                for line in initlog:
                    f.write(line + "\n")
            raise Exception("Path does not exist")
        else:
            print("Path found: {}".format(self.dname))
            initlog.append("Path found: {}".format(self.dname))

        self.set_tmkpath(self.tmk_path)

        print("init complete {}".format(str(datetime.datetime.now())))
        with open(self.log_file, 'a', encoding='utf-8') as f:
            for line in initlog:
                f.write(line + "\n")
        initlog = []

    def set_db(self, db):

        if db and (not os.path.exists(os.path.abspath(db)) or not os.path.isfile(os.path.abspath(db))):
            print("Database file not found")
            raise Exception("Database file not found")
        else:
            self.db = os.path.abspath(db)

    def set_tmkpath(self, tmkpath):
        self.tmk_path = os.path.abspath(tmkpath)
        if not os.path.exists(self.tmk_path):
            print("TMK path does not exist...")
            self.runlog.append("TMK path does not exist...")
            print("Creating TMK path: {}".format(self.tmk_path))
            self.runlog.append("Creating TMK path: {}".format(self.tmk_path))
            os.makedirs(self.tmk_path)
        else:
            print("TMK path found: {}".format(self.tmk_path))
            self.runlog.append("TMK path found: {}".format(self.tmk_path))

    def set_exactmatchfile(self, exactmatchfile):
        self.exact_match_file = os.path.abspath(exactmatchfile)
        if not os.path.exists(self.exact_match_file):
            print("Exact match file does not exist...")
            self.runlog.append("Exact match file does not exist...")
            print("Creating exact match file: {}".format(self.exact_match_file))
            self.runlog.append("Creating exact match file: {}".format(
                self.exact_match_file))
            open(self.exact_match_file, 'a', encoding='utf-8').close()
        else:
            print("Exact match file exists: {}".format(self.exact_match_file))
            self.runlog.append("Exact match file exists: {}".format(
                self.exact_match_file))
            print("Data will be appended to this file")
            self.runlog.append("Data will be appended to this file")

    def set_logfile(self, logfile):
        self.log_file = os.path.abspath(logfile)
        if not os.path.exists(self.log_file):
            print("Log file does not exist...")
            self.runlog.append("Log file does not exist...")
            print("Creating log file: {}".format(self.log_file))
            self.runlog.append("Creating log file: {}".format(self.log_file))
            open(self.log_file, 'a', encoding='utf-8').close()
        else:
            print("Log file exists: {}".format(self.log_file))
            self.runlog.append("Log file exists: {}".format(self.log_file))
            print("Data will be appended to this file")
            self.runlog.append("Data will be appended to this file")

    def set_processcnt(self, processcnt):
        if processcnt < 1 or processcnt > multiprocessing.cpu_count():
            self.processcnt = 1
        else:
            self.processcnt = processcnt

        print("Process count: {}".format(self.processcnt))
        self.runlog.append("Process count: {}".format(self.processcnt))

    def process_folder(self):
        pool = multiprocessing.Pool(processes=self.processcnt)
        for file in os.scandir(self.dname):
            if file.is_file() and file.path.endswith(".mp4"):
                try:

                    pool.apply(self.add_to_db, [
                                    file.path, file.name, file.stat().st_size])
                except Exception as e:
                    print("Error processing file: {}".format(file.path))
                    self.runlog.append(
                        "Error processing file: {}".format(file.path))
                    print(e)
                    self.runlog.append(e)
                    with open(self.log_file, 'a', encoding='utf-8') as f:
                        for line in self.runlog:
                            f.write(line + "\n")
                    self.runlog = []
                    raise
        pool.close()
        pool.join()

    def add_to_db(self, path, name, size):

        with open(path, 'rb') as f:
            print("{} Processing file: {}".format(
                str(datetime.datetime.now()), path))
            self.runlog.append("{} Processing file: {}".format(
                str(datetime.datetime.now()), path))
            con = CONNECTION()
            try:
                con.connect(self.db)
            except Exception as e:
                print("{} Error connecting to database: {} {}".format(
                    str(datetime.datetime.now()), self.db, e))
                self.runlog.append("{} Error connecting to database: {} {}".format(
                    str(datetime.datetime.now()), self.db, e))
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    for line in self.runlog:
                        f.write(line + "\n")
                raise

            print("{} Calculating hash for {}".format(
                str(datetime.datetime.now()), path))
            self.runlog.append("{} Calculating hash for {}".format(
                str(datetime.datetime.now()), path))
            h = hashlib.sha256(f.read()).hexdigest()
            print(h)

            found = con.send("SELECT * FROM tmk WHERE id like '{}'".format(h))
            print ("{} Found {}".format(str(datetime.datetime.now()), found))
            self.runlog.append("{} Found {}".format(str(datetime.datetime.now()), found))
            
            if not found:
                try:
                    con.sendonly("INSERT INTO tmk (id, fullpath, filename, filesize, tmkpath) VALUES ('{}','{}','{}','{}','{}')".format(
                        h, path, name, size, self.tmk_path))
                    print("{} Adding file to database: {}".format(
                        str(datetime.datetime.now()), path))
                except Exception as e:
                    print("{} Error adding file to database: {} \n{}".format(
                        str(datetime.datetime.now()), path, e))
                    self.runlog.append("{} Error adding file to database: {} \n{}".format(
                        str(datetime.datetime.now()), path, e))
                    with open(self.log_file, 'a') as f:
                        for line in self.runlog:
                            f.write(line + "\n")
                    raise
                self.generate_tmk(path, h)
            elif path in found:
                print("{} File already in database: {}".format(
                    str(datetime.datetime.now()), path))
                self.runlog.append("{} File already in database: {}".format(
                    str(datetime.datetime.now()), path))
                return
            else:
                print("{} File is an exact sha256 match of an existing file in the database: {}".format(
                    str(datetime.datetime.now()), path))
                self.runlog.append("{} File is an exact sha256 match of an existing file in the database: {}".format(
                    str(datetime.datetime.now()), path))
                with open(self.exact_match_file, 'a', encoding='utf-8') as f:
                    f.write(path + " " + h + "\n")

    def generate_tmk(self, file, h):

        #print("Generating TMK for {}    ".format(file), end='')
        print("{} Generating TMK for {}".format(
            str(datetime.datetime.now()), file))
        self.runlog.append("{} Generating TMK for {}".format(
            str(datetime.datetime.now()), file))
        try:
            p = subprocess.Popen([self.tmk_hash_path, "-f", self.ffmpeg_path, "-i",
                                 file, "-d", self.tmk_path], stdout=sys.stdout, stderr=sys.stdout)
        except Exception as e:
            print("{} Error generating TMK: {}".format(
                str(datetime.datetime.now()), e))
            self.runlog.append("{} Error generating TMK: {}".format(
                str(datetime.datetime.now()), e))
            with open(self.log_file, 'a') as f:
                for line in self.runlog:
                    f.write(line + "\n")
            raise

        p.wait()

        if p.returncode == 1:
            print("{} Error generating TMK: {}".format(
                str(datetime.datetime.now())))
            self.runlog.append("{} Error generating TMK: {}".format(
                str(datetime.datetime.now())))
            with open(self.log_file, 'a') as f:
                for line in self.runlog:
                    f.write(line + "\n")
            raise
        else:
            prevname = os.path.join(
                self.tmk_path, os.path.basename(file)[:-4] + ".tmk")
            newname = os.path.join(self.tmk_path, h + ".tmk")
            print("{} Renaming {} to {}".format(
                str(datetime.datetime.now()), prevname, newname))
            self.runlog.append("{} Renaming {} to {}".format(
                str(datetime.datetime.now()), prevname, newname))
            os.rename(prevname, newname)
        print("{} TMK generated for {}".format(
            str(datetime.datetime.now()), file))
        self.runlog.append("{} TMK generated for {}".format(
            str(datetime.datetime.now()), file))
        with open(self.log_file, 'a', encoding='utf-8') as f:
            for line in self.runlog:
                f.write(line + "\n")
        self.runlog = []
        print("\n\n")


def main():
    if getattr(sys, 'frozen', False):
        dname = os.path.abspath(os.path.dirname(sys.executable))
    else:
        dname = os.path.abspath(os.path.dirname(__file__))

    os.chdir(dname)
    print("Current working directory: {}".format(dname))
    db = ""
    tmk_path = ""
    video_path = ""

    parser = argparse.ArgumentParser(
        description='Python tmk pdq wrapper for finding video duplicates')
    parser.add_argument('-db', metavar='--database', type=str,
                        nargs='?', action='store', help='full path to database')
    parser.add_argument('-p', metavar='--path', type=str, nargs='?',
                        action='store', help='full path to video folder')
    parser.add_argument('-t', metavar='--tmkpath', type=str,
                        nargs='?', action='store', help='full path to tmk folder')

    args = parser.parse_args()

    if not args.p:
        
        print(" Will process subfolders of {}".format(dname))
        for folder in sorted(os.scandir(dname), key=lambda e: e.name):
            skip = False
            auto = False
            response = ""
            if folder.is_dir() and not folder.is_symlink():

                for file in os.scandir(folder.path):
                    if file.is_file() and (file.path.endswith(".skiptmk") or file.path.endswith(".donetmk")):
                        skip = True
                        break
                    elif file.is_file() and file.path.endswith(".prepd"):
                        auto = True
                        response = "y"

                if skip:
                    continue
                
                if not auto:
                    response = input(
                        "Process {}? (y)es (s)kip (q)uit =>  ".format(folder.path))
                    while response.lower() != "y" and response.lower() != "s" and response.lower() != "q":
                        print("Invalid response")
                        response = input(
                            "Process {}? (y)es (s)kip (q)uit ".format(folder.path))

                if response.lower() == "y":
                    vd = VideoDedup(folder.path)
                    if args.t:
                        vd.set_tmkpath = os.path.abspath(args.t)

                    if args.db:
                        vd.set_db = os.path.abspath(args.db)

                    vd.process_folder()
                    with open(os.path.join(folder.path, ".donetmk"), 'a') as f:
                        f.write('.\n')

                elif response.lower() == "s":
                    print("Skipping {}".format(folder.path))
                    continue
                elif response.lower() == "q":
                    print("Exiting...")
                    break
    else:
        response = input(
            "Process {}? (y)es (q)uit =>  ".format(args.p))
        while response.lower() != "y" and response.lower() != "q":
            print("Invalid response")
            response = input(
                "Process {}? (y)es (q)uit ".format(args.p))
        if response.lower() == "y":
            vd = VideoDedup(args.p)
            if args.t:
                vd.set_tmkpath = os.path.abspath(args.t)

            if args.db:
                vd.set_db = os.path.abspath(args.db)

            vd.process_folder()

    input("Press Any key to exit")


if __name__ == "__main__":
    main()
