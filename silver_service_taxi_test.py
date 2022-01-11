from silver_service_taxi import SilverServiceTaxi


def main():
    benz = SilverServiceTaxi("benz", 200, 2)
    benz.drive(18)
    print(benz)


if __name__ == '__main__':
    main()
