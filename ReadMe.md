# Streamlit Demo
Этот проект демонстрирует, как представить решение машинного обучения в виде веб-приложения с использованием платформы Streamlit. Данные, используемые в этом репозитории - Данные об удовлетворенности клиентов полетом.

# Files
* `app.py`: streamlit приложение
* `model.pickle`: обученная модель
* `model_for_app.ipynb`: jupyter-notebook с обучением модели с помощью Random Forest classifier model
* `requirements.txt`: файл зависимостей
* `transformers.pickle`: обученный обработчик входных данных

# Run Demo Locally
Для прямого запуска streamlit локально в корневой папке репозитория следующим образом:
```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```

Откройте http://localhost:8501, чтобы увидеть приложение.
#  Streamlit Cloud Deployment
1. Поместите ваше приложение на GitHub (как этот репозиторий).
Убедитесь, что оно находится в публичной папке и что у вас есть файл «requirements.txt».

2. Зарегестрируйтесь в Streamlit Cloud
Зарегистрируйтесь в share.streamlit.io с вашим имейлом GitHub, вам нужно иметь доступ к сервису Streamlit Cloud.

3. Развертывайте и делитесь!
Нажмите "New app", затем выберите репозиторий, ветку и путь к файлу, выберите версию Python (3.11 для этой демонстрации) и нажмите "Deploy", тогда вы сможете увидеть ваше приложение.