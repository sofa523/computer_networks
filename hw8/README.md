## Устанавливаем ngrok:

```
# Скачиваем архив
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip

# Расповываем архив
unzip ngrok-stable-linux-amd64.zip

# Перемещаем ngrok в /usr/local/bin/
sudo mv ngrok /usr/local/bin/

# Удаляем архив
rm ngrok-stable-linux-amd64.zip

#  Проверяем, что всё установилось
ngrok version
```

## Регистрируемся на ngrok.com 

## Добавляем токен аутентификации в конфигурационный файл ngrok.yml
```
ngrok config add-authtoken <токен>
```

## Разворачиваем свое приложение онлайн
```
ngrok http 80
```

## Проверка
Для проверки необходимо перейти по ссылке: https://willpower-unknown-unmolded.ngrok-free.dev/api/data