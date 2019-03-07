# Mainly used to write notes on new concepts and findings...
import os
from sys import stdin

dir = './notes'
rights = 00755
file = 'project-notes.txt'

def main():
    global dir
    global rights
    global file
    if os.path.isdir(dir):
        note_writer(file)
    else:
        try:
            os.mkdir(dir, rights)
        except OSError as e:
            print('{} directory creation failed'.format(dir))
        else:
            print('{} directory created successfully'.format(dir))


def note_writer(filename):
    try:
        print('Attempting to open your file...')
        with open(filename, 'a+') as file_handle:
            print('Success!\nEnter your notes to be added to your notepad:')
            for line in stdin:
                if line == '':
                    break
                file_handle.write(line)
    except Exception as e:
        print('an error occured: {}'.format(str(e)))


if __name__ == '__main__':
    main()
