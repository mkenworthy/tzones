# tzones

A Python script to print out local times in user-defined cities around
the world, to help me schedule meetings.
A local copy of timezones for all large world cities is included
(database copied from http://www.geonames.org/).

## Getting Started

To use, edit the script `tzones.py` and add the name of the cities you
want the local times for in the order you want to see them. They are
stored in `cities`.

Example usage and output:

```
git clone https://github.com/mkenworthy/tzones.git
cd tzones
python tzones.py

Current time in Leiden is 2018-01-21 12:51 CET+0100

Current time in Phoenix is 2018-01-21 04:51 MST-0700

Current time in Baltimore is 2018-01-21 06:51 EST-0500

Current time in Louisville is 2018-01-21 06:51 EST-0500
```

### Prerequisites

It uses `astropy` for reading and parsing the tables, and `pytz` for the
timezone calculations.

If multiple cities are found (e.g. Louisville has 2 hits) then use the
`geoid` code which will be displayed and use that instead.

## License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

Inspired by code from https://stackoverflow.com/questions/16505501/get-timezone-from-city-in-python-django
 by user https://stackoverflow.com/users/4279/jfs

