class Feeder(object):

    @staticmethod
    def get_data(conn):
        pass

    @classmethod
    def feed(cls, r):
        conn = cls.build_connector()
        data = {}
        if conn:
            data = cls.get_data(conn)
        pipe = r.pipeline()
        for key, value in data.items():
            pipe.set(key, value)
        pipe.execute()
