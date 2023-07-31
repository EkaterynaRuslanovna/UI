import os
import subprocess


def ping_websites(sites, num_requests=5):
    """
    A function for checking the ping of sites

    :param sites: (list): A list of URLs for sites to check.
    :param num_requests: (int): Number of ping requests (4 by default).
    :return: None -  outputs the ping result to the console.
    """

    operating_system = os.name

    for site in sites:
        print(f"Ping website: {site}")
        try:
            if operating_system == 'nt':                                                       # 'nt' - for Windows
                ping_cmd = ["ping", "-n", str(num_requests), site]
            else:
                ping_cmd = ["ping", "-c", str(num_requests), site]                                    # for macOS, Linux

            result = subprocess.run(ping_cmd, capture_output=True, text=True)
            print(result.stdout)

        except Exception as error:
            print(f"An error occurred while pinging the site {site}: {error}")
        print("-" * 50)


websites_to_ping = ["www.google.com", "www.ithillel.ua", "www.github.com"]
ping_websites(websites_to_ping, num_requests=3)
