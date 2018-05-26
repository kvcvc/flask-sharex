# flask-sharex 
<a href="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square&colorB=2196F3" alt="License"></a> 
<a href="https://www.python.org/downloads/release/python-365/"><img src="https://img.shields.io/badge/Python-v3.6.5-brightgreen.svg?style=flat-square&colorB=FFEB3B" alt="Python"></a> 
<a href="https://github.com/markylon/flask-sharex/commits/master"><img src="https://img.shields.io/github/last-commit/markylon/flask-sharex.svg?style=flat-square&colorB=CDDC39" alt="Commit"></a>

---

`flask-sharex` is a flask image destination server to upload screenshots to from the ShareX client. The project was made in [Python](https://www.python.org/), with the [Flask](http://flask.pocoo.org/) microframework.

## Configuration
In server.py, configure `storage_folder` and `secret_key` variables to your desired vaules.

## Setting up
1. Under destination settings, head over to custom uploaders and import the config that is included within the repository. 
2. Set the secret_key under arguments to the value of the secret_key variable in server.py.
3. Ready to go!

## License

`flask-sharex` is under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0).
