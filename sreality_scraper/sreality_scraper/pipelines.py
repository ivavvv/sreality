import psycopg2
from itemadapter import ItemAdapter

class PostgresPipeline:
    def open_spider(self, spider):
        hostname = 'db'
        username = 'postgres' 
        password = '12345' 
        database = 'srealitydb'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

        # Clear the table
        self.cur.execute("TRUNCATE TABLE sreality_data;")
        self.connection.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.cur.execute("insert into sreality_data(name, images) values(%s,%s)", (adapter['name'], adapter['images']))
        self.connection.commit()
        return item

