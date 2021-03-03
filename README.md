# Spanish Person Name Generator
This script generate a 10k list of random names extracted from the gazeteers compiled by the Instituto Nacional de Estadística.

Given a list of male and female names, creates random names composed of:
- name + first name + second name

where each of them can be composed of one or more words.

## Usage
It expects a folder called 'gazeteers' with three files within it:
- female_names.txt
- male_names.txt
- surnames.txt

```sh
python3 generate_random_names.py 
```
