from GetGithubDetails import getGithubDetails

def test_getGithubDetails1():
  assert getGithubDetails('cs-paz') == [
    'Repo: ahch_app Number of commits: 30',
    'Repo: CS-115 Number of commits: 1',
    'Repo: CS-135 Number of commits: 1',
    'Repo: CS-146 Number of commits: 5',
    'Repo: CS-284 Number of commits: 1',
    'Repo: CS-385 Number of commits: 1',
    'Repo: CS-392 Number of commits: 1',
    'Repo: CS-496 Number of commits: 2',
    'Repo: DuckDorms Number of commits: 7',
    'Repo: ssw567HW0 Number of commits: 2',
    'Repo: ssw567HW1 Number of commits: 3',
    'Repo: ssw567HW2 Number of commits: 8',
    'Repo: ssw567HW4 Number of commits: 13'
  ]

def test_getGithubDetails2(): 
  assert getGithubDetails('') == []

def test_getGithubDetails3(): 
  assert getGithubDetails('this does not exist') == []

if __name__ == '__main__':
    test_getGithubDetails1()
    test_getGithubDetails2()
    test_getGithubDetails3()
