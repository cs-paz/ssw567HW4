from GetGithubDetails import getGithubDetails
import unittest

class TestGetGithubDetails(unittest.TestCase):
  # removed this function and replaced to check the length instead
  # keeps causing errors because the number of commits in my repos
  # continuously change
  # def test_getGithubDetails1(self):
  #   self.assertEqual(getGithubDetails('cs-paz'), [
  #     'Repo: ahch_app Number of commits: 30',
  #     'Repo: CS-115 Number of commits: 1',
  #     'Repo: CS-135 Number of commits: 1',
  #     'Repo: CS-146 Number of commits: 5',
  #     'Repo: CS-284 Number of commits: 1',
  #     'Repo: CS-385 Number of commits: 1',
  #     'Repo: CS-392 Number of commits: 1',
  #     'Repo: CS-496 Number of commits: 2',
  #     'Repo: DuckDorms Number of commits: 7',
  #     'Repo: ssw567HW0 Number of commits: 2',
  #     'Repo: ssw567HW1 Number of commits: 3',
  #     'Repo: ssw567HW2 Number of commits: 8',
  #     'Repo: ssw567HW4 Number of commits: 13'
  #   ])

  def test_getGithubDetails1(self):
    self.assertEqual(len(getGithubDetails('cs-paz')), 13)

  def test_getGithubDetails2(self): 
    self.assertEqual(getGithubDetails(''), [])

  def test_getGithubDetails3(self): 
    self.assertEqual(getGithubDetails('this does not exist'), [])

if __name__ == '__main__':
    unittest.main()
