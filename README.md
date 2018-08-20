<h4 align=center>Maya Test</h4> 
<p align=center><img src=https://img.shields.io/badge/-2013sp1-green.svg> <img src=https://img.shields.io/badge/-2013sp2-green.svg> <img src=https://img.shields.io/badge/-2014sp1-green.svg> <img src=https://img.shields.io/badge/-2014sp2-green.svg> <img src=https://img.shields.io/badge/-2014sp3-green.svg> <img src=https://img.shields.io/badge/-2014sp4-green.svg> <img src=https://img.shields.io/badge/-2015sp1-green.svg><br>  <img src=https://img.shields.io/badge/-2015sp2-green.svg> <img src=https://img.shields.io/badge/-2015sp3-green.svg> <img src=https://img.shields.io/badge/-2015sp4-green.svg> <img src=https://img.shields.io/badge/-2015sp5-green.svg> <img src=https://img.shields.io/badge/-2015sp6-green.svg> <img src=https://img.shields.io/badge/-2016sp1-green.svg> <img src=https://img.shields.io/badge/-2017-green.svg> <img src=https://img.shields.io/badge/-2018-green.svg> 
</p>

<p align=center><i>Run your Python script, in every version of Maya.</i></p>

<br>

### Usecases

Use this project when you want to know whether, in each version of Maya..

- [Is this workaround consistent?](https://github.com/mottosso/maya-test/pull/1)
- [Does this bug occur?](https://github.com/mottosso/maya-test/pull/1)
- [What is the result of `cmds.about(version=True)`?](https://github.com/mottosso/maya-test/pull/2)

### Usage

The goal of this project is comparing the response of a single Python script in all current versions of Maya.

1. [Edit `run.py`](https://github.com/mottosso/maya-test/edit/master/run.py)
2. See results [here](https://travis-ci.org/mottosso/maya-test)

#### Test with Nose

Use the nose testing framework for a more complete test coverage.

```python
def test_case1():
	assert True

def test_case2():
	assert False
```

1. [Edit `.travis.yml`](https://github.com/mottosso/maya-test/edit/master/.travis.yml)
2. Replace `mottosso/maya:${VERSION} run.py`<br>
   with `mottosso/maya:${VERSION} -m nose.__main__ --verbose run.py`

#### Speed up testing

Running the test in every version of Maya takes >30 mins. You can iterate faster by removing versions you aren't interested in.

```yml
matrix:
  include:
  # - env:
  #   - VERSION=2013sp1
  # - env:
  #   - VERSION=2013sp2
  - env:
    - VERSION=2014sp1
  - env:
    - VERSION=2014sp2
```

1. [Edit `.travis.yml`](https://github.com/mottosso/maya-test/edit/master/.travis.yml)
2. Remove versions
