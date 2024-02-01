import time


class Printer:

    def __init__(self, name, color: bool, print_speed: float):
        self.name = name
        self.color = color
        self.print_speed = print_speed
        self.pages_count = 0

    def add_pages(self, nr_of_pages):
        self.pages_count += nr_of_pages

    def get_printer_info(self):
        return f"Name: {self.name}, Color: {self.color}, Pages: {self.pages_count}, Speed: {self.print_speed}"

    def print(self, nr_of_pages, number_of_copies, color=False):
        """
        Printam de number_of_copies ori, fiecare pagina
        Verificam daca putem printa color, in caz ca nu, avem eroare
        Daca nu mai este hartie, avem eroare
        :param nr_of_pages:
        :param number_of_copies:
        :param color:
        :return:
        """
        if color and self.color is False:
            raise TypeError("This printer can not do color")
        if nr_of_pages * number_of_copies > self.pages_count:
            raise ValueError("Not enough pages in the printer to start job")

        print(f"Starting print job of {number_of_copies} for {nr_of_pages}")
        for copy in range(number_of_copies):
            for page in range(nr_of_pages):
                print(f"Printing page {page + 1} of copy: {copy + 1}")
                time.sleep(self.print_speed)
                self.pages_count -= 1
        print("Done!")


home_printer = Printer("HP", False, 1)
print(home_printer.get_printer_info())
home_printer.add_pages(10)
print(home_printer.get_printer_info())
# home_printer.print(3, 3, False)
print(home_printer.get_printer_info())

industrial_printer = Printer("HP PRO", True, 0.1)
print(industrial_printer.get_printer_info())
industrial_printer.add_pages(10000000)
print(industrial_printer.get_printer_info())
industrial_printer.print(3, 3, False)
industrial_printer.print(1000, 1000, False)







