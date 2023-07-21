from django import template
from paper.models import *

register = template.Library()  # экземпляр класса через который происходит регистрация всех шаблонных тегов

base_template_context = {

    # base.html
    'title': 'WWB - Информационный портал.',

    # header/header.html
    'main_header': 'World Wide Blog - Информационный портал',
    'main_about': 'Выполнил студент группы БВТ2252 Медведев Т.Ф',
    'main_button': 'Открыть главное меню',

    # canvas_menu_modal.html
    'menu_modal_title': 'Категория',  # title modal window
    'menu_modal_button': 'Закрыть',  # button for close modal window

    # canvas_menu.html
    'menu_title': 'Главное меню',
    'menu_button_home': 'Перейти на главную',
    'menu_button_modal': 'Поиск статей по категориям',
    'menu_button_logout': 'Выход',
    'menu_button_addpage': 'Добавить статью',
    'main_register': "Для продолжения вам необходимо пройти авторизацию",
    'main_register_button': 'Регистрация',
    'main_login_button': 'Вход',
}

# routes/...
# show_content.html
routes_show_content = {
    'index_open_state': 'Читать полностью'
}

routes_show_post = {
    'index_home_state': 'Вернуться на главную',
    'index_publish': 'Статья была снята из публикации по запросу администратора',
    'index_publish_none': 'Статей пока что нет ^_^'
}

routes_addpage = {
    'index_addpage_header': 'Добавить статью',
    'index_addpage_button': 'Добавить'
}

routes_login = {
    'index_login_header': 'Авторизация',
    'index_login_button': 'Войти'
}

routes_register = {
    'index_register_header': 'Регистрация',
    'index_register_button': 'Отправить'
}

base_template_context.update(routes_show_content)
base_template_context.update(routes_show_post)
base_template_context.update(routes_addpage)
base_template_context.update(routes_login)
base_template_context.update(routes_register)


@register.simple_tag()
def load_base_context():  # user tag
    return base_template_context


# tempalte tag
@register.inclusion_tag('paper/menu/inclusion_tags/categories.html')
def load_categories():  # give
    cats = Categories.objects.all()
    return {"cats": cats}
