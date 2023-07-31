from chain_group import ChainDispenser

if __name__ == '__main__':

    # Initialize the chain responsability

    chain = ChainDispenser()

    amount = int(input('Enter a amount more than 10 and multiple of 10 '))

    if amount < 10 or amount % 10 != 0:
        print("Amount has to be more than 10 and multiple of 10")
        exit()

    chain.dispenser_50.handle(amount)
    print("Probando")
