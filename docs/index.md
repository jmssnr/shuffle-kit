<figure markdown>
  ![Image title](https://raw.githubusercontent.com/jmssnr/shuffle-kit/main/docs/logos/shuffle-kit-logo-small.png)
</figure>

**shuffle-kit** is a Python package for modelling and analyzing playing card shuffles.

It offers realistic models of commonly used playing card shuffles (e.g., riffle shuffle or strip cuts) that can be composed into complex shuffle sequences such as the well-known _riffle, riffle, strip, riffle, cut_ sequence.

Several utility functions are provided to make it easy to answer questions such as:

- What is the probability of finding a certain card at a certain position after a shuffle?
- Is there a bias in a particular shuffle sequence?
- Given two shuffles, which one is more thorough?

and much more.

## Installation

### Requirements

shuffle-kit requires Python 3.11+.

To check if Python and pip are already installed on your machine you can run:

```
python --version
pip --version
```

### Installing into an existing Python environment

To install the latest stable version in your current Python environment, run:

```
pip install shuffl
```

### Installing using Poetry

To install shuffle-kit into an existing [Poetry](https://python-poetry.org/) project, run:

```
poetry add shuffl
```