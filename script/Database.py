import cx_Oracle
import pandas as pd
import sys


class Tfrdb(object):

    def __init__(self, ioid):

        self.ioid = ioid
        self.conn = None

    def connect_tfr(self):

        self.conn = cx_Oracle.connect("TFR_REP/welcome@10.29.20.76/tfrdb")
        query_summary_mv = "select * from TFR_REP.SUMMARY_MV where IO_ID = {0}".format(self.ioid)
        query_read = pd.read_sql(query_summary_mv, self.conn)
        print(query_read)

    def main(self):
        self.connect_tfr()


if __name__ == '__main__':
    r = int(sys.argv[1])
    obj = Tfrdb(r)
    obj.main()