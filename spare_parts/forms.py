from wtforms import Form, StringField, TextAreaField, IntegerField


class SparePartForm(Form):
    title = StringField('Заголовок')
    price = IntegerField('Цена')
    amount = IntegerField('Количество')
    description = TextAreaField('Описание')
