{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fswiss\fprq2\fcharset0 Calibri;}{\f1\fnil\fcharset1 Segoe UI Symbol;}{\f2\fswiss\fprq2\fcharset129 Malgun Gothic;}{\f3\fmodern\fprq1\fcharset0 Lucida Console;}{\f4\fmodern\fprq1\fcharset0 Ubuntu Mono;}{\f5\fswiss\fprq2\fcharset0 Segoe UI;}{\f6\fnil\fcharset0 Calibri;}}
{\colortbl ;\red255\green0\blue0;\red0\green176\blue240;\red255\green255\blue0;\red0\green0\blue255;\red28\green168\blue0;\red177\green72\blue198;\red192\green160\blue0;\red0\green168\blue154;\red125\green151\blue255;\red212\green44\blue58;\red55\green65\blue81;}
{\*\generator Riched20 10.0.22621}\viewkind4\uc1 
\pard\widctlpar\sa160\sl252\slmult1\qc\cf1\kerning2\b\f0\fs44 Linux\par

\pard\widctlpar\sa160\sl252\slmult1\cf0\fs22 Check if Github is intalled by typing \par
\b0 git --version \par
\par
if not instaled you can install it by typing Git apt\par
\par
\cf2 sudo apt-get install git\par
\cf0\par
\cf2 You need to the .git in the directory that you want to connect .\par
\cf0\par
Current directory for info\par
\f1\fs20\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ pwd                       \par
/home/kali/pythonPractice\par
\fs22    \par
\cf2 Note: You cannot see the .git directory in this folder                                                                                                         \par
\cf0\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ ls -la\par
total 20\par
drwxr-xr-x  2 kali kali 4096 Jul  1 14:29 .\par
drwx------ 19 kali kali 4096 Jul  1 14:20 ..\par
-rw-r--r--  1 kali kali 2080 Jun 30 10:57 1basicPython.py\par
-rw-r--r--  1 kali kali  735 Jul  1 12:31 2basicRecievingInputs.py\par
-rw-r--r--  1 kali kali  479 Jul  1 13:33 3basicFunctions.py\par
 \par
\cf2 Note: To add  .git , run git init command                                                                                                \par
\cf0\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ \cf2 git init                                                             \cf0\par
hint: Using 'master' as the name for the initial branch. This default branch name\par
hint: is subject to change. To configure the initial branch name to use in all\par
hint: of your new repositories, which will suppress this warning, call:\par
hint: \par
hint:   git config --global init.defaultBranch <name>\par
hint: \par
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and\par
hint: 'development'. The just-created branch can be renamed via this command:\par
hint: \par
hint:   git branch -m <name>\par
Initialized empty Git repository in /home/kali/pythonPractice/.git/\par
\cf2    Now .git directory added                                                                                                   \par
\cf0\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ ls -la\par
total 24\par
drwxr-xr-x  3 kali kali 4096 Jul  1 14:29 .\par
drwx------ 19 kali kali 4096 Jul  1 14:20 ..\par
-rw-r--r--  1 kali kali 2080 Jun 30 10:57 1basicPython.py\par
-rw-r--r--  1 kali kali  735 Jul  1 12:31 2basicRecievingInputs.py\par
-rw-r--r--  1 kali kali  479 Jul  1 13:33 3basicFunctions.py\par
drwxr-xr-x  7 kali kali 4096 Jul  1 14:\highlight3 29 .git\highlight0\par
                                                                                                     \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ \par
                                                                                                    \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git status \par
On branch master\par
\par
No commits yet\par
\par
Untracked files:\par
  (\b use "git add <file>..." to include in what will be committed)\b0\par
        1basicPython.py\par
        2basicRecievingInputs.py\par
        3basicFunctions.py\par
\par
nothing added to commit but untracked files present (use "git add" to track)\par
                                                                                                     \par
\par
\highlight3 using git add -A to add the current and subdirectory changes to git repo\highlight0                                                                                             \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git add -A  \par
                                                                                                     \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git status\par
On branch master\par
\par
No commits yet\par
\par
Changes to be committed:\par
  (use "git rm --cached <file>..." to unstage)\par
        new file:   1basicPython.py\par
        new file:   2basicRecievingInputs.py\par
        new file:   3basicFunctions.py\par
\par
  Note: You cannot add commit unless user and email is added.                                                                                                \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git commit -m " This  directory to the repository for the first time"\par
Author identity unknown\par
\par
*** Please tell me who you are.\par
\par
Run\par
\par
  git config --global user.email "you@example.com"\par
  git config --global user.name "Your Name"\par
\par
to set your account's default identity.\par
Omit --global to set the identity only in this repository.\par
\par
fatal: empty ident name (for <shujaatmcse@gmail.com>) not allowed\par
 \par
Note: You can use any email or username , not the github one . It is for local only                                                                                               \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git config --global user.name "Python learner"              \par
                                                                                                     \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git config --global user.email "MyTestAnyEMail@gmail.com"\par
         \par
                                                                                                     \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git commit -m " This  directory to the repository for the first time"\par
[master (root-commit) 45ba16c]  This  directory to the repository for the first time\par
 3 files changed, 142 insertions(+)\par
 create mode 100644 1basicPython.py\par
 create mode 100644 2basicRecievingInputs.py\par
 create mode 100644 3basicFunctions.py\par
  \par
Adding remote origin                                                                                                    \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git remote add origin {{\field{\*\fldinst{HYPERLINK https://github.com/shujaatmcse/EthicalHacking.git }}{\fldrslt{https://github.com/shujaatmcse/EthicalHacking.git\ul0\cf0}}}}\f0\fs22  \par
  \par
Note: You have to use the token when prompted for password, Github no longer uses password.\par
Token -> profile photo -> Settings -> Developer settings- >  "Personal access tokens".-> clasics                                                                  \par
\f1\u9484?\u9472?\u9472?\f0 (kali\f2\'a2\'de\f0 kali)-[~/pythonPractice]\par
\f1\u9492?\u9472?\f0 $ git push -u origin master \par
Username for '{{\field{\*\fldinst{HYPERLINK https://github.com }}{\fldrslt{https://github.com\ul0\cf0}}}}\f0\fs22 ': shujaatmcse\par

\pard\widctlpar\sa160\sl252\slmult1\qc\cf2\b\par
WINDOWS\par

\pard\widctlpar\sa160\sl252\slmult1 YOU CAN INSTALL {\cf0{\field{\*\fldinst{HYPERLINK https://git-scm.com/download/win }}{\fldrslt{https://git-scm.com/download/win\ul0\cf0}}}}\f0\fs22  SCM and then right click in the folder you can open bash and use git commands .\par

\pard\widctlpar\cf5\kerning0\b0\f3\fs18 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \highlight3 pwd\highlight0\par
/c/Users/Shujaat Ali/OneDrive/Python Ethical Hacking/EthicalHacking\par
\par
\cf1 NO .GIT file yet\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ ls -la\par
total 24\par
drwxr-xr-x 1 Shujaat Ali 197121     0 Jul  1 16:20 \cf9 .\cf0 /\par
drwxr-xr-x 1 Shujaat Ali 197121     0 Jul  1 15:55 \cf9 ..\cf0 /\par
-rw-r--r-- 1 Shujaat Ali 197121 19790 Jul  1 16:06 GitHub.docx\par
\par
\cf1 Adding .GIT file in the directory \par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \highlight3 git init\highlight0\par
Initialized empty Git repository in C:/Users/Shujaat Ali/OneDrive/Python Ethical Hacking/EthicalHacking/.git/\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par

\pard\widctlpar\qc\cf1\b\fs36 SETUP USER AND EMAIL\par

\pard\widctlpar\b0\fs18 $ git config --global user.name "Python learner\cf0 "\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \cf1 git config --global user.email "MyTestAnyEMail@gmail.com"\cf0\par
\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ git remote add origin {{\field{\*\fldinst{HYPERLINK https://github.com/shujaatmcse/EthicalHacking.git }}{\fldrslt{https://github.com/shujaatmcse/EthicalHacking.git\ul0\cf0}}}}\f3\fs18\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0\par
\cf1      Pulling the remote origin repo local so it can be merged\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \cf1 git pull origin master\cf0\par
remote: Enumerating objects: 5, done.\par
remote: Counting objects: 100% (5/5), done.\par
remote: Compressing objects: 100% (5/5), done.\par
remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0\par
Unpacking objects: 100% (5/5), 1.83 KiB | 98.00 KiB/s, done.\par
From {{\field{\*\fldinst{HYPERLINK https://github.com/shujaatmcse/EthicalHacking }}{\fldrslt{https://github.com/shujaatmcse/EthicalHacking\ul0\cf0}}}}\f3\fs18\par
 * branch            master     -> FETCH_HEAD\par
 * [new branch]      master     -> origin/master\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \cf1 git commit -m "Tring to Push work from Windows PC for the first time to a previosu repo"\par
\cf0 On branch master\par
Untracked files:\par
  (use "git add <file>..." to include in what will be committed)\par
        \cf10 GitHub.docx\par
\par
\cf0 nothing added to commit but untracked files present (use "git add" to track)\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \cf1 git add -A\cf0\par
\par

\pard\widctlpar\qc\cf1 COMMIT and ADD  IS NEEDED TO STAGE THE CHANGES\par

\pard\widctlpar You need to use three command to upload changes to a repo.\par

\pard\brdrl\brdrs\brdrw5\brsp100 \brdrt\brdrs\brdrw5 \brdrr\brdrs\brdrw5 \brdrb\brdrs\brdrw5 {\pntext\f5 1.\tab}{\*\pn\pnlvlbody\pnf5\pnindent360\pnstart1\pndec{\pntxta.}}
\widctlpar\fi-360\li720\cf11\b\f4\fs21 git add .\b0\f5\fs24\par
{\pntext\f5 2.\tab}\b\f4\fs21 git commit -m "Commit message"\b0\f5\fs24\par
{\pntext\f5 3.\tab}\b\f4\fs21 git push origin <branch>\b0\f5\fs24\par

\pard\widctlpar\cf1\f3\fs18\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \cf1 git commit -m "uploading Word doc"\cf0\par
[master 41adce1] uploading Word doc\par
 1 file changed, 0 insertions(+), 0 deletions(-)\par
 create mode 100644 GitHub.docx\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $ \cf1 git push origin master\cf0\par
Enumerating objects: 4, done.\par
Counting objects: 100% (4/4), done.\par
Delta compression using up to 6 threads\par
Compressing objects: 100% (3/3), done.\par
Writing objects: 100% (3/3), 16.65 KiB | 8.33 MiB/s, done.\par
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0\par
remote: Resolving deltas: 100% (1/1), completed with 1 local object.\par
To {{\field{\*\fldinst{HYPERLINK https://github.com/shujaatmcse/EthicalHacking.git }}{\fldrslt{https://github.com/shujaatmcse/EthicalHacking.git\ul0\cf0}}}}\f3\fs18\par
   45ba16c..41adce1  master -> master\par
\par
\cf5 Shujaat Ali@DESKTOP-RGFS0J8 \cf6 MINGW64 \cf7 ~/OneDrive/Python Ethical Hacking/EthicalHacking\cf8  (master)\par
\cf0 $\par

\pard\widctlpar\sa160\sl252\slmult1\cf2\kerning2\b\f0\fs22\par

\pard\sa200\sl276\slmult1\cf0\kerning0\b0\f6\lang9\par
}
 