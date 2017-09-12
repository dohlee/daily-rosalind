import sys
import os
import shutil
from bs4 import BeautifulSoup
import time
import requests
import argparse

os.chdir(os.path.dirname(os.path.abspath(__file__)))

LOCATIONS = ['python-village',
			 'bioinformatics-stronghold',
			 'bioinformatics-armory',
			 'bioinformatics-textbook-track',
			 'algorithmic-heights']
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
HEADERS = {'user-agent': USER_AGENT}


def parse_argument():
	parser = argparse.ArgumentParser(description='This script will do all the tiresome stuffs for you.\n \
												  Just fill given scripts, test with toy datasets prepared already!')

	parser.add_argument('-a', '--author', required=True, help='Your name will be automatically written to all of your scripts.\n \
															   Feel some ownership in your codes! [REQUIRED]')

	return parser.parse_args()

def try_remove_directory(directory):
	try:
		print('Trying to remove "%s"...' % directory, end=' ')
		shutil.rmtree(directory)
		print('OK')
	except FileNotFoundError:
		print('Directory does not exist.')

def try_make_directory(directory):
	print('Trying to make "%s"...' % directory, end=' ')
	try:
		shutil.os.makedirs(directory)
		print('OK')
	except Exception:
		print('Failed!')
		sys.exit(1)

def get_problems(location):
	if not os.path.exists('html/%s.html' % location):
		res = requests.get('http://rosalind.info/problems/list-view/?location=%s' % location, headers=HEADERS)

		print('Wating for a moment not to burden rosalind server...')
		time.sleep(3)

		with open('html/%s.html' % location, 'w') as outFile:
			print(res.content, file=outFile)

	soup = BeautifulSoup(open('html/%s.html' % location, encoding='utf-8'), 'html.parser')

	problems = []
	for tr in soup.select('tbody > tr'):
		problem = {}
		for i, td in enumerate(tr.select('td')):
			if i == 0:
				problem['code'] = td.get_text().replace(r'\n', '').strip()
			if i == 1:
				problem['title'] = td.get_text().replace(r'\n', '').strip()
		problem['url'] = 'http://rosalind.info/problems/%s/' % problem['code']

		problems.append(problem)

	return problems

def translate_mathjax(mathjax):
	if not mathjax:
		return
	# translate mathjax expressions as much as possible
	# if you have some another mathjax expressions that could be written in typical characters,
	# please let me know!
	replaceDict = {'$': '',
				   '\lt': '<',
				   '\le': '<=',
				   '\leq': '<=',
				   'gt': '>',
				   '\geq': '>=',
				   '\ge': '>=',
				   '\approx':'~',
				   '\Delta':'Delta_',
				   '{': '(',
				   '}': ')',
				   '\mathrm': '',
				   '\mathscr': '',
				   '\ldots': '...',
				   '\textrm': ''}
	
	for k, v in replaceDict.items():
		mathjax = mathjax.replace(k, v)

	return mathjax

def clip(text):
	# if text is too long, insert newlines so that each line has less than about 50 characters wide.
	# ensure text does not have newlines and braces
	text = text.replace('\n', ' ').replace('{', '').replace('}', '')
	textFragments = []

	while len(text) > 50:
		try:
			clipSite = text.index(' ', 45)
		except ValueError:
			# substring not found
			break
		textFragments.append(text[:clipSite] + '\n# ')
		text = text[clipSite:]

	textFragments.append(text)

	return ''.join(textFragments)

def prepare_problem_script(problem, location, author):
	if os.path.exists('template_scripts/%s/%s.py' % (location, problem['code'])):
		with open('template_scripts/%s/%s.py' % (location, problem['code'])) as inFile:
			script = inFile.read().format(author=author)

		with open('../scripts/%s/%s.py' % (location, problem['code']), 'w') as outFile:
			print(script, file=outFile)
		return


	print('Wating for a moment not to burden rosalind server...')
	time.sleep(3)

	res = requests.get('http://rosalind.info/problems/%s' % problem['code'], headers=HEADERS)
	soup = BeautifulSoup(res.content, 'html.parser')

	for mathjax in soup.select('mathjax'):
		mathjax.replace_with(translate_mathjax(mathjax.get_text()))

	isGiven = True
	given, ret = '', ''
	for p in soup.select('p'):
		if len(p.select('span.given-return')) != 0:
			if isGiven:
				given = clip(p.get_text()).encode('ascii', 'ignore').decode('utf-8')
				isGiven = False
			else:
				ret = clip(p.get_text()).encode('ascii', 'ignore').decode('utf-8')

	with open('template_code.py') as inFile:
		script = inFile.read().format(url=problem['url'], title=problem['title'], code=problem['code'], given=given, ret=ret, author=author)

	with open('../scripts/%s/%s.py' % (location, problem['code']), 'w') as outFile:
		print(script, file=outFile)

def prepare_scripts(location, author):
	problems = get_problems(location)

	for i, problem in enumerate(problems, 1):
		print("[%d/%d] Preparing %s - %s : %s" % (i, len(problems), location, problem['code'], problem['title']))
		prepare_problem_script(problem, location, author)

def prepare_problem_dataset(problem, location):
	if os.path.exists('../done/datasets/rosalind_%s.txt' % problem['code']):
		shutil.copy('../done/datasets/rosalind_%s.txt' % problem['code'], '../datasets/')
		return

	print('Wating for a moment not to burden rosalind server...')
	time.sleep(3)

	res = requests.get('http://rosalind.info/problems/%s' % problem['code'], headers=HEADERS)
	soup = BeautifulSoup(res.content, 'html.parser')

	pres = soup.select('div.problem-statement > div.codehilite > pre')
	if len(pres) == 0:
		sampleInput = ''
	else:
		sampleInput = pres[0].get_text().strip()
	with open('../datasets/rosalind_%s.txt' % problem['code'], 'w') as outFile:
		print(sampleInput, file=outFile)

def prepare_datasets(location):
	problems = get_problems(location)
	
	for i, problem in enumerate(problems, 1):
		print("[%d/%d] Preparing %s - %s : %s" % (i, len(problems), location, problem['code'], problem['title']))
		prepare_problem_dataset(problem, location)

if __name__ == '__main__':
	args = parse_argument()
	author = args.author

	try_remove_directory('../scripts')
	try_remove_directory('../datasets')

	for location in LOCATIONS:
		try_make_directory('../scripts/%s' % location)
	try_make_directory('../datasets/')

	for location in LOCATIONS:
		prepare_scripts(location, author)
		prepare_datasets(location)	