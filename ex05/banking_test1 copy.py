from the_bank import Bank, Account

def main():
    # Créer une instance de Bank
    bank = Bank()

    # Créer un compte corrompu (avec un attribut 'bref')
    corrupted_account = Account(name="Smith Jane", value=1000.0, addr="123 Main St", zip="12345", bref="corrupted")

    # Vérifier si le compte est corrompu
    corruption_checks = bank.is_corrupted(corrupted_account)

    # Déterminer si le compte est corrompu
    if corruption_checks:
        print("Le compte est corrompu.")
    else:
        print("Le compte n'est pas corrompu.")

    bank.fix_account(corrupted_account)

    corruption_checks = bank.is_corrupted(corrupted_account)

        if corruption_checks:
            print("Le compte est corrompu.")
        else:
            print("Le compte n'est pas corrompu.")

if __name__ == "__main__":
    main()
    