import git
from git import Repo

#def git_push():
try:

    repo = Repo("C:\CUBESAT\CubeSat") #PATH TO YOUR GITHUB REPO
    repo.git.add("C:\CUBESAT\CubeSat\Images") #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
    repo.index.commit('New Photo')
    print('made the commit')
    origin = repo.remote('origin')
    print('added remote')
    origin.push()
    print('pushed changes')

except:
    print('Couldn't upload to git')
