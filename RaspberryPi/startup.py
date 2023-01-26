import git

repo = git.Repo.clone_from('git@gitlab.com:philipstr01/sphere-ixd/RaspberryPi/raspy',
                           '/home/philip/Documents',
                           branch='master')
