# hr-contact
Convert "Danh sách nhân sự" --> Google Contact


## Usage


### Setup
```
git clone https://github.com/greenglobal/hr-contact.git
cd  hr-contact
poetry install
```

### Download "Danh sách nhân sự"

Go to Google Sheet, find "Danh sách nhân sự", download as CSV file into "./hr-data.csv".

### Run script


```
poetry run python3 convert.py
```

Result will be saved into "./output.csv"

### Import contact

Import "./output.csv" into your Google Contact. Then fix the  duplicate if any.
