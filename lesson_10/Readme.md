            # **Как запустить тесты для формирования отчёта Allure**

1.Убедитесь, что установлены зависимости
В вашем проекте должны быть установлены:

bash
_ _pip install pytest allure-pytest_ _

2.Запустите тесты с генерацией отчёта
Используйте команду:

bash
_ _pytest --alluredir=allure-results_ _
Где:

--alluredir=allure-results — указывает папку, куда сохранятся JSON-файлы с результатами тестов.

3.Проверьте, что отчёт сгенерировался

4.Убедитесь, что в папке allure-results появились файлы:

bash
_ _ls allure-results_ _
(Должны быть файлы вида *.json)

                # **Как просмотреть сформированный отчёт Allure**

**Способ 1:**
Запуск локального сервера (рекомендуется)
bash
_ _allure serve allure-results_ _
Откроется браузер с интерактивным отчётом.

Сервер автоматически запускается на http://localhost:port.

**Способ 2:**
Генерация HTML-отчёта
bash
_ _allure generate allure-results -o allure-report --clean_ _
-o allure-report — папка, куда сохранится HTML-отчёт.

--clean — очищает предыдущий отчёт.

После генерации откройте файл:

bash
_ _allure open allure-report_ _
Или вручную:

bash
_ _start allure-report/index.html_ _

                # **Краткая шпаргалка**

- Запуск тестов _ _pytest --alluredir=allure-results_ _
- Просмотр отчёта _ _allure serve allure-results_ _
- Генерация HTML _ _allure generate allure-results -o allure-report --clean_ _
    - Открыть HTML _ _allure open allure-report_ _
    -
          #**Если отчёт не открывается**
  
- Проверьте, что Allure установлен:

  bash
  _ _allure --version_ _
  -Убедитесь, что папка allure-results не пустая.

-Если Allure не в PATH, используйте полный путь:

bash
_ _~\scoop\apps\allure\current\bin\allure.bat serve allure-results_ _
Теперь вы можете запускать тесты и анализировать отчёты в удобном интерфейсе Allure! 

     