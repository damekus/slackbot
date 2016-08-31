try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
config = {
	'description' : 'My Project',
	'author' : 'Damian',
	'url' : 'http://worldinashell.wordpress.com',
	'download_url' : 'https://github.com/damekus/Project1',
	'author_email':'damiansfo@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages',['NAME'],
	'scripts':[],
	'name':'projectname'
}

setup(**config)