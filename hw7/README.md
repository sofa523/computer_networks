## Устанавливаем GeoIP2 модуль
```
sudo apt install libnginx-mod-http-geoip2
```

## Скачиваем базу GeoIP2 Country
```
sudo mkdir -p /etc/nginx/geoip
cd /etc/nginx/geoip
sudo wget https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb
```

## Создание конфигурации (находится в nginx.conf)
```
sudo nano /etc/nginx/sites-available/quotes-proxy
```

##
```
sudo nano /etc/nginx/nginx.conf
```
Содержимое:
```
http {
    # ... другие настройки ...
    geoip2 /etc/nginx/geoip/GeoLite2-Country.mmdb{
        auto_reload 5m;
        $geoip2_data_country_code country iso_code;
    }

    map $geoip2_data_country_code $is_ru{
        default 0;
        RU 1;
    }

    set_real_ip_from 127.0.0.1;
    set_real_ip_from ::1;
    real_ip_header X-Forwarded-For;
    real_ip_recursive on;

    # ... другие настройки ...
}
```

## Проверяем синтаксис
```
sudo nginx -t
```

## Перезагружаем Nginx
```
sudo systemctl reload nginx
```

## Проверка

```
curl -L -H "X-Forwarded-For: 5.255.255.255" http://localhost/api/data
```

## Пример вывода

```
<!DOCTYPE html>
<html>
<head>
    <title>Доступ ограничен</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Доступ с территории РФ запрещён</h1>
    <p>Извините, данный ресурс недоступен для пользователей из Российской Федерации.</p>
</body>
</html>
```

## Проверка

```
curl -H "X-Forwarded-For: 8.8.8.8" http://localhost/api/data
```

## Пример вывода

```
[{"id": 1, "name": "Mooer MSC20 Pro Amber Brown", "price": "27990.00", "article": "98752", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc20_pro_amber_brown"}, {"id": 2, "name": "Omni S12-ST BL", "price": "16990.00", "article": "97534", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s12_st_bl"}, {"id": 3, "name": "Omni S12-ST WH", "price": "16990.00", "article": "A0606", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s12_st_wh"}, {"id": 4, "name": "Omni S12-ST BK", "price": "16990.00", "article": "A0605", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s12_st_bk"}, {"id": 5, "name": "Mooer MSC10 Pro Black", "price": "18990.00", "article": "98644", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_black"}, {"id": 6, "name": "Mooer MSC10 Pro Sunburst", "price": "18990.00", "article": "98647", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_sunburst"}, {"id": 7, "name": "Mooer MSC20 Pro Black Burst", "price": "27990.00", "article": "98750", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc20_pro_black_burst"}, {"id": 8, "name": "Mooer MSC20 Pro Ocean Blue", "price": "27990.00", "article": "98749", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc20_pro_ocean_blue"}, {"id": 9, "name": "Mooer MSC10 Pro C Black", "price": "18990.00", "article": "98686", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_c_black"}, {"id": 10, "name": "Mooer MSC10 Pro Daphne Blue", "price": "18990.00", "article": "98685", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc10_pro_daphne_blue"}, {"id": 11, "name": "Mooer MSC12 Pro Iron Silver", "price": "21990.00", "article": "99275", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc12_pro_iron_silver"}, {"id": 12, "name": "Mooer MSC11 Pro Black", "price": "21990.00", "article": "99274", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc11_pro_black"}, {"id": 13, "name": "Mooer MSC11 Pro Polar White", "price": "21990.00", "article": "99273", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/mooer_msc11_pro_polar_white"}, {"id": 14, "name": "Omni JM-40FM BB", "price": "24490.00", "article": "97540", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_jm_40fm_bb"}, {"id": 15, "name": "Omni JM-20 BK", "price": "21990.00", "article": "97535", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_jm_20_bk"}, {"id": 16, "name": "Omni S10-ST WH", "price": "12990.00", "article": "97533", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s10_st_wh"}, {"id": 17, "name": "Omni S10-ST BK", "price": "12990.00", "article": "97532", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/omni_s10_st_bk"}, {"id": 18, "name": "Cort X100-OPBC", "price": "17990.00", "article": "94080", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/cort_x100_opbc"}, {"id": 19, "name": "Cort X100-OPBK", "price": "17990.00", "article": "99133", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/cort_x100_opbk"}, {"id": 20, "name": "Cort X100-OPBB", "price": "17990.00", "article": "99132", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/cort_x100_opbb"}, {"id": 21, "name": "Sire L3 P90 TVY", "price": "44990.00", "article": "97077", "availability": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", "link": "https://mirm.ru/catalog/products/sire_l3_p90_tvy"}]
```