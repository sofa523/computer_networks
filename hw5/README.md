## Создание сети
```
docker network create my_network
```

## Запуск контейнера с PostgreSQL
```
docker run -d \
  --name postgres_db \
  --network my_network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=... \
  -e POSTGRES_DB=products_db \
  -p 5432:5432 \
  postgres:13
```

## Сборка Docker-образа приложения
```
docker build -t my_flask_app .
```

## Запуск контейнера приложения
```
docker run -d --name my_app --network my_network -e DB_HOST=postgres_db -p 8080:5000 my_flask_app
```

## Проверка

Или перейдите по ссылкам: 
http://localhost:8080/api/parser?pages_count=1
http://localhost:8080/api/data
http://localhost:8080/api/clear

Или введите:
```
curl "http://localhost:8080/api/parser?pages_count=1"
curl "http://localhost:8080/api/data"
```

## Пример вывода

```
[{"id": 1, "name": "Mooer MSC20 Pro Amber Brown", "price": "27990.00", "article": "98752", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc20_pro_amber_brown"}, {"id": 2, "name": "Omni S12-ST BL", "price": "16990.00", "article": "97534", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s12_st_bl"}, {"id": 3, "name": "Omni S12-ST WH", "price": "16990.00", "article": "A0606", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s12_st_wh"}, {"id": 4, "name": "Omni S12-ST BK", "price": "16990.00", "article": "A0605", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s12_st_bk"}, {"id": 5, "name": "Mooer MSC10 Pro Black", "price": "18990.00", "article": "98644", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_black"}, {"id": 6, "name": "Mooer MSC10 Pro Sunburst", "price": "18990.00", "article": "98647", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_sunburst"}, {"id": 7, "name": "Mooer MSC20 Pro Black Burst", "price": "27990.00", "article": "98750", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc20_pro_black_burst"}, {"id": 8, "name": "Mooer MSC20 Pro Ocean Blue", "price": "27990.00", "article": "98749", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc20_pro_ocean_blue"}, {"id": 9, "name": "Mooer MSC10 Pro C Black", "price": "18990.00", "article": "98686", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_c_black"}, {"id": 10, "name": "Mooer MSC10 Pro Daphne Blue", "price": "18990.00", "article": "98685", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_daphne_blue"}, {"id": 11, "name": "Mooer MSC12 Pro Iron Silver", "price": "21990.00", "article": "99275", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc12_pro_iron_silver"}, {"id": 12, "name": "Mooer MSC11 Pro Black", "price": "21990.00", "article": "99274", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc11_pro_black"}, {"id": 13, "name": "Mooer MSC11 Pro Polar White", "price": "21990.00", "article": "99273", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc11_pro_polar_white"}, {"id": 14, "name": "Omni JM-40FM BB", "price": "24490.00", "article": "97540", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_jm_40fm_bb"}, {"id": 15, "name": "Omni JM-20 BK", "price": "21990.00", "article": "97535", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_jm_20_bk"}, {"id": 16, "name": "Omni S10-ST WH", "price": "12990.00", "article": "97533", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s10_st_wh"}, {"id": 17, "name": "Omni S10-ST BK", "price": "12990.00", "article": "97532", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s10_st_bk"}, {"id": 18, "name": "Cort X100-OPBC", "price": "17990.00", "article": "94080", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/cort_x100_opbc"}, {"id": 19, "name": "Cort X100-OPBK", "price": "17990.00", "article": "99133", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/cort_x100_opbk"}, {"id": 20, "name": "Cort X100-OPBB", "price": "17990.00", "article": "99132", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/cort_x100_opbb"}, {"id": 21, "name": "Sire L3 P90 TVY", "price": "44990.00", "article": "97077", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/sire_l3_p90_tvy"}]
```