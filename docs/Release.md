## Release Processs 

Release process is not currently automated, I will enable a github action workflow as soon the project get some additional commiters.

```
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```