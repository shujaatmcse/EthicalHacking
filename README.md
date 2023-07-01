# **Linux**

**Check if Github is intalled by typing**

git --version

if not instaled you can install it by typing Git apt

sudo apt-get install git

You need to the .git in the directory that you want to connect .

Current directory for info

┌──(kali㉿kali)-[~/pythonPractice]

└─$ pwd

/home/kali/pythonPractice

Note: You cannot see the .git directory in this folder

┌──(kali㉿kali)-[~/pythonPractice]

└─$ ls -la

total 20

drwxr-xr-x 2 kali kali 4096 Jul 1 14:29 .

drwx------ 19 kali kali 4096 Jul 1 14:20 ..

-rw-r--r-- 1 kali kali 2080 Jun 30 10:57 1basicPython.py

-rw-r--r-- 1 kali kali 735 Jul 1 12:31 2basicRecievingInputs.py

-rw-r--r-- 1 kali kali 479 Jul 1 13:33 3basicFunctions.py

Note: To add .git , run git init command

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git init

hint: Using 'master' as the name for the initial branch. This default branch name

hint: is subject to change. To configure the initial branch name to use in all

hint: of your new repositories, which will suppress this warning, call:

hint:

hint: git config --global init.defaultBranch \<name\>

hint:

hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and

hint: 'development'. The just-created branch can be renamed via this command:

hint:

hint: git branch -m \<name\>

Initialized empty Git repository in /home/kali/pythonPractice/.git/

Now .git directory added

┌──(kali㉿kali)-[~/pythonPractice]

└─$ ls -la

total 24

drwxr-xr-x 3 kali kali 4096 Jul 1 14:29 .

drwx------ 19 kali kali 4096 Jul 1 14:20 ..

-rw-r--r-- 1 kali kali 2080 Jun 30 10:57 1basicPython.py

-rw-r--r-- 1 kali kali 735 Jul 1 12:31 2basicRecievingInputs.py

-rw-r--r-- 1 kali kali 479 Jul 1 13:33 3basicFunctions.py

drwxr-xr-x 7 kali kali 4096 Jul 1 14:29 .git

┌──(kali㉿kali)-[~/pythonPractice]

└─$

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git status

On branch master

No commits yet

Untracked files:

(**use "git add \<file\>..." to include in what will be committed)**

1basicPython.py

2basicRecievingInputs.py

3basicFunctions.py

nothing added to commit but untracked files present (use "git add" to track)

using git add -A to add the current and subdirectory changes to git repo

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git add -A

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git status

On branch master

No commits yet

Changes to be committed:

(use "git rm --cached \<file\>..." to unstage)

new file: 1basicPython.py

new file: 2basicRecievingInputs.py

new file: 3basicFunctions.py

Note: You cannot add commit unless user and email is added.

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git commit -m " This directory to the repository for the first time"

Author identity unknown

\*\*\* Please tell me who you are.

Run

git config --global user.email "you@example.com"

git config --global user.name "Your Name"

to set your account's default identity.

Omit --global to set the identity only in this repository.

fatal: empty ident name (for \<shujaatmcse@gmail.com\>) not allowed

Note: You can use any email or username , not the github one . It is for local only

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git config --global user.name "Python learner"

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git config --global user.email "MyTestAnyEMail@gmail.com"

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git commit -m " This directory to the repository for the first time"

[master (root-commit) 45ba16c] This directory to the repository for the first time

3 files changed, 142 insertions(+)

create mode 100644 1basicPython.py

create mode 100644 2basicRecievingInputs.py

create mode 100644 3basicFunctions.py

Adding remote origin

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git remote add origin https://github.com/shujaatmcse/EthicalHacking.git

Note: You have to use the token when prompted for password, Github no longer uses password.

Token -\> profile photo -\> Settings -\> Developer settings- \> "Personal access tokens".-\> clasics

┌──(kali㉿kali)-[~/pythonPractice]

└─$ git push -u origin master

Username for 'https://github.com': shujaatmcse

**WINDOWS**

**YOU CAN INSTALL** [**https://git-scm.com/download/win**](https://git-scm.com/download/win) **SCM and then right click in the folder you can open bash and use git commands .**

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ pwd

/c/Users/Shujaat Ali/OneDrive/Python Ethical Hacking/EthicalHacking

NO .GIT file yet

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ ls -la

total 24

drwxr-xr-x 1 Shujaat Ali 197121 0 Jul 1 16:20 ./

drwxr-xr-x 1 Shujaat Ali 197121 0 Jul 1 15:55 ../

-rw-r--r-- 1 Shujaat Ali 197121 19790 Jul 1 16:06 GitHub.docx

Adding .GIT file in the directory

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git init

Initialized empty Git repository in C:/Users/Shujaat Ali/OneDrive/Python Ethical Hacking/EthicalHacking/.git/

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

**SETUP USER AND EMAIL**

$ git config --global user.name "Python learner"

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git config --global user.email "MyTestAnyEMail@gmail.com"

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git remote add origin https://github.com/shujaatmcse/EthicalHacking.git

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

Pulling the remote origin repo local so it can be merged

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git pull origin master

remote: Enumerating objects: 5, done.

remote: Counting objects: 100% (5/5), done.

remote: Compressing objects: 100% (5/5), done.

remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0

Unpacking objects: 100% (5/5), 1.83 KiB | 98.00 KiB/s, done.

From https://github.com/shujaatmcse/EthicalHacking

\* branch master -\> FETCH\_HEAD

\* [new branch] master -\> origin/master

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git commit -m "Tring to Push work from Windows PC for the first time to a previosu repo"

On branch master

Untracked files:

(use "git add \<file\>..." to include in what will be committed)

GitHub.docx

nothing added to commit but untracked files present (use "git add" to track)

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git add -A

COMMIT and ADD IS NEEDED TO STAGE THE CHANGES

You need to use three command to upload changes to a repo.

1. **git add .**
2. **git commit -m "Commit message"**
3. **git push origin \<branch\>**

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git commit -m "uploading Word doc"

[master 41adce1] uploading Word doc

1 file changed, 0 insertions(+), 0 deletions(-)

create mode 100644 GitHub.docx

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$ git push origin master

Enumerating objects: 4, done.

Counting objects: 100% (4/4), done.

Delta compression using up to 6 threads

Compressing objects: 100% (3/3), done.

Writing objects: 100% (3/3), 16.65 KiB | 8.33 MiB/s, done.

Total 3 (delta 1), reused 0 (delta 0), pack-reused 0

remote: Resolving deltas: 100% (1/1), completed with 1 local object.

To https://github.com/shujaatmcse/EthicalHacking.git

45ba16c..41adce1 master -\> master

Shujaat Ali@DESKTOP-RGFS0J8 MINGW64 ~/OneDrive/Python Ethical Hacking/EthicalHacking (master)

$
