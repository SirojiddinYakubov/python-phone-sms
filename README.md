![banner](https://i.postimg.cc/brrfqW8k/banner.jpg "banner")



[![Downloads](https://img.shields.io/badge/telegram-yakubovdeveloper-green)](https://t.me/yakubovdeveloper)
[![Downloads](https://img.shields.io/badge/author-Sirojiddin_Yakubov-green)](https://t.me/Sirojiddin_Yakubov)
<div align="center">
<h1>Интеграция системы (Eskiz, Playmobile, Infobip) отправить sms в Python</h1>
</div>

Этот репозиторий содержит готовые коды того, как можно отправлять СМС операторам мобильной связи. 

Эти коды содержат интеграции следующих сервисов:
- Eskiz - Успей забронировать свое место в Интернете. [Официальный сайт](https://eskiz.uz/)
- Playmobile - SMS оператор для бизнеса. [Официальный сайт](https://playmobile.uz/)
- Infobip - Подключайтесь по всему миру с помощью ведущего SMS-сервиса. [Официальный сайт](https://www.infobip.com/sms)


## Необходимые пакеты
[Requests](https://requests.readthedocs.io/) - это элегантная и простая HTTP-библиотека для Python, созданная для людей.

## Установка
Клонируйте проект с github
```console
git clone https://github.com/SirojiddinYakubov/python-phone-sms.git
```

Установите все пакеты, необходимые для работы sms-сервисов
```bash
pip install -r req.txt
```

## Интеграция [Eskiz.uz](https://eskiz.uz/)

Чтобы начать интеграцию через службу Eskiz, вам понадобятся `ESKIZ_EMAIL` и `ESKIZ_PASSWORD`. Вы можете получить эту информацию, после заключения [контракта с компанией](https://eskiz.uz/reseller)

После того, как вы получили необходимые ключи, вы должны записать их, создав файл `.env` или просто скопируйте готовый шаблон `env.md`
```console
cp env.md .env
```

Заполните `ESKIZ_EMAIL` и `ESKIZ_PASSWORD`

Перейдите к файлу `eskiz.py` и введите свой номер телефона в переменную `phone`

### Приступаем к отправке первого СМС
```console
python eskiz.py
```

Для получения дополнительной информации перейдите по [этой ссылке](https://documenter.getpostman.com/view/663428/RzfmES4z?version=latest)

### Полезные ссылки

- Официальный сайт - https://eskiz.uz
- Персоналный кабинет - https://my.eskiz.uz/dashboard
- Проверит баланс - https://my.eskiz.uz/sms
- Руководство разработчика - https://documenter.getpostman.com/view/663428/RzfmES4z?version=latest

## Интеграция [Playmobile.uz](https://playmobile.uz/)

Чтобы начать интеграцию через службу Playmobile, вам понадобятся `PLAYMOBILE_USERNAME`, `PLAYMOBILE_PASSWORD` и `PLAYMOBILE_ENDPOINT`. Вы можете получить эту информацию, после заключения [контракта с компанией](https://playmobile.uz/contacts/)

После того, как вы получили необходимые ключи, вы должны записать их, создав файл `.env` или просто скопируйте готовый шаблон `env.md`
```console
cp env.md .env
```

Заполните `PLAYMOBILE_USERNAME`, `PLAYMOBILE_PASSWORD` и `PLAYMOBILE_ENDPOINT`

Перейдите к файлу `playmobile.py` и введите свой номер телефона в переменную `phone`

### Приступаем к отправке первого СМС
```console
python playmobile.py
```

Для получения дополнительной информации перейдите по [этой ссылке](https://playmobile.uz/instruction/)

### Полезные ссылки

- Официальный сайт - https://playmobile.uz
- Руководство разработчика - https://playmobile.uz/instruction/
- SMS-Broker API - https://playmobile.uz/wp-content/uploads/2022/08/http.pdf

## Интеграция [Infobip.com](https://www.infobip.com/)

Чтобы начать интеграцию через службу Infobip, вам понадобятся `INFOBIP_API_KEY` и `INFOBIP_BASE_URL`. Вы можете получить эту информацию переходя по [этой ссылке](https://portal.infobip.com/homepage/)

<img src="https://i.ibb.co/MgxrXXc/infobip2.png" width="70%">

После того, как вы получили необходимые ключи, вы должны записать их, создав файл `.env` или просто скопируйте готовый шаблон `env.md`
```console
cp env.md .env
```

Заполните `INFOBIP_API_KEY` и `INFOBIP_BASE_URL`

Перейдите к файлу `infobip.py` и введите свой номер телефона в переменную `RECIPIENT`

### Приступаем к отправке первого СМС
```console
python infobip.py
```

Для получения дополнительной информации перейдите по [этой ссылке](https://www.infobip.com/docs/api)

### Полезные ссылки

- Официальный сайт - https://www.infobip.com
- Персоналный кабинет - https://portal.infobip.com/homepage
- Руководство разработчика - https://www.infobip.com/docs/api
- Cписок отправленных SMS - https://portal.infobip.com/dev/api-transaction-log
- Проверить API через браузер - https://tryapi.infobip.com/send-sms-python-lib

## Примеры

Для более подробной информации вы можете посмотреть это видео

[![Watch the video](https://img.youtube.com/vi/dMlRWSS1Y3s/maxresdefault.jpg)](https://www.youtube.com/watch?v=dMlRWSS1Y3s)

<h3>Спасибо за внимание!</h3>

## Автор
[Sirojiddin Yakubov](https://t.me/Sirojiddin_Yakubov)

## Социальные сети
<div align="center">
  Подпишитесь на нас, чтобы получать больше новостей о веб-программировании: <br>
  <a href="https://www.youtube.com/@yakubovdeveloper">YouTube</a>
  <span> | </span>
  <a href="https://www.instagram.com/yakubovdeveloper">Instagram</a>
  <span> | </span>
  <a href="https://www.facebook.com/yakubovdeveloper">Facebook</a>
  <span> | </span>
  <a href="https://www.tiktok.com/@yakubovdeveloper">TikTok</a>
  <span> | </span>
  <a href="https://t.me/yakubovdeveloper">Telegram</a>
</div>