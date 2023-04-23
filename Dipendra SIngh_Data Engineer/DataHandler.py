"""
In this file, I have extracted the xml link in zip format
then unzip the link and read the content of xml and
then save the data into the csv format
"""

import zipfile
import requests
import pandas as pd
import urllib.request
import pandas_read_xml as pdx
from Perform_logging import log


class Assessment:
    """
    A class that represents an assessment of fecting data from url and save data to a csv file.
    Attributes:
    -----------
    xml_url : str
        The URL of the XML file containing the data.
    ZipFileName : str
        The name of the ZIP file used to store the downloaded data.
    """

    def __init__(self, url: str) -> None:
        """
        Initializes a new instance of the Assessment class.

        Parameters:
        -----------
        url : str
            The URL of the XML file containing the data on which we want to perform some operations
        """
        self.xml_url = url
        self.ZipFileName = 'master.zip'

    def get_link(self, df: pd.DataFrame) -> str:
        """
        Gets the download link for the DLTINS file from the given XML data.

        Parameters:
        -----------
        df : pandas.DataFrame
            A pandas dataframe containing the XML data.

        Returns:
        --------
        str
            The download link where the file type is DLTINS.
        """
        log.info("Getting the link of xml file......")
        data = df['response'][0]
        data['result'].keys()
        size = len(data['result']['doc'])
        for i in range(size):
            val = data['result']['doc'][i]
            link = None
            for item in val['str']:
                if item['@name'] == 'download_link':
                    link = item['#text']

                if item['@name'] == 'file_type' and item['#text'] == 'DLTINS':
                    log.info(
                        "Succesfully got the link where file_type: DLTINS......")
                    return link

    def parse_xml(self, url: str) -> None:
        """
        Parses the XML data at the given URL and downloads the corresponding ZIP file.

        Parameters:
        -----------
        url : str
            The URL of the XML file containing the data on which we want to perform some operations.

        Raises:
        -------
        urllib.error.URLError
            If the URL is invalid or cannot be accessed.
        """
        try:
            log.info("Sending the request to open the link......")
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            log.info("Reading the xml file with encoding utf-8......")
            df = pdx.read_xml(text, encoding='utf-8')
            # Here i have called function inside function to get the link from
            # the xml file.
            link = self.get_link(df)
            log.info("Got the link from xml file")
            r = requests.get(link)
            log.info("Download the link into the zip format......")
            with open(self.ZipFileName, 'wb') as f:
                f.write(r.content)
        except:
            log.error("Request cannot be accessed. Invalid URL!!")

    def extract_zip(self) -> None:
        """
        Extracts the ZIP file containing the  data.
        """
        log.info("Extractin the zip file......")
        with zipfile.ZipFile(self.ZipFileName, 'r') as zip_ref:
            zip_ref.extractall()
        log.info("Sucessfully extracted the zip file")

    def xml_to_CSV(self, data: dict) -> None:
        """
        Converts the extracted xml data to a CSV file.

        Parameters:
        -----------
        data : dict
            A dictionary containing the data in the key value format.

        Raises:
        -------
        KeyError
            If the dictionary does not contain the expected keys.
        """
        # Created all the empty list of all extracted field type
        Id = []
        FullNm = []
        ClssfctnTp = []
        CmmdtyDerivInd = []
        NtnlCcy = []
        Issr = []
        size = len(data['Pyld']['Document']
                   ["FinInstrmRptgRefDataDltaRpt"]["FinInstrm"])
        # Saved the predefined extracted data till FinInstrm to the content variable
        content = data['Pyld']['Document']["FinInstrmRptgRefDataDltaRpt"]["FinInstrm"]
        log.info("Getting the all required attributes......")
        for i in range(size):
            try:
                Id.append(
                    content[i]['TermntdRcrd']['FinInstrmGnlAttrbts']['Id'])
                FullNm.append(
                    content[i]['TermntdRcrd']['FinInstrmGnlAttrbts']['FullNm'])
                ClssfctnTp.append(
                    content[i]['TermntdRcrd']['FinInstrmGnlAttrbts']['ClssfctnTp'])
                CmmdtyDerivInd.append(
                    content[i]['TermntdRcrd']['FinInstrmGnlAttrbts']['CmmdtyDerivInd'])
                NtnlCcy.append(content[i]['TermntdRcrd']
                               ['FinInstrmGnlAttrbts']['NtnlCcy'])
                Issr.append(content[i]['TermntdRcrd']['Issr'])
            except:
                continue
        # Assigning list of values to its title name (to all the field required)
        # Created a data frame of thta
        df = pd.DataFrame({'Id': Id, 'FullNm': FullNm,
                           'ClssfctnTp': ClssfctnTp,
                           'CmmdtyDerivInd': CmmdtyDerivInd,
                           'NtnlCcy': NtnlCcy, 'Issr': Issr})
        df.to_csv('fininstrm_data.csv', index=False)
        log.info("Successfully saved the data to csv")

    def run(self):
        """
        Downloads and extracts the zip file from the provided XML URL, parses the extracted XML file,
        and saves the relevant data as a CSV file.

        Parameters:
            None

        Returns:
            None
        """
        self.parse_xml(self.xml_url)
        self.extract_zip()

        df = pdx.read_xml('DLTINS_20210117_01of01.xml', encoding='utf-8')
        data = df['BizData'][0]
        self.xml_to_CSV(data)
