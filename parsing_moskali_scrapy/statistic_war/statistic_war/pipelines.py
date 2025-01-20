# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StatisticWarPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)      # Будь-який item який він розпарсить попадає сюди
        if "date" in adapter.keys():
            print("------------ SAVE TO MONGODB ------------")   # Імітуємо збереження до mongodb
            print(adapter)
        return item
