from DataHandler import Assessment
from Bucket_Creation import Bucket
if __name__ == "__main__":
    """
    Downloading zip from xml and creating a csv file with provided link
    """

    url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-01T00:00:00Z+TO+2021-01-31T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
    MyAssessment = Assessment(url)
    MyAssessment.run()

    """
    Uploading the CSV file to S3 bucket
    """
    access_key = "XXXXXXXXXXXXXXXXXXXXX"
    secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    MyBucket = Bucket("fininstrm_data.csv", access_key, secret_key)
    MyBucket.run()
