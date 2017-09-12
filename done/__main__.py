import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
	with open('README_template.md') as inFile:
		template = inFile.read()

	with open('../README.md', 'w') as outFile:
		print(template.format(status='aaa'), file=outFile)

if __name__ == '__main__':
	main()