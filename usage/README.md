# Usage
You can manage your rosalind codes, while automatically tracking the number of problems that you have solved.

## Requirements
Unfortunately, daily-rosalind project only allows **Python** solutions to be automatically tested. 

- Python
- BeautifulSoup (to fetch new problems when they're out!)

## Workflow
1. Fork the repository, and clone your own repository to get local copy of the daily rosalind project.
2. When you are ready, type `python prepare --author <your name>` to get your own fresh backbone scripts and toy datasets for testing. 
3. Visit [Rosalind](http://rosalind.info/) and register. Try to solve [Installing Python](http://rosalind.info/problems/ini1/) as a warm-up.
4. Try another problem, and fill corresponding script in `scripts/` directory to solve it. (You can identify scripts with their own locations and IDs. For example, ID 'INI2' is for Problem 'Variables and Some Arithmetic', so you should fill `scripts/python-village/INI2.py`) 
5. When you are done, type `python done` to celebrate your progress.
6. Push the repository if you want.

## Note
Automatic scoring system is not complete yet, since it just compares whether your answer and desired answer is identical. It cannot properly score when the order of answer is not relevant.

The datasets used in scoring system of this project is rather simple, so be sure to check whether your algorithms work on big datasets given by Rosalind. (You might often need more efficient algorithm to get answer in 5 minutes) 

Please use this project to efficiently manage your codes, and to motivate yourself!

## TODO
- [ ] Score order-irrelevant answers.
