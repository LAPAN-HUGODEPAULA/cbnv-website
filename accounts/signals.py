from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

User = get_user_model()


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if not created:
        return
    if not instance.email:
        return
    send_mail(
        subject="Bem-vindo(a) ao CBNV 2026!",
        message=(
            f"Olá, {instance.first_name}!\n\n"
            "Seu cadastro no XII Congresso Brasileiro de Neurociências "
            "da Visão foi realizado com sucesso.\n\n"
            "Acesse o painel para gerenciar suas submissões:\n"
            "https://cbnv2026.org/painel/\n\n"
            "Atenciosamente,\nEquipe CBNV 2026"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.email],
        fail_silently=True,
    )


def notify_role_assignment(user, role):
    if not user.email:
        return
    role_labels = {
        "reviewer": "Revisor(a)",
        "chair": "Membro da Comissão Científica",
    }
    label = role_labels.get(role, role)
    send_mail(
        subject=f"Novo papel atribuído — CBNV 2026",
        message=(
            f"Olá, {user.first_name}!\n\n"
            f"Você foi designado(a) como {label} no XII Congresso Brasileiro "
            "de Neurociências da Visão.\n\n"
            f"Acesse o painel: https://cbnv2026.org/painel/\n\n"
            "Atenciosamente,\nEquipe CBNV 2026"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=True,
    )
