import time
import bcrypt
from User import User

class UrTube:
    """
    Класс для управления системой видеоплатформы, аналогичной YouTube.

    Этот класс предоставляет функционал для регистрации пользователей, входа и выхода из системы,
    а также добавления и просмотра видео. Платформа поддерживает базовые функции управления видео,
    такие как поиск по названию, просмотр с учетом возраста пользователя и другие.

    Атрибуты:
        users (list): Список всех зарегистрированных пользователей.
        videos (list): Список всех загруженных видео на платформу.
        current_user (User or None): Текущий вошедший пользователь.
    """

    def __init__(self):
        """
        Инициализация объекта UrTube.

        Создает пустые списки для пользователей и видео, а также устанавливает текущее значение
        пользователя как None.
        """
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий вошедший пользователь

    def register(self, nickname, password, age):
        """
        Регистрирует нового пользователя на платформе.

        Проверяет, не существует ли уже пользователя с данным никнеймом. Если пользователь с таким
        ником уже зарегистрирован, выводится сообщение об ошибке. В противном случае создается новый 
        пользователь и он добавляется в список пользователей.

        Аргументы:
            nickname (str): Никнейм нового пользователя.
            password (str): Пароль нового пользователя.
            age (int): Возраст нового пользователя.

        Возвращает:
            None
        """
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошёл в систему")

    def log_out(self):
        """
        Выход пользователя из системы.

        Если пользователь вошел в систему, он выходит из нее, и его учетная запись
        становится недоступной до следующего входа. Печатает сообщение о выходе.

        Аргументы:
            None

        Возвращает:
            None
        """
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы")
            self.current_user = None
        else:
            print("Нет вошедшего пользователя")

    def log_in(self, nickname, password):
        """
        Вход пользователя в систему.

        Проверяет, существует ли пользователь с данным никнеймом, и если существует,
        сверяет введенный пароль с хранимым. В случае успешной проверки, пользователь 
        получает доступ к системе. В случае ошибки выводится сообщение.

        Аргументы:
            nickname (str): Никнейм пользователя.
            password (str): Пароль пользователя.

        Возвращает:
            None
        """
        for user in self.users:
            if nickname == user.nickname:
                if bcrypt.checkpw(password.encode(), user.password):
                    self.current_user = user
                    print(f"Пользователь {nickname} вошел в систему")
                    return
                else:
                    print("Неверный пароль")
                    return
        print("Пользователь не найден")

    def add(self, *new_video):
        """
        Добавляет одно или несколько видео на платформу.

        Проверяет, что видео с таким же названием еще не существует в системе, и если не существует,
        добавляет его в список видео.

        Аргументы:
            new_video (Video): Одно или несколько объектов Video.

        Возвращает:
            None
        """
        for video in new_video:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        """
        Ищет видео по ключевому слову в названии.

        Проводит поиск видео по части названия, игнорируя регистр. Возвращает список найденных видео.

        Аргументы:
            search_word (str): Ключевое слово для поиска в названии видео.

        Возвращает:
            list: Список названий найденных видео.
        """
        found_video = []
        word_lower = search_word.lower()

        for video in self.videos:
            if word_lower in video.title.lower():
                found_video.append(video.title)

        return found_video

    def watch_video(self, name_video):
        """
        Смотрит видео.

        Платформа проверяет, вошел ли пользователь в систему. Если не вошел — просит войти. 
        Также учитывает возраст пользователя, проверяя наличие взрослого контента, и в случае 
        несоответствия возрасту выводит предупреждение. В случае успешного просмотра видео,
        оно воспроизводится с таймером (имитация просмотра).

        Аргументы:
            name_video (str): Название видео для просмотра.

        Возвращает:
            None
        """
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return

            if name_video == video.title:
                for second in range(1, video.duration + 1):
                    print(second, end=' ')
                    time.sleep(1)

                print("Конец видео")
                video.time_now = 0  # Сброс времени просмотра
                return

        print("Видео не найдено")

                         
        
                
        
