# a script publish the content
import sys
import argparse
import configparser
import json
import shutil
import subprocess


def main():
    argv = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='the config file')
    args = parser.parse_args()

    if 'config' not in args:
        # error 
        return

    config = configparser.ConfigParser()
    config.read(args.config)


    dest_dir = config.get("DEFAULT", 'dest')
    print(dest_dir)
    print(config.get("DEFAULT", 'path'))
    path_list = json.loads(config.get("DEFAULT", 'path'))
    for path in path_list:
        # 1. copy to the dest dir
        shutil.copy(path, dest_dir)

    # 2. git push
    command = 'cd {}; git pull; git add -A; git commit -am \'update\'; git push'.format(dest_dir)
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0].strip()


if __name__ == "__main__":
    main()
