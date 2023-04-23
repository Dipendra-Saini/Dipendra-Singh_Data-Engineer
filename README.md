# Data-Engineer-Assignment
<hr>
<h2>This repository contain five file named as:</h2>
<ul>
<li>DataHandler.py</li>
<li>Bucket_Creation.py</li>
<li>Perform_logging.py</li>
<li>Unit_testing.py</li>
<li>main.py</li>
<li>mylog.log</li>
</ul>
<hr>
<h2>Libraries required to complete the project is:</h2>
<ul>
<li>boto</li>
<li>boto3</li>
<li>pandas</li>
<li>request</li>
<li>zipfile</li>
<li>urllib</li>
<li>unittest</li>
<li>logging</li>
<li>os</li>
</ul>
<hr>
<h2>Files includes:</h2>
<h3><li>DataHandler.py</li></h3>
<p>
The script includes a class Assessment that has the following methods:
<ul><li>__init__(self, url: str) : Constructor of the class, that initializes the url of the xml file and the zip file name.</ul></li>
<ul><li>get_link(self, df: pd.DataFrame) -> str: Method that extracts the download link of the xml file.</ul></li>
<ul><li>parse_xml(self, url: str) -> None: Method that parses the xml file at the given url, gets the download link for the DLTINS file, downloads the corresponding ZIP file, and extracts it.</ul></li>
<ul><li>extract_zip(self) -> None: Method that extracts the downloaded ZIP file.</ul></li>
<ul><li>xml_to_CSV(self, data: dict) -> None: Method that converts the extracted xml data to a CSV file.</ul></li>
</p>

<h3><li>Bucket_Creation.py</li></h3>
<p>
This code defines a class Bucket that provides three methods:
<ul><li>create_connection_bucket(): creates a connection to an S3 bucket using AWS access and secret keys.</ul></li>
<ul><li>upload_file_to_s3bucket(): uploads a CSV file to an S3 bucket.</ul></li>
<ul><li>run(): runs the complete process of creating a connection to the S3 bucket and uploading the CSV file to the S3 bucket.</ul></li>
<h4>The Bucket class has the following attributes:</h4>
<ul><li>file_name: the name of the CSV file to be uploaded to S3 bucket.</ul></li>
<ul><li>access_key: the AWS access key.</ul></li>
<ul><li>secret_key: the AWS secret access key.</ul></li>
</p>

<h3><li><b>main.py</b></li></h3>
<p>
<ul><li>It import both the above files and run their run() function simultaneously</ul></li>
</p>

<h3><li>Unit_testing.py</li></h3>
<p>
A class to test the functions in DataHandler.py file
    Methods
    test_download_xml()
        Tests the get_link() function to download XML file.

    test_parse_xml()
        Tests the parse_xml() function to parse XML data.

    test_parse_xml_exist()
        Tests the parse_xml() function to check if the downloaded file exists.

    test_extract_zip()
        Tests the extract_zip() function to check if extracted the XML file exists or not.

    test_xml_to_CSV()
        Tests the xml_to_CSV() function whether the xml file converted to csv and it exists.
</p>


<h3><li>Perform_logging.py</li></h3>
<p>
<ul><li>This code sets up basic configuration for logging in Python and defines the format for the log content that will be saved in a file located at a specific path. It uses the built-in logging module to create a logger object and set its level to debug.</ul></li>
</p>


# Final result of the assignment

<h3>All the unit tests passed that i have methioned in my Unit_testing.py files</h3>

![test_result](https://user-images.githubusercontent.com/84001857/233851418-eea2c45d-c7ea-4cc2-9822-1281583565ff.png)

<h3>This is the final result of csv file that i got from xml file and uploaded the same into the aws S3 bucket as well</h3>

![output](https://user-images.githubusercontent.com/84001857/233851434-e0963395-712c-4df5-b109-71073b6ed281.png)
