# Project WOLF

A simple CRUD application that can be used by organizations to measure  
employees' work engagement level.

## Description
Investment in information technologies and systems provides  
real economic value to the firm. This application utilises  
a well-establish scale called: The WOrk-reLated Flow inventory (WOLF),  
where flow is defined as “a short-term peak experience at work”  
characterised by:  
absorption, work enjoyment,  and intrinsic work motivation.
By means of a self-administered questionnaire the response is collected  
from the employees which can be entered through the application  
directly by the respondent, or by the admin. The database can then be  
analysed to measure the flow level in order to suggest the best  
approach to enhance it. Flow at work is directly related to increased  
performance.

## Getting Started

### Dependencies

* Ubuntu
* MySQL
* Jenkins
* Cloud sever
* Python

### Executing program

* Clone GitHub Repository
* Create & activate virtual environment
* Install requirements
* Test
* Deploy

```
git clone https://github.com/WaledSalem/Project812.git
cd Project812
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
pytest tests --cov=application --cov-report term-missing
gunicorn --workers=2 --bind=0.0.0.0:5000 app:app
```

## Authors

Contributors names and contact info

Waled Salem  
[@WaledSalem](https://www.linkedin.com/in/waled-salem-9894261ba)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [Arnold B. Bakker; Professor of Organizational Psychology, Erasmus University](http://www.arnoldbakker.com/flow.php)
