# EloXL - Elo Ratings Calculator

## Installation

Currenty not set up.

```bash
    python -m pip install EloXL
```

## Configuration

### Module

Module configuration is in `setup.cfg`.

### XLWings

XLWings configuration is in `xlwings.conf`.

## Usage

### Updating Data

- Running this updates all leagues and overwrites the master `fbd.json` file in the root directory.

```bash
    python ./app/data/updater_json.py
```

### Outputs

#### JSON Files

The updater scripts in `./app/data/` write output JSON files to the `./app/json/` directory.

- List of updater scripts:
    - `updater_json.py`: Updates all league data
    - `write_statics.py`: Updates static JSON files that contain information on leagues and teams.
    - `updater.py`: Currently obsolete - contains logic for updating HDF5 tables.

### Excel Integration

#### Python: XLWings

The main script for controlling the xlsm file is `EloXL.py`.

## Development

```bash
    git clone https://github.com/amunger3/EloXL
```
