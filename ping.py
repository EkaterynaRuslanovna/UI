import os
import subprocess


def ping_websites(sites, num_requests=5):
    """
    Функція для перевірки пінгу сайтів.

    :param sites: (list): Список із URL-адресами сайтів, які необхідно перевірити.
    :param num_requests: (int): Кількість пінг запитів (по замовчуванню 4).
    :return: None -  виводить результат пінгування в консоль.
    """

    operating_system = os.name

    for site in sites:
        print(f"Ping website: {site}")
        try:
            if operating_system == 'nt':                                                       # 'nt' -назва для Windows
                ping_cmd = ["ping", "-n", str(num_requests), site]
            else:
                ping_cmd = ["ping", "-c", str(num_requests), site]                                      # (macOS, Linux)

            result = subprocess.run(ping_cmd, capture_output=True, text=True)
            print(result.stdout)

        except Exception as error:
            print(f"An error occurred while pinging the site {site}: {error}")
        print("-" * 50)


websites_to_ping = ["www.google.com", "www.ithillel.ua", "www.github.com"]
ping_websites(websites_to_ping, num_requests=3)
