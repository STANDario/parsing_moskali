"""
scrapy startproject statictic_war      - Так пишемо в консолі, тоді стартує scrapy. Робить папку statictic_war

scrapy genspider get_urls index.minfin.com.ua   - Створюємо павука з назвою get_urls, після цього пишемо доменне ім'я сайту. Писати в консолі всередині папки statictic_war

scrapy crawl get_urls      - Запускає нашого павука get_urls

scrapy crawl get_urls -o links.json      - зберігає в links.json результат. Якщо запускаю повторно, він туди дописує.

scrapy crawl get_urls -O links.json      - зберігає в links.json результат. Якщо такий файл вже є, він його перезапише
"""

"""
Щоб дані перехоплювались треба в settings.py розкоментувати:
ITEM_PIPELINES = {
   "statistic_war.pipelines.StatisticWarPipeline": 300,
}

Далі записуємо в pipelines.py певну дію з цими даними

"""