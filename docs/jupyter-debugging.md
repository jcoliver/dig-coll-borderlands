# Updating Jupyter Notebook locally

**Background**: instance of Jupyter Notebook of unknown antiquity on laptop. Trying to update it in response to error message:
```
jupyter --version
Traceback (most recent call last):
  File "/usr/local/bin/jupyter", line 7, in <module>
    from jupyter_core.command import main
ModuleNotFoundError: No module named 'jupyter_core'
```

Quick fix from https://jupyter-notebook.readthedocs.io/en/stable/changelog.html:
`python -m pip install notebook --upgrade`
(was `pip install notebook --upgrade`, but `pip` is throwing it's own hissy fit)

Returns:
```
Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/zmq'
Consider using the `--user` option or check the permissions.

You are using pip version 19.0.3, however version 20.0.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

Answers at https://github.com/googlesamples/assistant-sdk-python/issues/236
Tried adding user option:
```
python -m pip install --user notebook --upgrade
```

Invoking jupyter from command line actually worked?!?!