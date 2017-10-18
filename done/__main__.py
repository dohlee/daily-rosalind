from __future__ import print_function
import os
import shutil
from functools import wraps
import subprocess
import traceback
import re
DONE_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(DONE_PATH)

def ensure_at_done(func):
    """ Decorator function which ensures 
    the wrapped function executed at 'done' directory
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        os.chdir(DONE_PATH)
        return func(*args, **kwargs)
    return wrapper

LOCATIONS = ['python-village',
             'bioinformatics-stronghold',
             'bioinformatics-armory',
             'bioinformatics-textbook-track',
             'algorithmic-heights']
ORDER_IRRELEVANT_PROBLEMS = [line.strip() for line in open('order_irrelevant_problems.txt').readlines()]
IGNORED_PROBLEMS = [line.strip() for line in open('ignored_problems.txt').readlines()]

def stash_directories():
    shutil.move('../datasets/', '../datasets_/')
    shutil.move('../answers/', '../answers_/')

@ensure_at_done
def restore_directories():
    shutil.rmtree('../datasets/')
    shutil.rmtree('../answers/')

    shutil.move('../datasets_/', '../datasets/')
    shutil.move('../answers_/', '../answers/')

def prepare_test_environment():
    shutil.copytree('./datasets/', '../datasets/')
    os.mkdir('../answers/')

def progress_bar(curr, total, barLength=20):
    l = int(curr / total * barLength)

    filled = '#' * l
    blanks = ' ' * (barLength - l)
    return '[' + filled + blanks + ']'

def test():
    testResult = dict()

    for location in LOCATIONS:
        os.chdir('../scripts/%s' % location)
        testResult[location] = dict()
        
        scripts = os.listdir()
        codes = [script[:-3] for script in scripts if script.endswith('.py')]

        correctCount, total = 0, len(codes)
        for curr, (code, script) in enumerate(zip(codes, scripts), 1):
            subprocess.call(['python', script])

            correct = test_single(location, code)
            if correct:
                correctCount += 1
                
            print('Testing %-30s [%3d/%3d] %s [%3d/%3d Correct]' % (location, curr, total, progress_bar(curr, total), correctCount, total), end='\r')

        testResult[location]['correctCount'] = correctCount
        testResult[location]['total'] = total

        print()
        os.chdir('../../done/')

    return testResult

def squash_consecutive_whitespaces(string):
    """Substitute all runs of whitespace with a tab."""
    return re.sub(r'\s+', '\t', string)

def identity_test(myAnswerFile, answerFile):
    with open(myAnswerFile) as inFile:
        myAnswer = squash_consecutive_whitespaces(inFile.read().strip())

    with open(answerFile) as inFile:
        answer = squash_consecutive_whitespaces(inFile.read().strip())

    return myAnswer.strip() == answer.strip()

def order_irrelevant_test(myAnswerFile, answerFile):
    with open(myAnswerFile) as inFile:
        myAnswerSet = set([squash_consecutive_whitespaces(line.strip()) for line in inFile.readlines()])

    with open(answerFile) as inFile:
        answerSet = set([squash_consecutive_whitespaces(line.strip()) for line in inFile.readlines()])

    return myAnswerSet == answerSet

def test_single(location, code, verbose=False):
    myAnswerFile = '../../answers/rosalind_%s_out.txt' % code
    answerFile = '../../done/answers/rosalind_%s.txt' % code

    if not os.path.exists('../../answers/rosalind_%s_out.txt' % code):
        return False

    if code.upper() in ORDER_IRRELEVANT_PROBLEMS:
        return order_irrelevant_test(myAnswerFile, answerFile)

    if code.upper() in IGNORED_PROBLEMS:
        return True

    else:
        return identity_test(myAnswerFile, answerFile)
    

def preserve_whitespaces(string):
    s = re.sub('\s', '&nbsp;&nbsp;', string)
    return s

@ensure_at_done
def update_readme(testResult):
    status = []
    for location in LOCATIONS:
        correctCount = testResult[location]['correctCount']
        total = testResult[location]['total']
        stat = '%s|%s|[%3d/%3d Correct]' % (location, progress_bar(correctCount, total), correctCount, total)
        status.append(preserve_whitespaces(stat))

    status = '\n'.join(status)

    with open('README_template.md') as inFile:
        template = inFile.read()

    with open('../README.md', 'w') as outFile:
        print(template.format(status=status), file=outFile)

def main():
    try:
        stash_directories()
        prepare_test_environment()

        testResult = test()

        update_readme(testResult)

    except:
        traceback.print_exc()

    finally:
        restore_directories()

if __name__ == '__main__':
    main()