from time import sleep
class UrTube:
    current_user = None
    def __init__(self):
        self.users = []
        self.videos = []
    def log_in(self, nickname,password):
        for usr in self.users:
            if usr.nickname == nickname and hash(password) == usr.password:
                self.current_user = usr

    def register(self, nickname, password, age):
        for usr in self.users:
            if nickname == usr.nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, all_videos):
        return [video.__str__() for video in
                filter(lambda video: all_videos.lower() in video.title.lower(), self.videos)]

    def watch_video(self, title):
        if self.current_user:
            for video in self.videos:
                if title == video.title:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
                    for i in range(1, 11):
                        print(i, end=' ')
                        sleep(1)
                    print('Конец видео')
                    video.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return self.title

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
