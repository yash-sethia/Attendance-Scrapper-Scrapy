<h1>ATTENDANCE SCRAPPER USING SCRAPY</h1>

This is the source code for a Web Crawler implemented through the python library 'Scrapy'. It scrapes the attendance records of a student of BMIET College, IPU and calculates the attendance percentage.


In order to run the spider, clone this repository on your system and open it in Pycharm (or any other IDE where you have installed scrapy and can form an virtual environment. Open the file "Spidey.py" and type "scrapy crawl spidyy" in the terminal if you just want to run the spider. (NOTE : I have erased the username and password for obvious reasons) It will automatically scrape the data and create a file in the same Directory as "final.csv"


The Calculator.py uses basic operations of Pandas library on the data it read from a file "final.csv" after calling the web crawler "spidyy" written in the file "spidey.py".
NOTE: Write the Location of the file final.csv in the calculator.py and the file pipelines.py
