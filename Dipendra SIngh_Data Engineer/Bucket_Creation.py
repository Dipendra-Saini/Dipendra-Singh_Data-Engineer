"""
In this file, I have created the connection to my aws S3 bucket
Then i have uploaded my csv file to s3 bucket
"""

import boto
import boto3
import pandas as pd
from io import StringIO
import boto.s3.connection
from Perform_logging import log


class Bucket:
    """
    A class representing a bucket in Amazon S3.

    Attributes:
    -----------
    file_name : str
        The name of the CSV file to be uploaded to S3 bucket.
    access_key : str
        The AWS access key.
    secret_key : str
        The AWS secret access key.

    Methods:
    --------
    create_connection_bucket() -> None:
        Creates a connection to an S3 bucket using the given access and secret keys.
    upload_file_to_s3bucket() -> None:
        Uploads the CSV file to the S3 bucket.
    run() -> None:
        Runs the complete process of creating the connection to the S3 bucket and uploading the CSV file to the S3 bucket.
    """

    def __init__(self, file_name: str, access_key: str, secret_key: str) -> None:
        """
        Constructs a Bucket object.

        Parameters:
        -----------
        file_name : str
            The name of the CSV file to be uploaded to S3 bucket.
        access_key : str
            The AWS access key.
        secret_key : str
            The AWS secret access key.
        """

        self.CsvFileName = file_name
        self.__access_key = access_key
        self.__secret_key = secret_key

    def create_connection_bucket(self) -> None:
        """
        Creates a connection to an S3 bucket using the given access and secret keys.
        """
        log.info('Creating connection to S3 bucket...')
        conn = boto.connect_s3(
            aws_access_key_id=self.__access_key,
            aws_secret_access_key=self.__secret_key)

        buck1 = conn.create_bucket('my_data')
        log.info('Connection created successfully!')

    def upload_file_to_s3bucket(self) -> None:
        """
        Uploads the CSV file to the S3 bucket.
        """
        log.info('Uploading file to S3 bucket...')
        my_file = pd.read_csv(self.CsvFileName)

        s3 = boto3.client('s3',
                          aws_access_key_id=self.__access_key,
                          aws_secret_access_key=self.__secret_key)
        csv_buff = StringIO()
        my_file.to_csv(csv_buff, header=True, index=False)
        csv_buff.seek(0)
        s3.put_object(Bucket='Fininstrm_data',
                      Body=csv_buff.getvalue(), key='fininstrm_data')
        log.info('File uploaded successfully!')

    def run(self) -> None:
        """
        Runs the complete process of creating the connection to the S3 bucket and uploading the CSV file to the S3 bucket.
        """

        log.info(
            'Starting process to create connection to S3 bucket and upload file...')
        self.create_connection_bucket()
        self.upload_file_to_s3bucket()
        log.info('Process completed successfully!')
