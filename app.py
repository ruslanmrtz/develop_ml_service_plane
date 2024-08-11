import streamlit as st
from PIL import Image
import pandas as pd
import pickle


def process_data(df):
    features = ['Leg room service',
                'Baggage handling',
                'On-board service',
                'Age',
                'Checkin service',
                'Type of Travel']

    with open('transformer.pickle', 'rb') as f:
        transformer = pickle.load(f)

    df = pd.DataFrame(transformer.transform(df), columns=features)

    st.write(df)

    return df


def app():
    main_page()
    process_model()


def side_bar():
    st.sidebar.title('Заданные параметры полета')

    type_of_travel = st.sidebar.selectbox("Тип поездки", ("Личная поездка", "Деловая поездка"))

    age = st.sidebar.slider("Возраст клиента", min_value=1, max_value=120,
                            value=25, step=1)

    leg = st.sidebar.slider("Оценка клиентом места в ногах на борту", min_value=1, max_value=40,
                            value=15, step=1)

    baggage = st.sidebar.slider("Оценка клиентом обращения с багажом", min_value=1, max_value=40,
                                value=15, step=1)

    onboard_service = st.sidebar.slider("Оценка клиентом обслуживания на борту", min_value=1, max_value=40,
                                        value=15, step=1)

    сheck_in_service = st.sidebar.slider("Оценка клиентом регистрации на рейс", min_value=1, max_value=40,
                                         value=15, step=1)

    translatetion = {
        "Личная поездка": 0,
        "Деловая поездка": 1,
    }

    data = {
        'Leg room service': leg,
        'Baggage handling': baggage,
        'On-board service': onboard_service,
        'Age': age,
        'Checkin service': сheck_in_service,
        'Type of Travel': translatetion[type_of_travel]
    }

    df = pd.DataFrame(data, index=[0])

    return df


def write_data(df):
    st.header('Данные полета')
    st.write(df)


def write_prediction(df):
    new_df = process_data(df)

    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict_proba(new_df)

    d = {
        True: 'Ура! Клиент доволен',
        False: 'Клиент остался недоволен'
    }

    st.header('Предсказание')
    st.write(d[prediction[0][0] > 0.5])

    st.header('Вероятность предсказания')
    proba = pd.DataFrame(prediction, columns=['Клиент доволен с вероятностью', 'Клиент недоволен с вероятностью'])
    st.write(proba)


def process_model():
    df = side_bar()

    write_data(df)
    write_prediction(df)

def main_page():
    st.title('Классификация удовлетворенности клиентов')
    st.subheader('Определяем, кому из пассажиров понравился полет, а кому – нет.')

    img = Image.open('photos/scale_1200.jfif')
    st.image(img)


if __name__ == '__main__':
    app()