from ping import ping_websites
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Ping websites from the command line.")
    parser.add_argument("websites", nargs="+", help="List of websites to ping.")
    parser.add_argument("-n", "--num_requests", type=int, default=4, help="Number of ping requests (default: 4)")

    args = parser.parse_args()

    websites_to_ping = args.websites
    num_requests = args.num_requests

    ping_websites(websites_to_ping, num_requests)

    # websites_to_ping = ["www.google.com", "www.example.com", "www.github.com"]
    # ping_websites(websites_to_ping, num_requests=5)
