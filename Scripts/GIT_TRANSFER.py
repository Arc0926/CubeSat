import os
from git import Repo

def git_push(img_file_path):
    try:
        absolutepath = os.path.abspath(__file__)
        repoDirectory = os.path.dirname(os.path.dirname(absolutepath))
        fileName = os.path.join(repoDirectory, img_file_path).replace("\\","/")
        print(repoDirectory)
        repo = Repo(repoDirectory) #PATH TO YOUR GITHUB REPO
        repo.git.add(fileName) #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')

    except:
        print("Couldn't upload to git")

git_push("Images")