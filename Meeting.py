class Client:
  def __init__(self, name, surname, city):
    self.name = name
    self.surname = surname
    self.city = city
  def get_client(self):
    return f"{self.name} {self.surname}г.{self.city}"

client1 = Client("Иван", "Петров", "Москва")
client2 = Client("Маша", "Иванова", "Омск")
client3 = Client("Олег", "Жучков", "Киев")

client_list = [client1, client2, client3]

for client in client_list:
    print(client.get_client())