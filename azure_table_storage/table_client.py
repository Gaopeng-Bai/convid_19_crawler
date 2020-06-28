#!/usr/bin/python3
# -*-coding:utf-8 -*-

# Reference:**********************************************
# @Time    : 6/25/2020 5:26 PM
# @Author  : Gaopeng.Bai
# @File    : table_client.py
# @User    : gaope
# @Software: PyCharm
# @Description: 
# Reference:**********************************************
# Instantiate a BlobServiceClient using a connection string
from azure.cosmosdb.table import TableService


class azure_table:
    def __init__(self, table_name='HemoniDataTable'):
        connection_string = "DefaultEndpointsProtocol=https;AccountName=storageklsbxnntmyn76;AccountKey=6QPT2nKpoY9S229wh5NwWa1TgQRquROR+uNP/T5ldIPSxBavZUsoGyZhtmA+zR3v2YhDGsPZGQKztmP2nWKLSA==;EndpointSuffix=core.windows.net"

        self.table_client = TableService(connection_string=connection_string)
        self.table_name = table_name
        if self.table_client.exists(table_name):
            pass
        else:
            self.table_client.create_table(table_name=table_name)

    def delete_table(self):
        self.table_client.delete_table(table_name=self.table_name)

    def insert_entity(self, entity):
        """
        When inserting an entity into a table, you must specify values for the
        PartitionKey and RowKey system properties. Together, these properties
        form the primary key and must be unique within the table. Both the
        PartitionKey and RowKey values must be string values; each key value may
        be up to 64 KB in size. If you are using an integer value for the key
        value, you should convert the integer to a fixed-width string, because
        they are canonically sorted. For example, you should convert the value
        1 to 0000001 to ensure proper sorting.
        :param entity:The entity to insert. Could be a dict or an entity object.
            Must contain a PartitionKey and a RowKey.
        :return: null
        """
        self.table_client.insert_or_replace_entity(table_name=self.table_name, entity=entity)

    def get_entity(self, partition, row):
        """
        Get an entity from the specified table. Throws if the entity does not exist.
        :param partition:  The PartitionKey of the entity.
        :param row: The RowKey of the entity.
        :return:
        """
        return self.table_client.get_entity(self.table_name, partition_key=partition, row_key=row)


if __name__ == '__main__':
    a = azure_table()
