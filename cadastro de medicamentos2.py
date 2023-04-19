class Customer:
    def __init__(self, medicação, lote, id, validade):
        self.medicação = medicação
        self.lote = lote
        self.id = id
        self.validade = validade

class CustomerDatabase:
    def __init__(self):
        self.customers = []
        
    def add_customer(self, customer):
        self.customers.append(customer)
        
    def display_customers(self):
        for customer in self.customers:
            print("medicação: ", customer.medicação)
            print("lote: ", customer.lote)
            print("id: ", customer.id)
            print("validade: ", customer.validade)
            print(" ")

# Sample usage

customer_db = CustomerDatabase()

customer1 = Customer("Haloperidol", "0A2213", "000001", "10/10/2026")
customer_db.add_customer(customer1)

customer2 = Customer("Prometazina", "0B3324", "000002", "11/11/2027")
customer_db.add_customer(customer2)

customer_db.display_customers()
