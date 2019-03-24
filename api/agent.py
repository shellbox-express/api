class Agent:

    messages = {
        "nearest_store": "A loja Shell Select mais próxima que possui seu produto está há {dist} quilômetros. Deseja ir até lá?",
        "confirm_purchase": "Sua compra no valor de {price} reais foi confirmada. Você chegará na loja em {min} minutos"
    }

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def locate_product(self, product, lat=-22.6956, long=-47.62):
        # TODO: UNMOCK!
        return {"name": "Posto Santa Fé", "distance": 10}

    def confirm_purchase(self, product_id=10, store_id=20):
        # TODO: UNMOCK!
        return {"price": 20, "min": 8}

    def proccess_watson(self, input):
        # GAMBIARRA!!!
        if "ABRIR O WAZE COM COORDENADAS" in input:
            return self.messages["confirm_purchase"].format(**self.confirm_purchase())

        if input.count("-") == 0:
            return

        separator_index = input.index("-")
        message = input[: separator_index - 1]
        function = input[separator_index + 10 :]

        if function == "searchSelect":
            product = message.split()[-1]
            store = self.locate_product(product)
            dist = store["distance"]

            return self.messages["nearest_store"].format(dist=dist)

