# Setup for working with this project.

You will need to create environment variables wherein you store your secrets.
Currently the secrets which are required to keep this bot running are these

1. discord_token - token for the bot to connect to discord servers
2. reddit_client_id - client id for the app you created on reddit to access 
the memes
3. reddit_client_secret - client secret for the reddit app

If you add some other secrets to this project it is recommended that you add 
it to this list. 

These secrets are fetched from the env.py file present in the root directly. 

It is recommended that you use the same file for other secrets as well.

# Working with this project.

While i hope that you all know how you will work in this environment. If you
dont know here is a quick lesson.

Make sure you are not working on the master branch. Always checkout to a
personal feature branch and work on there. After you are done with the changes 
ask maintainer to merge it.

To checkout to a new branch do something like this.
```
git checkout -b yourname-featurename 
```

After you are done with the changes push your branch to the repo and ask the
maintainer to merge it if there are no conflicts. To reduce conflicts make sure
you dont edit any files in which you are not working.

to push your branch you can do something like this.
```
git push -u nameofremoterepo nameofyourbranch
```