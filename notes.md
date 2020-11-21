# Notes

## Issues with `psycopg2`

Some OS's will play nice with psycopg2. Others will not, see https://git.generalassemb.ly/ga-wdi-boston/django-relationships/issues/8 and discussion on installfest, linked inside issue.

### Solutions (for now):

#### Use an Install Flag

`PIP_NO_BINARY=psycopg2 pipenv install`

#### Install `psycopg2-binary` instead

This isn't great, `psycopg2-binary` is only for "toy projects" per the documentation.

Remove the line with `psycopg2` from the Pipfile, and run `pipenv install psycopg2-binary`.
