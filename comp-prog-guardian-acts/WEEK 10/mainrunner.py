
import Capacitor
import Resistor
import Inductor

while True:

    selector = input(
        "\nSelect calculator (CC_CV, R_OHM, L_REACT, EXIT): "
    ).upper()

    match selector:

        case "CC_CV":
            print("Capacitance Calculator (C = Q / V)")
            charge = float(input("Enter the charge: "))
            voltage = float(input("Enter the voltage: "))
            Capacitor.get_capacitance_by_CV(charge, voltage)

        case "R_OHM":
            print("Resistance Calculator (Ohm's Law)")
            current = float(input("Enter the current: "))
            voltage = float(input("Enter the voltage: "))
            Resistor.get_resistance_by_ohms_law(voltage, current)

        case "L_REACT":
            print("Inductive Reactance Calculator")
            frequency = float(input("Enter the frequency: "))
            inductance = float(input("Enter the inductance: "))
            Inductor.get_inductive_reactance(frequency, inductance)

        case "EXIT":
            print("Program terminated.")
            break

        case _:
            print("Invalid selection. Try again.")
