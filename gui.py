# GIT Commands
# git config --global user.name Jayesh ---->to set user name
# git config --global user.email jayeshkr73608@gmail.com ---->to set user email
# git config --global user.name ---->to check user name
# git config --global user.email ---->to check user name
# git init ----->Initialized empty Git repository in folder----> D:/pro/.git/
# ls -lart ------>to check all the files present in the folder including hidden file
# git status ----> to check the status of the files weather untracked or commited
# git add file name ----->use to add file to track it and commit it
# git commit -----> To commite for the change in the file
# Press i --> initial commite ---->press Ese : w q --->enter
# git commit -m "Added more htmls"-------> This is another way to commit
# git commit -a -m "comment" ------>To add and comment a file directly
# touch filename -----> To create empty file
# git add -A ------> To track all the files in the folder at time
# clear -------> to clear the terminal
# git checkout -f ------> If we want to remove current edit and go to the last edit for all file at a time.
# git checkout filename ------> If we want to remove current edit and go to the last edit of one file.
# git log -------> To check about all the commits done with details.
# git log -p -2 ----->To check required number of commits along with all details.
# q enter ----> to come out of commit details
# git rm -----> To delete from stagging and directory both.
# git rm --cached waste.html -----> To delete only from staging area not from directory
# git diff ----->It compares working directory with stagging directory and shows the changes
# git status -s ------>summerised status, it show over view status of all files
# git branch -----> To check how many branches are there.
# git branch branchname -------> to create branch
# git checkout branchname ------>To switch to given branch name
# git checkout -b branchname------>To create and switch to new branch directly
# git remote add origin https://github.com/Jayesh321/jayesh.git ----->To add local repo to remote repo with url name origin
# git remote ------> To check how many origins are there
# git remote -v ------> To get url link to fectch and push the files
# ssh-keygen -t rsa -b 4096 -C "jayeshkr73608@gmail.com" ------->Generating the SSH key
# eval $(ssh-agent -s) ------>Adding SSH key to the ssh agent ----->Agent pid 2024
# ssh-add ~/.ssh/id_rsa ------->Add your SSH private key to the ssh-agent.------>Identity added: /c/Users/Jayesh/.ssh/id_rsa (jayeshkr73608@gmail.com)
# cat ~/.ssh/id_rsa.pub -------> Got big key which i copied and pasted in New SSh key to get read write access
# git remote set-url origin git@github.com:Jayesh321/jayesh.git ------->To change Url to get read and write access--->origin  git@github.com:Jayesh321/jayesh.git (fetch),  origin  git@github.com:Jayesh321/jayesh.git (push)
# git push -u origin master---->to push the master branch on remote repo
#