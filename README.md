# Scraping_Macro_ABC-store

## General Information:
These scripts are written to automate a mundate job of manually extract product's information from a wholesaler e-commercial site and then manually reformat and transform the data in excel before uploading it to Point-Of-Sale software for inventory tracking.

These scripts are written with selenium and scrapy libraries on Python to perform website scraping for product's information. The scraped data (UPC, Product Name, Product Number, Cost, Purchased Quantity, Product Image) are then exported to excel file where a Excel VBA script is used to load and transform these data into a proper format that can be uploaded into the POS sytem

There are 2 steps in this process
	1.	Extracting Product's infos with Scrapy or Selenium (Scrapy is faster, however Selenium is used on site with javascript)
	2. 	Exported data from step 1 are stored in excel files. Excel VBA script is then used to transform them into a format that can be uploaded to POS software
  
  ### Step 1: How to run scraping scripts:
 ```
  Scrapy:
		Install Scrapy library
		scrapy scrawl spider_name -o filename.csv
 ```
  Spider located in the spider folder (example: for PIC, spider name is login)
	
  ```
  Selenium:
		Install Selenium library
		Install webdriver - ChromeDriver
		Run the script with Python IDE or Jupyter Notebook
   ```
### Step 2: Run VBA Macro to transform the data
	
  After step 1, an excel file should be generated with all product infos, scarped from the wholeseller's webpage. These data then can be pasted into a macro enabled excel, where   a macro will load and transform them into format provided by the POS software. A final touch is done manually by the user to verify and categorize the produdct type    accordingly (Houseware, Kitch, Electronics,etc.). Once it is done, the complete excel file can be upload to the POS software for inventory / order management.

## Demonstration:
You can find a detailed comments and demonstration run in the Today_Selenium Scraper folder

## NOTE:
1. You wont be able to run the script without an account (these are B2B site, so account is only provided to partner business). However, I hope these python files and Macro scripts would be helpful to create your own scripts.

2. As much as I want to make the entire process automatically, human intervention is requried to categorize the product types. ML classification model can be used here to automate this process. However, the cost-benefit is not justified to build it for a small scale business.

3. It takes an average of 5 minutes to do complete the whole process with the scripts, compare to an average of 20 minutes to do it manually.

## Contact
Contact me @ haotruong24@hotmail.com if you have any questions
