Deployment of changes
=======================

## Required packages:

* fabric3

1. Commit all changes
```
git commit -am "This is the latest version"
```

2. Push to master
```
git push
```

3. Run fabric script from /development_tools
```
cd development_tools
fab deploy:host=django@fmularczyk.pl
```
