from datetime import datetime, timedelta

def format_relative_time(post_date, exact=False):
    now = datetime.now()  # Obtenha a hora e data atual na localização atual
    delta = now - post_date

    if not exact:
        if delta < timedelta(minutes=1):
            seconds = delta.seconds
            if seconds == 0:
                return 'Agora mesmo'
            else:
                return f'Agora mesmo - {seconds} segundos'
        elif delta < timedelta(hours=1):
            minutes = delta.seconds // 60
            if minutes == 1:
                return 'Há 1 minuto'
            else:
                return f'Há {minutes} minutos'
        elif delta < timedelta(days=1):
            hours = delta.seconds // 3600
            if hours == 1:
                return 'Há 1 hora'
            else:
                return f'Há {hours} horas'
        elif delta < timedelta(weeks=1):
            days = delta.days
            if days == 1:
                return 'Há 1 dia'
            else:
                return f'Há {days} dias'
        elif delta < timedelta(days=365):
            weeks = delta.days // 7
            if weeks == 1:
                return 'Há 1 semana'
            else:
                return f'Há {weeks} semanas'
        else:
            years = delta.days // 365
            if years == 1:
                return 'Há 1 ano'
            else:
                return f'Há {years} anos'
    else:
        return f'Em {post_date.strftime("%d/%m/%Y %H:%M:%S")}'
