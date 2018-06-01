from django import template


register = template.Library()


@register.filter(is_safe=True)
def bold_message(message):
    """
    Os filtros são chamados no momento de avaliação da template.
    É necessário carrega-los dentro do template em questão.
    :param message: str
    :return: bold text
    """
    return f"<b>{ message }</b>"
