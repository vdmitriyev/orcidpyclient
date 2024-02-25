## About

A simple wrapper around the orcid.org API. Ready to run examples can be found in the ```examples``` folder.

## Installation

### Using pip

Install latest relased version
```
pip install -i https://test.pypi.org/simple/ orcidpyclient
```

Install latest version from source code
```
pip install git+https://github.com/vdmitriyev/orcidpyclient.git
```

### Manual

* Download from the [GitHub](https://github.com/vdmitriyev/orcidpyclient/archive/master.zip) latest version
* Unzip archive
* Create *virtualenv* (```scripts/cmdInitiateEnv.bat```)
* Activate *virtualenv* (```scripts/cmdStartEnv.bat```)
* Run examples

## Documentation

Documentation is available [here](https://vdmitriyev.github.io/orcidpyclient/)

## Examples

#### Ready to Run Examples

* Examples could be found in the folder [examples](examples)

## Development

* Create virtualenv using ```scripts/cmdInitiateEnv.bat``` and activate it
* Star VS Code
```
code .
```
* Run tests -> pytest
```
cd tests
pytest
```
* Run tests -> tox
```
tox
tox -e py310
```

## License 

MIT 

## Credits

* Created based on the cloned repository https://github.com/scholrly/orcid-python lead by [Matt Luongo](https://github.com/mhluongo) from [Scholrly](https://github.com/scholrly/)
