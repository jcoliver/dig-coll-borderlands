# JupyterHub for workshops

## 2020-04-29
+ Lots of data files. Used `scp` to get them onto Atmosphere; they ended up in /home/<admin>/Documents/collections-as-data/data
+ Created a symbolic link to data directory in /home (`ln -s /home/<admin>/Documents/collections-as-data/data /home/data`)
+ From /home/<admin>/Documents/collections-as-data, changed permissions so all could read (`chmod -R a+r data`)
+ Logged on as "student2" to see if I could access the file.
http://128.196.142.60/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fjcoliver%2Fdig-coll-borderlands&urlpath=tree%2Fdig-coll-borderlands%2F
    + note IP will likely vary
    + note the link doesn't work witout encodings (i.e. link needs to have ""%2F" in place of "/" in the query string))
+ Need to install pandas for use by all
    + Logged into hub as admin
    + In the JupyterHub Git repo view, click "New > Terminal" in upper right
        + `sudo -E pip install pandas`
+ Logged in (after logging out as admin) as student2
    + `import pandas` returned no errors

## 2020-03-12
+ Logged on as "student1" with no problem.
+ Add nbgitpuller link per instructions at http://tljh.jupyter.org/en/latest/howto/content/nbgitpuller.html.
    But, the nbgitpuller relies on a static URL, which is not the case for the Atmo instance. Can create a link by hand using the pattern:
    http://<my-jhub-address>/hub/user-redirect/git-pull?repo=<your-repo-url>&branch=<your-branch-name>&subPath=<subPath>&app=<notebook | lab>
    Which, in practice should be (note the IP will change):
http://128.196.142.102/hub/user-redirect/git-pull?repo=https://github.com/jcoliver/dig-coll-borderlands
+ Add at least some dependencies through the JupyterHub interface (http://tljh.jupyter.org/en/latest/howto/env/user-environment.html).
    + Logged into hub as admin
    + In the JupyterHub Git repo view, click "New > Terminal" in upper right
    + `sudo -E pip install nltk`
    # Successfully installed nltk-3.4.5
    + In a python terminal on the hub, `import nltk` returned no errors.
    + In the python notebook, ran
    ```
    import nltk
    nltk.download('stopwords')
    ```

## 2020-03-10
1. Resumed instance
2. ssh to instance and ran `cat /etc/group`; each user gets their own group
3. Reran the startup script
    + This time, added username _AND_ password (per instructions at http://tljh.jupyter.org/en/latest/topic/customizing-installer.html):
    ```
    curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py \
         | sudo python3 - \
         --admin <admin-user1>:<password-user1>
    ```
    replacing <admin-user1> and <password-user1> as appropriate
4. Did **not** run any of the commands about authentication
5. Through a web browser, point to IP and try to log in
    + This **worked**

## Setup overview
1. Spin up Atmosphere instance (use Jetstream tutorial)
2. Add JupyterHub install in setup
3. Install python dependencies on this instance; should probably be done through the Jupyter Notebook interface with `pip` (http://tljh.jupyter.org/en/latest/howto/env/user-environment.html)
4. Allow anyone to log into the JupyterHub (http://tljh.jupyter.org/en/latest/howto/auth/firstuse.html#allowing-anyone-to-log-in-to-your-jupyterhub); it looks like this can be done via:
```
sudo tljh-config set auth.type firstuseauthenticator.FirstUseAuthenticator
sudo tljh-config reload
tljh-config set auth.FirstUseAuthenticator.create_users true
tljh-config reload
```
5. Set up GitHub repository with Jupyter Notebook
6. Generate a nbgitpuller link and point to the Jupyter Notebook from step 3
7. Follow nbgitpuller link to Jupyter Notebook running on Atmosphere instance

## Setup implementation
1. Atmosphere. Use image Ubuntu 18.04 GUI XFCE Base. Skip the Deployment Script part of "Installing The Littlest JupyterHub" (steps 6-11 on the tutorial) http://tljh.jupyter.org/en/latest/install/jetstream.html.
2. When Atmo instance is live, log in via ssh. First make sure python 3 is default python:
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
sudo update-alternatives --set python /usr/bin/python3.6
```
Do some specific updates, then update entire system:
```
sudo apt-get install --yes python3 python3-venv python3-pip git
sudo apt-get update
sudo apt-get upgrade
```
Finally, run the command that would have been used in the Deployment Script (**replacing** `<admin-user-name>` with the admin name for the Atmo instance):
```
curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py | sudo python3 - --admin <admin-user-name>
```
3. Skipping python dependencies for now
4. Allow anyone to log in (tutorial does not run commands 3 and 4 as super-user, though...)
```
sudo tljh-config set auth.type firstuseauthenticator.FirstUseAuthenticator
sudo tljh-config reload
sudo tljh-config set auth.FirstUseAuthenticator.create_users true
sudo tljh-config reload
```
But Spawn fails.
looking at logs (), error looks to be thrown:
`"getgrnam(): name not found: 'jupyterhub-users'""`
5. Set up GitHub repository with Jupyter Notebook (just using https://github.com/jcoliver/dig-coll-borderlands)
6.


## Questions
1. How can materials generated on JupyterHub (e.g. data files, images) be downloaded to a local computer?

## References

### JupterHub home
http://tljh.jupyter.org/en/latest/