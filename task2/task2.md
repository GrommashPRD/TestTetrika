# Как решал?

Установил `pip install requests beautifulsoup4 lxml`

requests - для выолнения запросов к wiki.
beautifulsoup4 & lxml - для парсинга.

Сделал словарь для хранения счетчиков.
При помощи GET запроса к wiki и каждой нужной нам странице,
залезал в контейнер `<div> "mw-pages"` (если он есть) и по всем `<li>`, 
внутри этого `<div>` дергал по одному элементу.
