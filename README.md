#### pre-requisites

```
pip install pelican markdown ghp-import
```

#### updating http://namoopsoo.github.com/mlao-blog 

* Add/Edit files.
* Put images into s3.
* git add files in content/ dir.
* git commit 

* run pelican command from the `/` root dir of the project.
```
pelican content -o output -s pelicanconf.py
```

* Use ghp import tool to throw the latest to the special branch
```
ghp-import output
```

* finally push to github , 
```
git push origin gh-pages
```

#### preview/test locally...
```
cd ~/projects/yoursite/output
python -m pelican.server

```

#### or all together...
```
pelican content -o output -s pelicanconf.py

# (likely have to copy any local images from content/ to output/ as well)

# edit `./output/theme/css/main.css` , inserting the extra line shown below.

ghp-import output
git push origin gh-pages
```

#### when only editing select outputs..
```
pelican --write-selected output/posts/my-post-title.html

```


#### for now, it seems like i have to update `main.css` all the time
* Need to update it after running the `pelican` command, unless i can figure out how to include the custom css at some point
* Adding this in `main.css` helped make images not cover up everything:

```css
/*
	Body
*****************/
#content {} 

/* update image width*/
img {width: 100%; }
```

