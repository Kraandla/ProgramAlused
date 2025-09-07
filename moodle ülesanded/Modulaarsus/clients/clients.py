"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount
        self.earnings_per_day_cache = None

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        earned_income = self.current_amount - self.starting_amount
        self.earnings_per_day_cache = earned_income / self.account_age
        return self.earnings_per_day_cache


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    list_of_names = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            name, bank, account_age, starting_amount, current_amount = line.split(',')
            list_of_names.append(Client(name, bank, int(account_age), int(starting_amount), int(current_amount)))

    # Legacy code
    # for i in client_date:
    #     # takes corresponding data from the clients
    #     name = i[0]
    #     bank = i[1]
    #     account_age = int(i[2])
    #     starting_amount = int(i[3])
    #     current_amount = int(i[4])
    #     # sends it to Client class
    #     client = Client(name, bank, account_age, starting_amount, current_amount)
    #     list_of_names.append(client)

    return list_of_names


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    filtered_names = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            name, client_bank, account_age, starting_amount, current_amount = line.split(',')
            if bank == client_bank:
                filtered_names.append(Client(name, bank, int(account_age), int(starting_amount), int(current_amount)))

    return filtered_names


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    # array to store client data and send to Client class
    client_data = read_from_file_into_list(filename)
    # array to store clients earnings by day

    for client in client_data:
        Client.earnings_per_day(client)

    # sorts through the list to find the most earnings by
    client_data = sorted(client_data, key=lambda client: (client.earnings_per_day_cache, -client.account_age), reverse=True)

    if client_data[0].earnings_per_day_cache <= 0:
        return None

    return client_data[0]


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    client_data = read_from_file_into_list(filename)

    for client in client_data:
        Client.earnings_per_day(client)

    client_data = sorted(client_data, key=lambda client: (-client.earnings_per_day_cache, -client.account_age),
                         reverse=True)

    if client_data[0].earnings_per_day_cache >= 0:
        return None

    return client_data[0]


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
