from unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("bad car", 100, 5)
    reliable_car = UnreliableCar("great car", 100, 95)

    for i in range(1, 7):
        print("{} drive - {}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{} drive - {}km".format(unreliable_car.name, unreliable_car.drive(i)))

    print(unreliable_car)
    print(reliable_car)


if __name__ == '__main__':
    main()
