from datetime import datetime
from random import randint
from .models import LastProduct, Purchase


class Agent:

    messages = {
        "nearest_store": "A loja Shell Select mais próxima que possui seu {product} está há {dist} quilômetros. Deseja ir até lá?",
        "confirm_purchase": "Sua compra no valor de {price} reais foi confirmada. Você chegará na loja em {min} minutos",
    }

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def locate_product(self, product, lat=-22.6956, long=-47.62):
        # TODO: UNMOCK!
        return {"name": "Posto Santa Fé", "distance": 10}

    def confirm_purchase(self, product_id=10, store_id=20):
        price = randint(5, 50)
        min_ = randint(3, 20)
        qtd = randint(1, 5)

        lp = LastProduct().select()[-1]
        p = Purchase(
            date=datetime.now(),
            qtd=qtd,
            price=price,
            station="Santa Fé",
            product=lp.name,
            eta=10
        )
        try:
            p.save()
        except:
            pass

        return {"price": price, "min": min_}

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
            lp = LastProduct(name=product)

            try:
                lp.save()
            except:
                pass

            store = self.locate_product(product)
            dist = store["distance"]

            return self.messages["nearest_store"].format(dist=dist, product=product)

