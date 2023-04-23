"""
Here i have performed unit test of the functions in DataHandler.py file
"""

import os
import zipfile
import requests
import unittest
import pandas as pd
import urllib.request
import pandas_read_xml as pdx
from Perform_logging import log
from DataHandler import Assessment


url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-01T00:00:00Z+TO+2021-01-31T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"


class TestXMLToCSV(unittest.TestCase):
    """
    A class to perform unit test of the functions in DataHandler.py file

    ...

    Methods
    -------
    test_download_xml()
        Tests the get_link() function to download XML file.

    test_parse_xml()
        Tests the parse_xml() function to parse XML data.

    test_parse_xml_exist()
        Tests the parse_xml() function to check if the downloaded file exists.

    test_extract_zip()
        Tests the extract_zip() function to extract the XML file from the downloaded ZIP file.

    test_xml_to_CSV()
        Tests the xml_to_CSV() function to convert XML data to CSV.
    """

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assessment = Assessment(url)
        self.link = self.assessment.parse_xml(url)
        self.assessment.extract_zip()
        df = pdx.read_xml('DLTINS_20210117_01of01.xml', encoding='utf-8')
        data = df['BizData'][0]
        self.assessment.xml_to_CSV(data)

    def test_get_link(self) -> None:
        """
        Tests the whether link able to fetch from xml or not.

        AssertTrue will be testing type of response is string link or not, indicating a successful request.

        Parameters:
            None

        Returns:
            None
        """
        log.info("Starting download xml test")

        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        df = pdx.read_xml(text, encoding='utf-8')

        self.response = self.assessment.get_link(df)
        self.assertTrue(type(self.response), str)
        log.info("Successfully got the xml link")

    def test_parse_xml_exist(self) -> None:
        """
        Test the parse_xml() function to check if the downloaded file exists.
        """
        log.info('Starting parse_xml test')
        self.assertTrue(os.path.exists("master.zip"))
        log.info('Zip file downloaded successfully')

    def test_extract_zip(self) -> None:
        """
        Test the extract_zip() function to extract the XML file from the downloaded ZIP file.
        """
        log.info('Starting extract_zip test')
        self.assertTrue(os.path.exists('DLTINS_20210117_01of01.xml'))
        log.info('Zip file extracted successfully')

    def test_xml_to_CSV(self) -> None:
        """
        Test the xml_to_CSV() function to convert XML data to CSV.
        whether the converted csv file exists in location or not.
        """
        log.info('Starting xml_to_CSV test')
        # self.assessment.parse_xml(self.xml_url)
        # self.assessment.extract_zip()
        # df = pd.read_xml('DLTINS_20210117_01of01.xml', encoding='utf-8')
        # data = df['BizData'][0]
        # self.assessment.xml_to_CSV(data)
        self.assertTrue(os.path.exists('fininstrm_data.csv'))
        log.info('CSV file created successfully')


if __name__ == '__main__':
    unittest.main()
